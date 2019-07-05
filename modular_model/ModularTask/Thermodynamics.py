#!/usr/bin/env python
#-*- coding:utf-8 -*-
import re

class Thermodynamics(object):
    def __init__(self, task):
        self.task = task
        self.attributes = {'NumOfComponent':None,'Custimized':False}
    def instanciate(self, name, varAlias, indexList):
        return ThermodynamicsInst(self, name, varAlias, indexList)
    def getInstanceImport(self, inst):
        return ""
    def generatePyomoModel(self):
        return ""
    def getInstancePara(self, inst):
        return ""
    def getInstanceVar(self, inst):
        return ""
    def getInstanceExpr(self, inst):
        return ""
    def getInstanceCon(self, inst):
        return ""
    def getModifiedString(self,inst,str):
        def replaceForVar(m):
            s = m.group(1).split(sep=',')
            if len(s) == 1:
                s = s[0].strip()
                if s in self.interfaceVar:
                    return inst.varAlias[s]
                else:
                    raise Exception("Unknown interface variable %s in thermodynamics %s." % (s, inst.name))
            elif len(s) == 2:
                var_name = s[0].strip()
                if var_name in self.compInterfaceVar:
                    comp = s[1].strip()
                    if comp in self.task.component:
                        return inst.varAlias[var_name].replace('#comp#',"\""+comp+"\"")
                    else:
                        raise Exception("Unknown component %s in thermodynamics %s." % (comp, inst.name))
                else:
                    raise Exception("Unknown interface variable %s in thermodynamics %s." % (var_name, inst.name))
            else:
                raise Exception("Too many parameters in interface variable substitution.")
        str = re.sub(r'\$(.*?)\$', replaceForVar, str)  #$x$代表接口变量x
        def replaceForVar2(m):
            s = m.group(1).strip()
            if s in self.interfaceVar:
                s2 = inst.varAlias[s].split(sep='[')
                return s2[0].strip()
            else:
                raise Exception("Unknown interface variable %s in thermodynamics %s." % (s, inst.name))
        str = re.sub(r'@(.*?)@', replaceForVar2, str) #@x@代表不带索引的接口变量x
        str = str.replace("#thermo_name#", inst.name)
        str = str.replace("#prim_thermo_name#", inst.prim_name)
        str = str.replace("#model_name#", self.task.name)
        index_str = ""
        index_data_str = ""
        index_in_def_str = ""
        first_flag = True
        for item in inst.indexList:
            if first_flag:
                first_flag = False
            else:
                index_str += ','
            index_data_str +=self.task.name + "." + item[1]+ ','
            index_str += item[0]
            index_in_def_str += ','+ item[0]
        str = str.replace("#index#", index_str)
        str = str.replace('#index_in_def#', index_in_def_str)
        str = str.replace("#index_data#", index_data_str)
        return str

class CstmThermodynamics(Thermodynamics):
    def instanciate(self, name, varAlias, indexList, creatFile):
        inst = super().instanciate(name, varAlias, indexList)
        inst.flagCreatFile = creatFile
        return inst
    def instanciateColumnThermo(self, name, varAlias, indexList, creatFile):
        return ColumnCstmThermoInst(self, name, varAlias, indexList, creatFile)
    def getColCstmInstanceImport(self, inst):
        return ""
    def getColCstmInstancePara(self, inst):
        return ""
    def getColCstmInstanceVar(self, inst):
        return ""
    def getColCstmInstanceExpr(self, inst):
        return ""
    def getColCstmInstanceCon(self, inst):
        return ""
    def __init__(self, task):
        super().__init__(task)
        self.required_param = []

class CompositionThermo(Thermodynamics):
    @staticmethod
    def defaultMethod(task):
        return CompositionThermo(task)
    def __init__(self, task):
        super().__init__(task)
        self.interfaceVar = ['x','y','T','P']
        self.compInterfaceVar = ['x','y']

class VaporEnthalpyThermo(Thermodynamics):
    @staticmethod
    def defaultMethod(task):
        return VaporEnthalpyThermo(task)
    def __init__(self, task):
        super().__init__(task)
        self.interfaceVar = ['y','T','P','hv']
        self.compInterfaceVar = ['y']

