#!/usr/bin/env python
#-*- coding:utf-8 -*-
import ModularTask.Device as Device
import ModularTask.Task as Task

class NaiveReboiler(Device.PyomoDevice):
    def __init__(self, task, name):
        super().__init__(task, name)

    def setSpecificaitons(self, specifications):
        if not hasattr(self, 'options'):
            raise Exception("Please set options for the model first in %s." % self.name)
        if self.options['Pressure'] == 'SameWithInlet':
            required_specifications = []
        elif self.options['Pressure'] == 'Other':
            required_specifications = [
                'Pressure'
            ]
        self.setDeviceSpecs(required_specifications, specifications)

    def setConstraintWeight(self, weights):
        required_weights = [
            'FlowEquWeight',
            'EnthalpyEquWeight'
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
            'CompositionThermo': 'ModularTask.Thermodynamics.CompositionThermo',
            'VaporEnthalpy': 'ModularTask.Thermodynamics.VaporEnthalpyThermo',
            'LiquidEnthalpy': 'ModularTask.Thermodynamics.LiquidEnthalpyThermo',
            'Pressure' : ['SameWithInlet','Other'],
            'CheckTempDifference' : [False, True]
        }
        self.setDeviceOptions(available_options, options)
        # -----------------------------
        #      RegisterParts
        # -----------------------------
        if options['CompositionThermo'] not in self.task.processParts:
            self.task.processParts.append(options['CompositionThermo'])
        if options['VaporEnthalpy'] not in self.task.processParts:
            self.task.processParts.append(options['VaporEnthalpy'])
        if options['LiquidEnthalpy'] not in self.task.processParts:
            self.task.processParts.append(options['LiquidEnthalpy'])
        # ----------------------------------------
        #      Set Public Parts Used Variable Names
        # -----------------------------------------
        if isinstance(self.task, Task.PyomoStaticTask):
            PubPartsUsedVarNames = {
                'y': self.name + 'VapLvMFrac[#comp#]',
                'T': self.name + 'Temp',
                'P': self.name + 'Pressure',
                'hv': self.name + 'VapLvMEtlp',
                'x': self.name + 'LiqLvMFrac[#comp#]',
                'hl': self.name + 'LiqLvMEtlp'
            }
        elif isinstance(self.task, Task.PyomoDynamicTask):
            PubPartsUsedVarNames = {
                'y': self.name + 'VapLvMFrac[#index#,#comp#]',
                'T': self.name + 'Temp[#index#]',
                'P': self.name + 'Pressure[#index#]',
                'hv': self.name + 'VapLvMEtlp[#index#]',
                'x': self.name + 'LiqLvMFrac[#index#,#comp#]',
                'hl': self.name + 'LiqLvMEtlp[#index#]'
            }
        # -----------------------------
        #      Set Thermodynamics
        # -----------------------------
        varAlias = {}
        for interfVar in options['VaporEnthalpy'].interfaceVar:
            varAlias[interfVar] = PubPartsUsedVarNames[interfVar]
        if isinstance(self.task, Task.PyomoStaticTask):
            indexList = []
        elif isinstance(self.task, Task.PyomoDynamicTask):
            indexList = [['time', 'Time']]
        if options['VaporEnthalpy'].attributes['Custimized'] == False:
            self.vap_enthalpy = options['VaporEnthalpy'].instanciate(name=self.name + "Hdlp",
                                                                     varAlias=varAlias, indexList=indexList)
        elif options['VaporEnthalpy'].attributes['Custimized'] == True:
            self.vap_enthalpy = options['VaporEnthalpy'].instanciate(name=self.name + "Hdlp",
                                                                                         varAlias=varAlias,
                                                                                         indexList=indexList,
                                                                                         creatFile=self.options[
                                                                                             'CreateCustimizedFile'])
            inst_param = {}
            for key in options["VaporEnthalpy"].required_param:
                if key == 'temp_span':
                    inst_param['temp_span'] = self.nominal_range[self.name + 'Temp']
                elif key == 'pressure_span':
                    inst_param['pressure_span'] = self.nominal_range[self.name + 'Pressure']
            self.vap_enthalpy.setParameters(inst_param)
        varAlias = {}
        for interfVar in options['LiquidEnthalpy'].interfaceVar:
            varAlias[interfVar] = PubPartsUsedVarNames[interfVar]
        if isinstance(self.task, Task.PyomoStaticTask):
            indexList = []
        elif isinstance(self.task, Task.PyomoDynamicTask):
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
                    inst_param['temp_span'] = self.nominal_range[self.name + 'Temp']
                elif key == 'pressure_span':
                    inst_param['pressure_span'] = self.nominal_range[self.name + 'Pressure']
            self.liq_enthalpy.setParameters(inst_param)
        varAlias = {}
        for interfVar in options['CompositionThermo'].interfaceVar:
            varAlias[interfVar] = PubPartsUsedVarNames[interfVar]
        if isinstance(self.task, Task.PyomoStaticTask):
            indexList = []
        elif isinstance(self.task, Task.PyomoDynamicTask):
            indexList = [['time', 'Time']]
        if options['CompositionThermo'].attributes['Custimized'] == False:
            self.thermo_comp = options['CompositionThermo'].instanciate(name=self.name + "Hdlp",
                                                                        varAlias=varAlias, indexList=indexList)
        elif options['CompositionThermo'].attributes['Custimized'] == True:
            self.thermo_comp = options['CompositionThermo'].instanciate(name=self.name + "Hdlp",
                                                                                         varAlias=varAlias,
                                                                                         indexList=indexList,
                                                                                         creatFile=self.options[
                                                                                             'CreateCustimizedFile'])
            inst_param = {}
            for key in options["CompositionThermo"].required_param:
                if key == 'temp_span':
                    inst_param['temp_span'] = self.nominal_range[self.name + 'Temp']
                elif key == 'pressure_span':
                    inst_param['pressure_span'] = self.nominal_range[self.name + 'Pressure']
            self.thermo_comp.setParameters(inst_param)
        # -----------------------------
        #      RegisterParts-inst
        # -----------------------------
        self.task.processParts.append(self.vap_enthalpy)
        self.task.processParts.append(self.liq_enthalpy)
        self.task.processParts.append(self.thermo_comp)
        # ---------------------------------
        #      Set Input and Output
        # ---------------------------------
        if options['Pressure'] == 'SameWithInlet':
            if isinstance(self.task, Task.PyomoStaticTask):
                dict = {'F': self.name + 'InMFlow',
                        'c': self.name + 'InMFrac[#comp#]',
                        'P': self.name + 'Pressure',
                        'h': self.name + 'InMEtlp'
                        }
            elif isinstance(self.task, Task.PyomoDynamicTask):
                dict = {'F': self.name + 'InMFlow[#time#]',
                        'c': self.name + 'InMFrac[#time#, #comp#]',
                        'P': self.name + 'Pressure[#time#]',
                        'h': self.name + 'InMEtlp[#time#]'
                        }
            self.inputStreams['Inlet'] = Device.InputStream(self.name + 'Inlet', dict)
        elif options['Pressure'] == 'Other':
            if isinstance(self.task, Task.PyomoStaticTask):
                dict = {'F': self.name + 'InMFlow',
                        'c': self.name + 'InMFrac[#comp#]',
                        'h': self.name + 'InMEtlp'
                        }
            elif isinstance(self.task, Task.PyomoDynamicTask):
                dict = {'F': self.name + 'InMFlow[#time#]',
                        'c': self.name + 'InMFrac[#time#, #comp#]',
                        'h': self.name + 'InMEtlp[#time#]'
                        }
            self.inputStreams['Inlet'] = Device.InputStream(self.name + 'Inlet', dict)
        if self.options['CheckTempDifference']:
            if isinstance(self.task, Task.PyomoStaticTask):
                dict = {'Q': self.name + 'MHeatIn',
                        'T': self.name + 'InHeatTemp',
                        }
            elif isinstance(self.task, Task.PyomoDynamicTask):
                dict = {'Q': self.name + 'MHeatIn[#time#]',
                        'T': self.name + 'InHeatTemp[#time#]',
                        }
            self.inputStreams['HeatFlow'] = Device.InputStream(self.name + 'HeatFlow', dict)
        else:
            if isinstance(self.task, Task.PyomoStaticTask):
                dict = {'Q': self.name + 'MHeatIn',
                        }
            elif isinstance(self.task, Task.PyomoDynamicTask):
                dict = {'Q': self.name + 'MHeatIn[#time#]',
                        }
            self.inputStreams['HeatFlow'] = Device.InputStream(self.name + 'HeatFlow', dict)
        if isinstance(self.task, Task.PyomoStaticTask):
            dict = {'F': self.name + 'LiqLvMFlow',
                    'c': self.name + 'LiqLvMFrac[#comp#]',
                    'h': self.name + 'LiqLvMEtlp',
                    'P': self.name + 'Pressure'
                    }
        elif isinstance(self.task, Task.PyomoDynamicTask):
            dict = {'F': self.name + 'LiqLvMFlow[#time#]',
                    'c': self.name + 'LiqLvMFrac[#time#, #comp#]',
                    'h': self.name + 'LiqLvMEtlp[#time#]',
                    'P': self.name + 'Pressure[#time#]'
                    }
        output_var = ['c', 'F', 'h', 'P']
        self.outputStreams['LiqLv'] = Device.OutputStream(self.name + 'LiqLv', dict, output_var)
        if isinstance(self.task, Task.PyomoStaticTask):
            dict = {'F': self.name + 'VapLvMFlow',
                    'c': self.name + 'VapLvMFrac[#comp#]',
                    'h': self.name + 'VapLvMEtlp',
                    'P': self.name + 'Pressure'
                    }
        elif isinstance(self.task, Task.PyomoDynamicTask):
            dict = {'F': self.name + 'VapLvMFlow[#time#]',
                    'c': self.name + 'VapLvMFrac[#time#, #comp#]',
                    'h': self.name + 'VapLvMEtlp[#time#]',
                    'P': self.name + 'Pressure[#time#]'
                    }
        output_var = ['c', 'F', 'h', 'P']
        self.outputStreams['VapLv'] = Device.OutputStream(self.name + 'VapLv', dict, output_var)

    def generatePublicPEVar(self):
        PE_str = ""
        PE_str += "#--------%s---------\n" % self.name
        if type(self.task) == Task.PyomoPETask:
            if self.options['Pressure'] == 'Other':
                PE_str += ModularTask.ModelingTools.to_pe_public_var("Pressure",
                                                                     self.specifications["Pressure"])
        else:
            raise Exception("This is not a PE task.")
        PE_str = PE_str.replace('#model_name#', self.task.name).replace("#device_name#", self.name).replace(
            "#prim_name#", self.primitive_name)
        return PE_str

    def generatePEConstraint(self):
        PE_str = ""
        PE_str += "#--------%s---------\n" % self.name
        if type(self.task) == Task.PyomoPETask:
            if self.options['Pressure'] == 'Other':
                if isinstance(self.specifications['Pressure'], ModularTask.PE.EstimatedSpec):
                    PE_str += ModularTask.ModelingTools.to_pe_constraint("Pressure", 1e-3)
        else:
            raise Exception("This is not a PE task.")
        PE_str = PE_str.replace('#model_name#', self.task.name).replace("#device_name#", self.name).replace(
            "#prim_name#", self.primitive_name)
        return PE_str

    def generatePyomoPara(self):
        str = ""
        if self.options['Pressure'] == 'Other':
            str += "#--------%s---------\n" % self.name
            if isinstance(self.task, Task.PyomoStaticTask):
                str += ModularTask.ModelingTools.ss_or_pe_para(self.task, "Pressure",
                                                               self.specifications['Pressure'])
            elif isinstance(self.task, Task.PyomoDynamicTask):
                str += ModularTask.ModelingTools.gen_dynamic_para(self.task, "Pressure",
                                                                  self.specifications['Pressure'])
        str = str.replace('#model_name#', self.task.name).replace("#device_name#", self.name)
        return str

    def generatePyomoVar(self):
        str = ""
        str += "#--------%s---------\n" % self.name
        if isinstance(self.task, Task.PyomoStaticTask):
            str += "#model_name#.#device_name#LiqLvMFlow = Var(within=NonNegativeReals)\n"
            str += "#model_name#.#device_name#VapLvMFlow = Var(within=NonNegativeReals)\n"
            str += "#model_name#.#device_name#Temp = Var()\n"
        elif isinstance(self.task, Task.PyomoDynamicTask):
            str += "#model_name#.#device_name#LiqLvMFlow = Var(#model_name#.Time, within=NonNegativeReals)\n"
            str += "#model_name#.#device_name#VapLvMFlow = Var(#model_name#.Time, within=NonNegativeReals)\n"
            str += "#model_name#.#device_name#Temp = Var(#model_name#.Time)\n"
        str += self.thermo_comp.generatePyomoVar()
        str = str.replace('#model_name#', self.task.name).replace("#device_name#", self.name)
        return str

    def generatePyomoExpression(self):
        str = ""
        str += "#--------%s Enthalpy---------\n" % self.name
        str += self.vap_enthalpy.generatePyomoExpression()
        str += self.liq_enthalpy.generatePyomoExpression()
        return str

    def generatePyomoCon(self):
        str = ""
        str += "#--------%s Mass Balance---------\n" % self.name
        str += self.generateMassBalance()
        str += "#--------%s Energy Balance---------\n" % self.name
        str += self.generateEnergyBalance()
        str += "#--------%s Phase Equilibrium---------\n" % self.name
        str += self.generateEquilibrium()
        str += "#--------%s Summation---------\n" % self.name
        str += self.generateSummation()
        if self.options['CheckTempDifference']:
            str += "#--------%s Heat Transfer---------\n" % self.name
            str += self.generateHeatTransfer()
        return str

    def generateMassBalance(self):
        str = ""
        if isinstance(self.task, Task.PyomoStaticTask):
            str += "def #device_name#MassBlnc(m,comp):\n"
            str += "\treturn (m.#device_name#InMFlow * m.#device_name#InMFrac[comp]-\\\n"
            str += "\t    m.#device_name#LiqLvMFlow * m.#device_name#LiqLvMFrac[comp]-\\\n"
            str += "\t    m.#device_name#VapLvMFlow * m.#device_name#VapLvMFrac[comp])*%f==0\n" % self.weights[
                'FlowEquWeight']
            str += "#model_name#.#device_name#MassBlnc = Constraint(#model_name#.Component, rule=#device_name#MassBlnc)\n"
        elif isinstance(self.task, Task.PyomoDynamicTask):
            str += "def #device_name#MassBlnc(m,time,comp):\n"
            str += "\treturn (m.#device_name#InMFlow[time] * m.#device_name#InMFrac[time,comp]-\\\n"
            str += "\t    m.#device_name#LiqLvMFlow[time] * m.#device_name#LiqLvMFrac[time,comp]-\\\n"
            str += "\t    m.#device_name#VapLvMFlow[time] * m.#device_name#VapLvMFrac[time,comp])*%f==0\n" % self.weights['FlowEquWeight']
            str += "#model_name#.#device_name#MassBlnc = Constraint(#model_name#.Time, #model_name#.Component, rule=#device_name#MassBlnc)\n"
        str = str.replace('#model_name#', self.task.name).replace("#device_name#", self.name)
        return str

    def generateEnergyBalance(self):
        str = ""
        if isinstance(self.task, Task.PyomoStaticTask):
            str += "def #device_name#EngBlnc(m):\n"
            str += "\treturn (m.#device_name#InMFlow * m.#device_name#InMEtlp+m.#device_name#MHeatIn-\\\n"
            str += "\t    m.#device_name#LiqLvMFlow * m.#device_name#LiqLvMEtlp-\\\n"
            str += "\t    m.#device_name#VapLvMFlow * m.#device_name#VapLvMEtlp)*%f==0\n" % self.weights[
                'EnthalpyEquWeight']
            str += "#model_name#.#device_name#EngBlnc = Constraint(rule=#device_name#EngBlnc)\n"
        elif isinstance(self.task, Task.PyomoDynamicTask):
            str += "def #device_name#EngBlnc(m,time):\n"
            str += "\treturn (m.#device_name#InMFlow[time] * m.#device_name#InMEtlp[time]+m.#device_name#MHeatIn[time]-\\\n"
            str += "\t    m.#device_name#LiqLvMFlow[time] * m.#device_name#LiqLvMEtlp[time]-\\\n"
            str += "\t    m.#device_name#VapLvMFlow[time] * m.#device_name#VapLvMEtlp[time])*%f==0\n"% self.weights['EnthalpyEquWeight']
            str += "#model_name#.#device_name#EngBlnc = Constraint(#model_name#.Time, rule=#device_name#EngBlnc)\n"
        str = str.replace('#model_name#', self.task.name).replace("#device_name#", self.name)
        return str

    def generateEquilibrium(self):
        str = ""
        str += self.thermo_comp.generatePyomoCon()
        return str

    def generateSummation(self):
        str = ""
        if isinstance(self.task, Task.PyomoStaticTask):
            str += "def #device_name#LiqSum(m):\n"
            str += "\treturn sum([m.#device_name#LiqLvMFrac[c] for c in m.Component]) == 1\n"
            str += "#model_name#.#device_name#LiqSum = Constraint(rule=#device_name#LiqSum)\n"

            str += "def #device_name#VapSum(m):\n"
            str += "\treturn sum([m.#device_name#VapLvMFrac[c] for c in m.Component]) == 1\n"
            str += "#model_name#.#device_name#VapSum = Constraint(rule=#device_name#VapSum)\n"
        elif isinstance(self.task, Task.PyomoDynamicTask):
            str += "def #device_name#LiqSum(m,time):\n"
            str += "\treturn sum([m.#device_name#LiqLvMFrac[time,c] for c in m.Component]) == 1\n"
            str += "#model_name#.#device_name#LiqSum = Constraint(#model_name#.Time, rule=#device_name#LiqSum)\n"

            str += "def #device_name#VapSum(m,time):\n"
            str += "\treturn sum([m.#device_name#VapLvMFrac[time,c] for c in m.Component]) == 1\n"
            str += "#model_name#.#device_name#VapSum = Constraint(#model_name#.Time, rule=#device_name#VapSum)\n"
        str = str.replace('#model_name#', self.task.name).replace("#device_name#", self.name)
        return str

    def generateHeatTransfer(self):
        str = ""
        if isinstance(self.task, Task.PyomoStaticTask):
            str += "def #device_name#HeatTsfTemp(m):\n"
            str += "\treturn m.#device_name#InHeatTemp-m.#device_name#Temp >= 0\n"
            str += "#model_name#.#device_name#HeatTsfTemp = Constraint(rule=#device_name#HeatTsfTemp)\n"
        elif isinstance(self.task, Task.PyomoDynamicTask):
            str += "def #device_name#HeatTsfTemp(m,time):\n"
            str += "\treturn m.#device_name#InHeatTemp[time]-m.#device_name#Temp[time] >= 0\n"
            str += "#model_name#.#device_name#HeatTsfTemp = Constraint(#model_name#.Time, rule=#device_name#HeatTsfTemp)\n"
        str = str.replace('#model_name#', self.task.name).replace("#device_name#", self.name)
        return str