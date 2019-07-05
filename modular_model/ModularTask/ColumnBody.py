#!/usr/bin/env python
#-*- coding:utf-8 -*-
import ModularTask.Device as Device
import ModularTask.Task as Task
import ModularTask.Thermodynamics

class GeneralColumnBody(Device.PyomoDevice):
    def __init__(self, task, name):
        super().__init__(task, name)

    def setTrayInfo(self, numberOfTray, feeds, extractions):
        self.numberOfTray = numberOfTray
        if feeds == None:
            raise Exception("A column body must has at least one feed.")
        else:
            self.feeds = feeds
        if extractions == None:
            self.extractions = {}
        else:
            self.extractions = extractions
        self.specialTrays = []

    def setConstraintWeight(self, weights):
        required_weights = [
            'FlowEquWeight',
            'EnthalpyEquWeight',
            'PressureEquWeight'
        ]
        if len(weights) != len(required_weights):
            raise Exception("The numbers of constraint weights for %s in not correct." % self.name)
        for key, value in weights.items():
            if not key in required_weights:
                raise Exception("The constraint weight " + key + "is unavailable.")
        self.weights = weights
        if isinstance(self.task, Task.PyomoDynamicTask):
            weights = {
                'FlowEquWeight': self.weights['FlowEquWeight']
            }
            self.hydraulics.setWeights(weights)

    def setSpecificaitons(self, specifications):
        if not hasattr(self, 'options'):
            raise Exception("Please set options for the model first in %s." % self.name)
        required_specifications = [
            'TopPressure',
            'BtmPressure'
        ]
        for i in self.extractions.keys():
            required_specifications.append("Ext%dMFlow"%i)
        if self.options["TrayHeatLeakage"]:
            required_specifications.append("UALeakage" )
            required_specifications.append("AmbientTemp")
        self.setDeviceSpecs(required_specifications, specifications)

    def setModelingOption(self, options):
        # -----------------------------
        #      Set Options
        # -----------------------------
        if isinstance(self.task, Task.PyomoStaticTask):
            available_options = {
                'TrayEfficiency': [False, True],
                'TrayHeatLeakage': [False, True],
                'CompositionThermo': 'ModularTask.Thermodynamics.CompositionThermo',
                'VaporEnthalpy': 'ModularTask.Thermodynamics.VaporEnthalpyThermo',
                'LiquidEnthalpy': 'ModularTask.Thermodynamics.LiquidEnthalpyThermo',
                'PressureProfile': ['SimpleLinear', 'VaporFeedDepend'],
                'CreateCustimizedFile' : [True, False]
            }
        elif isinstance(self.task, Task.PyomoDynamicTask):
            available_options = {
                'TrayEfficiency': [False, True],
                'TrayHeatLeakage': [False, True],
                'FloodingConstraint': [False, True],
                'FloodingIndication': [False, True],
                'SumpLevelControl': [False, True],
                'CompositionThermo': 'ModularTask.Thermodynamics.CompositionThermo',
                'VaporEnthalpy': 'ModularTask.Thermodynamics.VaporEnthalpyThermo',
                'LiquidEnthalpy': 'ModularTask.Thermodynamics.LiquidEnthalpyThermo',
                'IndexReduRelatedThermo': 'ModularTask.Thermodynamics.IndexReduRelatedThermo',
                'Hydraulics': 'ModularTask.Hydraulics.Hydraulics',
                'PressureProfile': ['SimpleLinear', 'VaporFeedDepend'],
                'CreateCustimizedFile' : [True, False]
            }
        self.setDeviceOptions(available_options, options)
        #-----------------------------
        #      RegisterParts
        #-----------------------------
        if options['CompositionThermo'] not in self.task.processParts:
            self.task.processParts.append(options['CompositionThermo'])
        if options['VaporEnthalpy'] not in self.task.processParts:
            self.task.processParts.append(options['VaporEnthalpy'])
        if options['LiquidEnthalpy'] not in self.task.processParts:
            self.task.processParts.append(options['LiquidEnthalpy'])
        if isinstance(self.task, Task.PyomoDynamicTask):
            if options['Hydraulics'] not in self.task.processParts:
                self.task.processParts.append(options['Hydraulics'])
            if options['IndexReduRelatedThermo'] not in self.task.processParts:
                self.task.processParts.append(options['IndexReduRelatedThermo'])
        # ----------------------------------------
        #      Set Public Parts Used Variable Names
        # -----------------------------------------
        if isinstance(self.task, Task.PyomoStaticTask):
            PubPartsUsedVarNames = {
                'y': self.name + 'VapLvMFrac[#index#,#comp#]',
                        'T': self.name + 'TrayTemp[#index#]',
                        'P': self.name + 'TrayPressure[#index#]',
                        'hv': self.name + 'VapLvMEtlp[#index#]',
                        'x': self.name + 'LiqLvMFrac[#index#,#comp#]',
                        'hl': self.name + 'LiqLvMEtlp[#index#]',
                        'L': self.name + 'LiqLvMFlow[#index#]'
            }
        elif isinstance(self.task, Task.PyomoDynamicTask):
            PubPartsUsedVarNames = {
                        'y': self.name + 'VapLvMFrac[#index#,#comp#]',
                        'T': self.name + 'TrayTemp[#index#]',
                        'P': self.name + 'TrayPressure[#index#]',
                        'hv': self.name + 'VapLvMEtlp[#index#]',
                        'x': self.name + 'LiqLvMFrac[#index#,#comp#]',
                        'hl': self.name + 'LiqLvMEtlp[#index#]',
                        'DtP': self.name + 'DtTrayPressure[#index#]',
                        'DtT': self.name + 'DtTrayTemp[#index#]',
                        'Dtm': self.name + 'DtTrayMHldp[#index#,#comp#]',
                        'PTh': self.name + 'PTTrayMEtlpHldp[#index#]',
                        'PPh': self.name + 'PPTrayMEtlpHldp[#index#]',
                        'Pxh': self.name + 'PxTrayMEtlpHldp[#index#,#comp#]',
                        'Dtx': self.name + 'DtLiqLvMFrac[#index#,#comp#]',
                        'M': self.name + 'TrayMHldp[#index#]',
                        'L': self.name + 'LiqLvMFlow[#index#]',
                        'DtM': self.name + 'DtTrayMHldp[#index#]',
                        'DtE': self.name + 'DtTrayMEtlpHldp[#index#]'
                                  }
        # -----------------------------
        #      Set Thermodynamics
        # -----------------------------
        varAlias = {}
        for interfVar in options['VaporEnthalpy'].interfaceVar:
            varAlias[interfVar] = PubPartsUsedVarNames[interfVar]
        if isinstance(self.task, Task.PyomoStaticTask):
            indexList = [['tray', self.name + 'Trays']]
        elif isinstance(self.task, Task.PyomoDynamicTask):
            indexList = [['time', 'Time'], ['tray', self.name + 'Trays']]
        if options['VaporEnthalpy'].attributes['Custimized'] == False:
            self.vap_enthalpy = options['VaporEnthalpy'].instanciate(name=self.name + "AllTrays",
                                                                     varAlias=varAlias, indexList=indexList)
        elif options['VaporEnthalpy'].attributes['Custimized'] == True:
            self.vap_enthalpy = options['VaporEnthalpy'].instanciateColumnThermo(name=self.name + "AllTrays",
                                                                                         varAlias=varAlias,
                                                                                         indexList=indexList,
                                                                                         creatFile=self.options[
                                                                                             'CreateCustimizedFile'])
            inst_param = {}
            for i in range(1, self.numberOfTray + 1):
                inst_param[i] = {}
                for key in options["VaporEnthalpy"].required_param:
                    if key == 'temp_span':
                        inst_param[i]['temp_span'] = self.nominal_range[self.name + 'TrayTemp'][i]
                    elif key == 'pressure_span':
                        inst_param[i]['pressure_span'] = self.nominal_range[self.name + 'TrayPressure'][i]
            self.vap_enthalpy.setParameters(inst_param)
        varAlias = {}
        for interfVar in options['LiquidEnthalpy'].interfaceVar:
            varAlias[interfVar] = PubPartsUsedVarNames[interfVar]
        if isinstance(self.task, Task.PyomoStaticTask):
            indexList = [['tray', self.name + 'Trays']]
        elif isinstance(self.task, Task.PyomoDynamicTask):
            indexList = [['time', 'Time'], ['tray', self.name + 'Trays']]
        if options['LiquidEnthalpy'].attributes['Custimized'] == False:
            self.liq_enthalpy = options['LiquidEnthalpy'].instanciate(name=self.name + "AllTrays",
                                                                      varAlias=varAlias, indexList=indexList)
        elif options['LiquidEnthalpy'].attributes['Custimized'] == True:
            self.liq_enthalpy = options['LiquidEnthalpy'].instanciateColumnThermo(name=self.name + "AllTrays",
                                                                                         varAlias=varAlias,
                                                                                         indexList=indexList,
                                                                                         creatFile=self.options[
                                                                                             'CreateCustimizedFile'])
            inst_param = {}
            for i in range(1, self.numberOfTray + 1):
                inst_param[i] = {}
                for key in options["LiquidEnthalpy"].required_param:
                    if key == 'temp_span':
                        inst_param[i]['temp_span'] = self.nominal_range[self.name + 'TrayTemp'][i]
                    elif key == 'pressure_span':
                        inst_param[i]['pressure_span'] = self.nominal_range[self.name + 'TrayPressure'][i]
            self.liq_enthalpy.setParameters(inst_param)
        varAlias = {}
        for interfVar in options['CompositionThermo'].interfaceVar:
            varAlias[interfVar] = PubPartsUsedVarNames[interfVar]
        if isinstance(self.task, Task.PyomoStaticTask):
            indexList = [['tray', self.name + 'Trays']]
        elif isinstance(self.task, Task.PyomoDynamicTask):
            indexList = [['time', 'Time'], ['tray', self.name + 'Trays']]
        if options['CompositionThermo'].attributes['Custimized'] == False:
            self.tray_thermo_comp = options['CompositionThermo'].instanciate(name=self.name + "AllTrays",
                                                                         varAlias=varAlias, indexList=indexList)
        elif options['CompositionThermo'].attributes['Custimized'] == True:
            self.tray_thermo_comp = options['CompositionThermo'].instanciateColumnThermo(name=self.name + "AllTrays",
                                                                             varAlias=varAlias, indexList=indexList,creatFile=self.options['CreateCustimizedFile'])
            inst_param = {}
            for i in range(1,self.numberOfTray+1):
                inst_param[i]={}
                for key in options["CompositionThermo"].required_param:
                    if key == 'temp_span':
                        inst_param[i]['temp_span'] = self.nominal_range[self.name + 'TrayTemp'][i]
                    elif key == 'pressure_span':
                        inst_param[i]['pressure_span'] = self.nominal_range[self.name + 'TrayPressure'][i]
            self.tray_thermo_comp.setParameters(inst_param)
        # -----------------------------
        #      Set Hydraulics
        # -----------------------------
        if isinstance(self.task, Task.PyomoDynamicTask):
            varAlias = {}
            for interfVar in options['Hydraulics'].interfaceVar:
                varAlias[interfVar] = PubPartsUsedVarNames[interfVar]
            indexList = [['time', 'Time'], ['tray', self.name + 'Trays']]
            self.hydraulics = options['Hydraulics'].instanciate(name=self.name + "AllTrays",
                                                                             varAlias=varAlias, indexList=indexList)
        # -----------------------------------
        #      Set Index Reduction Related
        # -----------------------------------
        if isinstance(self.task, Task.PyomoDynamicTask):
            varAlias = {}
            for interfVar in options['IndexReduRelatedThermo'].interfaceVar:
                varAlias[interfVar] = PubPartsUsedVarNames[interfVar]
            indexList = [['time', 'Time'], ['tray', self.name + 'Trays']]
            if options['IndexReduRelatedThermo'].attributes['Custimized'] == False:
                self.ir_thermo = options['IndexReduRelatedThermo'].instanciate(name=self.name + "AllTrays",
                                                                               varAlias=varAlias, indexList=indexList)
            elif options['IndexReduRelatedThermo'].attributes['Custimized'] == True:
                self.ir_thermo = options['IndexReduRelatedThermo'].instanciateColumnThermo(name=self.name + "AllTrays",
                                                                               varAlias=varAlias, indexList=indexList,
                                                                        creatFile=self.options['CreateCustimizedFile'])
                inst_param = {}
                for i in range(1, self.numberOfTray + 1):
                    inst_param[i] = {}
                    for key in options["IndexReduRelatedThermo"].required_param:
                        if key == 'temp_span':
                            inst_param[i]['temp_span'] = self.nominal_range[self.name + 'TrayTemp'][i]
                        elif key == 'pressure_span':
                            inst_param[i]['pressure_span'] = self.nominal_range[self.name + 'TrayPressure'][i]
                self.ir_thermo.setParameters(inst_param)
        # -----------------------------
        #      RegisterParts-inst
        # -----------------------------
        self.task.processParts.append(self.vap_enthalpy)
        self.task.processParts.append(self.liq_enthalpy)
        self.task.processParts.append(self.tray_thermo_comp)
        if isinstance(self.task, Task.PyomoDynamicTask):
            self.task.processParts.append(self.ir_thermo)
        # ---------------------------------
        #      Set Input and Output
        # ---------------------------------
        for i in self.feeds.values():
            if i not in ['TwoPhaseFeed', 'VaporFeed', 'LiquidFeed']:
                raise Exception("The feed type %s is not suitable for a column." % i)
        for i in self.extractions.values():
            if i not in ['VaporExtractions', 'LiquidExtractions']:
                raise Exception("The extraction type %s is not suitable for a column." % i)
        if isinstance(self.task, Task.PyomoStaticTask):
            dict = {'F': self.name + 'RefMFlow',
                    'c': self.name + 'RefMFrac[#comp#]',
                    'h': self.name + 'RefMEtlp'
                    }
        elif isinstance(self.task, Task.PyomoDynamicTask):
            dict = {'F': self.name + 'RefMFlow[#time#]',  #注意：time是一个专有变量
                    'c': self.name + 'RefMFrac[#time#,#comp#]',
                    'h': self.name + 'RefMEtlp[#time#]'
                    }
        self.inputStreams['Reflux'] = Device.InputStream(self.name+'Reflux',dict)
        if isinstance(self.task, Task.PyomoStaticTask):
            dict = {'F': self.name + 'LiqLvMFlow[1]',
                    'c': self.name + 'LiqLvMFrac[1,#comp#]',
                    'h': self.name + 'LiqLvMEtlp[1]',
                    'P': self.name + 'TrayPressure[1]',
                    'T': self.name + 'TrayTemp[1]'
                    }
        elif isinstance(self.task, Task.PyomoDynamicTask):
            dict = {'F': self.name + 'LiqLvMFlow[#time#,1]',
                    'c': self.name + 'LiqLvMFrac[#time#,1,#comp#]',
                    'h': self.name + 'LiqLvMEtlp[#time#,1]',
                    'P': self.name + 'TrayPressure[#time#,1]',
                    'T': self.name + 'TrayTemp[#time#,1]'
                    }
        output_var = ['c', 'F', 'h', 'P','T']
        self.outputStreams['SumpOutlet'] = Device.OutputStream(self.name+'SumpOutlet',dict, output_var)
        if isinstance(self.task, Task.PyomoStaticTask):
            dict = {'F': self.name + 'VapLvMFlow[%d]' % self.numberOfTray,
                    'c': self.name + 'VapLvMFrac[%d,#comp#]' % self.numberOfTray,
                    'h': self.name + 'VapLvMEtlp[%d]' % self.numberOfTray,
                    'P': self.name + 'TrayPressure[%d]' % self.numberOfTray
                    }
        elif isinstance(self.task, Task.PyomoDynamicTask):
            dict = {'F': self.name + 'VapLvMFlow[#time#,%d]' % self.numberOfTray,
                    'c': self.name + 'VapLvMFrac[#time#,%d,#comp#]' % self.numberOfTray,
                    'h': self.name + 'VapLvMEtlp[#time#,%d]' % self.numberOfTray,
                    'P': self.name + 'TrayPressure[#time#,%d]' % self.numberOfTray
                    }
        output_var = ['c', 'F', 'h', 'P']
        self.outputStreams['ToCondensor'] = Device.OutputStream(self.name+'ToCondensor',dict, output_var)
        for i in self.feeds.keys():
            if isinstance(self.task, Task.PyomoStaticTask):
                dict = {'F': self.name + "Feed%dMFlow" % i,
                        'c': self.name + "Feed%dMFrac[#comp#]" % i,
                        'h': self.name + "Feed%dMEtlp" % i
                        }
            elif isinstance(self.task, Task.PyomoDynamicTask):
                dict = {'F': self.name + "Feed%dMFlow[#time#]" % i,
                        'c': self.name + "Feed%dMFrac[#time#,#comp#]" % i,
                        'h': self.name + "Feed%dMEtlp[#time#]" % i
                        }
            self.inputStreams['Feed%d' % i] = Device.InputStream(self.name+'Feed%d' % i,dict)
            if not i in self.specialTrays:
                self.specialTrays.append(i)
        for i in self.extractions.keys():
            if isinstance(self.task, Task.PyomoStaticTask):
                dict = {'F': self.name + "Ext%dMFlow" % i,
                        'c': self.name + "Ext%dMFrac[#comp#]" % i,
                        'h': self.name + "Ext%dMEtlp" % i,
                        'P': self.name + 'TrayPressure[%d]' % i
                        }
            elif isinstance(self.task, Task.PyomoDynamicTask):
                dict = {'F': self.name + "Ext%dMFlow[#time#]" % i,
                        'c': self.name + "Ext%dMFrac[#time#,#comp#]" % i,
                        'h': self.name + "Ext%dMEtlp[#time#]" % i,
                        'P': self.name + 'TrayPressure[#time#,%d]' % i
                        }
            output_var = ['c','F','h', 'P']
            self.outputStreams['Extraction%d' % i] = Device.OutputStream(self.name+'Extraction%d' % i,dict, output_var)
            if not i in self.specialTrays:
                self.specialTrays.append(i)
        if 1 not in self.specialTrays:
            self.specialTrays.append(1)
        if self.numberOfTray not in self.specialTrays:
            self.specialTrays.append(self.numberOfTray)

    def generatePEConstraint(self):
        PE_str = ""
        PE_str += "#--------%s---------\n" % self.name
        if type(self.task) == Task.PyomoPETask:
            for index, value in self.extractions.items():
                if isinstance(self.specifications["Ext%dMFlow" % index], ModularTask.PE.EstimatedSpec):
                    PE_str+=ModularTask.ModelingTools.to_pe_constraint("Ext%dMFlow"%index, self.weights["FlowEquWeight"])
            if isinstance(self.specifications['TopPressure'], ModularTask.PE.EstimatedSpec):
                PE_str+=ModularTask.ModelingTools.to_pe_constraint("TopPressure", 1e-3)
            if isinstance(self.specifications['BtmPressure'], ModularTask.PE.EstimatedSpec):
                PE_str+=ModularTask.ModelingTools.to_pe_constraint("BtmPressure", 1e-3)
            if self.options["TrayHeatLeakage"]:
                if isinstance(self.specifications['UALeakage'], ModularTask.PE.EstimatedSpec):
                    PE_str+=ModularTask.ModelingTools.to_pe_constraint("UALeakage", 1e-3)
                if isinstance(self.specifications['AmbientTemp'], ModularTask.PE.EstimatedSpec):
                    PE_str+=ModularTask.ModelingTools.to_pe_constraint("AmbientTemp", 1e-1)
        else:
            raise Exception("This is not a PE task.")
        PE_str = PE_str.replace('#model_name#', self.task.name).replace("#device_name#", self.name).replace("#prim_name#", self.primitive_name)
        return PE_str

    def generatePublicPEVar(self):
        PE_str = ""
        PE_str += "#--------%s---------\n" % self.name
        if type(self.task) == Task.PyomoPETask:
            for index, value in self.extractions.items():
                PE_str+=ModularTask.ModelingTools.to_pe_public_var("Ext%dMFlow"%index,
                                                                       self.specifications["Ext%dMFlow" % index])
            PE_str += ModularTask.ModelingTools.to_pe_public_var("TopPressure",
                                                                 self.specifications["TopPressure"])
            PE_str += ModularTask.ModelingTools.to_pe_public_var("BtmPressure",
                                                                 self.specifications["BtmPressure"])
            if self.options["TrayHeatLeakage"]:
                PE_str += ModularTask.ModelingTools.to_pe_public_var("UALeakage",
                                                                     self.specifications["UALeakage"])
                PE_str += ModularTask.ModelingTools.to_pe_public_var("AmbientTemp",
                                                                     self.specifications["AmbientTemp"])
        else:
            raise Exception("This is not a PE task.")
        PE_str = PE_str.replace('#model_name#', self.task.name).replace("#device_name#", self.name).replace("#prim_name#", self.primitive_name)
        return PE_str

    def generatePyomoPara(self):
        para_str = ""
        para_str += "#--------%s---------\n" % self.name
        para_str += "#model_name#.#device_name#Trays = RangeSet(1, %d)\n" % self.numberOfTray
        for index, value in self.extractions.items():
            if isinstance(self.task, Task.PyomoStaticTask):
                para_str += ModularTask.ModelingTools.ss_or_pe_para(self.task, "Ext%dMFlow"%index,
                                                                    self.specifications["Ext%dMFlow" % index])
            elif isinstance(self.task, Task.PyomoDynamicTask):
                para_str += ModularTask.ModelingTools.gen_dynamic_para(self.task, "Ext%dMFlow"%index,
                                                            self.specifications["Ext%dMFlow" % index])
        if isinstance(self.task, Task.PyomoStaticTask):
            para_str += ModularTask.ModelingTools.ss_or_pe_para(self.task, "TopPressure",
                                                                self.specifications['TopPressure'])
            para_str += ModularTask.ModelingTools.ss_or_pe_para(self.task, "BtmPressure",
                                                                self.specifications['BtmPressure'])
        elif isinstance(self.task, Task.PyomoDynamicTask):
            para_str += ModularTask.ModelingTools.gen_dynamic_para(self.task, "TopPressure", self.specifications['TopPressure'])
            para_str += ModularTask.ModelingTools.gen_dynamic_para(self.task, "BtmPressure",
                                                                   self.specifications['BtmPressure'])
        para_str += self.tray_thermo_comp.generatePyomoPara()
        para_str += self.vap_enthalpy.generatePyomoPara()
        para_str += self.liq_enthalpy.generatePyomoPara()
        if isinstance(self.task, Task.PyomoDynamicTask):
            para_str += self.hydraulics.generatePyomoPara()
            para_str += self.ir_thermo.generatePyomoPara()
        if self.options["TrayHeatLeakage"]:
            if isinstance(self.task, Task.PyomoStaticTask):
                para_str += ModularTask.ModelingTools.ss_or_pe_para(self.task, "UALeakage",
                                                                    self.specifications['UALeakage'])
                para_str += ModularTask.ModelingTools.ss_or_pe_para(self.task, "AmbientTemp",
                                                                    self.specifications['AmbientTemp'])
            elif isinstance(self.task, Task.PyomoDynamicTask):
                para_str += ModularTask.ModelingTools.gen_dynamic_para(self.task, "UALeakage",
                                                                       self.specifications['UALeakage'])
                para_str += ModularTask.ModelingTools.gen_dynamic_para(self.task, "AmbientTemp",
                                                                       self.specifications['AmbientTemp'])
        para_str = para_str.replace('#model_name#', self.task.name).replace("#device_name#", self.name)
        return para_str

    def generatePyomoVar(self):
        str = ""
        str += "#--------%s---------\n" % self.name
        if isinstance(self.task, Task.PyomoStaticTask):
            str += "#model_name#.#device_name#VapLvMFlow = Var(#model_name#.#device_name#Trays, within=NonNegativeReals)\n"
            str += "#model_name#.#device_name#LiqLvMFlow = Var(#model_name#.#device_name#Trays, within=NonNegativeReals)\n"
            str += "#model_name#.#device_name#TrayTemp = Var(#model_name#.#device_name#Trays)\n"
            str += "#model_name#.#device_name#TrayPressure = Var(#model_name#.#device_name#Trays)\n"
        elif isinstance(self.task, Task.PyomoDynamicTask):
            str += "#model_name#.#device_name#VapLvMFlow = Var(#model_name#.Time, #model_name#.#device_name#Trays, within=NonNegativeReals)\n"
            str += "#model_name#.#device_name#LiqLvMFlow = Var(#model_name#.Time, #model_name#.#device_name#Trays, within=NonNegativeReals)\n"
            str += "#model_name#.#device_name#TrayTemp = Var(#model_name#.Time, #model_name#.#device_name#Trays)\n"
            str += "#model_name#.#device_name#TrayPressure = Var(#model_name#.Time, #model_name#.#device_name#Trays)\n"
        str += self.tray_thermo_comp.generatePyomoVar()
        str += self.vap_enthalpy.generatePyomoVar()
        str += self.liq_enthalpy.generatePyomoVar()
        if len(self.extractions) >0:
            str += "#--------%s's var in extractions---------\n" % self.name
            if isinstance(self.task, Task.PyomoStaticTask):
                for tray_no in self.extractions.keys():
                    # str += "#model_name#.#device_name#Ext%dMFlow = Var(within=NonNegativeReals)\n"%tray_no
                    str += "#model_name#.#device_name#Ext%dMFrac = Var(#model_name#.Component, bounds=(0,1))\n"%tray_no
                    str += "#model_name#.#device_name#Ext%dMEtlp = Var()\n"%tray_no
            elif isinstance(self.task, Task.PyomoDynamicTask):
                for tray_no in self.extractions.keys():
                    # str += "#model_name#.#device_name#Ext%dMFlow = Var(#model_name#.Time, within=NonNegativeReals)\n"%tray_no
                    str += "#model_name#.#device_name#Ext%dMFrac = Var(#model_name#.Time, #model_name#.Component, bounds=(0,1))\n"%tray_no
                    str += "#model_name#.#device_name#Ext%dMEtlp = Var(#model_name#.Time)\n"%tray_no
        if isinstance(self.task, Task.PyomoDynamicTask):
            str += "#--------%s's var in differential equations---------\n" % self.name
            str += self.hydraulics.generatePyomoVar()
            str += self.ir_thermo.generatePyomoVar()
            str += "#model_name#.#device_name#TrayMHldp = Var(#model_name#.Time, #model_name#.#device_name#Trays, within=NonNegativeReals)\n"
            str += "#model_name#.#device_name#DtTrayMHldp = DerivativeVar(#model_name#.#device_name#TrayMHldp)\n"
            str += "#model_name#.#device_name#TrayMCompHldp = Var(#model_name#.Time, #model_name#.#device_name#Trays, #model_name#.Component, within=NonNegativeReals)\n"
            str += "#model_name#.#device_name#DtTrayMCompHldp = DerivativeVar(#model_name#.#device_name#TrayMCompHldp)\n"
            str += "#model_name#.#device_name#DtTrayMEtlpHldp = Var(#model_name#.Time, #model_name#.#device_name#Trays)\n"
            str += "#model_name#.#device_name#DtTrayPressure = DerivativeVar(#model_name#.#device_name#TrayPressure)\n"
        str = str.replace('#model_name#', self.task.name).replace("#device_name#", self.name)
        return str

    def generatePyomoExpression(self):
        str = ""
        str += "#--------%s Component Flowrate---------\n" % self.name
        if isinstance(self.task, Task.PyomoStaticTask):
            str += "def #device_name#VapLvMCompFlow(m, tray, comp):\n"
            str += "\treturn m.#device_name#VapLvMFrac[tray, comp] * m.#device_name#VapLvMFlow[tray]\n"
            str += "#model_name#.#device_name#VapLvMCompFlow = Expression(#model_name#.#device_name#Trays, #model_name#.Component, rule=#device_name#VapLvMCompFlow)\n"
            str += "def #device_name#LiqLvMCompFlow(m, tray, comp):\n"
            str += "\treturn m.#device_name#LiqLvMFrac[tray, comp] * m.#device_name#LiqLvMFlow[tray]\n"
            str += "#model_name#.#device_name#LiqLvMCompFlow = Expression(#model_name#.#device_name#Trays, #model_name#.Component, rule=#device_name#LiqLvMCompFlow)\n"
        elif isinstance(self.task, Task.PyomoDynamicTask):
            str += "def #device_name#VapLvMCompFlow(m, time, tray, comp):\n"
            str += "\treturn m.#device_name#VapLvMFrac[time, tray, comp] * m.#device_name#VapLvMFlow[time, tray]\n"
            str += "#model_name#.#device_name#VapLvMCompFlow = Expression(#model_name#.Time, #model_name#.#device_name#Trays, #model_name#.Component, rule=#device_name#VapLvMCompFlow)\n"
            str += "def #device_name#LiqLvMCompFlow(m, time, tray, comp):\n"
            str += "\treturn m.#device_name#LiqLvMFrac[time, tray, comp] * m.#device_name#LiqLvMFlow[time, tray]\n"
            str += "#model_name#.#device_name#LiqLvMCompFlow = Expression(#model_name#.Time, #model_name#.#device_name#Trays, #model_name#.Component, rule=#device_name#LiqLvMCompFlow)\n"
        str += "#--------%s Thermo and Enthalpy---------\n" % self.name
        str += self.tray_thermo_comp.generatePyomoExpression()
        str += self.vap_enthalpy.generatePyomoExpression()
        str += self.liq_enthalpy.generatePyomoExpression()
        if isinstance(self.task, Task.PyomoDynamicTask):
            str += "#--------%s Dynamic Related---------\n" % self.name
            str += "def #device_name#DtLiqLvMFrac(m, time, tray, comp):\n"
            str += "\treturn (m.#device_name#DtTrayMCompHldp[time, tray, comp] - m.#device_name#LiqLvMFrac[time, tray, comp] *\\\n"
            str += "\t      m.#device_name#DtTrayMHldp[time, tray]) / m.#device_name#TrayMHldp[time, tray]\n"
            str += "#model_name#.#device_name#DtLiqLvMFrac = Expression(#model_name#.Time, #model_name#.#device_name#Trays, #model_name#.Component, rule=#device_name#DtLiqLvMFrac)\n"
            str += self.hydraulics.generatePyomoExpression()
            str += self.ir_thermo.generatePyomoExpression()
        str = str.replace('#model_name#', self.task.name).replace("#device_name#", self.name)
        return str

    def generatePyomoCon(self):
        str = ""
        str += "#--------%s Mass Balance---------\n" % self.name
        str += self.generateMassBalance()
        if isinstance(self.task, Task.PyomoDynamicTask):
            str += self.con_MCompHldp()
        str += "#--------%s Energy Balance---------\n" % self.name
        str += self.generateEnergyBalance()
        if isinstance(self.task, Task.PyomoDynamicTask):
            str += self.ir_thermo.generatePyomoCon()
        str += "#--------%s Phase Equilibrium & System Parts---------\n" % self.name
        str += self.generateEquilibrium()
        str += self.vap_enthalpy.generatePyomoCon()
        str += self.liq_enthalpy.generatePyomoCon()
        if isinstance(self.task, Task.PyomoDynamicTask):
            str += "#--------%s Hydraulics---------\n" % self.name
            str += self.hydraulics.generatePyomoCon()
        str += "#--------%s Summation---------\n" % self.name
        str += self.generateSummation()
        str += "#--------%s Pressure Profile---------\n" % self.name
        str += self.generatePressureProfile()
        if len(self.extractions) != 0:
            str += "#--------%s Extractions---------\n" % self.name
            str += self.generateExtractions()
        if isinstance(self.task, Task.PyomoDynamicTask):
            str += "#--------%s Integration Initial Condition---------\n" % self.name
            str += self.generateInitialCondition()
        return str

    def generateMassBalance(self):
        str = ""
        if isinstance(self.task, Task.PyomoStaticTask):
            str += "def #device_name#MassBlnc(m,tray, comp):\n"
        elif isinstance(self.task, Task.PyomoDynamicTask):
            str += "def #device_name#MassBlnc(m,time, tray, comp):\n"
        first_statement = True
        for tray in self.specialTrays:
            substr = ""
            if first_statement:
                substr += "\tif tray == %d:\n" % tray
                first_statement = False
            else:
                substr += "\telif tray == %d:\n" % tray
            if tray == 1:
                if isinstance(self.task, Task.PyomoStaticTask):
                    substr += "\t\treturn (m.#device_name#LiqLvMCompFlow[tray + 1, comp]- m.#device_name#LiqLvMCompFlow[tray, comp] - m.#device_name#VapLvMCompFlow[tray, comp]"
                elif isinstance(self.task, Task.PyomoDynamicTask):
                    substr += "\t\treturn (m.#device_name#LiqLvMCompFlow[time, tray + 1, comp]- m.#device_name#LiqLvMCompFlow[time, tray, comp] - m.#device_name#VapLvMCompFlow[time, tray, comp]"
            elif tray == self.numberOfTray:
                if isinstance(self.task, Task.PyomoStaticTask):
                    substr += "\t\treturn (m.#device_name#RefMFlow*m.#device_name#RefMFrac[comp] + m.#device_name#VapLvMCompFlow[tray - 1, comp] - m.#device_name#LiqLvMCompFlow[tray, comp] - m.#device_name#VapLvMCompFlow[tray, comp]"
                elif isinstance(self.task, Task.PyomoDynamicTask):
                    substr += "\t\treturn (m.#device_name#RefMFlow[time]*m.#device_name#RefMFrac[time, comp] + m.#device_name#VapLvMCompFlow[time, tray - 1, comp] - m.#device_name#LiqLvMCompFlow[time, tray, comp] - m.#device_name#VapLvMCompFlow[time, tray, comp]"
            else:
                if isinstance(self.task, Task.PyomoStaticTask):
                    substr += "\t\treturn (m.#device_name#LiqLvMCompFlow[tray + 1, comp] + m.#device_name#VapLvMCompFlow[tray - 1, comp] - m.#device_name#LiqLvMCompFlow[tray, comp] - m.#device_name#VapLvMCompFlow[tray, comp]"
                elif isinstance(self.task, Task.PyomoDynamicTask):
                    substr += "\t\treturn (m.#device_name#LiqLvMCompFlow[time, tray + 1, comp] + m.#device_name#VapLvMCompFlow[time, tray - 1, comp] - m.#device_name#LiqLvMCompFlow[time, tray, comp] - m.#device_name#VapLvMCompFlow[time, tray, comp]"
            if tray in self.feeds.keys():
                if isinstance(self.task, Task.PyomoStaticTask):
                    substr += "+m.#device_name#Feed%dMFlow*m.#device_name#Feed%dMFrac[comp]" % (tray, tray)
                elif isinstance(self.task, Task.PyomoDynamicTask):
                    substr += "+m.#device_name#Feed%dMFlow[time]*m.#device_name#Feed%dMFrac[time, comp]" % (tray, tray)
            if tray in self.extractions.keys():
                if isinstance(self.task, Task.PyomoStaticTask):
                    substr += "-m.#device_name#Ext%dMFlow*m.#device_name#Ext%dMFrac[comp]" % (tray, tray)
                elif isinstance(self.task, Task.PyomoDynamicTask):
                    substr += "-m.#device_name#Ext%dMFlow[time]*m.#device_name#Ext%dMFrac[time, comp]" % (tray, tray)
            if isinstance(self.task, Task.PyomoDynamicTask):
                substr += "-m.#device_name#DtTrayMCompHldp[time,tray,comp]"
            substr += ")*%f == 0\n" % self.weights['FlowEquWeight']
            str += substr
        substr = ""
        substr += "\telse:\n"
        if isinstance(self.task, Task.PyomoStaticTask):
            substr += "\t\treturn (m.#device_name#LiqLvMCompFlow[tray + 1, comp] + m.#device_name#VapLvMCompFlow[tray - 1, comp] - m.#device_name#LiqLvMCompFlow[tray, comp] - m.#device_name#VapLvMCompFlow[tray, comp]"
        elif isinstance(self.task, Task.PyomoDynamicTask):
            substr += "\t\treturn (m.#device_name#LiqLvMCompFlow[time, tray + 1, comp] + m.#device_name#VapLvMCompFlow[time, tray - 1, comp] - m.#device_name#LiqLvMCompFlow[time, tray, comp] - m.#device_name#VapLvMCompFlow[time, tray, comp]-m.#device_name#DtTrayMCompHldp[time,tray,comp]"
        substr += ")*%f == 0\n" % self.weights['FlowEquWeight']
        str += substr
        if isinstance(self.task, Task.PyomoStaticTask):
            str += "#model_name#.#device_name#MassBlnc = Constraint(#model_name#.#device_name#Trays, #model_name#.Component, rule=#device_name#MassBlnc)\n"
        elif isinstance(self.task, Task.PyomoDynamicTask):
            str += "#model_name#.#device_name#MassBlnc = Constraint(#model_name#.Time, #model_name#.#device_name#Trays, #model_name#.Component, rule=#device_name#MassBlnc)\n"
        str = str.replace('#model_name#', self.task.name).replace("#device_name#", self.name)
        return str

    def generateEnergyBalance(self):
        str = ""
        if isinstance(self.task, Task.PyomoStaticTask):
            str += "def #device_name#EngBlnc(m,tray):\n"
        elif isinstance(self.task, Task.PyomoDynamicTask):
            str += "def #device_name#EngBlnc(m,time,tray):\n"
        first_statement = True
        for tray in self.specialTrays:
            substr = ""
            if first_statement:
                substr += "\tif tray == %d:\n" % tray
                first_statement = False
            else:
                substr += "\telif tray == %d:\n" % tray
            if tray == 1:
                if isinstance(self.task, Task.PyomoStaticTask):
                    substr += "\t\treturn (m.#device_name#LiqLvMFlow[tray + 1] * m.#device_name#LiqLvMEtlp[tray+1] \\\n" + \
                              "\t\t        - m.#device_name#LiqLvMFlow[tray] * m.#device_name#LiqLvMEtlp[tray] \\\n" + \
                              "\t\t        - m.#device_name#VapLvMFlow[tray] * m.#device_name#VapLvMEtlp[tray]"
                elif isinstance(self.task, Task.PyomoDynamicTask):
                    substr += "\t\treturn (m.#device_name#LiqLvMFlow[time,tray + 1] * m.#device_name#LiqLvMEtlp[time,tray+1] \\\n" + \
                          "\t\t        - m.#device_name#LiqLvMFlow[time,tray] * m.#device_name#LiqLvMEtlp[time,tray] \\\n" + \
                          "\t\t        - m.#device_name#VapLvMFlow[time,tray] * m.#device_name#VapLvMEtlp[time,tray]"
            elif tray == self.numberOfTray:
                if isinstance(self.task, Task.PyomoStaticTask):
                    substr += "\t\treturn (m.#device_name#RefMFlow * m.#device_name#RefMEtlp \\\n" + \
                              "\t\t        + m.#device_name#VapLvMFlow[tray-1] * m.#device_name#VapLvMEtlp[tray-1] \\\n" + \
                              "\t\t        - m.#device_name#LiqLvMFlow[tray] * m.#device_name#LiqLvMEtlp[tray] \\\n" + \
                              "\t\t        - m.#device_name#VapLvMFlow[tray] * m.#device_name#VapLvMEtlp[tray]"
                elif isinstance(self.task, Task.PyomoDynamicTask):
                    substr += "\t\treturn (m.#device_name#RefMFlow[time] * m.#device_name#RefMEtlp[time] \\\n" + \
                              "\t\t        + m.#device_name#VapLvMFlow[time,tray-1] * m.#device_name#VapLvMEtlp[time,tray-1] \\\n" + \
                              "\t\t        - m.#device_name#LiqLvMFlow[time,tray] * m.#device_name#LiqLvMEtlp[time,tray] \\\n" + \
                              "\t\t        - m.#device_name#VapLvMFlow[time,tray] * m.#device_name#VapLvMEtlp[time,tray]"
            else:
                if isinstance(self.task, Task.PyomoStaticTask):
                    substr += "\t\treturn (m.#device_name#LiqLvMFlow[tray + 1] * m.#device_name#LiqLvMEtlp[tray+1] \\\n" + \
                              "\t\t        + m.#device_name#VapLvMFlow[tray-1] * m.#device_name#VapLvMEtlp[tray-1] \\\n" + \
                              "\t\t        - m.#device_name#LiqLvMFlow[tray] * m.#device_name#LiqLvMEtlp[tray] \\\n" + \
                              "\t\t        - m.#device_name#VapLvMFlow[tray] * m.#device_name#VapLvMEtlp[tray]"
                elif isinstance(self.task, Task.PyomoDynamicTask):
                    substr += "\t\treturn (m.#device_name#LiqLvMFlow[time,tray + 1] * m.#device_name#LiqLvMEtlp[time,tray+1] \\\n" + \
                          "\t\t        + m.#device_name#VapLvMFlow[time,tray-1] * m.#device_name#VapLvMEtlp[time,tray-1] \\\n" + \
                          "\t\t        - m.#device_name#LiqLvMFlow[time,tray] * m.#device_name#LiqLvMEtlp[time,tray] \\\n" + \
                          "\t\t        - m.#device_name#VapLvMFlow[time,tray] * m.#device_name#VapLvMEtlp[time,tray]"
            if tray in self.feeds.keys():
                if isinstance(self.task, Task.PyomoStaticTask):
                    substr += "\\\n\t\t        +m.#device_name#Feed%dMFlow*m.#device_name#Feed%dMEtlp" % (tray, tray)
                elif isinstance(self.task, Task.PyomoDynamicTask):
                    substr += "\\\n\t\t        +m.#device_name#Feed%dMFlow[time]*m.#device_name#Feed%dMEtlp[time]" % (tray, tray)
            if tray in self.extractions.keys():
                if isinstance(self.task, Task.PyomoStaticTask):
                    substr += "\\\n\t\t        -m.#device_name#Ext%dMFlow*m.#device_name#Ext%dMEtlp" % (tray, tray)
                elif isinstance(self.task, Task.PyomoDynamicTask):
                    substr += "\\\n\t\t        -m.#device_name#Ext%dMFlow[time]*m.#device_name#Ext%dMEtlp[time]" % (tray, tray)
            if isinstance(self.task, Task.PyomoDynamicTask):
                substr += "-m.#device_name#DtTrayMEtlpHldp[time,tray]"
            if self.options["TrayHeatLeakage"]:
                if isinstance(self.task, Task.PyomoStaticTask):
                    substr += "-m.#device_name#UALeakage*(m.#device_name#AmbientTemp-m.#device_name#TrayTemp[tray])"
                elif isinstance(self.task, Task.PyomoDynamicTask):
                    substr += "-m.#device_name#UALeakage[time]*(m.#device_name#AmbientTemp[time]-m.#device_name#TrayTemp[time,tray])"
            substr += ")*%f == 0\n" % self.weights['EnthalpyEquWeight']
            str += substr
        substr = ""
        substr += "\telse:\n"
        if isinstance(self.task, Task.PyomoStaticTask):
            substr += "\t\treturn (m.#device_name#LiqLvMFlow[tray + 1] * m.#device_name#LiqLvMEtlp[tray+1] \\\n" + \
                      "\t\t        + m.#device_name#VapLvMFlow[tray-1] * m.#device_name#VapLvMEtlp[tray-1] \\\n" + \
                      "\t\t        - m.#device_name#LiqLvMFlow[tray] * m.#device_name#LiqLvMEtlp[tray] \\\n" + \
                      "\t\t        - m.#device_name#VapLvMFlow[tray] * m.#device_name#VapLvMEtlp[tray]"
        elif isinstance(self.task, Task.PyomoDynamicTask):
            substr += "\t\treturn (m.#device_name#LiqLvMFlow[time,tray + 1] * m.#device_name#LiqLvMEtlp[time,tray+1] \\\n" + \
                      "\t\t        + m.#device_name#VapLvMFlow[time,tray-1] * m.#device_name#VapLvMEtlp[time,tray-1] \\\n" + \
                      "\t\t        - m.#device_name#LiqLvMFlow[time,tray] * m.#device_name#LiqLvMEtlp[time,tray] \\\n" + \
                      "\t\t        - m.#device_name#VapLvMFlow[time,tray] * m.#device_name#VapLvMEtlp[time,tray] \\\n" + \
                      "\t\t        - m.#device_name#DtTrayMEtlpHldp[time,tray]"
        if self.options["TrayHeatLeakage"]:
            if isinstance(self.task, Task.PyomoStaticTask):
                substr += "-m.#device_name#UALeakage*(m.#device_name#AmbientTemp-m.#device_name#TrayTemp[tray])"
            elif isinstance(self.task, Task.PyomoDynamicTask):
                substr += "-m.#device_name#UALeakage[time]*(m.#device_name#AmbientTemp[time]-m.#device_name#TrayTemp[time,tray])"
        substr += ")*%f == 0\n" % self.weights['EnthalpyEquWeight']
        str += substr
        if isinstance(self.task, Task.PyomoStaticTask):
            str += "#model_name#.#device_name#EngBlnc = Constraint(#model_name#.#device_name#Trays,rule=#device_name#EngBlnc)\n"
        elif isinstance(self.task, Task.PyomoDynamicTask):
            str += "#model_name#.#device_name#EngBlnc = Constraint(#model_name#.Time, #model_name#.#device_name#Trays,rule=#device_name#EngBlnc)\n"
        str = str.replace('#model_name#', self.task.name).replace("#device_name#", self.name)
        return str

    def con_MCompHldp(self):
        str = ""
        str += "def #device_name#MCompHldpEqu(m, time, tray, comp):\n"
        str += "\treturn (m.#device_name#TrayMCompHldp[time, tray, comp] - m.#device_name#TrayMHldp[time, tray] * m.#device_name#LiqLvMFrac[time, tray, comp]) * 1e-2 == 0\n"
        str += "#model_name#.#device_name#MCompHldpEqu = Constraint(#model_name#.Time, #model_name#.#device_name#Trays, #model_name#.Component, rule=#device_name#MCompHldpEqu)\n"
        str = str.replace('#model_name#', self.task.name).replace("#device_name#", self.name)
        return str

    def generateEquilibrium(self):
        str = ""
        str += self.tray_thermo_comp.generatePyomoCon()
        return str

    def generateSummation(self):
        str = ""
        if isinstance(self.task, Task.PyomoStaticTask):
            str += "def #device_name#LiqSum(m, tray):\n"
            str += "\treturn sum([m.#device_name#LiqLvMFrac[tray, c] for c in m.Component]) == 1\n"
            str += "#model_name#.#device_name#LiqSum = Constraint(#model_name#.#device_name#Trays, rule=#device_name#LiqSum)\n"

            str += "def #device_name#VapSum(m, tray):\n"
            str += "\treturn sum([m.#device_name#VapLvMFrac[tray, c] for c in m.Component]) == 1\n"
            str += "#model_name#.#device_name#VapSum = Constraint(#model_name#.#device_name#Trays, rule=#device_name#VapSum)\n"
        elif isinstance(self.task, Task.PyomoDynamicTask):
            str += "def #device_name#LiqSum(m,time, tray):\n"
            str += "\treturn sum([m.#device_name#LiqLvMFrac[time, tray, c] for c in m.Component]) == 1\n"
            str += "#model_name#.#device_name#LiqSum = Constraint(#model_name#.Time, #model_name#.#device_name#Trays, rule=#device_name#LiqSum)\n"

            str += "def #device_name#VapSum(m,time, tray):\n"
            str += "\treturn sum([m.#device_name#VapLvMFrac[time, tray, c] for c in m.Component]) == 1\n"
            str += "#model_name#.#device_name#VapSum = Constraint(#model_name#.Time, #model_name#.#device_name#Trays, rule=#device_name#VapSum)\n"
        str = str.replace('#model_name#', self.task.name).replace("#device_name#", self.name)
        return str

    def generatePressureProfile(self):
        equ_str = ""
        if self.options['PressureProfile'] == 'SimpleLinear':
            if isinstance(self.task, Task.PyomoStaticTask):
                equ_str += "def #device_name#PProf(m, tray):\n"
                equ_str+= "\treturn ((m.#device_name#TopPressure-m.#device_name#BtmPressure)/%d"%(self.numberOfTray-1)+"*(tray-1)" +\
                          "+m.#device_name#BtmPressure - m.#device_name#TrayPressure[tray])*%f == 0\n" % self.weights['PressureEquWeight']
                equ_str += "#model_name#.#device_name#PProf = Constraint(#model_name#.#device_name#Trays, rule=#device_name#PProf)\n"
            elif isinstance(self.task, Task.PyomoDynamicTask):
                equ_str += "def #device_name#PProf(m, time, tray):\n"
                sub_equ_str = "\treturn ((m.#device_name#TopPressure[time]-m.#device_name#BtmPressure[time])/%d" % (self.numberOfTray - 1) + "*(tray-1)" + \
                           "+m.#device_name#BtmPressure[time] - m.#device_name#TrayPressure[time, tray])*%f == 0\n" % self.weights['PressureEquWeight']
                # if "TopPressure" in self.timeDependParam:
                #     sub_equ_str = sub_equ_str.replace("TopPressure", "TopPressure[time]")
                # if "BtmPressure" in self.timeDependParam:
                #     sub_equ_str = sub_equ_str.replace("BtmPressure", "BtmPressure[time]")
                equ_str += sub_equ_str
                equ_str += "#model_name#.#device_name#PProf = Constraint(#model_name#.Time, #model_name#.#device_name#Trays, rule=#device_name#PProf)\n"
        equ_str = equ_str.replace('#model_name#', self.task.name).replace("#device_name#", self.name)
        return equ_str

    def getNaiveDynamicInitValue(self):
        self.static_init[self.name + 'DtTrayPressure'] = {}
        self.static_init[self.name + 'DtTrayMEtlpHldp'] = {}
        self.static_init[self.name + 'DtTrayMCompHldp'] = {}
        self.static_init[self.name + 'DtTrayMHldp'] = {}
        self.static_init[self.name + 'TrayMHldp'] = {}
        self.static_init[self.name + 'TrayMCompHldp'] = {}
        for i in range(1,self.numberOfTray+1):
            self.static_init[self.name + 'DtTrayPressure'][i] = 0
            self.static_init[self.name + 'DtTrayMEtlpHldp'][i] = 0
            for j in self.task.component:
                self.static_init[self.name + 'DtTrayMCompHldp'][i,j] = 0
            self.static_init[self.name + 'DtTrayMHldp'][i] = 0
            self.static_init[self.name + 'TrayMHldp'][i] = self.hydraulics.getHoldupInit({'L':self.static_init[self.name + 'LiqLvMFlow'][i]})
            for j in self.task.component:
                self.static_init[self.name + 'TrayMCompHldp'][i, j] = self.static_init[self.name + 'TrayMHldp'][i]*self.static_init[self.name + 'LiqLvMFrac'][i,j]

    def generateInitialCondition(self):
        cond_str = ""
        cond_str += "def #device_name#ICTrayMHldp(m):\n"
        for i in range(1,self.numberOfTray+1):
            cond_str += "\tyield m.#device_name#TrayMHldp[0, %d] == %f\n"%(i, self.static_init[self.name + 'TrayMHldp'][i])
        cond_str += "#model_name#.#device_name#ICTrayMHldp = ConstraintList(rule=#device_name#ICTrayMHldp)\n"
        cond_str += "def #device_name#ICTrayMCompHldp(m):\n"
        for i in range(1, self.numberOfTray + 1):
            for index, comp in enumerate(self.task.component):
                if index == len(self.task.component)-1:
                    continue
                else:
                    cond_str += "\tyield m.#device_name#TrayMCompHldp[0, %d, \"" % i+comp+"\"] == %f\n"%(self.static_init[self.name + 'TrayMCompHldp'][i,comp])
        cond_str += "#model_name#.#device_name#ICTrayMCompHldp = ConstraintList(rule=#device_name#ICTrayMCompHldp)\n"
        # 物料积累量变化率初始条件
        cond_str += "def #device_name#ICDtTrayMHldp(m, tray):\n"
        first_statement = True
        for tray in self.specialTrays:
            subcond_str = ""
            if first_statement:
                subcond_str += "\tif tray == %d:\n" % tray
                first_statement = False
            else:
                subcond_str += "\telif tray == %d:\n" % tray
            if tray == 1:
                subcond_str += "\t\treturn (m.#device_name#LiqLvMFlow[0, tray + 1]- m.#device_name#LiqLvMFlow[0, tray] - m.#device_name#VapLvMFlow[0, tray]"
            elif tray == self.numberOfTray:
                subcond_str += "\t\treturn (m.#device_name#RefMFlow[0] + m.#device_name#VapLvMFlow[0, tray - 1] - m.#device_name#LiqLvMFlow[0, tray] - m.#device_name#VapLvMFlow[0, tray]"
            else:
                subcond_str += "\t\treturn (m.#device_name#LiqLvMFlow[0, tray + 1] + m.#device_name#VapLvMFlow[0, tray - 1] - m.#device_name#LiqLvMFlow[0, tray] - m.#device_name#VapLvMFlow[0, tray]"
            if tray in self.feeds.keys():
                subcond_str += "+m.#device_name#Feed%dMFlow[0]" % tray
            if tray in self.extractions.keys():
                subcond_str += "-m.#device_name#Ext%dMFlow[0]" % tray
            subcond_str += "-m.#device_name#DtTrayMHldp[0,tray]"
            subcond_str += ")*%f == 0\n" % self.weights['FlowEquWeight']
            cond_str += subcond_str
        subcond_str = ""
        subcond_str += "\telse:\n"
        subcond_str += "\t\treturn (m.#device_name#LiqLvMFlow[0, tray + 1] + m.#device_name#VapLvMFlow[0, tray - 1] - m.#device_name#LiqLvMFlow[0, tray] - m.#device_name#VapLvMFlow[0, tray]-m.#device_name#DtTrayMHldp[0,tray]"
        subcond_str += ")*%f == 0\n" % self.weights['FlowEquWeight']
        cond_str += subcond_str
        cond_str += "#model_name#.#device_name#ICDtTrayMHldp = Constraint(#model_name#.#device_name#Trays, rule=#device_name#ICDtTrayMHldp)\n"
        # 塔压变化率初始条件
        cond_str += "def #device_name#ICDtTrayPressure(m):\n"
        for tray in range(1,self.numberOfTray+1):
            cond_str += "\tyield m.#device_name#DtTrayPressure[0,%d] == 0\n"%tray
        cond_str += "#model_name#.#device_name#ICDtTrayPressure = ConstraintList(rule=#device_name#ICDtTrayPressure)\n"
        cond_str = cond_str.replace('#model_name#', self.task.name).replace("#device_name#", self.name)
        return cond_str

    def generateExtractions(self):
        str = ""
        if isinstance(self.task, Task.PyomoStaticTask):
            for index, value in self.extractions.items():
                if value == 'VaporExtractions':
                    # str += "def #device_name#Ext%dMFlowSpec(m):\n"%index
                    # str += "\treturn (m.#device_name#Ext%dMFlow - %f)* % f == 0\n"%(index, self.specifications["Ext%dMFlow"%index], self.weights['FlowEquWeight'])
                    # str += "#model_name#.#device_name#Ext%dMFlowSpec = Constraint(rule=#device_name#Ext%dMFlowSpec)\n"%(index,index)
                    str += "def #device_name#Ext%dMFracSpec(m, comp):\n" % index
                    str += "\treturn m.#device_name#Ext%dMFrac[comp] - m.#device_name#VapLvMFrac[%d, comp] == 0 \n" % (index, index)
                    str += "#model_name#.#device_name#Ext%dMFracSpec = Constraint(#model_name#.Component, rule=#device_name#Ext%dMFracSpec)\n" % (index, index)
                    str += "def #device_name#Ext%dMEtlpSpec(m):\n" % index
                    str += "\treturn (m.#device_name#Ext%dMEtlp - m.#device_name#VapLvMEtlp[%d])* % f == 0\n" % (index, index, self.weights['EnthalpyEquWeight'])
                    str += "#model_name#.#device_name#Ext%dMEtlpSpec = Constraint(rule=#device_name#Ext%dMEtlpSpec)\n" % (index, index)
                elif value == 'LiquidExtractions':
                    # str += "def #device_name#Ext%dMFlowSpec(m):\n" % index
                    # str += "\treturn (m.#device_name#Ext%dMFlow - %f)* % f == 0\n" % (
                    # index, self.specifications["Ext%dMFlow" % index], self.weights['FlowEquWeight'])
                    # str += "#model_name#.#device_name#Ext%dMFlowSpec = Constraint(rule=#device_name#Ext%dMFlowSpec)\n" % (
                    # index, index)
                    str += "def #device_name#Ext%dMFracSpec(m, comp):\n" % index
                    str += "\treturn m.#device_name#Ext%dMFrac[comp] - m.#device_name#LiqLvMFrac[%d, comp] == 0 \n" % (
                    index, index)
                    str += "#model_name#.#device_name#Ext%dMFracSpec = Constraint(#model_name#.Component, rule=#device_name#Ext%dMFracSpec)\n" % (
                    index, index)
                    str += "def #device_name#Ext%dMEtlpSpec(m):\n" % index
                    str += "\treturn (m.#device_name#Ext%dMEtlp - m.#device_name#LiqLvMEtlp[%d])* % f == 0\n" % (
                    index, index, self.weights['EnthalpyEquWeight'])
                    str += "#model_name#.#device_name#Ext%dMEtlpSpec = Constraint(rule=#device_name#Ext%dMEtlpSpec)\n" % (
                    index, index)
        elif isinstance(self.task, Task.PyomoDynamicTask):
            for index, value in self.extractions.items():
                if value == 'VaporExtractions':
                    # str += "def #device_name#Ext%dMFlowSpec(m, time):\n" % index
                    # str += "\treturn (m.#device_name#Ext%dMFlow[time] - %f)* % f == 0\n" % (
                    # index, self.specifications["Ext%dMFlow" % index], self.weights['FlowEquWeight'])
                    # str += "#model_name#.#device_name#Ext%dMFlowSpec = Constraint(#model_name#.Time, rule=#device_name#Ext%dMFlowSpec)\n" % (
                    # index, index)
                    str += "def #device_name#Ext%dMFracSpec(m, time, comp):\n" % index
                    str += "\treturn m.#device_name#Ext%dMFrac[time, comp] - m.#device_name#VapLvMFrac[time, %d, comp] == 0 \n" % (
                    index, index)
                    str += "#model_name#.#device_name#Ext%dMFracSpec = Constraint(#model_name#.Time, #model_name#.Component, rule=#device_name#Ext%dMFracSpec)\n" % (
                    index, index)
                    str += "def #device_name#Ext%dMEtlpSpec(m, time):\n" % index
                    str += "\treturn (m.#device_name#Ext%dMEtlp[time] - m.#device_name#VapLvMEtlp[time, %d])* % f == 0\n" % (
                    index, index, self.weights['EnthalpyEquWeight'])
                    str += "#model_name#.#device_name#Ext%dMEtlpSpec = Constraint(#model_name#.Time, rule=#device_name#Ext%dMEtlpSpec)\n" % (
                    index, index)
                elif value == 'LiquidExtractions':
                    # str += "def #device_name#Ext%dMFlowSpec(m, time):\n" % index
                    # str += "\treturn (m.#device_name#Ext%dMFlow[time] - %f)* % f == 0\n" % (
                    #     index, self.specifications["Ext%dMFlow" % index], self.weights['FlowEquWeight'])
                    # str += "#model_name#.#device_name#Ext%dMFlowSpec = Constraint(#model_name#.Time, rule=#device_name#Ext%dMFlowSpec)\n" % (
                    #     index, index)
                    str += "def #device_name#Ext%dMFracSpec(m, time, comp):\n" % index
                    str += "\treturn m.#device_name#Ext%dMFrac[time, comp] - m.#device_name#LiqLvMFrac[time, %d, comp] == 0 \n" % (
                        index, index)
                    str += "#model_name#.#device_name#Ext%dMFracSpec = Constraint(#model_name#.Time, #model_name#.Component, rule=#device_name#Ext%dMFracSpec)\n" % (
                        index, index)
                    str += "def #device_name#Ext%dMEtlpSpec(m, time):\n" % index
                    str += "\treturn (m.#device_name#Ext%dMEtlp[time] - m.#device_name#LiqLvMEtlp[time, %d])* % f == 0\n" % (
                        index, index, self.weights['EnthalpyEquWeight'])
                    str += "#model_name#.#device_name#Ext%dMEtlpSpec = Constraint(#model_name#.Time, rule=#device_name#Ext%dMEtlpSpec)\n" % (
                        index, index)
        str = str.replace('#model_name#', self.task.name).replace("#device_name#", self.name)
        return str