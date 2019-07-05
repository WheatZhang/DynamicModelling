#!/usr/bin/env python
#-*- coding:utf-8 -*-
import ModularTask.Device as Device
import ModularTask.Task as Task
import ModularTask.Controller as Controller
import ModularTask

class GeneralColumnSump(Device.PyomoDevice):
    def setDeviceParams(self, specifications):
        required_specifications = [
            'SumpCSArea',
            'ControllerKc',
            'ControllerTi'
        ]
        self.setDeviceDevParam(required_specifications, specifications)

    def setSpecificaitons(self, specifications):
        # -----------------------------
        #      Set Specifications
        # -----------------------------
        if not hasattr(self, 'options'):
            raise Exception("Please set options for the model first in %s." % self.name)
        if self.options['HoldupDensity'] == 'Constant':
            required_specifications = [
                'LiqRho',
                'LevelSP'
            ]
        elif self.options['HoldupDensity'] == 'Thermodynamics':
            required_specifications = [
                'LevelSP'
            ]
        self.setDeviceSpecs(required_specifications, specifications)

    def setupLevelController(self):
        # -----------------------------
        #      Set PI Controller
        # -----------------------------
        varAlias = {'MV': self.name + 'OutMFlow[time]',
                    'CV': self.name + 'HldpLevel[time]'
                    }
        controller = Controller.FixedPIController(self.task)
        self.level_controller = controller.instanciate(self.name + "LC", varAlias)
        para_value = {"Kc": self.device_param['ControllerKc'],
                      "Ti": self.device_param['ControllerTi']}
        self.level_controller.setParameterValue(para_value)
        self.level_controller.setCtrlOffset(self.static_init[self.name + 'OutMFlow'],
                                            self.specifications['LevelSP'])

    def setConstraintWeight(self, weights):
        required_weights = [
            'FlowEquWeight'
        ]
        if len(weights) != len(required_weights):
            raise Exception("The numbers of constraint weights for %s in not correct." % self.name)
        for key, value in weights.items():
            if not key in required_weights:
                raise Exception("The constraint weight " + key + "is unavailable.")
        self.weights = weights

    def setModelingOption(self, options):
        # -----------------------------
        #      Set Options
        # -----------------------------
        available_options = {
            'HoldupDensity' : ['Thermodynamics', 'Constant'],
            'LiquidDensityThermo':'ModularTask.Thermodynamics.LiqDensityThermo',
            'LiquidEnthalpy': 'ModularTask.Thermodynamics.LiquidEnthalpyThermo',
            'CreateCustimizedFile' : [True, False]
        }
        self.setDeviceOptions(available_options, options)
        # -----------------------------
        #      RegisterParts
        # -----------------------------
        if 'LiquidDensityThermo' in options.keys():
            if options['LiquidDensityThermo'] not in self.task.processParts:
                self.task.processParts.append(options['LiquidDensityThermo'])
        if isinstance(self.task, Task.PyomoDynamicTask):
            if options['LiquidEnthalpy'] not in self.task.processParts:
                self.task.processParts.append(options['LiquidEnthalpy'])
        # ----------------------------------------
        #      Set Public Parts Used Variable Names
        # -----------------------------------------
        if isinstance(self.task, Task.PyomoStaticTask):
            PubPartsUsedVarNames = {
                'T': self.name + 'Temp',
                'P': self.name + 'Pressure',
                'c': self.name + 'MFrac[#comp#]',
                'rhol': self.name + 'LiqRho'
            }
        elif isinstance(self.task, Task.PyomoDynamicTask):
            PubPartsUsedVarNames = {
                'T': self.name + 'Temp[#index#]',
                'P': self.name + 'Pressure[#index#]',
                'c': self.name + 'MFrac[#index#,#comp#]',
                'rhol': self.name + 'LiqRho[#index#]',
                'x': self.name + 'HldpMFrac[#index#,#comp#]',
                'hl': self.name + 'OutMEtlp[#index#]'
            }
        # -----------------------------
        #      Set Thermodynamics
        # -----------------------------
        if 'LiquidDensityThermo' in options.keys():
            varAlias = {}
            for interfVar in options['LiquidDensityThermo'].interfaceVar:
                varAlias[interfVar] = PubPartsUsedVarNames[interfVar]
            if isinstance(self.task, Task.PyomoStaticTask):
                indexList = []
            elif isinstance(self.task, Task.PyomoDynamicTask):
                indexList = [['time', 'Time']]
            self.liq_density = options['LiquidDensityThermo'].instanciate(name=self.name + "Hdlp",
                                                                     varAlias=varAlias, indexList=indexList)
        if isinstance(self.task, Task.PyomoDynamicTask):
            varAlias = {}
            for interfVar in options['LiquidEnthalpy'].interfaceVar:
                varAlias[interfVar] = PubPartsUsedVarNames[interfVar]
            indexList = [['time', 'Time']]
            if options['LiquidEnthalpy'].attributes['Custimized'] == False:
                self.liq_enthalpy = options['LiquidEnthalpy'].instanciate(name=self.name + "Hdlp",
                                                                         varAlias=varAlias, indexList=indexList)
            elif options['LiquidEnthalpy'].attributes['Custimized'] == True:
                self.liq_enthalpy = options['LiquidEnthalpy'].instanciate(name=self.name + "Hdlp",
                                                                                             varAlias=varAlias,
                                                                                             indexList=indexList,
                                                                                             creatFile=self.options[
                                                                                                 'CreateCustimizedFile'])
                inst_param = {}
                for key in options["LiquidEnthalpy"].required_param:
                    if key == 'temp_span':
                        inst_param['temp_span'] = self.nominal_range[self.name + 'TrayTemp']
                    elif key == 'pressure_span':
                        inst_param['pressure_span'] = self.nominal_range[self.name + 'TrayPressure']
                self.liq_enthalpy.setParameters(inst_param)
        # -----------------------------
        #      RegisterParts-inst
        # -----------------------------
        if isinstance(self.task, Task.PyomoDynamicTask):
            self.task.processParts.append(self.liq_enthalpy)
        if 'LiquidDensityThermo' in options.keys():
            self.task.processParts.append(self.liq_density)
        # ---------------------------------
        #      Set Input and Output
        # ---------------------------------
        if isinstance(self.task, Task.PyomoStaticTask):
            dict = {'F': self.name + 'InMFlow',
                    'c': self.name + 'InMFrac[#comp#]',
                    'P': self.name + 'Pressure',
                    'h': self.name + 'InMEtlp',
                    'T': self.name + 'Temp'
                    }
        elif isinstance(self.task, Task.PyomoDynamicTask):
            dict = {'F': self.name + 'InMFlow[#time#]',
                    'c': self.name + 'InMFrac[#time#, #comp#]',
                    'P': self.name + 'Pressure[#time#]',
                    'h': self.name + 'InMEtlp[#time#]',
                    'T': self.name + 'Temp[#time#]'
                    }
        self.inputStreams['Inlet'] = Device.InputStream(self.name + 'Inlet', dict)
        if isinstance(self.task, Task.PyomoStaticTask):
            dict = {'F': self.name + 'OutMFlow',
                    'c': self.name + 'InMFrac[#comp#]',
                    'h': self.name + 'InMEtlp',
                    'P': self.name + 'Pressure'
                    }
        elif isinstance(self.task, Task.PyomoDynamicTask):
            dict = {'F': self.name + 'OutMFlow[#time#]',
                    'c': self.name + 'HldpMFrac[#time#, #comp#]',
                    'h': self.name + 'OutMEtlp[#time#]',
                    'P': self.name + 'Pressure[#time#]'
                    }
        output_var = ['c', 'F', 'h', 'P']
        self.outputStreams['Outlet'] = Device.OutputStream(self.name + 'Outlet', dict, output_var)

    def generatePublicPEVar(self):
        PE_str = ""
        PE_str += "#--------%s---------\n" % self.name
        if type(self.task) == Task.PyomoPETask:
            PE_str += ModularTask.ModelingTools.to_pe_public_var("LiqRho",
                                                                 self.specifications["LiqRho"])
        else:
            raise Exception("This is not a PE task.")
        PE_str = PE_str.replace('#model_name#', self.task.name).replace("#device_name#", self.name).replace(
            "#prim_name#", self.primitive_name)
        return PE_str

    def generatePEConstraint(self):
        PE_str = ""
        PE_str += "#--------%s---------\n" % self.name
        if type(self.task) == Task.PyomoPETask:
            if isinstance(self.specifications['LiqRho'], ModularTask.PE.EstimatedSpec):
                PE_str += ModularTask.ModelingTools.to_pe_constraint("LiqRho", 1)
        else:
            raise Exception("This is not a PE task.")
        PE_str = PE_str.replace('#model_name#', self.task.name).replace("#device_name#", self.name).replace(
            "#prim_name#", self.primitive_name)
        return PE_str

    def generatePyomoPara(self):
        if isinstance(self.task, Task.PyomoDynamicTask):
            self.setupLevelController()
        str = ""
        str += "#--------%s---------\n" % self.name
        if isinstance(self.task, Task.PyomoDynamicTask):
            str += self.level_controller.generatePyomoPara()
            str += ModularTask.ModelingTools.gen_dynamic_para(self.task, "LevelSP",
                                                                   self.specifications['LevelSP'])
        if self.options['HoldupDensity'] == 'Constant':
            if isinstance(self.task, Task.PyomoStaticTask):
                str += ModularTask.ModelingTools.ss_or_pe_para(self.task, "LiqRho",
                                                                    self.specifications['LiqRho'])
            elif isinstance(self.task, Task.PyomoDynamicTask):
                str += ModularTask.ModelingTools.gen_dynamic_para(self.task, "LiqRho",
                                                                       self.specifications['LiqRho'])
        str += "#model_name#.#device_name#SumpCSArea = Param(initialize = %f)\n" % self.device_param["SumpCSArea"]
        str = str.replace('#model_name#', self.task.name).replace("#device_name#", self.name)
        return str

    def generatePyomoVar(self):
        str = ""
        str += "#--------%s---------\n" % self.name
        if isinstance(self.task, Task.PyomoStaticTask):
            str += "#model_name#.#device_name#OutMFlow = Var(within=NonNegativeReals)\n"
            str += "#model_name#.#device_name#HldpMFrac = Var(#model_name#.Component, bounds =(0,1))\n"
        elif isinstance(self.task, Task.PyomoDynamicTask):
            str += self.level_controller.generatePyomoVar()
            str += "#model_name#.#device_name#OutMFlow = Var(#model_name#.Time, within=NonNegativeReals)\n"
            str += "#model_name#.#device_name#MCompHldp = Var(#model_name#.Time, #model_name#.Component, within=NonNegativeReals)\n"
            str += "#model_name#.#device_name#DtMCompHldp = DerivativeVar(#model_name#.#device_name#MCompHldp)\n"
            str += "#model_name#.#device_name#HldpLevel = Var(#model_name#.Time, within=NonNegativeReals)\n"
            str += "#model_name#.#device_name#MHldp = Var(#model_name#.Time, within=NonNegativeReals)\n"
            str += "#model_name#.#device_name#HldpMFrac = Var(#model_name#.Time, #model_name#.Component, bounds =(0,1))\n"
        str = str.replace('#model_name#', self.task.name).replace("#device_name#", self.name)
        return str

    def generatePyomoExpression(self):
        str = ""
        if isinstance(self.task, Task.PyomoDynamicTask):
            str += "#--------%s Thermo and Enthalpy---------\n" % self.name
            if self.options['HoldupDensity'] == 'Thermodynamics':
                str += self.liq_density.generatePyomoExpression()
            str += self.liq_enthalpy.generatePyomoExpression()
        str = str.replace('#model_name#', self.task.name).replace("#device_name#", self.name)
        return str

    def generatePyomoCon(self):
        str = ""
        str += "#--------%s Mass Balance---------\n" % self.name
        str += self.generateMassBalance()
        if isinstance(self.task, Task.PyomoDynamicTask):
            str += "#--------%s Summation---------\n" % self.name
            str += self.generateSummation()
            str += "#--------%s Holdup Level---------\n" % self.name
            str += self.generateHoldupLevel()
            str += "#--------%s Integration Initial Condition---------\n" % self.name
            str += self.generateInitialCondition()
            str += "#--------%s Level Control---------\n" % self.name
            str += self.level_controller.generatePyomoCon()
        return str

    def generateMassBalance(self):
        str = ""
        if isinstance(self.task, Task.PyomoStaticTask):
            str += "def #device_name#MassBlnc(m):\n"
            str += "\treturn (m.#device_name#InMFlow-m.#device_name#OutMFlow)*%f==0\n" % \
                   self.weights['FlowEquWeight']
            str += "#model_name#.#device_name#MassBlnc = Constraint(rule=#device_name#MassBlnc)\n"
            str += "def #device_name#HldpMFracSpec(m, comp):\n"
            str += "\treturn m.#device_name#HldpMFrac[comp] - m.#device_name#InMFrac[comp] == 0\n"
            str += "#model_name#.#device_name#HldpMFracSpec = Constraint(#model_name#.Component, rule=#device_name#HldpMFracSpec)\n"
        elif isinstance(self.task, Task.PyomoDynamicTask):
            str += "def #device_name#MCompHldpSpec(m, time, comp):\n"
            str += "\treturn (m.#device_name#MCompHldp[time,comp] - m.#device_name#HldpMFrac[time, comp] * m.#device_name#MHldp[time])*%f == 0\n"% \
                   self.weights['FlowEquWeight']
            str += "#model_name#.#device_name#MCompHldpSpec = Constraint(#model_name#.Time, #model_name#.Component, rule=#device_name#MCompHldpSpec)\n"
            str += "def #device_name#MassBlnc(m, time, comp):\n"
            str += "\treturn (m.#device_name#DtMCompHldp[time, comp]-m.#device_name#InMFlow[time]*m.#device_name#InMFrac[time, comp]"
            str += "+m.#device_name#OutMFlow[time]*m.#device_name#HldpMFrac[time, comp])*%f==0\n" % \
                   self.weights['FlowEquWeight']
            str += "#model_name#.#device_name#MassBlnc = Constraint(#model_name#.Time,#model_name#.Component, rule=#device_name#MassBlnc)\n"
        str = str.replace('#model_name#', self.task.name).replace("#device_name#", self.name)
        return str

    def generateSummation(self):
        str = ""
        str += "def #device_name#LiqSum(m, time):\n"
        str += "\treturn sum([m.#device_name#HldpMFrac[time, c] for c in m.Component]) == 1\n"
        str += "#model_name#.#device_name#LiqSum = Constraint(#model_name#.Time, rule=#device_name#LiqSum)\n"
        str = str.replace('#model_name#', self.task.name).replace("#device_name#", self.name)
        return str

    def generateHoldupLevel(self):
        str = ""
        str += "def #device_name#LevelCal(m, time):\n"
        str += "\treturn m.#device_name#HldpLevel[time] - m.#device_name#MHldp[time] / m.#device_name#LiqRho[time] / m.#device_name#SumpCSArea == 0\n"
        str += "#model_name#.#device_name#LevelCal = Constraint(#model_name#.Time, rule=#device_name#LevelCal)\n"
        str = str.replace('#model_name#', self.task.name).replace("#device_name#", self.name)
        return str

    def generateInitialCondition(self):
        # 两个组分的holdup
        cond_str = ""
        # hold_up = self.specifications['LevelSP']*self.specifications['SumpCSArea']*self.specifications['LiqRho']
        cond_str += "def #device_name#ICMHldp(m):\n"
        cond_str += "\treturn m.#device_name#MHldp[0] == m.#device_name#LevelSP[0]*m.#device_name#SumpCSArea\
                                *m.#device_name#LiqRho[0]\n"
        cond_str += "#model_name#.#device_name#ICMHldp = Constraint(rule=#device_name#ICMHldp)\n"
        cond_str += "def #device_name#ICCompHldp(m):\n"
        for index, comp in enumerate(self.task.component):
            if index == len(self.task.component)-1:
                continue
            else:
                cond_str += "\tyield m.#device_name#MCompHldp[0,\"%s\"] == m.#device_name#LevelSP[0]*m.#device_name#SumpCSArea\
                                *m.#device_name#LiqRho[0]*%f\n" \
                            % (comp, self.static_init[self.name + 'HldpMFrac'][comp])
        cond_str += "#model_name#.#device_name#ICCompHldp = ConstraintList(rule=#device_name#ICCompHldp)\n"
        cond_str = cond_str.replace('#model_name#', self.task.name).replace("#device_name#", self.name)
        return cond_str

    def getNaiveDynamicInitValue(self):
        self.static_init[self.name + 'MCompHldp'] = {}
        self.static_init[self.name + 'DtMCompHldp'] = {}
        self.static_init[self.name + 'HldpLevel'] = {}
        self.static_init[self.name + 'MHldp'] = {}
        if self.options['HoldupDensity'] == 'Constant':
            self.static_init[self.name + 'MHldp'] = \
                ModularTask.ModelingTools.evaluate_dyna_para(self.specifications['LevelSP'],0) \
                * self.device_param['SumpCSArea'] \
                * ModularTask.ModelingTools.evaluate_dyna_para(self.specifications['LiqRho'],0)
        elif self.options['HoldupDensity'] == 'Thermodynamics':
            self.static_init[self.name + 'MHldp'] = \
                ModularTask.ModelingTools.evaluate_dyna_para(self.specifications['LevelSP'], 0)\
                *self.device_param['SumpCSArea']*1000
        self.static_init[self.name + 'HldpLevel'] = \
            ModularTask.ModelingTools.evaluate_dyna_para(self.specifications['LevelSP'], 0)
        for j in self.task.component:
            self.static_init[self.name + 'MCompHldp'][j] = self.static_init[self.name + 'MHldp']*self.static_init[self.name + 'HldpMFrac'][j]
            self.static_init[self.name + 'DtMCompHldp'][j] = 0
