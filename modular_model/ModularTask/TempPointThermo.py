#!/usr/bin/env python
#-*- coding:utf-8 -*-
import ModularTask.Thermodynamics

class SimpleFittingBubblePoint(ModularTask.Thermodynamics.BubblePointThermo):
    def __init__(self, task):
        super().__init__(task)
        self.attributes['NumOfComponent']=2
        self.attributes['Custimized']=False
    def generatePyomoModel(self):
        str = ""
        #str+= "from binary_fitting_result import bubble_point\n"
        return str

    def getInstanceVar(self, inst):
        str = ""
        str += "#model_name#.@T@ = Var(#index_data#initialize = 0)\n"
        str = self.getModifiedString(inst, str)
        return str

    def getInstanceCon(self, inst):
        str = ""
        str += "def #thermo_name#BubTemp(m#index_in_def#):\n"
        str += "\treturn m.$c,Oxygen$ == liquid_oxygen_composition(m.$P$,m.$T$)\n"
        str += "#model_name#.#thermo_name#BubTemp = Constraint(#index_data#rule=#thermo_name#BubTemp)\n"
        str = self.getModifiedString(inst, str)
        return str

class HPCCondensorBubblePoint(ModularTask.Thermodynamics.BubblePointThermo):
    def __init__(self, task):
        super().__init__(task)
        self.attributes['NumOfComponent']=3
        self.attributes['Custimized']=False
    def generatePyomoModel(self):
        str = ""
        #str+= "from binary_fitting_result import bubble_point\n"
        return str

    def getInstanceImport(self, inst):#适用于容器设备
        str = ""
        str += "import triHPCThermo." + inst.name + "CstmLiqO2\n"
        return str

    def getInstanceVar(self, inst):
        str = ""
        str += "#model_name#.@T@ = Var(#index_data#initialize = 0)\n"
        str = self.getModifiedString(inst, str)
        return str

    def getInstanceCon(self, inst):
        str = ""
        str += "def #thermo_name#BubTemp(m#index_in_def#):\n"
        str += "\treturn m.$c,Oxygen$ == triHPCThermo.#prim_thermo_name#CstmLiqO2.LiqO2(m.$P$,m.$T$,m.$c,Nitrogen$)\n"
        str += "#model_name#.#thermo_name#BubTemp = Constraint(#index_data#rule=#thermo_name#BubTemp)\n"
        str = self.getModifiedString(inst, str)
        return str