#!/usr/bin/env python
#-*- coding:utf-8 -*-
import ModularTask.CstmThermo
import ModularTask.Thermodynamics
import os

class SimpleFittingComposition(ModularTask.Thermodynamics.CompositionThermo):
    def __init__(self, task):
        super().__init__(task)
        self.attributes['NumOfComponent']=2
        self.attributes['Custimized']=False

    def generatePyomoModel(self):
        return "from binary_fitting_result import vapor_oxygen_composition,liquid_oxygen_composition\n"

    def getInstanceVar(self,inst):
        str = ""
        str += "#model_name#.@x@ = Var(#index_data##model_name#.Component, bounds=(0, 1))\n"
        str += "#model_name#.@y@ = Var(#index_data##model_name#.Component, bounds=(0, 1))\n"
        str = self.getModifiedString(inst, str)
        return str

    def getInstanceCon(self, inst):
        str = ""
        str+="def #thermo_name#VapFrac(m#index_in_def#):\n"
        str+="\treturn m.$y,Oxygen$ == vapor_oxygen_composition(m.$P$,m.$T$)\n"
        str+="#model_name#.#thermo_name#VapFrac = Constraint(#index_data#rule=#thermo_name#VapFrac)\n"

        str += "def #thermo_name#LiqFrac(m#index_in_def#):\n"
        str += "\treturn m.$x,Oxygen$ == liquid_oxygen_composition(m.$P$,m.$T$)\n"
        str += "#model_name#.#thermo_name#LiqFrac = Constraint(#index_data#rule=#thermo_name#LiqFrac)\n"
        str = self.getModifiedString(inst,str)
        return str

class CstmBinaryMargulesCompo(ModularTask.Thermodynamics.CompositionThermo, ModularTask.Thermodynamics.CstmThermodynamics):
    def __init__(self, task):
        super().__init__(task)
        self.attributes['NumOfComponent']=2
        self.attributes['Custimized']=True
        self.required_param = ['temp_span','pressure_span']

    def getInstanceImport(self, inst):
        if not os.path.exists('margules/'):
            os.makedirs('margules')
        str = ""
        str += "import margules." + inst.name + "CstmComp as "+ inst.name + "CstmComp\n"
        if inst.flagCreatFile:
            ModularTask.CstmThermo.margules.create_binary_margules(filename = "margules/"+inst.name + "CstmComp", temp_span=inst.param['temp_span'],
                                                       pressure_span=inst.param['pressure_span'])
        return str

    def getInstanceVar(self,inst):
        str = ""
        str += "#model_name#.@x@ = Var(#index_data##model_name#.Component, bounds=(0, 1))\n"
        str += "#model_name#.@y@ = Var(#index_data##model_name#.Component, bounds=(0, 1))\n"
        str = self.getModifiedString(inst, str)
        return str

    def getInstanceCon(self, inst):
        str = ""
        str+="def #thermo_name#VapFrac(m#index_in_def#):\n"
        str+="\treturn m.$y,Oxygen$ == #prim_thermo_name#CstmComp.vap_oxygen_composition(m.$P$,m.$T$)\n"
        str+="#model_name#.#thermo_name#VapFrac = Constraint(#index_data#rule=#thermo_name#VapFrac)\n"

        str += "def #thermo_name#LiqFrac(m#index_in_def#):\n"
        str += "\treturn m.$x,Oxygen$ == #prim_thermo_name#CstmComp.liq_oxygen_composition(m.$P$,m.$T$)\n"
        str += "#model_name#.#thermo_name#LiqFrac = Constraint(#index_data#rule=#thermo_name#LiqFrac)\n"
        str = self.getModifiedString(inst,str)
        return str

    def getColCstmInstanceImport(self, inst):
        if not os.path.exists('margules/'):
            os.makedirs('margules')
        str = ""
        for key in inst.param.keys():
            str += "import margules." + inst.name + "CstmComp%d as " % key+ inst.name + "CstmComp%d\n" % key
        if inst.flagCreatFile:
            for key in inst.param.keys():
                ModularTask.CstmThermo.margules.create_binary_margules(filename = "margules/"+inst.name + "CstmComp%d"%key, temp_span=inst.param[key]['temp_span'],
                                                       pressure_span=inst.param[key]['pressure_span'])
        return str

    def getColCstmInstanceVar(self,inst):
        str = ""
        str += "#model_name#.@x@ = Var(#index_data##model_name#.Component, bounds=(0, 1))\n"
        str += "#model_name#.@y@ = Var(#index_data##model_name#.Component, bounds=(0, 1))\n"
        str = self.getModifiedString(inst, str)
        return str

    def getColCstmInstanceCon(self, inst):
        str = ""
        if inst.indexList[0][0] ==  "time":
            trayName = inst.indexList[1][0]
        else:
            trayName = inst.indexList[0][0]
        str+="def #thermo_name#VapFrac(m#index_in_def#):\n"
        fist_statement = True
        for key,value in inst.param.items():
            if fist_statement:
                str+="\tif "+trayName+"==%d:\n"%key
                fist_statement=False
            else:
                str += "\telif " + trayName + "==%d:\n" % key
            str+="\t\treturn m.$y,Oxygen$ == #prim_thermo_name#CstmComp%d.vap_oxygen_composition(m.$P$,m.$T$)\n"%key
        str+="#model_name#.#thermo_name#VapFrac = Constraint(#index_data#rule=#thermo_name#VapFrac)\n"

        str += "def #thermo_name#LiqFrac(m#index_in_def#):\n"
        fist_statement = True
        for key, value in inst.param.items():
            if fist_statement:
                str += "\tif " + trayName + "==%d:\n" % key
                fist_statement = False
            else:
                str += "\telif " + trayName + "==%d:\n" % key
            str += "\t\treturn m.$x,Oxygen$ == #prim_thermo_name#CstmComp%d.liq_oxygen_composition(m.$P$,m.$T$)\n"%key
        str += "#model_name#.#thermo_name#LiqFrac = Constraint(#index_data#rule=#thermo_name#LiqFrac)\n"
        str = self.getModifiedString(inst,str)
        return str

