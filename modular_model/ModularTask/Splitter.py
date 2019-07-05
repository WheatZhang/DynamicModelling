#!/usr/bin/env python
#-*- coding:utf-8 -*-
import ModularTask.Device as Device
import ModularTask.Task as Task

class NaiveSplitter(Device.PyomoDevice):
    def setSpecificaitons(self, specifications):
        if not hasattr(self, 'options'):
            raise Exception("Please set options for the model first in %s." % self.name)
        if self.options['Mode'] == 'OutletARatio':
            required_specifications = [
                'OutARatio'
            ]
        elif self.options['Mode'] == 'OutAMFlow':
            required_specifications = [
                'OutAMFlow'
            ]
        self.setDeviceSpecs(required_specifications, specifications)

    def setConstraintWeight(self, weights):
        required_weights = [
            'FlowEquWeight'
        ]
        if len(weights) != len(required_weights):
            raise Exception("The numbers of constraint weights for %s in not correct." % self.name)
        for key, value in weights.items():
            if not key in required_weights:
                raise Exception("The constraint weight " + key + "is unavailable.")
        self.weights = weights

    def setModelingOption(self, options):
        # -----------------------------
        #      Set Options
        # -----------------------------
        available_options = {
            'Mode' : ['OutletARatio', 'OutAMFlow']
        }
        self.setDeviceOptions(available_options, options)
        # ---------------------------------
        #      Set Input and Output
        # ---------------------------------
        if isinstance(self.task, Task.PyomoStaticTask):
            dict = {'F': self.name + 'InMFlow',
                    'c': self.name + 'MFrac[#comp#]',
                    'P': self.name + 'Pressure',
                    'h': self.name + 'MEtlp'
                    }
        elif isinstance(self.task, Task.PyomoDynamicTask):
            dict = {'F': self.name + 'InMFlow[#time#]',
                    'c': self.name + 'MFrac[#time#, #comp#]',
                    'P': self.name + 'Pressure[#time#]',
                    'h': self.name + 'MEtlp[#time#]'
                    }
        self.inputStreams['Inlet'] = Device.InputStream(self.name + 'Inlet', dict)
        if isinstance(self.task, Task.PyomoStaticTask):
            dict = {'F': self.name + 'OutAMFlow',
                    'c': self.name + 'MFrac[#comp#]',
                    'h': self.name + 'MEtlp',
                    'P': self.name + 'Pressure'
                    }
        elif isinstance(self.task, Task.PyomoDynamicTask):
            dict = {'F': self.name + 'OutAMFlow[#time#]',
                    'c': self.name + 'MFrac[#time#, #comp#]',
                    'h': self.name + 'MEtlp[#time#]',
                    'P': self.name + 'Pressure[#time#]'
                    }
        output_var = ['c', 'F', 'h', 'P']
        self.outputStreams['OutletA'] = Device.OutputStream(self.name + 'OutletA', dict, output_var)
        if isinstance(self.task, Task.PyomoStaticTask):
            dict = {'F': self.name + 'OutBMFlow',
                    'c': self.name + 'MFrac[#comp#]',
                    'h': self.name + 'MEtlp',
                    'P': self.name + 'Pressure'
                    }
        elif isinstance(self.task, Task.PyomoDynamicTask):
            dict = {'F': self.name + 'OutBMFlow[#time#]',
                    'c': self.name + 'MFrac[#time#, #comp#]',
                    'h': self.name + 'MEtlp[#time#]',
                    'P': self.name + 'Pressure[#time#]'
                    }
        output_var = ['c', 'F', 'h', 'P']
        self.outputStreams['OutletB'] = Device.OutputStream(self.name + 'OutletB', dict, output_var)

    def generatePublicPEVar(self):
        PE_str = ""
        PE_str += "#--------%s---------\n" % self.name
        if type(self.task) == Task.PyomoPETask:
            if self.options['Mode'] == 'OutletARatio':
                PE_str += ModularTask.ModelingTools.to_pe_public_var("OutARatio",
                                                                     self.specifications["OutARatio"])
            elif self.options['Mode'] == 'OutAMFlow':
                PE_str += ModularTask.ModelingTools.to_pe_public_var("OutAMFlow",
                                                                     self.specifications["OutAMFlow"])
        else:
            raise Exception("This is not a PE task.")
        PE_str = PE_str.replace('#model_name#', self.task.name).replace("#device_name#", self.name).replace(
            "#prim_name#", self.primitive_name)
        return PE_str

    def generatePEConstraint(self):
        PE_str = ""
        PE_str += "#--------%s---------\n" % self.name
        if type(self.task) == Task.PyomoPETask:
            if self.options['Mode'] == 'OutletARatio':
                if isinstance(self.specifications['OutARatio'], ModularTask.PE.EstimatedSpec):
                    PE_str += ModularTask.ModelingTools.to_pe_constraint("OutARatio", 1e-3)
            elif self.options['Mode'] == 'OutAMFlow':
                if isinstance(self.specifications['OutAMFlow'], ModularTask.PE.EstimatedSpec):
                    PE_str += ModularTask.ModelingTools.to_pe_constraint("OutAMFlow", 1e-3)
        else:
            raise Exception("This is not a PE task.")
        PE_str = PE_str.replace('#model_name#', self.task.name).replace("#device_name#", self.name).replace(
            "#prim_name#", self.primitive_name)
        return PE_str

    def generatePyomoPara(self):
        str = ""
        str += "#--------%s---------\n" % self.name
        if self.options['Mode'] == 'OutletARatio':
            if isinstance(self.task, Task.PyomoStaticTask):
                str += ModularTask.ModelingTools.ss_or_pe_para(self.task, "OutARatio",
                                                               self.specifications['OutARatio'])
            elif isinstance(self.task, Task.PyomoDynamicTask):
                str += ModularTask.ModelingTools.gen_dynamic_para(self.task, "OutARatio",
                                                                  self.specifications['OutARatio'])
        elif self.options['Mode'] == 'OutAMFlow':
            if isinstance(self.task, Task.PyomoStaticTask):
                str += ModularTask.ModelingTools.ss_or_pe_para(self.task, "OutAMFlow",
                                                               self.specifications['OutAMFlow'])
            elif isinstance(self.task, Task.PyomoDynamicTask):
                str += ModularTask.ModelingTools.gen_dynamic_para(self.task, "OutAMFlow",
                                                                  self.specifications['OutAMFlow'])
        str = str.replace('#model_name#', self.task.name).replace("#device_name#", self.name)
        return str

    def generatePyomoVar(self):
        str = ""
        str += "#--------%s---------\n" % self.name
        if self.options['Mode'] == 'OutletARatio':
            if isinstance(self.task, Task.PyomoStaticTask):
                str += "#model_name#.#device_name#OutAMFlow = Var(within=NonNegativeReals)\n"
            elif isinstance(self.task, Task.PyomoDynamicTask):
                str += "#model_name#.#device_name#OutAMFlow = Var(#model_name#.Time, within=NonNegativeReals)\n"
        if isinstance(self.task, Task.PyomoStaticTask):
            str += "#model_name#.#device_name#OutBMFlow = Var(within=NonNegativeReals)\n"
        elif isinstance(self.task, Task.PyomoDynamicTask):
            str += "#model_name#.#device_name#OutBMFlow = Var(#model_name#.Time, within=NonNegativeReals)\n"
        str = str.replace('#model_name#', self.task.name).replace("#device_name#", self.name)
        return str

    def generatePyomoCon(self):
        str = ""
        str += "#--------%s Mass Balance---------\n" % self.name
        str += self.generateMassBalance()
        return str

    def generateMassBalance(self):
        str = ""
        if self.options['Mode'] == 'OutletARatio':
            if isinstance(self.task, Task.PyomoStaticTask):
                str += "def #device_name#OutASpec(m):\n"
                str += "\treturn (m.#device_name#OutAMFlow-m.#device_name#InMFlow*m.#device_name#OutARatio)*%f==0\n" % \
                       self.weights['FlowEquWeight']
                str += "#model_name#.#device_name#OutASpec = Constraint(rule=#device_name#OutASpec)\n"
                str += "def #device_name#OutBSpec(m):\n"
                str += "\treturn (m.#device_name#OutBMFlow-m.#device_name#InMFlow*(1-m.#device_name#OutARatio))*%f==0\n" % \
                       self.weights['FlowEquWeight']
                str += "#model_name#.#device_name#OutBSpec = Constraint(rule=#device_name#OutBSpec)\n"
            elif isinstance(self.task, Task.PyomoDynamicTask):
                str += "def #device_name#OutASpec(m,time):\n"
                str += "\treturn (m.#device_name#OutAMFlow[time]-m.#device_name#InMFlow[time]*m.#device_name#OutARatio[time])*%f==0\n"%self.weights['FlowEquWeight']
                str += "#model_name#.#device_name#OutASpec = Constraint(#model_name#.Time, rule=#device_name#OutASpec)\n"
                str += "def #device_name#OutBSpec(m,time):\n"
                str += "\treturn (m.#device_name#OutBMFlow[time]-m.#device_name#InMFlow[time]*(1-m.#device_name#OutARatio[time]))*%f==0\n"%self.weights['FlowEquWeight']
                str += "#model_name#.#device_name#OutBSpec = Constraint(#model_name#.Time, rule=#device_name#OutBSpec)\n"
        elif self.options['Mode'] == 'OutAMFlow':
            if isinstance(self.task, Task.PyomoStaticTask):
                str += "def #device_name#OutBSpec(m):\n"
                str += "\treturn (m.#device_name#OutBMFlow+m.#device_name#OutAMFlow-m.#device_name#InMFlow)*%f==0\n" % \
                       self.weights['FlowEquWeight']
                str += "#model_name#.#device_name#OutBSpec = Constraint(rule=#device_name#OutBSpec)\n"
            elif isinstance(self.task, Task.PyomoDynamicTask):
                str += "def #device_name#OutBSpec(m,time):\n"
                str += "\treturn (m.#device_name#OutBMFlow[time]+m.#device_name#OutAMFlow[time]-m.#device_name#InMFlow[time])*%f==0\n"%self.weights['FlowEquWeight']
                str += "#model_name#.#device_name#OutBSpec = Constraint(#model_name#.Time, rule=#device_name#OutBSpec)\n"
        str = str.replace('#model_name#', self.task.name).replace("#device_name#", self.name)
        return str