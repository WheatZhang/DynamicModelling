#!/usr/bin/env python
#-*- coding:utf-8 -*-
import ModularTask.Device as Device
import ModularTask.Task as Task
import ModularTask

class GeneralStream(Device.PyomoDevice):
    def __init__(self, task, name):
        super().__init__(task, name)
        # ---------------------------------
        #      Set Input and Output
        # ---------------------------------
        if isinstance(self.task, Task.PyomoStaticTask):
            dict = {'c':self.name+'MFrac[#comp#]',
                    'F': self.name + 'MFlow',
                    'T': self.name + 'Temp',
                    'P': self.name + 'Pressure',
                    'h': self.name + 'MEtlp'
                    }
        elif isinstance(self.task, Task.PyomoDynamicTask):
            dict = {'c': self.name + 'MFrac[#time#,#comp#]',
                    'F': self.name + 'MFlow[#time#]',
                    'T': self.name + 'Temp[#time#]',
                    'P': self.name + 'Pressure[#time#]',
                    'h': self.name + 'MEtlp[#time#]'
                    }
        output_var = ['c', 'F', 'T', 'P']
        self.outputStreams['Outlet'] = Device.OutputStream(self.name+'Outlet',dict,output_var)

class TwoPhaseStream(GeneralStream):
    def __init__(self, task, name):
        super().__init__(task, name)
        if isinstance(self.task, Task.PyomoStaticTask):
            self.outputStreams['Outlet'].dict['x'] = self.name+'LiqMFrac[#comp#]'
            self.outputStreams['Outlet'].dict['y'] = self.name + 'VapMFrac[#comp#]'
            self.outputStreams['Outlet'].dict['f'] = self.name + 'MCompFlow[#comp#]'
            self.outputStreams['Outlet'].dict['L'] = self.name + 'LiqMFlow'
            self.outputStreams['Outlet'].dict['V'] = self.name + 'VapMFlow'
            self.outputStreams['Outlet'].dict['VF'] = self.name + 'VF'
        elif isinstance(self.task, Task.PyomoDynamicTask):
            self.outputStreams['Outlet'].dict['x'] = self.name + 'LiqMFrac[#time#, #comp#]'
            self.outputStreams['Outlet'].dict['y'] = self.name + 'VapMFrac[#time#, #comp#]'
            self.outputStreams['Outlet'].dict['f'] = self.name + 'MCompFlow[#time#, #comp#]'
            self.outputStreams['Outlet'].dict['L'] = self.name + 'LiqMFlow[#time#]'
            self.outputStreams['Outlet'].dict['V'] = self.name + 'VapMFlow[#time#]'
            self.outputStreams['Outlet'].dict['VF'] = self.name + 'VF[#time#]'
        self.outputStreams['Outlet'].output_var.append('x')
        self.outputStreams['Outlet'].output_var.append('y')
        self.outputStreams['Outlet'].output_var.append('VF')

        self.optional_specifications = [
            'Pressure',
            'Temp',
            'VF'
        ]
        self.required_specifications = [
            'MFlow',
            'MFrac'
        ]

    def setSpecificaitons(self, specifications):
        if not hasattr(self, 'options'):
            raise Exception("Please set options for the model first in %s." % self.name)
        if len(specifications) != len(self.required_specifications)+2:
            raise Exception("The numbers of specifications for %s in not correct." % self.name)
        for key, value in specifications.items():
            if not key in self.required_specifications:
                if not key in self.optional_specifications:
                    raise Exception("The specifications " + key + "is unavailable.")
        for key in self.required_specifications:
            if key not in specifications.keys():
                raise Exception("The required specifications " + key + "is not designated.")
        self.specifications = specifications

    def setModelingOption(self, options):
        # -----------------------------
        #      Set Options
        # -----------------------------
        available_options = {
            'CompositionThermo': 'ModularTask.Thermodynamics.CompositionThermo',
            'VaporEnthalpy': 'ModularTask.Thermodynamics.VaporEnthalpyThermo',
            'LiquidEnthalpy': 'ModularTask.Thermodynamics.LiquidEnthalpyThermo',
            'CreateCustimizedFile': [False, True]
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
        #        Set Public Parts Used Variable Names
        #  -----------------------------------------
        if isinstance(self.task, Task.PyomoStaticTask):
            PubPartsUsedVarNames = {
                        'x': self.name + 'LiqMFrac[#comp#]',
                        'y': self.name + 'VapMFrac[#comp#]',
                        'T': self.name + 'Temp',
                        'P': self.name + 'Pressure',
                        'hv': self.name + 'VapMEtlp',
                        'hl': self.name + 'LiqMEtlp'
                        }
        elif isinstance(self.task, Task.PyomoDynamicTask):
            PubPartsUsedVarNames = {
                        'x': self.name + 'LiqMFrac[#index#,#comp#]',
                        'y': self.name + 'VapMFrac[#index#,#comp#]',
                        'T': self.name + 'Temp[#index#]',
                        'P': self.name + 'Pressure[#index#]',
                        'hv': self.name + 'VapMEtlp[#index#]',
                        'hl': self.name + 'LiqMEtlp[#index#]'
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
            self.vap_enthalpy = options['VaporEnthalpy'].instanciate(name=self.name + "Self",
                                                                     varAlias=varAlias, indexList=indexList)
        elif options['VaporEnthalpy'].attributes['Custimized'] == True:
            self.vap_enthalpy = options['VaporEnthalpy'].instanciate(name=self.name + "Self",
                                                                                         varAlias=varAlias,
                                                                                         indexList=indexList,
                                                                                         creatFile=self.options[
                                                                                             'CreateCustimizedFile'])
            inst_param = {}
            for key in options["VaporEnthalpy"].required_param:
                if key == 'temp_span':
                    inst_param['temp_span'] = self.nominal_range[self.name + 'TrayTemp']
                elif key == 'pressure_span':
                    inst_param['pressure_span'] = self.nominal_range[self.name + 'TrayPressure']
            self.vap_enthalpy.setParameters(inst_param)
        varAlias = {}
        for interfVar in options['LiquidEnthalpy'].interfaceVar:
            varAlias[interfVar] = PubPartsUsedVarNames[interfVar]
        if isinstance(self.task, Task.PyomoStaticTask):
            indexList = []
        elif isinstance(self.task, Task.PyomoDynamicTask):
            indexList = [['time', 'Time']]
        if options['LiquidEnthalpy'].attributes['Custimized'] == False:
            self.liq_enthalpy = options['LiquidEnthalpy'].instanciate(name=self.name + "Self",
                                                                     varAlias=varAlias, indexList=indexList)
        elif options['LiquidEnthalpy'].attributes['Custimized'] == True:
            self.liq_enthalpy = options['LiquidEnthalpy'].instanciate(name=self.name + "Self",
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
        for interfVar in options['CompositionThermo'].interfaceVar:
            varAlias[interfVar] = PubPartsUsedVarNames[interfVar]
        if isinstance(self.task, Task.PyomoStaticTask):
            indexList = []
        elif isinstance(self.task, Task.PyomoDynamicTask):
            indexList = [['time', 'Time']]
        if options['CompositionThermo'].attributes['Custimized'] == False:
            self.thermo_comp = options['CompositionThermo'].instanciate(name=self.name + "Self",
                                                                     varAlias=varAlias, indexList=indexList)
        elif options['CompositionThermo'].attributes['Custimized'] == True:
            self.thermo_comp = options['CompositionThermo'].instanciate(name=self.name + "Self",
                                                                                         varAlias=varAlias,
                                                                                         indexList=indexList,
                                                                                         creatFile=self.options[
                                                                                             'CreateCustimizedFile'])
            inst_param = {}
            for key in options["CompositionThermo"].required_param:
                if key == 'temp_span':
                    inst_param['temp_span'] = self.nominal_range[self.name + 'TrayTemp']
                elif key == 'pressure_span':
                    inst_param['pressure_span'] = self.nominal_range[self.name + 'TrayPressure']
            self.thermo_comp.setParameters(inst_param)
        # -----------------------------
        #      RegisterParts-inst
        # -----------------------------
        self.task.processParts.append(self.vap_enthalpy)
        self.task.processParts.append(self.liq_enthalpy)
        self.task.processParts.append(self.thermo_comp)

    def generatePublicPEVar(self):
        PE_str = ""
        PE_str += "#--------%s---------\n" % self.name
        if type(self.task) == Task.PyomoPETask:
            for key, value in self.specifications.items():
                if key == 'MFlow':
                    PE_str += ModularTask.ModelingTools.to_pe_public_var("MFlow", value)
                elif key == 'MFrac':
                    if type(value) == ModularTask.PE.EstimatedSpec:
                        raise Exception("Indexed parameter esitmation is currently not supported.")
                elif key == 'Pressure':
                    PE_str += ModularTask.ModelingTools.to_pe_public_var("Pressure", value)
                elif key == 'Temp':
                    PE_str += ModularTask.ModelingTools.to_pe_public_var("Temp", value)
                elif key == 'VF':
                    PE_str += ModularTask.ModelingTools.to_pe_public_var("VF", value)
                else:
                    raise Exception("Unknown specifications in %s."%self.name)
        else:
            raise Exception("This is not a PE task.")
        PE_str = PE_str.replace('#model_name#', self.task.name).replace("#device_name#", self.name).replace(
            "#prim_name#", self.primitive_name)
        return PE_str

    def generatePEConstraint(self):
        PE_str = ""
        PE_str += "#--------%s---------\n" % self.name
        if type(self.task) == Task.PyomoPETask:
            for key, value in self.specifications.items():
                if key == 'MFlow':
                    if isinstance(value, ModularTask.PE.EstimatedSpec):
                        PE_str += ModularTask.ModelingTools.to_pe_constraint("MFlow", 1e-3)
                elif key == 'MFrac':
                    if type(value) == ModularTask.PE.EstimatedSpec:
                        raise Exception("Indexed parameter esitmation is currently not supported.")
                elif key == 'Pressure':
                    if isinstance(value, ModularTask.PE.EstimatedSpec):
                        PE_str += ModularTask.ModelingTools.to_pe_constraint("Pressure", 1e-3)
                elif key == 'Temp':
                    if isinstance(value, ModularTask.PE.EstimatedSpec):
                        PE_str += ModularTask.ModelingTools.to_pe_constraint("Temp", 1e-2)
                elif key == 'VF':
                    if isinstance(value, ModularTask.PE.EstimatedSpec):
                        PE_str += ModularTask.ModelingTools.to_pe_constraint("VF", 1)
                else:
                    raise Exception("Unknown specifications in %s."%self.name)
        else:
            raise Exception("This is not a PE task.")
        PE_str = PE_str.replace('#model_name#', self.task.name).replace("#device_name#", self.name).replace(
            "#prim_name#", self.primitive_name)
        return PE_str

    def generatePyomoPara(self):
        equ_str = ""
        equ_str += "#--------%s---------\n" % self.name
        if isinstance(self.task, Task.PyomoStaticTask):
            for key,value in self.specifications.items():
                if key == 'MFlow':
                    equ_str += ModularTask.ModelingTools.ss_or_pe_para(self.task, "MFlow", value)
                elif key == 'MFrac':
                    equ_str += "#model_name#.#device_name#MFrac = Param(#model_name#.Component, initialize = %s)\n" % str(
                        value)
                elif key == 'Pressure':
                    equ_str += ModularTask.ModelingTools.ss_or_pe_para(self.task, "Pressure", value)
                elif key == 'Temp':
                    equ_str += ModularTask.ModelingTools.ss_or_pe_para(self.task, "Temp", value)
                elif key == 'VF':
                    equ_str += ModularTask.ModelingTools.ss_or_pe_para(self.task, "VF", value)
                else:
                    raise Exception("Unknown specifications in %s."%self.name)
        elif isinstance(self.task, Task.PyomoDynamicTask):
            for key,value in self.specifications.items():
                if key == 'MFlow':
                    equ_str += ModularTask.ModelingTools.gen_dynamic_para(self.task, "MFlow", value)
                elif key == 'MFrac':
                    equ_str += ModularTask.ModelingTools.gen_dynamic_para(self.task, "MFrac", value,
                                                                          index_list=["Component"])
                elif key == 'Pressure':
                    equ_str += ModularTask.ModelingTools.gen_dynamic_para(self.task, "Pressure", value)
                elif key == 'Temp':
                    equ_str += ModularTask.ModelingTools.gen_dynamic_para(self.task, "Temp", value)
                elif key == 'VF':
                    equ_str += ModularTask.ModelingTools.gen_dynamic_para(self.task, "VF", value)
                else:
                    raise Exception("Unknown specifications in %s."%self.name)
        equ_str = equ_str.replace('#model_name#', self.task.name).replace("#device_name#", self.name)
        return equ_str

    def generatePyomoVar(self):
        str = ""
        str += "#--------%s---------\n" % self.name
        for i in self.optional_specifications:
            if i not in self.specifications.keys():
                if isinstance(self.task, Task.PyomoStaticTask):
                    if i == 'Pressure':
                        str += "#model_name#.#device_name#Pressure = Var()\n"
                    elif i == 'Temp':
                        str += "#model_name#.#device_name#Temp = Var()\n"
                    elif i == 'VF':
                        str += "#model_name#.#device_name#VF = Var(bounds = (0,1)\n"
                elif isinstance(self.task, Task.PyomoDynamicTask):
                    if i == 'Pressure':
                        str += "#model_name#.#device_name#Pressure = Var(#model_name#.Time)\n"
                    elif i == 'Temp':
                        str += "#model_name#.#device_name#Temp = Var(#model_name#.Time)\n"
                    elif i == 'VF':
                        str += "#model_name#.#device_name#VF = Var(#model_name#.Time, bounds = (0,1)\n"
        str += self.thermo_comp.generatePyomoVar()
        str = str.replace('#model_name#', self.task.name).replace("#device_name#", self.name)
        return str

    def generatePyomoExpression(self):
        str = ""
        if 'f' in self.outputStreams['Outlet'].output_needed.keys():
            str += "#--------%s Component Flowrate---------\n" % self.name
            if isinstance(self.task, Task.PyomoStaticTask):
                str += "def #device_name#MCompFlow(m, comp):\n"
                str += "\treturn m.#device_name#MFrac[comp] * m.#device_name#MFlow\n"
                str += "#model_name#.#device_name#MCompFlow = Expression(#model_name#.Component, rule=#device_name#MCompFlow)\n"
            elif isinstance(self.task, Task.PyomoDynamicTask):
                str += "def #device_name#MCompFlow(m, time, comp):\n"
                str += "\treturn m.#device_name#MFrac[time, comp] * m.#device_name#MFlow[time]\n"
                str += "#model_name#.#device_name#MCompFlow = Expression(#model_name#.Time, #model_name#.Component, rule=#device_name#MCompFlow)\n"
        if 'V' in self.outputStreams['Outlet'].output_needed.keys():
            str += "#--------%s Vapor Phase Flowrate---------\n" % self.name
            if isinstance(self.task, Task.PyomoStaticTask):
                str += "def #device_name#VapMFlow(m, comp):\n"
                str += "\treturn m.#device_name#VF * m.#device_name#MFlow\n"
                str += "#model_name#.#device_name#VapMFlow = Expression(rule=#device_name#VapMFlow)\n"
            elif isinstance(self.task, Task.PyomoDynamicTask):
                str += "def #device_name#VapMFlow(m, time, comp):\n"
                str += "\treturn m.#device_name#VF[time] * m.#device_name#MFlow[time]\n"
                str += "#model_name#.#device_name#VapMFlow = Expression(#model_name#.Time, rule=#device_name#VapMFlow)\n"
        if 'L' in self.outputStreams['Outlet'].output_needed.keys():
            str += "#--------%s Liquid Phase Flowrate---------\n" % self.name
            if isinstance(self.task, Task.PyomoStaticTask):
                str += "def #device_name#LiqMFlow(m, comp):\n"
                str += "\treturn (1-m.#device_name#VF) * m.#device_name#MFlow\n"
                str += "#model_name#.#device_name#LiqMFlow = Expression(rule=#device_name#LiqMFlow)\n"
            elif isinstance(self.task, Task.PyomoDynamicTask):
                str += "def #device_name#LiqMFlow(m, time, comp):\n"
                str += "\treturn (1-m.#device_name#VF[time]) * m.#device_name#MFlow[time]\n"
                str += "#model_name#.#device_name#LiqMFlow = Expression(#model_name#.Time, rule=#device_name#LiqMFlow)\n"
        str += "#--------%s Enthalpy---------\n" % self.name
        str += self.vap_enthalpy.generatePyomoExpression()
        str += self.liq_enthalpy.generatePyomoExpression()
        if isinstance(self.task, Task.PyomoStaticTask):
            str += "def #device_name#MEtlp(m):\n"
            str += "\treturn m.#device_name#LiqMEtlp * (1-m.#device_name#VF)+m.#device_name#VapMEtlp * m.#device_name#VF\n"
            str += "#model_name#.#device_name#MEtlp = Expression(rule=#device_name#MEtlp)\n"
        elif isinstance(self.task, Task.PyomoDynamicTask):
            str += "def #device_name#MEtlp(m, time):\n"
            str += "\treturn m.#device_name#LiqMEtlp[time] * (1-m.#device_name#VF[time])+m.#device_name#VapMEtlp[time] * m.#device_name#VF[time]\n"
            str += "#model_name#.#device_name#MEtlp = Expression(#model_name#.Time, rule=#device_name#MEtlp)\n"
        str = str.replace('#model_name#', self.task.name).replace("#device_name#", self.name)
        return str

    def generatePyomoCon(self):
        str = ""
        str += "#--------%s Mass Balance---------\n" % self.name
        str += self.generateMassBalance()
        str += "#--------%s Phase Equilibrium---------\n" % self.name
        str += self.generateEquilibrium()
        str += "#--------%s Summation---------\n" % self.name
        str += self.generateSummation()
        return str

    def generateMassBalance(self):
        str = ""
        if isinstance(self.task, Task.PyomoStaticTask):
            for i in range(0,len(self.task.component)-1):
                str += "def #device_name#MassBlnc%d(m):\n"%i
                str += "\treturn m.#device_name#VF * m.#device_name#VapMFrac['%s'] + \\\n" % self.task.component[i]
                str += "(1 - m.#device_name#VF)*m.#device_name#LiqMFrac['%s'] - m.#device_name#MFrac['%s'] == 0\n" % (
                self.task.component[i], self.task.component[i])
                str += "#model_name#.#device_name#MassBlnc%d = Constraint(rule=#device_name#MassBlnc%d)\n"%(i,i)
        elif isinstance(self.task, Task.PyomoDynamicTask):
            for i in range(0, len(self.task.component) - 1):
                str +="def #device_name#MassBlnc%d(m, time):\n"%i
                str += "\treturn m.#device_name#VF[time] * m.#device_name#VapMFrac[time, '%s'] + \\\n" % self.task.component[i]
                str += "(1 - m.#device_name#VF[time])*m.#device_name#LiqMFrac[time, '%s'] - m.#device_name#MFrac[time, '%s'] == 0\n" %(self.task.component[i],self.task.component[i])
                str += "#model_name#.#device_name#MassBlnc%d = Constraint(#model_name#.Time, rule=#device_name#MassBlnc%d)\n"%(i,i)
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
            str += "\treturn sum([m.#device_name#LiqMFrac[c] for c in m.Component]) == 1\n"
            str += "#model_name#.#device_name#LiqSum = Constraint(rule=#device_name#LiqSum)\n"
        elif isinstance(self.task, Task.PyomoDynamicTask):
            str += "def #device_name#LiqSum(m, time):\n"
            str += "\treturn sum([m.#device_name#LiqMFrac[time, c] for c in m.Component]) == 1\n"
            str += "#model_name#.#device_name#LiqSum = Constraint(#model_name#.Time, rule=#device_name#LiqSum)\n"
        if isinstance(self.task, Task.PyomoStaticTask):
            str += "def #device_name#VapSum(m):\n"
            str += "\treturn sum([m.#device_name#VapMFrac[c] for c in m.Component]) == 1\n"
            str += "#model_name#.#device_name#VapSum = Constraint(rule=#device_name#VapSum)\n"
        elif isinstance(self.task, Task.PyomoDynamicTask):
            str += "def #device_name#VapSum(m, time):\n"
            str += "\treturn sum([m.#device_name#VapMFrac[time, c] for c in m.Component]) == 1\n"
            str += "#model_name#.#device_name#VapSum = Constraint(#model_name#.Time, rule=#device_name#VapSum)\n"
        str = str.replace('#model_name#', self.task.name).replace("#device_name#", self.name)
        return str

class GeneralHeatStream(Device.PyomoDevice):
    def __init__(self, task, name):
        super().__init__(task, name)
        if isinstance(self.task, Task.PyomoStaticTask):
            dict = {'T': self.name + 'Temp[time]',
                    'Q': self.name + 'Heat[time]'
                    }
        elif isinstance(self,task, Task.PyomoDynamicTask):
            dict = {'T': self.name + 'Temp',
                    'Q': self.name + 'Heat'
                    }
        output_var = ['Q', 'T']
        self.outputStreams['Outlet'] = Device.OutputStream(self.name + 'Outlet', dict, output_var)
        self.required_specifications = [
            'Temp',
            'HeatFlow'
        ]

    def setSpecificaitons(self, specifications):
        self.setDeviceSpecs(self.required_specifications, specifications)

    def generatePublicPEVar(self):
        PE_str = ""
        PE_str += "#--------%s---------\n" % self.name
        if type(self.task) == Task.PyomoPETask:
            PE_str += ModularTask.ModelingTools.to_pe_public_var("Temp",
                                                                     self.specifications["Temp"])
            PE_str += ModularTask.ModelingTools.to_pe_public_var("Heat",
                                                                 self.specifications["HeatFlow"])
        else:
            raise Exception("This is not a PE task.")
        PE_str = PE_str.replace('#model_name#', self.task.name).replace("#device_name#", self.name).replace(
            "#prim_name#", self.primitive_name)
        return PE_str

    def generatePEConstraint(self):
        PE_str = ""
        PE_str += "#--------%s---------\n" % self.name
        if type(self.task) == Task.PyomoPETask:
            if isinstance(self.specifications['Temp'], ModularTask.PE.EstimatedSpec):
                PE_str += ModularTask.ModelingTools.to_pe_constraint("Temp", 1e-2)
            if isinstance(self.specifications['HeatFlow'], ModularTask.PE.EstimatedSpec):
                PE_str += ModularTask.ModelingTools.to_pe_constraint("Heat", 1e-6)
        else:
            raise Exception("This is not a PE task.")
        PE_str = PE_str.replace('#model_name#', self.task.name).replace("#device_name#", self.name).replace(
            "#prim_name#", self.primitive_name)
        return PE_str

    def generatePyomoPara(self):
        equ_str = ""
        equ_str += "#--------%s---------\n" % self.name
        if isinstance(self.task, Task.PyomoStaticTask):
            equ_str += ModularTask.ModelingTools.ss_or_pe_para(self.task, "Temp", self.specifications['Temp'])
            equ_str += ModularTask.ModelingTools.ss_or_pe_para(self.task, "Heat", self.specifications['HeatFlow'])
        elif isinstance(self,task, Task.PyomoDynamicTask):
            equ_str += ModularTask.ModelingTools.gen_dynamic_para(self.task, "Temp", self.specifications['Temp'])
            equ_str += ModularTask.ModelingTools.gen_dynamic_para(self.task, "Heat", self.specifications['HeatFlow'])
        equ_str = equ_str.replace('#model_name#', self.task.name).replace("#device_name#", self.name)
        return equ_str

class VaporPhaseStream(GeneralStream):
    def __init__(self, task, name):
        super().__init__(task, name)
        # ---------------------------------
        #      Set Input and Output
        # ---------------------------------
        if isinstance(self.task, Task.PyomoStaticTask):
            self.outputStreams['Outlet'].dict['y'] = self.name + 'MFrac[#comp#]'
            self.outputStreams['Outlet'].dict['V'] = self.name + 'MFlow'
            self.outputStreams['Outlet'].dict['hv'] = self.name + 'MEtlp'
        elif isinstance(self.task, Task.PyomoDynamicTask):
            self.outputStreams['Outlet'].dict['y'] = self.name + 'MFrac[time,#comp#]'
            self.outputStreams['Outlet'].dict['V'] = self.name + 'MFlow[time]'
            self.outputStreams['Outlet'].dict['hv'] = self.name + 'MEtlp[time]'

        self.required_specifications = [
            'MFlow',
            'MFrac',
            'Pressure',
            'Temp'
        ]

    def setSpecificaitons(self, specifications):
        if not hasattr(self, 'options'):
            raise Exception("Please set options for the model first in %s." % self.name)
        self.setDeviceSpecs(self.required_specifications, specifications)

    def setModelingOption(self, options):
        # -----------------------------
        #      Set Options
        # -----------------------------
        available_options = {
            'VaporEnthalpy': 'ModularTask.Thermodynamics.VaporEnthalpyThermo',
        }
        self.setDeviceOptions(available_options, options)
        # -----------------------------
        #      RegisterParts
        # -----------------------------
        if options['VaporEnthalpy'] not in self.task.processParts:
            self.task.processParts.append(options['VaporEnthalpy'])
        # ----------------------------------------
        #        Set Public Parts Used Variable Names
        #  -----------------------------------------
        if isinstance(self.task, Task.PyomoStaticTask):
            PubPartsUsedVarNames = {
                'y': self.name + 'MFrac[#comp#]',
                'T': self.name + 'Temp',
                'P': self.name + 'Pressure',
                'hv': self.name + 'MEtlp'
            }
        elif isinstance(self.task, Task.PyomoDynamicTask):
            PubPartsUsedVarNames = {
                'y': self.name + 'MFrac[#index#,#comp#]',
                'T': self.name + 'Temp[#index#]',
                'P': self.name + 'Pressure[#index#]',
                'hv': self.name + 'MEtlp[#index#]'
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
            self.vap_enthalpy = options['VaporEnthalpy'].instanciate(name=self.name + "Self",
                                                                      varAlias=varAlias, indexList=indexList)
        elif options['VaporEnthalpy'].attributes['Custimized'] == True:
            self.vap_enthalpy = options['VaporEnthalpy'].instanciate(name=self.name + "Self",
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
        # -----------------------------
        #      RegisterParts-inst
        # -----------------------------
        self.task.processParts.append(self.vap_enthalpy)

    def generatePublicPEVar(self):
        PE_str = ""
        PE_str += "#--------%s---------\n" % self.name
        if type(self.task) == Task.PyomoPETask:
            for key, value in self.specifications.items():
                if key == 'MFlow':
                    PE_str += ModularTask.ModelingTools.to_pe_public_var("MFlow", value)
                elif key == 'MFrac':
                    if type(value) == ModularTask.PE.EstimatedSpec:
                        raise Exception("Indexed parameter esitmation is currently not supported.")
                elif key == 'Pressure':
                    PE_str += ModularTask.ModelingTools.to_pe_public_var("Pressure", value)
                elif key == 'Temp':
                    PE_str += ModularTask.ModelingTools.to_pe_public_var("Temp", value)
                else:
                    raise Exception("Unknown specifications in %s."%self.name)
        else:
            raise Exception("This is not a PE task.")
        PE_str = PE_str.replace('#model_name#', self.task.name).replace("#device_name#", self.name).replace(
            "#prim_name#", self.primitive_name)
        return PE_str

    def generatePEConstraint(self):
        PE_str = ""
        PE_str += "#--------%s---------\n" % self.name
        if type(self.task) == Task.PyomoPETask:
            for key, value in self.specifications.items():
                if key == 'MFlow':
                    if isinstance(value, ModularTask.PE.EstimatedSpec):
                        PE_str += ModularTask.ModelingTools.to_pe_constraint("MFlow", 1e-3)
                elif key == 'MFrac':
                    if type(value) == ModularTask.PE.EstimatedSpec:
                        raise Exception("Indexed parameter esitmation is currently not supported.")
                elif key == 'Pressure':
                    if isinstance(value, ModularTask.PE.EstimatedSpec):
                        PE_str += ModularTask.ModelingTools.to_pe_constraint("Pressure", 1e-3)
                elif key == 'Temp':
                    if isinstance(value, ModularTask.PE.EstimatedSpec):
                        PE_str += ModularTask.ModelingTools.to_pe_constraint("Temp", 1e-2)
                else:
                    raise Exception("Unknown specifications in %s."%self.name)
        else:
            raise Exception("This is not a PE task.")
        PE_str = PE_str.replace('#model_name#', self.task.name).replace("#device_name#", self.name).replace(
            "#prim_name#", self.primitive_name)
        return PE_str

    def generatePyomoPara(self):
        equ_str = ""
        equ_str += "#--------%s---------\n" % self.name
        if isinstance(self.task, Task.PyomoStaticTask):
            for key, value in self.specifications.items():
                if key == 'MFlow':
                    equ_str += ModularTask.ModelingTools.ss_or_pe_para(self.task, "MFlow", value)
                elif key == 'MFrac':
                    equ_str += "#model_name#.#device_name#MFrac = Param(#model_name#.Component, initialize = %s)\n" % str(
                        value)
                elif key == 'Pressure':
                    equ_str += ModularTask.ModelingTools.ss_or_pe_para(self.task, "Pressure", value)
                elif key == 'Temp':
                    equ_str += ModularTask.ModelingTools.ss_or_pe_para(self.task, "Temp", value)
                else:
                    raise Exception("Unknown specifications in %s." % self.name)
        elif isinstance(self,task, Task.PyomoDynamicTask):
            for key,value in self.specifications.items():
                if key == 'MFlow':
                    equ_str += ModularTask.ModelingTools.gen_dynamic_para(self.task, "MFlow",value)
                elif key == 'MFrac':
                    equ_str += ModularTask.ModelingTools.gen_dynamic_para(self.task, "MFrac", value,index_list = ["Component"])
                elif key == 'Pressure':
                    equ_str += ModularTask.ModelingTools.gen_dynamic_para(self.task, "Pressure", value)
                elif key == 'Temp':
                    equ_str += ModularTask.ModelingTools.gen_dynamic_para(self.task, "Temp", value)
                else:
                    raise Exception("Unknown specifications in %s."%self.name)
        equ_str = equ_str.replace('#model_name#', self.task.name).replace("#device_name#", self.name)
        return equ_str

    def generatePyomoExpression(self):
        str = ""
        str += "#--------%s Enthalpy---------\n" % self.name
        str += self.vap_enthalpy.generatePyomoExpression()
        str = str.replace('#model_name#', self.task.name).replace("#device_name#", self.name)
        return str

class LiquidPhaseStream(GeneralStream):
    def __init__(self, task, name):
        super().__init__(task, name)
        # ---------------------------------
        #      Set Input and Output
        # ---------------------------------
        if isinstance(self.task, Task.PyomoStaticTask):
            self.outputStreams['Outlet'].dict['x'] = self.name + 'MFrac[#comp#]'
            self.outputStreams['Outlet'].dict['L'] = self.name + 'MFlow'
            self.outputStreams['Outlet'].dict['hl'] = self.name + 'MEtlp'
        elif isinstance(self.task, Task.PyomoDynamicTask):
            self.outputStreams['Outlet'].dict['x'] = self.name + 'MFrac[time.#comp#]'
            self.outputStreams['Outlet'].dict['L'] = self.name + 'MFlow[time]'
            self.outputStreams['Outlet'].dict['hl'] = self.name + 'MEtlp[time]'

        self.required_specifications = [
            'MFlow',
            'MFrac',
            'Pressure',
            'Temp'
        ]

    def setSpecificaitons(self, specifications):
        if not hasattr(self, 'options'):
            raise Exception("Please set options for the model first in %s." % self.name)
        self.setDeviceSpecs(self.required_specifications, specifications)

    def setModelingOption(self, options):
        # -----------------------------
        #      Set Options
        # -----------------------------
        available_options = {
            'LiquidEnthalpy': 'ModularTask.Thermodynamics.LiquidEnthalpyThermo',
        }
        self.setDeviceOptions(available_options, options)
        # -----------------------------
        #      RegisterParts
        # -----------------------------
        if options['LiquidEnthalpy'] not in self.task.processParts:
            self.task.processParts.append(options['LiquidEnthalpy'])
        # ----------------------------------------
        #        Set Public Parts Used Variable Names
        #  -----------------------------------------
        if isinstance(self.task, Task.PyomoStaticTask):
            PubPartsUsedVarNames = {
                'x': self.name + 'MFrac[#comp#]',
                'T': self.name + 'Temp',
                'P': self.name + 'Pressure',
                'hl': self.name + 'MEtlp'
            }
        elif isinstance(self.task, Task.PyomoDynamicTask):
            PubPartsUsedVarNames = {
                'x': self.name + 'MFrac[#index#,#comp#]',
                'T': self.name + 'Temp[#index#]',
                'P': self.name + 'Pressure[#index#]',
                'hl': self.name + 'MEtlp[#index#]'
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
            self.liq_enthalpy = options['LiquidEnthalpy'].instanciate(name=self.name + "Self",
                                                                     varAlias=varAlias, indexList=indexList)
        elif options['LiquidEnthalpy'].attributes['Custimized'] == True:
            self.liq_enthalpy = options['LiquidEnthalpy'].instanciate(name=self.name + "Self",
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
        # -----------------------------
        #      RegisterParts-inst
        # -----------------------------
        self.task.processParts.append(self.liq_enthalpy)

    def generatePublicPEVar(self):
        PE_str = ""
        PE_str += "#--------%s---------\n" % self.name
        if type(self.task) == Task.PyomoPETask:
            for key, value in self.specifications.items():
                if key == 'MFlow':
                    PE_str += ModularTask.ModelingTools.to_pe_public_var("MFlow", value)
                elif key == 'MFrac':
                    if type(value) == ModularTask.PE.EstimatedSpec:
                        raise Exception("Indexed parameter esitmation is currently not supported.")
                elif key == 'Pressure':
                    PE_str += ModularTask.ModelingTools.to_pe_public_var("Pressure", value)
                elif key == 'Temp':
                    PE_str += ModularTask.ModelingTools.to_pe_public_var("Temp", value)
                else:
                    raise Exception("Unknown specifications in %s."%self.name)
        else:
            raise Exception("This is not a PE task.")
        PE_str = PE_str.replace('#model_name#', self.task.name).replace("#device_name#", self.name).replace(
            "#prim_name#", self.primitive_name)
        return PE_str

    def generatePEConstraint(self):
        PE_str = ""
        PE_str += "#--------%s---------\n" % self.name
        if type(self.task) == Task.PyomoPETask:
            for key, value in self.specifications.items():
                if key == 'MFlow':
                    if isinstance(value, ModularTask.PE.EstimatedSpec):
                        PE_str += ModularTask.ModelingTools.to_pe_constraint("MFlow", 1e-3)
                elif key == 'MFrac':
                    if type(value) == ModularTask.PE.EstimatedSpec:
                        raise Exception("Indexed parameter esitmation is currently not supported.")
                elif key == 'Pressure':
                    if isinstance(value, ModularTask.PE.EstimatedSpec):
                        PE_str += ModularTask.ModelingTools.to_pe_constraint("Pressure", 1e-3)
                elif key == 'Temp':
                    if isinstance(value, ModularTask.PE.EstimatedSpec):
                        PE_str += ModularTask.ModelingTools.to_pe_constraint("Temp", 1e-2)
                else:
                    raise Exception("Unknown specifications in %s."%self.name)
        else:
            raise Exception("This is not a PE task.")
        PE_str = PE_str.replace('#model_name#', self.task.name).replace("#device_name#", self.name).replace(
            "#prim_name#", self.primitive_name)
        return PE_str

    def generatePyomoPara(self):
        equ_str = ""
        equ_str += "#--------%s---------\n" % self.name
        if isinstance(self.task, Task.PyomoStaticTask):
            for key, value in self.specifications.items():
                if key == 'MFlow':
                    equ_str += ModularTask.ModelingTools.ss_or_pe_para(self.task, "MFlow", value)
                elif key == 'MFrac':
                    equ_str += "#model_name#.#device_name#MFrac = Param(#model_name#.Component, initialize = %s)\n" % str(
                        value)
                elif key == 'Pressure':
                    equ_str += ModularTask.ModelingTools.ss_or_pe_para(self.task, "Pressure", value)
                elif key == 'Temp':
                    equ_str += ModularTask.ModelingTools.ss_or_pe_para(self.task, "Temp", value)
                else:
                    raise Exception("Unknown specifications in %s." % self.name)
        elif isinstance(self,task, Task.PyomoDynamicTask):
            for key,value in self.specifications.items():
                if key == 'MFlow':
                    equ_str += ModularTask.ModelingTools.gen_dynamic_para(self.task, "MFlow",value)
                elif key == 'MFrac':
                    equ_str += ModularTask.ModelingTools.gen_dynamic_para(self.task, "MFrac", value,index_list = ["Component"])
                elif key == 'Pressure':
                    equ_str += ModularTask.ModelingTools.gen_dynamic_para(self.task, "Pressure", value)
                elif key == 'Temp':
                    equ_str += ModularTask.ModelingTools.gen_dynamic_para(self.task, "Temp", value)
                else:
                    raise Exception("Unknown specifications in %s."%self.name)
        equ_str = equ_str.replace('#model_name#', self.task.name).replace("#device_name#", self.name)
        return equ_str

    def generatePyomoExpression(self):
        str = ""
        str += "#--------%s Enthalpy---------\n" % self.name
        str += self.liq_enthalpy.generatePyomoExpression()
        str = str.replace('#model_name#', self.task.name).replace("#device_name#", self.name)
        return str