class LiquidEnthalpyThermo(Thermodynamics):
    @staticmethod
    def defaultMethod(task):
        return LiquidEnthalpyThermo(task)
    def __init__(self, task):
        super().__init__(task)
        self.interfaceVar = ['x', 'T', 'P','hl']
        self.compInterfaceVar = ['x']

class BubblePointThermo(Thermodynamics):
    @staticmethod
    def defaultMethod(task):
        return BubblePointThermo(task)
    def __init__(self, task):
        super().__init__(task)
        self.interfaceVar = ['c','T','P']
        self.compInterfaceVar = ['c']

class IndexReduRelatedThermo(Thermodynamics):
    @staticmethod
    def defaultMethod(task):
        return IndexReduRelatedThermo(task)
    def __init__(self, task):
        super().__init__(task)

class LiqEquilDensityThermo(Thermodynamics):
    @staticmethod
    def defaultMethod(task):
        return LiqDensityThermo(task)
    def __init__(self, task):
        super().__init__(task)
        self.interfaceVar = ['T', 'P','rhol']
        self.compInterfaceVar = []

class LiqDensityThermo(Thermodynamics):
    @staticmethod
    def defaultMethod(task):
        return LiqDensityThermo(task)
    def __init__(self, task):
        super().__init__(task)
        self.interfaceVar = ['T', 'P','c','rhol']
        self.compInterfaceVar = ['c']

class VapEquilDensityThermo(Thermodynamics):
    @staticmethod
    def defaultMethod(task):
        return LiqDensityThermo(task)

    def __init__(self, task):
        super().__init__(task)
        self.interfaceVar = ['T', 'P', 'rhov']
        self.compInterfaceVar = []

class ThermodynamicsInst(object):
    def __init__(self, skema, name, varAlias, indexList):
        self.skema = skema
        self.name = name
        # if len(varAlias) != len(skema.interfaceVar):
        #     raise Exception("The interface var is not fully designated.")
        for k in varAlias.keys():
            if k not in skema.interfaceVar:
                raise Exception("The interface var name %s does not exist."% k)
        self.varAlias = varAlias
        self.indexList = indexList
        self.prim_name = name
    def setParameters(self,param):
        self.param = param

    def generatePyomoModel(self):
        return self.skema.getInstanceImport(self)

    def generatePyomoPara(self):
        return self.skema.getInstancePara(self)

    def generatePyomoVar(self):
        return self.skema.getInstanceVar(self)

    def generatePyomoExpression(self):
        return self.skema.getInstanceExpr(self)

    def generatePyomoCon(self):
        return self.skema.getInstanceCon(self)

class ColumnCstmThermoInst(ThermodynamicsInst):
    def __init__(self, skema, name, varAlias, indexList,creatFile):
        super().__init__(skema, name, varAlias, indexList)
        self.flagCreatFile = creatFile

    def generatePyomoModel(self):
        return self.skema.getColCstmInstanceImport(self)

    def generatePyomoPara(self):
        return self.skema.getColCstmInstancePara(self)

    def generatePyomoVar(self):
        return self.skema.getColCstmInstanceVar(self)

    def generatePyomoExpression(self):
        return self.skema.getColCstmInstanceExpr(self)

    def generatePyomoCon(self):
        return self.skema.getColCstmInstanceCon(self)

class ThermodynamicsInstList(object):
    def __init__(self):
        self.data = []
    def append(self,item):
        self.data.append(item)
    def generatePyomoModel(self):
        str = ""
        for i in self.data:
            str+=i.generatePyomoModel()
        return str

    def generatePyomoPara(self):
        str = ""
        for i in self.data:
            str += i.generatePyomoPara()
        return str

    def generatePyomoVar(self):
        str = ""
        for i in self.data:
            str += i.generatePyomoVar()
        return str

    def generatePyomoExpression(self):
        str = ""
        for i in self.data:
            str += i.generatePyomoExpression()
        return str

    def generatePyomoCon(self):
        str = ""
        for i in self.data:
            str += i.generatePyomoCon()
        return str


