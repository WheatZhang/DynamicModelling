#!/usr/bin/env python
#-*- coding:utf-8 -*-
import ModularTask.Task as Task
import re

class Controller(object):
    def __init__(self,task):
        self.task = task
        self.parameters = []
    def instanciate(self, name, varAlias):
        return ControllerInst(self, name, varAlias)
    def getInstancePara(self, inst):
        str = ""
        for i in self.parameters:
            str += "#model_name#.#ctrl_name#Para%s" % i + " = Param(initialize=%f)\n" % inst.para_value[i]
        str = self.getModifiedString(inst, str)
        return str
    def getInstanceVar(self, inst):
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
                    raise Exception("Unknown interface variable %s in controller instance %s." % (s, inst.name))
            else:
                raise Exception("Too many parameters in interface variable substitution.")
        str = re.sub(r'\$(.*?)\$', replaceForVar, str)
        def replaceForVar2(m):
            s = m.group(1).strip()
            if s in self.interfaceVar:
                s2 = inst.varAlias[s].split(sep='[')
                return s2[0].strip()
            else:
                raise Exception("Unknown interface variable %s in controller instance %s." % (s, inst.name))
        str = re.sub(r'@(.*?)@', replaceForVar2, str)
        str = str.replace("#ctrl_name#", inst.name)
        str = str.replace("#model_name#", self.task.name)
        return str

class PIController(Controller):
    def __init__(self, task):
        super().__init__(task)
        self.interfaceVar = ['MV','CV']
        self.parameters.append('Kc')
        self.parameters.append('Ti')

class ControllerInst(object):
    def __init__(self, skema, name, varAlias):
        self.skema = skema
        self.name = name
        if len(varAlias) != len(skema.interfaceVar):
            raise Exception("The interface var is not fully designated.")
        for k in varAlias.keys():
            if k not in skema.interfaceVar:
                raise Exception("The interface var name %s does not exist."% k)
        self.varAlias = varAlias

    def generatePyomoPara(self):
        return self.skema.getInstancePara(self)

    def generatePyomoVar(self):
        return self.skema.getInstanceVar(self)

    def generatePyomoCon(self):
        return self.skema.getInstanceCon(self)

    def setParameterValue(self, paraValue):
        self.para_value = {}
        if len(self.skema.parameters) != len(paraValue):
            raise Exception("The number of parameters for a controller is not correct.")
        for i in self.skema.parameters:
            self.para_value[i] = paraValue[i]

    def setCtrlOffset(self, mv_ss, cv_ss):
        self.mv_ss = mv_ss
        self.cv_ss = cv_ss

class FixedPIController(PIController):
    def getInstancePara(self, inst):
        str = ""
        str += super().getInstancePara(inst)
        str += "#model_name#.#ctrl_name#ParaMVSS = Param(initialize=%f)\n" % inst.mv_ss
        str += "#model_name#.#ctrl_name#ParaCVSS = Param(initialize=%f)\n" % inst.cv_ss
        str = self.getModifiedString(inst, str)
        return str
    def getInstanceVar(self, inst):
        str = ""
        str += "#model_name#.#ctrl_name#SumError = Var(#model_name#.Time, initialize=0)\n"
        str += "#model_name#.#ctrl_name#Error = DerivativeVar(#model_name#.#ctrl_name#SumError,initialize=0)\n"
        str = self.getModifiedString(inst, str)
        return str
    def getInstanceCon(self, inst):
        str = ""
        str += "def #ctrl_name#DefError(m, time):\n"
        str += "\treturn m.#ctrl_name#Error[time] - m.$CV$ + m.#ctrl_name#ParaCVSS == 0\n"
        str += "#model_name#.#ctrl_name#DefError = Constraint(#model_name#.Time,rule=#ctrl_name#DefError)\n"

        str += "def #ctrl_name#PILaw(m, time):\n"
        str += "\treturn m.#ctrl_name#ParaMVSS + m.#ctrl_name#ParaKc * (m.$CV$ - m.#ctrl_name#ParaCVSS)"
        str += "+m.#ctrl_name#ParaKc/m.#ctrl_name#ParaTi*m.#ctrl_name#SumError[time]-m.$MV$ == 0\n"
        str += "#model_name#.#ctrl_name#PILaw = Constraint(#model_name#.Time,rule=#ctrl_name#PILaw)\n"

        str += "def #ctrl_name#ICSumError(m):\n"
        str += "\treturn m.#ctrl_name#SumError[0] == 0\n"
        str += "#model_name#.#ctrl_name#ICSumError = Constraint(rule=#ctrl_name#ICSumError)\n"
        str = self.getModifiedString(inst, str)
        return str