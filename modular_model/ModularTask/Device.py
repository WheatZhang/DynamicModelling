#!/usr/bin/env python
#-*- coding:utf-8 -*-
from pyomo.environ import *
from pyomo.dae import *
import ModularTask.Task as Task
import ModularTask.ModelingTools
from types import FunctionType

class PyomoDevice(object):
    def __init__(self,task, name):
        self.task = task
        self.primitive_name = name
        self.name = name
        self.inputStreams = {}
        self.outputStreams = {}

    def setDeviceDevParam(self, required_specifications, specifications):
        if len(specifications) != len(required_specifications):
            raise Exception("The number of specifications for %s in not correct." % self.name)
        for key, value in specifications.items():
            if not key in required_specifications:
                raise Exception("The specification " + key + "is unavailable.")
            if isinstance(value, list):
                raise Exception("Device parameters can not be time varied.")
            if isinstance(value, FunctionType):
                raise Exception("Device parameters can not be time varied.")
        self.device_param = specifications

    def setDeviceOptions(self, available_options, options):
        for key, value in options.items():
            if type(available_options[key]) == 'list':
                if value not in available_options[key]:
                    raise Exception("The option value for " + key + "is not unavailable.")
            elif type(available_options[key]) == 'string':
                if not isinstance(value, available_options[key]):
                    raise Exception("The option value for " + key + "is type incorrect.")
        for key, value in available_options.items():
            if type(value) == 'list':
                if key not in options.keys():
                    options[key] = value[0]
        self.options = options

    def setDeviceSpecs(self, required_specifications, specifications):
        if len(specifications) != len(required_specifications):
            raise Exception("The number of specifications for %s in not correct." % self.name)
        for key, value in specifications.items():
            if not key in required_specifications:
                raise Exception("The specification " + key + "is unavailable.")
        self.specifications = specifications

    def generatePyomoPara(self):
        return ""

    def generatePyomoVar(self):
        return ""

    def generatePyomoExpression(self):
        return ""

    def generatePyomoCon(self):
        return ""

    def getNaiveDynamicInitValue(self):
        pass

    def rename(self, old_name, new_name):
        self.name = new_name
        all_attr = dir(self)
        for attr in all_attr:
            if isinstance(getattr(self,attr), ModularTask.Thermodynamics.ThermodynamicsInst):
                getattr(self, attr).name = getattr(self, attr).name.replace(old_name,new_name)
                for k in getattr(self, attr).varAlias.keys():
                    getattr(self, attr).varAlias[k] = getattr(self, attr).varAlias[k].replace(old_name,new_name)
                for r in range(len(getattr(self, attr).indexList)):
                    getattr(self, attr).indexList[r][1] = getattr(self, attr).indexList[r][1].replace(old_name,new_name)
        if hasattr(self, "inputStreams"):
            for s in self.inputStreams.values():
                s.name = s.name.replace(old_name,new_name)
                for k in s.dict.keys():
                    s.dict[k] = s.dict[k].replace(old_name,new_name)
        if hasattr(self, "outputStreams"):
            for s in self.outputStreams.values():
                s.name = s.name.replace(old_name,new_name)
                for k in s.dict.keys():
                    s.dict[k] = s.dict[k].replace(old_name,new_name)

class InputStream(object):
    def __init__(self,name,dict):
        self.dict = dict
        for key in self.dict.keys():
            self.dict[key] = self.dict[key].replace(" ","")
        self.name = name
        # self.type = type

class OutputStream(object):
    def __init__(self,name,dict,output_var):
        self.dict = dict
        for key in self.dict.keys():
            self.dict[key] = self.dict[key].replace(" ","")
        for i in output_var:
            if i not in dict.keys():
                raise Exception("Output variable set is not consistent.")
        self.output_var = output_var  #必定要求解的output_var
        self.output_needed = {}
        self.name = name
        # self.type = type

class Connection(object):
    var_without_comp = ['F','h','P','Q','T']
    var_with_comp = ['c','x','y','f']
    def __init__(self, name, task,sideAStream, sideBStream, sideADevice, sideBDevice):
        self.name = name
        if not isinstance(sideAStream, OutputStream):
            raise Exception('sideAStream for a connection must be an OutputStream.')
        if not isinstance(sideBStream, InputStream):
            raise Exception('sideBStream for a connection must be an InputStream.')
        self.sideAStream = sideAStream
        self.sideBStream = sideBStream
        self.sideADevice = sideADevice
        self.sideBDevice = sideBDevice
        self.task = task

    def generateInputVars(self):
        str = ""
        for key, value in self.sideBStream.output_needed.items():
            if key in Connection.var_without_comp:
                str += "#model_name#." + value + " = Var()\n"
            elif key in Connection.var_with_comp:
                str += "#model_name#." + value.split('[')[0] + " = Var(#model_name#.Component, bounds = (0,1))\n"
            else:
                raise Exception("Unknown connection stream variable %s." % key)
        str = str.replace('#model_name#', self.task.name)
        return str

    def generatePyomoConstraints(self):
        str = ""
        n_cons = 0
        str += "#--------Connections of %s and %s---------\n" % (self.sideAStream.name, self.sideBStream.name)
        if type(self.task) == Task.PyomoStaticTask:
            for key,value in self.sideBStream.output_needed.items():
                if key in Connection.var_without_comp:
                    str += "def #device_name#"+key+"Connection%d(m):\n"%n_cons
                    str += "\treturn m." +value+"-m."+self.sideAStream.dict[key]+"==0\n"
                    str += "#model_name#.#device_name#"+key+"Connection%d = Constraint(rule=#device_name#"%n_cons+key+"Connection%d)\n"%n_cons
                elif key in Connection.var_with_comp:
                    str += "def #device_name#"+key+"Connection%d(m, comp):\n"%n_cons
                    sub_str = "\treturn m." + value + "-m." + self.sideAStream.dict[key] + "==0\n"
                    str += sub_str.replace("#comp#","comp")
                    str += "#model_name#.#device_name#"+key+"Connection%d = Constraint(#model_name#.Component,rule=#device_name#"%n_cons+key+"Connection%d)\n"%n_cons
                else:
                    raise Exception("Unknown connection stream variable %s."%key)
                n_cons +=1
        elif type(self.task) == Task.PyomoDynamicTask:
            for key,value in self.sideBStream.output_needed.items():
                if key in Connection.var_without_comp:
                    str += "def #device_name#"+key+"Connection%d(m, time):\n"%n_cons
                    sub_str = "\treturn m." +value+"-m."+self.sideAStream.dict[key]+"==0\n"
                    str += sub_str.replace("#time#", "time")
                    str += "#model_name#.#device_name#"+key+"Connection%d = Constraint(#model_name#.Time, rule=#device_name#"%n_cons+key+"Connection%d)\n"%n_cons
                elif key in Connection.var_with_comp:
                    str += "def #device_name#"+key+"Connection%d(m, time, comp):\n"%n_cons
                    sub_str = "\treturn m." + value + "-m." + self.sideAStream.dict[key] + "==0\n"
                    str += sub_str.replace("#comp#","comp").replace("#time#","time")
                    str += "#model_name#.#device_name#"+key+"Connection%d = Constraint(#model_name#.Time, #model_name#.Component,rule=#device_name#"%n_cons+key+"Connection%d)\n"%n_cons
                else:
                    raise Exception("Unknown connection stream variable %s."%key)
                n_cons +=1
        str = str.replace('#model_name#', self.task.name).replace("#device_name#", self.name)
        return str