class CstmTrinaryHPCCompo(ModularTask.Thermodynamics.CompositionThermo, ModularTask.Thermodynamics.CstmThermodynamics):
    def __init__(self, task):
        super().__init__(task)
        self.attributes['NumOfComponent']=3
        self.attributes['Custimized']=True

    def getInstanceImport(self, inst):#适用于容器设备
        str = ""
        str += "import triHPCThermo." + inst.name + "CstmLiqO2\n"
        str += "import triHPCThermo." + inst.name + "CstmVapO2\n"
        str += "import triHPCThermo." + inst.name + "CstmVapN2\n"
        return str

    def getInstanceVar(self,inst):
        str = ""
        str += "#model_name#.@x@ = Var(#index_data##model_name#.Component, bounds=(0, 1))\n"
        str += "#model_name#.@y@ = Var(#index_data##model_name#.Component, bounds=(0, 1))\n"
        str = self.getModifiedString(inst, str)
        return str

    def getInstanceCon(self, inst):
        str = ""
        str += "def #thermo_name#LiqO2Frac(m#index_in_def#):\n"
        str += "\treturn m.$x,Oxygen$ == triHPCThermo.#prim_thermo_name#CstmLiqO2.LiqO2(m.$P$,m.$T$,m.$x,Nitrogen$)\n"
        str += "#model_name#.#thermo_name#LiqO2Frac = Constraint(#index_data#rule=#thermo_name#LiqO2Frac)\n"

        str += "def #thermo_name#VapO2Frac(m#index_in_def#):\n"
        str += "\treturn m.$y,Oxygen$ == triHPCThermo.#prim_thermo_name#CstmVapO2.VapO2(m.$P$,m.$T$,m.$x,Nitrogen$)\n"
        str += "#model_name#.#thermo_name#VapO2Frac = Constraint(#index_data#rule=#thermo_name#VapO2Frac)\n"

        str += "def #thermo_name#VapN2Frac(m#index_in_def#):\n"
        str += "\treturn m.$y,Nitrogen$ == triHPCThermo.#prim_thermo_name#CstmVapN2.VapN2(m.$P$,m.$T$,m.$x,Nitrogen$)\n"
        str += "#model_name#.#thermo_name#VapN2Frac = Constraint(#index_data#rule=#thermo_name#VapN2Frac)\n"
        str = self.getModifiedString(inst,str)
        return str

    def getColCstmInstanceImport(self, inst):#适用于精馏塔
        str = ""
        for key in inst.param.keys():
            str += "import triHPCThermo." + inst.name + "%dCstmLiqO2\n"%key
            str += "import triHPCThermo." + inst.name + "%dCstmVapO2\n"%key
            str += "import triHPCThermo." + inst.name + "%dCstmVapN2\n"%key
        return str

    def getColCstmInstanceVar(self,inst):
        str = ""
        str += "#model_name#.@x@ = Var(#index_data##model_name#.Component, bounds=(0, 1))\n"
        str += "#model_name#.@y@ = Var(#index_data##model_name#.Component, bounds=(0, 1))\n"
        str = self.getModifiedString(inst, str)
        return str

    def getColCstmInstanceCon(self, inst):
        str = ""
        if inst.indexList[0][0] ==  "time":
            trayName = inst.indexList[1][0]
        else:
            trayName = inst.indexList[0][0]
        str+="def #thermo_name#LiqO2Frac(m#index_in_def#):\n"
        fist_statement = True
        for key,value in inst.param.items():
            if fist_statement:
                str+="\tif "+trayName+"==%d:\n"%key
                fist_statement=False
            else:
                str += "\telif " + trayName + "==%d:\n" % key
            str+="\t\treturn m.$x,Oxygen$ == triHPCThermo.#prim_thermo_name#%dCstmLiqO2.LiqO2(m.$P$,m.$T$,m.$x,Nitrogen$)\n"%key
        str+="#model_name#.#thermo_name#LiqO2Frac = Constraint(#index_data#rule=#thermo_name#LiqO2Frac)\n"

        str += "def #thermo_name#VapO2Frac(m#index_in_def#):\n"
        fist_statement = True
        for key, value in inst.param.items():
            if fist_statement:
                str += "\tif " + trayName + "==%d:\n" % key
                fist_statement = False
            else:
                str += "\telif " + trayName + "==%d:\n" % key
            str += "\t\treturn m.$y,Oxygen$ == triHPCThermo.#prim_thermo_name#%dCstmVapO2.VapO2(m.$P$,m.$T$,m.$x,Nitrogen$)\n" % key
        str += "#model_name#.#thermo_name#VapO2Frac = Constraint(#index_data#rule=#thermo_name#VapO2Frac)\n"

        str += "def #thermo_name#VapN2Frac(m#index_in_def#):\n"
        fist_statement = True
        for key, value in inst.param.items():
            if fist_statement:
                str += "\tif " + trayName + "==%d:\n" % key
                fist_statement = False
            else:
                str += "\telif " + trayName + "==%d:\n" % key
            str += "\t\treturn m.$y,Nitrogen$ == triHPCThermo.#prim_thermo_name#%dCstmVapN2.VapN2(m.$P$,m.$T$,m.$x,Nitrogen$)\n" % key
        str += "#model_name#.#thermo_name#VapN2Frac = Constraint(#index_data#rule=#thermo_name#VapN2Frac)\n"
        str = self.getModifiedString(inst,str)
        return str