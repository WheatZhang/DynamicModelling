#!/usr/bin/env python
#-*- coding:utf-8 -*-
import re

class Hydraulics(object):
    @staticmethod
    def defaultMethod(task):
        return Hydraulics(task)

    def __init__(self, task):
        self.task = task
        self.attributes = {'Custimized':False}
        self.interfaceVar = ['L', 'M']
        self.parameters = []

    def setParameterValue(self, paraValue):
        self.para_value = {}
        if len(self.parameters) != len(paraValue):
            raise Exception("The number of parameters for hydraulic is not correct.")
        for i in self.parameters:
            self.para_value[i] = paraValue[i]

    def instanciate(self, name, varAlias, indexList):
        return HydraulicsInst(self, name, varAlias, indexList)

    def generatePyomoModel(self):
        return ""
    def getInstancePara(self, inst):
        str = ""
        for i in self.parameters:
            str += "#model_name#.#hydra_name#HydroPara%s" % i + " = Param(initialize=%f)\n" % self.para_value[i]
        str = self.getModifiedString(inst, str)
        return str
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
                    raise Exception("Unknown interface variable %s in hydraulics %s." % (s, inst.name))
            else:
                raise Exception("Too many parameters in interface variable substitution.")
        str = re.sub(r'\$(.*?)\$', replaceForVar, str)
        def replaceForVar2(m):
            s = m.group(1).strip()
            if s in self.interfaceVar:
                s2 = inst.varAlias[s].split(sep='[')
                return s2[0].strip()
            else:
                raise Exception("Unknown interface variable %s in hydraulics %s." % (s, inst.name))
        str = re.sub(r'@(.*?)@', replaceForVar2, str)
        str = str.replace("#hydra_name#", inst.name)
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

class HydraulicsInst(object):
    def __init__(self, skema, name, varAlias, indexList):
        self.skema = skema
        self.name = name
        if len(varAlias) != len(skema.interfaceVar):
            raise Exception("The interface var is not fully designated.")
        for k in varAlias.keys():
            if k not in skema.interfaceVar:
                raise Exception("The interface var name %s does not exist."% k)
        self.varAlias = varAlias
        self.indexList = indexList

    def getHoldupInit(self, other_var_init):
        return self.skema.getHoldupInit(other_var_init)

    def setWeights(self,weights):
        required_weights = [
            'FlowEquWeight'
        ]
        if len(weights) != len(required_weights):
            raise Exception("The numbers of constraint weights for %s in not correct." % self.name)
        for key, value in weights.items():
            if not key in required_weights:
                raise Exception("The constraint weight " + key + "is unavailable.")
        self.weights = weights

    def generatePyomoPara(self):
        return self.skema.getInstancePara(self)

    def generatePyomoVar(self):
        return self.skema.getInstanceVar(self)

    def generatePyomoExpression(self):
        return self.skema.getInstanceExpr(self)

    def generatePyomoCon(self):
        return self.skema.getInstanceCon(self)

class SimpleHydraulics(Hydraulics):
    def __init__(self, task):
        super().__init__(task)
        self.parameters.append('k') #L=k*M

    def getInstanceCon(self, inst):
        str = ""
        str+="def #hydra_name#Hydro(m#index_in_def#):\n"
        str+="\treturn (m.$L$ - m.#hydra_name#HydroParak*m.$M$)*%f == 0\n"%inst.weights['FlowEquWeight']
        str+="#model_name#.#hydra_name#Hydro = Constraint(#index_data#rule=#hydra_name#Hydro)\n"
        str = self.getModifiedString(inst,str)
        return str

    def getHoldupInit(self, other_var_init):
        return other_var_init['L']/self.para_value['k']
