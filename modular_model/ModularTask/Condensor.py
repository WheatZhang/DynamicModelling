#!/usr/bin/env python
#-*- coding:utf-8 -*-
import ModularTask.Device as Device
import ModularTask.Task as Task
import ModularTask

class NaiveTotalCondensor(Device.PyomoDevice):
    def __init__(self, task, name):
        super().__init__(task, name)

    def setSpecificaitons(self, specifications):
        if not hasattr(self, 'options'):
            raise Exception("Please set options for the model first in %s." % self.name)
        if self.options['Pressure'] == 'SameWithInlet':
            required_specifications = [
                'RefluxRatio'
            ]
        elif self.options['Pressure'] == 'Other':
            required_specifications = [
                'RefluxRatio',
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
            'BubblePoint': 'ModularTask.Thermodynamics.BubblePointThermo',
            'LiquidEnthalpy': 'ModularTask.Thermodynamics.LiquidEnthalpyThermo',
            'Pressure' : ['SameWithInlet','Other'],
            'CreateCustimizedFile' : [True, False]
        }
        self.setDeviceOptions(available_options, options)
        # -----------------------------
        #      RegisterParts
        # -----------------------------
        if options['BubblePoint'] not in self.task.processParts:
            self.task.processParts.append(options['BubblePoint'])
        if options['LiquidEnthalpy'] not in self.task.processParts:
            self.task.processParts.append(options['LiquidEnthalpy'])
        # ----------------------------------------
        #      Set Public Parts Used Variable Names
        # -----------------------------------------
        if isinstance(self.task, Task.PyomoStaticTask):
            PubPartsUsedVarNames = {
                'x': self.name + 'MFrac[#comp#]',
                'T': self.name + 'Temp',
                'P': self.name + 'Pressure',
                'hl': self.name + 'OutMEtlp',
                'c': self.name + 'MFrac[#comp#]'
            }
        elif isinstance(self.task, Task.PyomoDynamicTask):
            PubPartsUsedVarNames = {
                'x': self.name + 'MFrac[#index#,#comp#]',
                'T': self.name + 'Temp[#index#]',
                'P': self.name + 'Pressure[#index#]',
                'hl': self.name + 'OutMEtlp[#index#]',
                'c': self.name + 'MFrac[#index#,#comp#]'
            }
        # -----------------------------
        #      Set Thermodynamics
        # -----------------------------
        varAlias = {}
        for interfVar in options['LiquidEnthalpy'].interfaceVar:
            varAlias[interfVar] = PubPartsUsedVarNames[interfVar]
        if isinstance(self.task, Task.PyomoStaticTask):
            indexList = []
        elif isinstance(self.task, Task.PyomoDynamicTask):
            indexList = [['time', 'Time']]
        if options['LiquidEnthalpy'].attributes['Custimized'] == False:
            self.liq_enthalpy = options['LiquidEnthalpy'].instanciate(name=self.name + "Outlet",
                                                                     varAlias=varAlias, indexList=indexList)
        elif options['LiquidEnthalpy'].attributes['Custimized'] == True:
            self.liq_enthalpy = options['LiquidEnthalpy'].instanciate(name=self.name + "Outlet",
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
        varAlias = {}
        for interfVar in options['BubblePoint'].interfaceVar:
            varAlias[interfVar] = PubPartsUsedVarNames[interfVar]
        if isinstance(self.task, Task.PyomoStaticTask):
            indexList = []
        elif isinstance(self.task, Task.PyomoDynamicTask):
            indexList = [['time', 'Time']]
        if options['BubblePoint'].attributes['Custimized'] == False:
            self.thermo_bubble = options['BubblePoint'].instanciate(name=self.name + "Self",
                                                                    varAlias=varAlias, indexList=indexList)
        elif options['BubblePoint'].attributes['Custimized'] == True:
            self.thermo_bubble = options['BubblePoint'].instanciate(name=self.name + "Self",
                                                                                         varAlias=varAlias,
                                                                                         indexList=indexList,
                                                                                         creatFile=self.options[
                                                                                             'CreateCustimizedFile'])
            inst_param = {}
            for key in options["BubblePoint"].required_param:
                if key == 'temp_span':
                    inst_param['temp_span'] = self.nominal_range[self.name + 'TrayTemp']
                elif key == 'pressure_span':
                    inst_param['pressure_span'] = self.nominal_range[self.name + 'TrayPressure']
            self.thermo_bubble.setParameters(inst_param)
        # -----------------------------
        #      RegisterParts-inst
        # -----------------------------
        self.task.processParts.append(self.liq_enthalpy)
        self.task.processParts.append(self.thermo_bubble)
        # ---------------------------------
        #      Set Input and Output
        # ---------------------------------
        if options['Pressure'] == 'SameWithInlet':
            if isinstance(self.task, Task.PyomoStaticTask):
                dict = {'F': self.name + 'InMFlow',
                        'c': self.name + 'MFrac[#comp#]',
                        'P': self.name + 'Pressure',
                        'h': self.name + 'InMEtlp'
                        }
            elif isinstance(self.task, Task.PyomoDynamicTask):
                dict = {'F': self.name + 'InMFlow[#time#]',
                        'c': self.name + 'MFrac[#time#, #comp#]',
                        'P': self.name + 'Pressure[#time#]',
                        'h': self.name + 'InMEtlp[#time#]'
                        }
            self.inputStreams['Inlet'] = Device.InputStream(self.name + 'Inlet', dict)
        elif options['Pressure'] == 'Other':
            if isinstance(self.task, Task.PyomoStaticTask):
                dict = {'F': self.name + 'InMFlow',
                        'c': self.name + 'MFrac[#comp#]',
                        'h': self.name + 'InMEtlp'
                        }
            elif isinstance(self.task, Task.PyomoDynamicTask):
                dict = {'F': self.name + 'InMFlow[#time#]',
                        'c': self.name + 'MFrac[#time#, #comp#]',
                        'h': self.name + 'InMEtlp[#time#]'
                        }
            self.inputStreams['Inlet'] = Device.InputStream(self.name + 'Inlet', dict)
        if isinstance(self.task, Task.PyomoStaticTask):
            dict = {'F': self.name + 'RefMFlow',
                    'c': self.name + 'MFrac[#comp#]',
                    'h': self.name + 'OutMEtlp',
                    'P': self.name + 'Pressure'
                    }
        elif isinstance(self.task, Task.PyomoDynamicTask):
            dict = {'F': self.name + 'RefMFlow[#time#]',
                    'c': self.name + 'MFrac[#time#, #comp#]',
                    'h': self.name + 'OutMEtlp[#time#]',
                    'P': self.name + 'Pressure[#time#]'
                    }
        output_var = ['c', 'F', 'h', 'P']
        self.outputStreams['Reflux'] = Device.OutputStream(self.name + 'Reflux', dict, output_var)
        if isinstance(self.task, Task.PyomoStaticTask):
            dict = {'F': self.name + 'PrdtMFlow',
                    'c': self.name + 'MFrac[#comp#]',
                    'h': self.name + 'OutMEtlp',
                    'P': self.name + 'Pressure'
                    }
        elif isinstance(self.task, Task.PyomoDynamicTask):
            dict = {'F': self.name + 'PrdtMFlow[#time#]',
                    'c': self.name + 'MFrac[#time#, #comp#]',
                    'h': self.name + 'OutMEtlp[#time#]',
                    'P': self.name + 'Pressure[#time#]'
                    }
        output_var = ['c', 'F', 'h', 'P']
        self.outputStreams['Product'] = Device.OutputStream(self.name + 'Product', dict, output_var)
        if isinstance(self.task, Task.PyomoStaticTask):
            dict = {'Q': self.name + 'MHeatOut',
                    'T': self.name + 'Temp',
                    }
        elif isinstance(self.task, Task.PyomoDynamicTask):
            dict = {'Q': self.name + 'MHeatOut[#time#]',
                    'T': self.name + 'Temp[#time#]',
                    }
        output_var = ['Q','T']
        self.outputStreams['HeatFlow'] = Device.OutputStream(self.name + 'HeatFlow', dict, output_var)

    def generatePublicPEVar(self):
        PE_str = ""
        PE_str += "#--------%s---------\n" % self.name
        if type(self.task) == Task.PyomoPETask:
            if self.options['Pressure'] == 'Other':
                PE_str += ModularTask.ModelingTools.to_pe_public_var("Pressure",
                                                                     self.specifications["Pressure"])
            PE_str += ModularTask.ModelingTools.to_pe_public_var("RefluxRatio",
                                                                     self.specifications["RefluxRatio"])
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
            if isinstance(self.specifications['RefluxRatio'], ModularTask.PE.EstimatedSpec):
                PE_str += ModularTask.ModelingTools.to_pe_constraint("RefluxRatio",1)
        else:
            raise Exception("This is not a PE task.")
        PE_str = PE_str.replace('#model_name#', self.task.name).replace("#device_name#", self.name).replace(
            "#prim_name#", self.primitive_name)
        return PE_str

    def generatePyomoPara(self):
        str = ""
        str += "#--------%s---------\n" % self.name
        if self.options['Pressure'] == 'Other':
            if isinstance(self.task, Task.PyomoStaticTask):
                str += ModularTask.ModelingTools.ss_or_pe_para(self.task, "Pressure",
                                                               self.specifications['Pressure'])
            elif isinstance(self.task, Task.PyomoDynamicTask):
                str += ModularTask.ModelingTools.gen_dynamic_para(self.task, "Pressure",
                                                                  self.specifications['Pressure'])
        if isinstance(self.task, Task.PyomoStaticTask):
            str += ModularTask.ModelingTools.ss_or_pe_para(self.task, "RefluxRatio",
                                                           self.specifications['RefluxRatio'])
        elif isinstance(self.task, Task.PyomoDynamicTask):
            str += ModularTask.ModelingTools.gen_dynamic_para(self.task, "RefluxRatio",
                                                              self.specifications['RefluxRatio'])
        str = str.replace('#model_name#', self.task.name).replace("#device_name#", self.name)
        return str

    def generatePyomoVar(self):
        str = ""
        str += "#--------%s---------\n" % self.name
        if isinstance(self.task, Task.PyomoStaticTask):
            str += "#model_name#.#device_name#RefMFlow = Var(within=NonNegativeReals)\n"
            str += "#model_name#.#device_name#PrdtMFlow = Var(within=NonNegativeReals)\n"
            str += "#model_name#.#device_name#MHeatOut = Var(within=NonNegativeReals)\n"
        elif isinstance(self.task, Task.PyomoDynamicTask):
            str += "#model_name#.#device_name#RefMFlow = Var(#model_name#.Time, within=NonNegativeReals)\n"
            str += "#model_name#.#device_name#PrdtMFlow = Var(#model_name#.Time, within=NonNegativeReals)\n"
            str += "#model_name#.#device_name#MHeatOut = Var(#model_name#.Time, within=NonNegativeReals)\n"
        # str += "#model_name#.#device_name#OutMFrac = Var(#model_name#.Component,bounds=(0,1))\n"
        str += self.thermo_bubble.generatePyomoVar()
        str = str.replace('#model_name#', self.task.name).replace("#device_name#", self.name)
        return str

    def generatePyomoExpression(self):
        str = ""
        str += "#--------%s Enthalpy---------\n" % self.name
        str += self.liq_enthalpy.generatePyomoExpression()
        return str

    def generatePyomoCon(self):
        str = ""
        str += "#--------%s Mass Balance---------\n" % self.name
        str += self.generateMassBalance()
        str += "#--------%s Energy Balance---------\n" % self.name
        str += self.generateEnergyBalance()
        str += "#--------%s Bubble Point---------\n" % self.name
        str += self.thermo_bubble.generatePyomoCon()
        return str

    def generateMassBalance(self):
        str = ""
        if isinstance(self.task, Task.PyomoStaticTask):
            str += "def #device_name#MassBlnc(m):\n"
            str += "\treturn (m.#device_name#RefMFlow+m.#device_name#PrdtMFlow-m.#device_name#InMFlow)*%f==0\n" % \
                   self.weights['FlowEquWeight']
            str += "#model_name#.#device_name#MassBlnc = Constraint(rule=#device_name#MassBlnc)\n"
            str += "def #device_name#RefSpec(m):\n"
            str += "\treturn (m.#device_name#RefMFlow-m.#device_name#InMFlow*m.#device_name#RefluxRatio)*%f==0\n" % \
                   self.weights['FlowEquWeight']
            str += "#model_name#.#device_name#RefSpec = Constraint(rule=#device_name#RefSpec)\n"
        elif isinstance(self.task, Task.PyomoDynamicTask):
            str += "def #device_name#MassBlnc(m,time):\n"
            str += "\treturn (m.#device_name#RefMFlow[time]+m.#device_name#PrdtMFlow[time]-m.#device_name#InMFlow[time])*%f==0\n"%self.weights['FlowEquWeight']
            str += "#model_name#.#device_name#MassBlnc = Constraint(#model_name#.Time, rule=#device_name#MassBlnc)\n"
            str += "def #device_name#RefSpec(m,time):\n"
            str += "\treturn (m.#device_name#RefMFlow[time]-m.#device_name#InMFlow[time]*m.#device_name#RefluxRatio[time])*%f==0\n"%self.weights['FlowEquWeight']
            str += "#model_name#.#device_name#RefSpec = Constraint(#model_name#.Time, rule=#device_name#RefSpec)\n"
        # str += "def #device_name#OutComp(m, comp):\n"
        # str += "\treturn m.#device_name#InMFrac[comp]-m.#device_name#OutMFrac[comp]==0\n"
        # str += "#model_name#.#device_name#OutComp = Constraint(#model_name#.Component, rule=#device_name#OutComp)\n"
        str = str.replace('#model_name#', self.task.name).replace("#device_name#", self.name)
        return str

    def generateEnergyBalance(self):
        str = ""
        if isinstance(self.task, Task.PyomoStaticTask):
            str += "def #device_name#EngBlnc(m):\n"
            str += "\treturn (m.#device_name#InMFlow*(m.#device_name#InMEtlp-m.#device_name#OutMEtlp)-m.#device_name#MHeatOut)*%f==0\n" % \
                   self.weights['EnthalpyEquWeight']
            str += "#model_name#.#device_name#EngBlnc = Constraint(rule=#device_name#EngBlnc)\n"
        elif isinstance(self.task, Task.PyomoDynamicTask):
            str += "def #device_name#EngBlnc(m,time):\n"
            str += "\treturn (m.#device_name#InMFlow[time]*(m.#device_name#InMEtlp[time]-m.#device_name#OutMEtlp[time])-m.#device_name#MHeatOut[time])*%f==0\n"%self.weights['EnthalpyEquWeight']
            str += "#model_name#.#device_name#EngBlnc = Constraint(#model_name#.Time, rule=#device_name#EngBlnc)\n"
        str = str.replace('#model_name#', self.task.name).replace("#device_name#", self.name)
        return str