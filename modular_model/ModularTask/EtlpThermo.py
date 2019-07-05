#!/usr/bin/env python
#-*- coding:utf-8 -*-
import ModularTask.Thermodynamics

class SimpleFittingVaporEnthalpy(ModularTask.Thermodynamics.VaporEnthalpyThermo):
    def __init__(self, task):
        super().__init__(task)
        self.attributes['NumOfComponent']=2
        self.attributes['Custimized']=False

    def generatePyomoModel(self):
        str = ""
        str+= "from binary_fitting_result import vapor_nitrogen_enthalpy,vapor_oxygen_enthalpy\n"
        str += "def VaporPhaseEnthalpy(temperature, pressure, oxygen, nitrogen):\n"
        str += "\treturn vapor_nitrogen_enthalpy(pressure,temperature)*nitrogen+vapor_oxygen_enthalpy(pressure,temperature)*oxygen\n"
        return str

    def getInstanceExpr(self, inst):
        str = ""
        str += "def @hv@(m#index_in_def#):\n"
        str += "\treturn VaporPhaseEnthalpy(m.$T$, m.$P$,m.$y,Oxygen$,m.$y,Nitrogen$)\n"
        str += "#model_name#.@hv@ = Expression(#index_data#rule=@hv@)\n"
        str = self.getModifiedString(inst, str)
        return str

class SimpleFittingLiquidEnthalpy(ModularTask.Thermodynamics.LiquidEnthalpyThermo):
    def __init__(self, task):
        super().__init__(task)
        self.attributes['NumOfComponent']=2
        self.attributes['Custimized']=False
    def generatePyomoModel(self):
        str = ""
        str+= "from binary_fitting_result import liquid_nitrogen_enthalpy,liquid_oxygen_enthalpy\n"
        str += "def LiquidPhaseEnthalpy(temperature, pressure, oxygen, nitrogen):\n"
        str += "\treturn liquid_nitrogen_enthalpy(pressure,temperature)*nitrogen+liquid_oxygen_enthalpy(pressure,temperature)*oxygen\n"
        return str

    def getInstanceExpr(self, inst):
        str = ""
        str += "def @hl@(m#index_in_def#):\n"
        str += "\treturn LiquidPhaseEnthalpy(m.$T$, m.$P$,m.$x,Oxygen$,m.$x,Nitrogen$)\n"
        str += "#model_name#.@hl@ = Expression(#index_data#rule=@hl@)\n"
        str = self.getModifiedString(inst, str)
        return str

class CstmTrinaryHPCVapEtlp(ModularTask.Thermodynamics.VaporEnthalpyThermo, ModularTask.Thermodynamics.CstmThermodynamics):
    def __init__(self, task):
        super().__init__(task)
        self.attributes['NumOfComponent']=3
        self.attributes['Custimized']=True
        self.interfaceVar = ['y', 'x', 'T', 'P', 'hv']
        self.compInterfaceVar = ['y','x']

    def getInstanceImport(self, inst):#适用于容器设备
        str = ""
        str += "import triHPCThermo." + inst.name + "CstmVapEtlp\n"
        return str

    def getInstanceExpr(self, inst):
        str = ""
        str += "def @hv@(m#index_in_def#):\n"
        str += "\treturn triHPCThermo.#prim_thermo_name#CstmVapEtlp.VapEtlp(m.$P$, m.$T$,m.$x,Nitrogen$)\n"
        str += "#model_name#.@hv@ = Expression(#index_data#rule=@hv@)\n"
        str = self.getModifiedString(inst, str)
        return str

    def getColCstmInstanceImport(self, inst):#适用于精馏塔
        str = ""
        for key in inst.param.keys():
            str += "import triHPCThermo." + inst.name + "%dCstmVapEtlp\n"%key
        return str

    def getColCstmInstanceExpr(self,inst):
        str = ""
        if inst.indexList[0][0] ==  "time":
            trayName = inst.indexList[1][0]
        else:
            trayName = inst.indexList[0][0]
        str += "def @hv@(m#index_in_def#):\n"
        fist_statement = True
        for key, value in inst.param.items():
            if fist_statement:
                str += "\tif " + trayName + "==%d:\n" % key
                fist_statement = False
            else:
                str += "\telif " + trayName + "==%d:\n" % key
            str += "\t\treturn triHPCThermo.#prim_thermo_name#%dCstmVapEtlp.VapEtlp(m.$P$, m.$T$,m.$x,Nitrogen$)\n" % key
        str += "#model_name#.@hv@ = Expression(#index_data#rule=@hv@)\n"
        str = self.getModifiedString(inst, str)
        return str

class CstmTrinaryHPCLiqEtlp(ModularTask.Thermodynamics.LiquidEnthalpyThermo, ModularTask.Thermodynamics.CstmThermodynamics):
    def __init__(self, task):
        super().__init__(task)
        self.attributes['NumOfComponent']=3
        self.attributes['Custimized']=True

    def getInstanceImport(self, inst):#适用于容器设备
        str = ""
        str += "import triHPCThermo." + inst.name + "CstmLiqEtlp\n"
        return str

    def getInstanceExpr(self, inst):
        str = ""
        str += "def @hl@(m#index_in_def#):\n"
        str += "\treturn triHPCThermo.#prim_thermo_name#CstmLiqEtlp.LiqEtlp(m.$P$, m.$T$,m.$x,Nitrogen$)\n"
        str += "#model_name#.@hl@ = Expression(#index_data#rule=@hl@)\n"
        str = self.getModifiedString(inst, str)
        return str

    def getColCstmInstanceImport(self, inst):#适用于精馏塔
        str = ""
        for key in inst.param.keys():
            str += "import triHPCThermo." + inst.name + "%dCstmLiqEtlp\n"%key
        return str

    def getColCstmInstanceExpr(self,inst):
        str = ""
        if inst.indexList[0][0] ==  "time":
            trayName = inst.indexList[1][0]
        else:
            trayName = inst.indexList[0][0]
        str += "def @hl@(m#index_in_def#):\n"
        fist_statement = True
        for key, value in inst.param.items():
            if fist_statement:
                str += "\tif " + trayName + "==%d:\n" % key
                fist_statement = False
            else:
                str += "\telif " + trayName + "==%d:\n" % key
            str += "\t\treturn triHPCThermo.#prim_thermo_name#%dCstmLiqEtlp.LiqEtlp(m.$P$, m.$T$,m.$x,Nitrogen$)\n" % key
        str += "#model_name#.@hl@ = Expression(#index_data#rule=@hl@)\n"
        str = self.getModifiedString(inst, str)
        return str