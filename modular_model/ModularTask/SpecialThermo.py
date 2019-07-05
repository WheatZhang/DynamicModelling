#!/usr/bin/env python
#-*- coding:utf-8 -*-
import ModularTask.Thermodynamics

class SimpleFitIndexReduRelatedThermo(ModularTask.Thermodynamics.IndexReduRelatedThermo):
    #与模型约简有关的热力学
    def __init__(self, task):
        super().__init__(task)
        self.attributes['NumOfComponent']=2
        self.attributes['Custimized']=False
        self.interfaceVar = ['T', 'P', 'x', 'DtP', 'DtT', 'Dtm', 'PTh', 'Pxh', 'Dtx', 'M', 'hl', 'DtM', 'DtE']
        self.compInterfaceVar = ['x', 'Dtm', 'Pxh', 'Dtx']

    def generatePyomoModel(self):
        str = ""
        str += "from binary_fitting_gradient import liquid_nitrogen_enthalpy_DT,liquid_oxygen_enthalpy_DT,liquid_oxygen_composition_DP,liquid_oxygen_composition_DT\n"
        str += "def LiquidPhaseEnthalpyPartialT(temperature, pressure, oxygen, nitrogen):\n"
        str += "\treturn liquid_nitrogen_enthalpy_DT(pressure, temperature) * nitrogen + liquid_oxygen_enthalpy_DT(pressure,temperature) * oxygen\n"
        return str

    def getInstanceExpr(self, inst):
        str = ""
        str+="def @PTh@(m#index_in_def#):\n"
        str+="\treturn LiquidPhaseEnthalpyPartialT(m.$T$, m.$P$,m.$x,Oxygen$,m.$x,Nitrogen$) \n"
        str+="#model_name#.@PTh@ = Expression(#index_data#rule=@PTh@)\n"
        str+="def @Pxh@(m#index_in_def#, comp):\n"
        str+="\tif comp == 'Oxygen':\n"
        str+="\t\treturn liquid_oxygen_enthalpy(m.$P$, m.$T$)\n"
        str+="\telif comp == 'Nitrogen':\n"
        str+="\t\treturn liquid_nitrogen_enthalpy(m.$P$, m.$T$)\n"
        str+="#model_name#.@Pxh@ = Expression(#index_data##model_name#.Component, rule=@Pxh@)\n"
        str+="def @DtT@(m#index_in_def#):\n"
        str+="\treturn (m.$Dtx,Oxygen$ - liquid_oxygen_composition_DP(m.$P$,m.$T$) *m.$DtP$) / liquid_oxygen_composition_DT(m.$P$, m.$T$)\n"
        str+="#model_name#.@DtT@ = Expression(#index_data#rule=@DtT@)\n"
        str = self.getModifiedString(inst, str)
        return str

    def getInstanceCon(self, inst):
        str = ""
        str += "def #thermo_name#MEtlpEqu(m#index_in_def#):\n"
        str += "\treturn (m.$M$ * (m.$PTh$ * m.$DtT$ + \\\n"
        str += "\t      sum([m.@Pxh@[time, tray, c] * m.@Dtx@[time, tray, c] for c in m.Component])) + \\\n"
        str += "\t      m.$hl$ * m.$DtM$ - m.$DtE$) * 1e-2 == 0\n"
        str += "#model_name#.#thermo_name#MEtlpEqu = Constraint(#index_data#rule=#thermo_name#MEtlpEqu)\n"
        str = self.getModifiedString(inst, str)
        return str

