#!/usr/bin/env python
#-*- coding:utf-8 -*-
import ModularTask.Thermodynamics

class SimpleFitLiqEquilDensityThermo(ModularTask.Thermodynamics.LiqEquilDensityThermo):
    def __init__(self, task):
        super().__init__(task)
        self.attributes['NumOfComponent']=2
        self.attributes['Custimized']=False
    def generatePyomoModel(self):
        str = ""
        str+= "from binary_fitting_density import liquid_density\n"
        return str

    def getInstanceExpr(self, inst):
        str = ""
        str += "def @rhol@(m#index_in_def#):\n"
        str += "\treturn liquid_density(m.$P$, m.$T$)\n"
        str += "#model_name#.@rhol@ = Expression(#index_data#rule=@rhol@)\n"
        str = self.getModifiedString(inst, str)
        return str

class SimpleFitVapEquilDensityThermo(ModularTask.Thermodynamics.VapEquilDensityThermo):
    def __init__(self, task):
        super().__init__(task)
        self.attributes['NumOfComponent']=2
        self.attributes['Custimized']=False
    def generatePyomoModel(self):
        str = ""
        str+= "from binary_fitting_density import vapor_density\n"
        return str

    def getInstanceExpr(self, inst):
        str = ""
        str += "def @rhov@(m#index_in_def#):\n"
        str += "\treturn liquid_density(m.$P$, m.$T$)\n"
        str += "#model_name#.@rhov@ = Expression(#index_data#rule=@rhov@)\n"
        str = self.getModifiedString(inst, str)
        return str

class CstmTrinaryHPCLiqDensity(ModularTask.Thermodynamics.LiqEquilDensityThermo, ModularTask.Thermodynamics.CstmThermodynamics):
    def __init__(self, task):
        super().__init__(task)
        self.attributes['NumOfComponent']=3
        self.attributes['Custimized']=True

    def getInstanceImport(self, inst):#适用于容器设备
        str = ""
        str += "import triHPCThermo." + inst.name + "CstmLiqRho\n"
        return str

    def getInstanceExpr(self, inst):
        str = ""
        str += "def @rhol@(m#index_in_def#):\n"
        str += "\treturn triHPCThermo.#prim_thermo_name#CstmLiqRho.LiqRho(m.$P$, m.$T$,m.$x,Nitrogen$)\n"
        str += "#model_name#.@rhol@ = Expression(#index_data#rule=@rhol@)\n"
        str = self.getModifiedString(inst, str)
        return str

    def getColCstmInstanceImport(self, inst):#适用于精馏塔
        str = ""
        for key in inst.param.keys():
            str += "import triHPCThermo." + inst.name + "%dCstmLiqRho\n"%key
        return str

    def getColCstmInstanceExpr(self,inst):
        str = ""
        if inst.indexList[0][0] ==  "time":
            trayName = inst.indexList[1][0]
        else:
            trayName = inst.indexList[0][0]
        str += "def @rhol@(m#index_in_def#):\n"
        fist_statement = True
        for key, value in inst.param.items():
            if fist_statement:
                str += "\tif " + trayName + "==%d:\n" % key
                fist_statement = False
            else:
                str += "\telif " + trayName + "==%d:\n" % key
            str += "\t\treturn triHPCThermo.#prim_thermo_name#%dCstmLiqRho.LiqRho(m.$P$, m.$T$,m.$x,Nitrogen$)\n" % key
        str += "#model_name#.@rhol@ = Expression(#index_data#rule=@rhol@)\n"
        str = self.getModifiedString(inst, str)
        return str