class HPCIndexReduRelatedThermo(ModularTask.Thermodynamics.IndexReduRelatedThermo, ModularTask.Thermodynamics.CstmThermodynamics):
    #与模型约简有关的热力学
    def __init__(self, task):
        super().__init__(task)
        self.attributes['NumOfComponent']=3
        self.attributes['Custimized']=True
        self.interfaceVar = ['T', 'P', 'x', 'DtP', 'DtT', 'Dtm', 'PTh', 'PPh', 'Pxh', 'Dtx', 'M', 'hl', 'DtM', 'DtE']
        self.compInterfaceVar = ['x', 'Dtm', 'Pxh', 'Dtx']

    def getColCstmInstanceImport(self, inst):  # 适用于精馏塔
        str = ""
        for key in inst.param.keys():
            str += "import triHPCThermo." + inst.name + "%dCstmLiqEtlp_pT\n" % key
            str += "import triHPCThermo." + inst.name + "%dCstmLiqEtlp_pP\n" % key
            str += "import triHPCThermo." + inst.name + "%dCstmLiqEtlp_px_N2\n" % key
            str += "import triHPCThermo." + inst.name + "%dCstmLiqO2_pT\n" % key
            str += "import triHPCThermo." + inst.name + "%dCstmLiqO2_pP\n" % key
            str += "import triHPCThermo." + inst.name + "%dCstmLiqO2_px_N2\n" % key
        return str

    def getColCstmInstanceExpr(self, inst):  # 适用于精馏塔
        str = ""
        str+="def @PTh@(m#index_in_def#):\n"
        if inst.indexList[0][0] ==  "time":
            trayName = inst.indexList[1][0]
        else:
            trayName = inst.indexList[0][0]
        fist_statement = True
        for key, value in inst.param.items():
            if fist_statement:
                str += "\tif " + trayName + "==%d:\n" % key
                fist_statement = False
            else:
                str += "\telif " + trayName + "==%d:\n" % key
            str+="\t\treturn triHPCThermo.#prim_thermo_name#%dCstmLiqEtlp_pT.LiqEtlp_pT(m.$P$,m.$T$,m.$x,Nitrogen$) \n"%key
        str+="#model_name#.@PTh@ = Expression(#index_data#rule=@PTh@)\n"
        str += "def @PPh@(m#index_in_def#):\n"
        fist_statement = True
        for key, value in inst.param.items():
            if fist_statement:
                str += "\tif " + trayName + "==%d:\n" % key
                fist_statement = False
            else:
                str += "\telif " + trayName + "==%d:\n" % key
            str += "\t\treturn triHPCThermo.#prim_thermo_name#%dCstmLiqEtlp_pP.LiqEtlp_pP(m.$P$,m.$T$,m.$x,Nitrogen$) \n" % key
        str += "#model_name#.@PPh@ = Expression(#index_data#rule=@PPh@)\n"
        str+="def @Pxh@(m#index_in_def#, comp):\n"
        fist_statement = True
        for key, value in inst.param.items():
            if fist_statement:
                str += "\tif " + trayName + "==%d:\n" % key
                fist_statement = False
            else:
                str += "\telif " + trayName + "==%d:\n" % key
            str+="\t\tif comp == 'Nitrogen':\n"
            str+="\t\t\treturn triHPCThermo.#prim_thermo_name#%dCstmLiqEtlp_px_N2.LiqEtlp_px_N2(m.$P$,m.$T$,m.$x,Nitrogen$) \n" % key
            str += "\t\telse:\n"
            str +="\t\t\treturn 0\n"
        str+="#model_name#.@Pxh@ = Expression(#index_data##model_name#.Component, rule=@Pxh@)\n"
        str+="def @DtT@(m#index_in_def#):\n"
        fist_statement = True
        for key, value in inst.param.items():
            if fist_statement:
                str += "\tif " + trayName + "==%d:\n" % key
                fist_statement = False
            else:
                str += "\telif " + trayName + "==%d:\n" % key
            str+="\t\treturn (m.$Dtx,Oxygen$ - triHPCThermo.#prim_thermo_name#%dCstmLiqO2_pP.LiqO2_pP(m.$P$,m.$T$,m.$x,Nitrogen$) *m.$DtP$\\\n"%key
            str+="    - triHPCThermo.#prim_thermo_name#%dCstmLiqO2_px_N2.LiqO2_px_N2(m.$P$,m.$T$,m.$x,Nitrogen$) *m.$Dtx,Nitrogen$) /\\\n"%key
            str+="    triHPCThermo.#prim_thermo_name#%dCstmLiqO2_pT.LiqO2_pT(m.$P$, m.$T$,m.$x,Nitrogen$)\n"%key
        str+="#model_name#.@DtT@ = Expression(#index_data#rule=@DtT@)\n"
        str = self.getModifiedString(inst, str)
        return str

    def getColCstmInstanceCon(self, inst):
        str = ""
        str += "def #thermo_name#MEtlpEqu(m#index_in_def#):\n"
        str += "\treturn (m.$M$ * (m.$PTh$ * m.$DtT$ + \\\n"
        str += "\t      sum([m.@Pxh@[time, tray, c] * m.@Dtx@[time, tray, c] for c in m.Component])) + \\\n"
        str += "\t      m.$hl$ * m.$DtM$ - m.$DtE$) * 1e-2 == 0\n"
        str += "#model_name#.#thermo_name#MEtlpEqu = Constraint(#index_data#rule=#thermo_name#MEtlpEqu)\n"
        str = self.getModifiedString(inst, str)
        return str