#!/usr/bin/env python
#-*- coding:utf-8 -*-
import ModularTask.ColumnBody
import ModularTask.ColumnSump
import ModularTask.Stream
import ModularTask.Device
import ModularTask.Condensor
import ModularTask.Reboiler
import ModularTask.Splitter
from pyomo.environ import *
import re
from scipy.interpolate  import lagrange

class PyomoTask(object):
    def __init__(self, name,component,units):
        self.name = name #模型名称
        self.component = component
        self.units = units #物理变量的单位
        self.symbols = []
        self.devices = {}
        self.connections = []
        self.processParts = []

    def addDevice(self,deviceType, name):
        if name in self.symbols:
            raise Exception("This name has been used."+ name)
        else:
            self.symbols.append(name)
        if deviceType == 'ColumnBody':
            self.devices[name] = ModularTask.ColumnBody.GeneralColumnBody(self, name)
        elif deviceType == 'ColumnSump':
            self.devices[name] = ModularTask.ColumnSump.GeneralColumnSump(self, name)
        elif deviceType == 'TwoPhaseStream':
            self.devices[name] = ModularTask.Stream.TwoPhaseStream(self, name)
        elif deviceType == 'LiquidStream':
            self.devices[name] = ModularTask.Stream.LiquidPhaseStream(self, name)
        elif deviceType == 'VaporStream':
            self.devices[name] = ModularTask.Stream.VaporPhaseStream(self, name)
        elif deviceType == 'HeatStream':
            self.devices[name] = ModularTask.Stream.GeneralHeatStream(self, name)
        elif deviceType == 'NaiveTotalCondensor':
            self.devices[name] = ModularTask.Condensor.NaiveTotalCondensor(self, name)
        elif deviceType == 'NaiveReboiler':
            self.devices[name] = ModularTask.Reboiler.NaiveReboiler(self, name)
        elif deviceType == 'NaiveSplitter':
            self.devices[name] = ModularTask.Splitter.NaiveSplitter(self, name)
        else:
            raise Exception("Unknown device type.")

    def loadNominalRange(self, file_name):
        for device in self.devices.values():
            device.static_init = {}
        names = list(self.devices.keys())
        names.sort(key=lambda x: -len(x))
        status = "Ready"
        file = open(file_name)
        for line in file:
            line_split = line.split('\t')
            # print(line_split)
            for i in range(len(line_split)):
                line_split[i] = line_split[i].strip()
            if status == "Ready":
                if len(line_split) == 0:
                    continue
                elif len(line_split) == 1:
                    if line_split[0] == "":
                        continue
                    else:
                        status = "IndexedVarStart"
                        var_name = line_split[0]
                        dict = {}
                        continue
                elif len(line_split) == 2:
                    if line_split[0] == "":
                        continue
                    elif line_split[1] == "":
                        status = "IndexedVarStart"
                        var_name = line_split[0]
                        dict = {}
                        continue
                    else:
                        self.setNominalRange(line_split[0], eval(line_split[1]),names)
                        continue
                else:
                    raise Exception("Wrong template format.")
            elif status == 'IndexedVarStart':
                if len(line_split) == 0:
                    self.setNominalRange(var_name, dict,names)
                    status = "Ready"
                    continue
                elif len(line_split) == 1:
                    if line_split[0] == "":
                        self.setNominalRange(var_name, dict,names)
                        status = "Ready"
                        continue
                    else:
                        self.setNominalRange(var_name, dict, names)
                        status = "IndexedVarStart"
                        var_name = line_split[0]
                        continue
                elif len(line_split) == 2:
                    if line_split[0] == "":
                        self.setNominalRange(var_name, dict, names)
                        status = "Ready"
                        continue
                    else:
                        str = line_split[0]
                        if str[0] == "\"":
                            str = str[1:-1]
                        if str[0] == '(':
                            dict[eval(str)] = eval(line_split[1])
                        else:
                            if str.isdigit():
                                dict[int(str)] = eval(line_split[1])
                            elif re.match(r'[a-zA-Z]', str) == None:
                                if type(eval(str)) == float:
                                    dict[float(str)] = eval(line_split[1])
                                else:
                                    raise Exception("Wrong index format.")
                            else:
                                dict[str] = eval(line_split[1])
                else:
                    raise Exception("Wrong template format.")
        file.close()

    def setNominalRange(self, name, value,names):
        flag = 0
        for i in names:
            if re.match(i,name) == None:
                continue
            else:
                if not hasattr(self.devices[i],'nominal_range'):
                    self.devices[i].nominal_range = {}
                self.devices[i].nominal_range[name] = value
                flag = 1
                break
        if flag == 0:
            raise Exception('There is no device name which matches the name %s.'%name)

    def addConnections(self, connectionList):
        for i,item in enumerate(connectionList):
            if len(item)!= 4:
                raise Exception("A connection must be given 4 parameters.")
            self.connections.append(ModularTask.Device.Connection("Cnct%d"%i, self, self.devices[item[0]].outputStreams[item[1]], \
                                self.devices[item[2]].inputStreams[item[3]], item[0], item[2]))

    def AdjustOutputName(self):
        output_input_same = []
        for name, device in self.devices.items():
            for output in device.outputStreams.values():
                for output_var_symbol, output_var in output.output_needed.items():
                    for input in device.inputStreams.values():
                        if output_var in input.dict.values():
                            input_var_symbol = list(input.dict.keys())[list(input.dict.values()).index(output_var)]
                            output_input_same.append([input, input_var_symbol, output, output_var_symbol, None])
        for i in output_input_same:
            # print([i[0].name, i[1], i[2].name, i[3]])
            for j in self.connections:
                if i[0] == j.sideBStream:
                    i[0] = j.sideAStream
                    break
        # print("--------------")
        # for i in output_input_same:
        #     print([i[0].name, i[1], i[2].name, i[3]])
        # print("--------------")
        while len(output_input_same) != 0:
            for i in output_input_same:
                for j in output_input_same:
                    if i[0] == j[2]:
                        i[4] = False  # 非源头变量
                        break
                    i[4] = True
            for i in output_input_same:
                if i[4] == True:
                    i[2].output_needed[i[3]] = i[0].output_needed[i[1]]
            i = 0
            while i < len(output_input_same):
                if output_input_same[i][4] == True:
                    # print([output_input_same[i][0].name,output_input_same[i][1],output_input_same[i][2].name,output_input_same[i][3]])
                    output_input_same.pop(i)
                    i -= 1
                i += 1

    def setNeedOutputVar(self):
        for name, device in self.devices.items():
            for output in device.outputStreams.values():
                for out_var in output.output_var:
                    output.output_needed[out_var] = output.dict[out_var]
        for name, device in self.devices.items():
            for input in device.inputStreams.values():
                for conn in self.connections:
                    if conn.sideBStream == input:
                        for in_var in input.dict.keys():
                            if in_var not in conn.sideAStream.output_needed.keys():
                                conn.sideAStream.output_needed[in_var] = conn.sideAStream.dict[in_var]

class PyomoStaticTask(PyomoTask):
    def setModelingOption(self, options):
        available_options = {
            'ConnectionMode': ['IsolatedMode', 'CombinedMode']
        }
        for key, value in options.items():
            if type(available_options[key]) == 'list':
                if value not in available_options[key]:
                    raise Exception("The option value for " + key + "is not unavailable.")
            elif type(available_options[key]) == 'string':
                if not isinstance(value, available_options[key]):
                    raise Exception("The option value for " + key + "is type incorrect.")
        self.options = options

    def addConnections(self, connectionList):
        for i,item in enumerate(connectionList):
            if len(item)!= 4:
                raise Exception("A connection must be given 4 parameters.")
            self.connections.append(ModularTask.Device.Connection("Cnct%d"%i, self, self.devices[item[0]].outputStreams[item[1]], \
                                self.devices[item[2]].inputStreams[item[3]], item[0], item[2]))

    def generatePyomoModel(self, filename):
        self.setNeedOutputVar()
        if self.options['ConnectionMode'] == 'CombinedMode':
            self.AdjustOutputName() #为了避免input, output重名
        f = open(filename, 'w')
        f.write("from pyomo.environ import *\n\n")
        f.write(self.name+" = ConcreteModel()\n")
        f.write(self.name+".Component = Set(initialize="+str(self.component)+")\n")
        title = '''
#===================================
#
#      Process Parts
#
#===================================
'''
        f.write(title)
        for processPart in self.processParts:
            f.write(processPart.generatePyomoModel())
        #写入集合、参数、变量、表达式、约束的定义
        self.write_SPVEC_to_file(f)
        f.close()

    def write_SPVEC_to_file(self,f):
        title = '''
#===================================
#
#      Parameters & Sets
#
#===================================
'''
        f.write(title)
        for device in self.devices.values():
            f.write(device.generatePyomoPara())
        title = '''
#===================================
#
#         Variables
#
#===================================
'''
        f.write(title)
        for device in self.devices.values():
            f.write(device.generatePyomoVar())
        if self.options['ConnectionMode'] == 'IsolatedMode':
            title = '''
#----------------------------------
#        Connection Var
#----------------------------------
'''
            f.write(title)
            for con in self.connections:
                f.write(con.generateInputVars())
        title = '''
#===================================
#
#         Expressions
#
#===================================
'''
        f.write(title)
        if self.options['ConnectionMode'] == 'IsolatedMode':
            for device in self.devices.values():
                f.write(device.generatePyomoExpression())
        elif self.options['ConnectionMode'] == 'CombinedMode':
            for name, device in self.devices.items():
                this_str = device.generatePyomoExpression()
                for con in self.connections:
                    if con.sideBDevice == name:
                        this_str = substitute_input_symbol(this_str, con)
                f.write(this_str)
        title = '''
#===================================
#
#         Constraints
#
#===================================
'''
        f.write(title)
        if self.options['ConnectionMode'] == 'IsolatedMode':
            for device in self.devices.values():
                title = '''
#----------------------------------
#           %s
#----------------------------------
''' % device.name
                f.write(title)
                f.write(device.generatePyomoCon())
        elif self.options['ConnectionMode'] == 'CombinedMode':
            for name, device in self.devices.items():
                title = '''
#----------------------------------
#           %s
#----------------------------------
''' % device.name
                f.write(title)
                this_str = device.generatePyomoCon()
                for con in self.connections:
                    if con.sideBDevice == name:
                        this_str = substitute_input_symbol(this_str, con)
                f.write(this_str)
        if self.options['ConnectionMode'] == 'IsolatedMode':
            title = '''
#===================================
#
#         Connections
#
#===================================
'''
            f.write(title)
            for con in self.connections:
                f.write(con.generatePyomoConstraints())

class PyomoDynamicTask(PyomoTask):
    def setSimulationTime(self, timespan, nfe, fe_point_specified = None, ncp = 3):
        self.timespan = timespan
        self.nfe = nfe
        self.ncp = ncp
        self.fe_point_specified = fe_point_specified
        Discretizer = ModularTask.RuntimeTools.TimeDiscretizer(nfe=nfe, ncp=ncp, bounds=self.timespan)
        Discretizer.set_fe_point(self.fe_point_specified)
        self.time_list = Discretizer.get_para_time()

    def write_dynamic_report(self,file_name, model, vars, time=None):
        f = open(file_name, "w")
        report_str = ""
        report_str = "Time"
        for var in vars:
            report_str += '\t' + var
        report_str += "\n"
        f.write(report_str)
        if time == None:
            for t in self.time_list:
                report_str = ""
                report_str += str(t)
                for var in vars:
                    report_str += '\t'+str(value(eval("model."+var.replace("*",str(t)))))
                report_str +="\n"
                f.write(report_str)
        elif isinstance(time, list):
            for t in time:
                report_str = ""
                report_str += str(t)
                for var in vars:
                    report_str += '\t' + str(self.get_var_at_t(model, var, t))
                report_str += "\n"
                f.write(report_str)
        f.close()

    def get_var_at_t(self, model, var, time):
        self.time_list.sort()
        fes = model.Time._fe
        if time <= self.time_list[0]:
            return value(eval("model."+var.replace("*",str(self.time_list[0]))))
        elif time >= self.time_list[-1]:
            return value(eval("model."+var.replace("*",str(self.time_list[-1]))))
        else:
            for index, i in enumerate(fes):
                if i >= time:
                    fe_b = i
                    fe_a = fes[index-1]
                    break
            x = []
            y = []
            for i in self.time_list:
                if i>=fe_a and i <= fe_b:
                    x.append(i)
            if len(x) != self.ncp+1:
                raise Exception("The number of allocation point found is not consistent with ncp.")
            for i in x:
                y.append(value(eval("model."+var.replace("*",str(i)))))
            return lagrange(x, y)(time)

    def setModelingOption(self, options):
        available_options = {
            'ConnectionMode': ['IsolatedMode', 'CombinedMode']
        }
        for key, value in options.items():
            if type(available_options[key]) == 'list':
                if value not in available_options[key]:
                    raise Exception("The option value for " + key + "is not unavailable.")
            elif type(available_options[key]) == 'string':
                if not isinstance(value, available_options[key]):
                    raise Exception("The option value for " + key + "is type incorrect.")
        self.options = options

    def generateNaiveInitTxt(self, filename):
        f = open(filename, "w")
        for device in self.devices.values():
            for key, value in device.static_init.items():
                if type(value) == dict:
                    f.write(key + '\n')
                    for k, v in value.items():
                        f.write(str(k) + '\t')
                        f.write(str(v) + '\n')
                    f.write('\n')
                else:
                    f.write(key + '\t')
                    f.write(str(value))
                    f.write('\n\n')
        f.close()

    def generatePyomoModel(self, filename):
        self.setNeedOutputVar()
        if self.options['ConnectionMode'] == 'CombinedMode':
            self.AdjustOutputName() #为了避免input, output重名
        f = open(filename, 'w')
        f.write("from pyomo.environ import *\nfrom pyomo.dae import *\nimport ModularTask\n\n")
        f.write(self.name+" = ConcreteModel()\n")
        f.write(self.name+".Component = Set(initialize="+str(self.component)+")\n")
        title = '''
#===================================
#
#      Modelling Time
#
#===================================
'''
        f.write(title)
        string = ""
        string += "Discretizer = ModularTask.RuntimeTools.TimeDiscretizer(nfe=%d, ncp=%d, bounds="%(self.nfe,self.ncp)+str(self.timespan)+")\n"
        string += "Discretizer.set_fe_point("+str(self.fe_point_specified)+")\n"
        string += "Discretizer.initialize_time("+self.name+", 'Time')\n"
        string += "pe_list = Discretizer.get_para_time()\n"
        string += self.name+".ParaTime = Set(initialize=pe_list)\n"
        f.write(string)
        title = '''
#===================================
#
#      Process Parts
#
#===================================
'''
        f.write(title)
        for processPart in self.processParts:
            f.write(processPart.generatePyomoModel())
        title = '''
#===================================
#
#      Parameters & Sets
#
#===================================
'''
        f.write(title)
        for device in self.devices.values():
            f.write(device.generatePyomoPara())
        title = '''
#===================================
#
#         Variables
#
#===================================
'''
        f.write(title)
        for device in self.devices.values():
            f.write(device.generatePyomoVar())
        if self.options['ConnectionMode'] == 'IsolatedMode':
            title = '''
#----------------------------------
#        Connection Var
#----------------------------------
'''
            f.write(title)
            for con in self.connections:
                f.write(con.generateInputVars())
        title = '''
#===================================
#
#         Expressions
#
#===================================
'''
        f.write(title)
        if self.options['ConnectionMode'] == 'IsolatedMode':
            for device in self.devices.values():
                f.write(device.generatePyomoExpression())
        elif self.options['ConnectionMode'] == 'CombinedMode':
            for name, device in self.devices.items():
                this_str = device.generatePyomoExpression()
                for con in self.connections:
                    if con.sideBDevice == name:
                        this_str = substitute_input_symbol(this_str, con)
                f.write(this_str)
        title = '''
#===================================
#
#         Constraints
#
#===================================
'''
        f.write(title)
        if self.options['ConnectionMode'] == 'IsolatedMode':
            for device in self.devices.values():
                title = '''
#----------------------------------
#           %s
#----------------------------------
''' % device.name
                f.write(title)
                f.write(device.generatePyomoCon())
        elif self.options['ConnectionMode'] == 'CombinedMode':
            for name, device in self.devices.items():
                title = '''
#----------------------------------
#           %s
#----------------------------------
''' % device.name
                f.write(title)
                this_str = device.generatePyomoCon()
                for con in self.connections:
                    if con.sideBDevice == name:
                        this_str = substitute_input_symbol(this_str, con)
                f.write(this_str)
        if self.options['ConnectionMode'] == 'IsolatedMode':
            title = '''
#===================================
#
#         Connections
#
#===================================
'''
            f.write(title)
            for con in self.connections:
                f.write(con.generatePyomoConstraints())
        title = '''
#===================================
#
#         Discretize
#
#===================================
'''
        f.write(title)
        f.write("Discretizer.discretilize(%s)\n"%self.name)

        self.generateNaiveInitTxt(self.name+"NaiveInit.txt")
        title = '''
#===================================
#
#     Variable Initialization
#
#===================================
'''
        f.write(title)
        f.write("ModularTask.InitValueTools.load_naive_var_init(%s,\"%s\")\t"%(self.name, self.name+"NaiveInit.txt"))
        f.close()

    def loadStaticInitValue(self, file_name):
        for device in self.devices.values():
            device.static_init = {}
        names = list(self.devices.keys())
        names.sort(key=lambda x: -len(x))
        status = "Ready"
        file = open(file_name)
        for line in file:
            line_split = line.split('\t')
            # print(line_split)
            for i in range(len(line_split)):
                line_split[i] = line_split[i].strip()
            if status == "Ready":
                if len(line_split) == 0:
                    continue
                elif len(line_split) == 1:
                    if line_split[0] == "":
                        continue
                    else:
                        status = "IndexedVarStart"
                        var_name = line_split[0]
                        dict = {}
                        continue
                elif len(line_split) == 2:
                    if line_split[0] == "":
                        continue
                    elif line_split[1] == "":
                        status = "IndexedVarStart"
                        var_name = line_split[0]
                        dict = {}
                        continue
                    else:
                        self.setStaticInitValue(line_split[0], float(line_split[1]),names)
                        continue
                else:
                    raise Exception("Wrong template format.")
            elif status == 'IndexedVarStart':
                if len(line_split) == 0:
                    self.setStaticInitValue(var_name, dict,names)
                    status = "Ready"
                    continue
                elif len(line_split) == 1:
                    if line_split[0] == "":
                        self.setStaticInitValue(var_name, dict,names)
                        status = "Ready"
                        continue
                    else:
                        self.setStaticInitValue(var_name, dict, names)
                        status = "IndexedVarStart"
                        var_name = line_split[0]
                        continue
                elif len(line_split) == 2:
                    if line_split[0] == "":
                        self.setStaticInitValue(var_name, dict, names)
                        status = "Ready"
                        continue
                    else:
                        str = line_split[0]
                        if str[0] == "\"":
                            str = str[1:-1]
                        if str[0] == '(':
                            dict[eval(str)] = float(line_split[1])
                        else:
                            if str.isdigit():
                                dict[int(str)] = float(line_split[1])
                            elif re.match(r'[a-zA-Z]', str) == None:
                                if type(eval(str)) == float:
                                    dict[float(str)] = float(line_split[1])
                                else:
                                    raise Exception("Wrong index format.")
                            else:
                                dict[str] = float(line_split[1])
                else:
                    raise Exception("Wrong template format.")
        file.close()

    def setStaticInitValue(self, name, value,names):
        flag = 0
        for i in names:
            if re.match(i,name) == None:
                continue
            else:
                self.devices[i].static_init[name] = value
                flag = 1
                break
        if flag == 0:
            raise Exception('There is no device name which matches the name %s.'%name)

    def getNaiveDynamicInitValue(self):
        for device in self.devices.values():
            device.getNaiveDynamicInitValue()

def substitute_input_symbol(str, con):
    def replaceForVar(str_replacing):
        def replace_fun(m):
            if '#comp#' in str_replacing:
                if '#time#' in str_replacing:
                    return str_replacing.replace('#time#',m.group(1)).replace('#comp#',m.group(2))
                else:
                    return str_replacing.replace('#comp#', m.group(1))
            else:
                if '#time#' in str_replacing:
                    return str_replacing.replace('#time#',m.group(1))
                else:
                    return str_replacing
        return replace_fun
    for key,value in con.sideBStream.dict.items():
        if not key in ModularTask.Device.Connection.var_with_comp:
            if not key in ModularTask.Device.Connection.var_without_comp:
                raise Exception("Unknown connection stream variable %s." % key)
        expr = re.sub(r'[\[\]\(\)\.\,]', r'\\\g<0>', value).replace("#time#", "(.*?)").replace("#comp#","(.*?)")
        str = re.sub(expr, replaceForVar(con.sideAStream.output_needed[key]), str)
    return str

class PyomoPETask(PyomoStaticTask):
    def __init__(self, name,component,units, number_of_case):
        super().__init__(name,component,units)
        self.PE_setting_files = []
        self.PE_init_file = []
        self.number_of_case = number_of_case

    def add_case(self, setting, init):
        self.PE_setting_files.append(setting)
        self.PE_init_file.append(init)

    def setModelingOption(self, options):
        available_options = {
            'ConnectionMode': ['IsolatedMode', 'CombinedMode']
        }
        for key, value in options.items():
            if type(available_options[key]) == 'list':
                if value not in available_options[key]:
                    raise Exception("The option value for " + key + "is not unavailable.")
            elif type(available_options[key]) == 'string':
                if not isinstance(value, available_options[key]):
                    raise Exception("The option value for " + key + "is type incorrect.")
        self.options = options

    def generateNonObjModel(self, filename):
        f = open(filename, 'w')
        f.write("from pyomo.environ import *\n\n")
        f.write(self.name + " = ConcreteModel()\n")
        f.write(self.name + ".Component = Set(initialize=" + str(self.component) + ")\n")
        title = '''
#===================================
#
#      Process Parts
#
#===================================
'''
        f.write(title)
        for processPart in self.processParts:
            f.write(processPart.generatePyomoModel())
        # 产生Case Depend 的参数
        title = '''
#===================================
#
#       Case Depend Paras
#
#===================================
'''
        f.write(title)
        for i in range(self.number_of_case):
            for device in self.devices.values():
                for spec,value in device.specifications.items():
                    if type(value) == ModularTask.PE.CaseDependSpec:
                        para_name = device.primitive_name + "PE%d"%i+spec
                        f.write(self.name+"."+para_name+" = Param(initialize = 0)\n")
        # 写入集合、参数、变量、表达式、约束的定义
        for i in range(self.number_of_case):
            title = '''
#===========================================
#===========================================
#===                                     ===
#===        PE MODEL SECTION %2d          ===
#===                                     ===
#===========================================
#===========================================
'''%i
            f.write(title)
            for device in self.devices.values():
                device.rename(device.name, device.primitive_name+"PE%d"%i)
            self.setNeedOutputVar()
            if self.options['ConnectionMode'] == 'CombinedMode':
                self.AdjustOutputName()  # 为了避免input, output重名
            self.write_SPVEC_to_file(f)
        if self.number_of_case > 1:
            title = '''
#===================================
#
#       Parameter Estimation
#
#===================================
'''
            f.write(title)
            for device in self.devices.values():
                f.write(device.generatePublicPEVar())
            for i in range(self.number_of_case):
                for device in self.devices.values():
                    device.rename(device.name, device.primitive_name + "PE%d" % i)
                    f.write(device.generatePEConstraint())
        f.close()

    def generateCompleteModel(self, filename):
        f = open(filename, 'w')
        # 读取设置文件
        if len(self.PE_setting_files)!=self.number_of_case:
            raise Exception("The number of setting files is not equal to the number of cases.")
        if len(self.PE_init_file)!=self.number_of_case:
            raise Exception("The number of init value files is not equal to the number of cases.")
        self.case_depend_params = {}
        self.obj_included_vars = {}
        for s in self.PE_setting_files:
            ModularTask.PE.load_PE_setting(self, s)
        # 生成模型
        f.write("from pyomo.environ import *\n\n")
        f.write(self.name + " = ConcreteModel()\n")
        f.write(self.name + ".Component = Set(initialize=" + str(self.component) + ")\n")
        title = '''
#===================================
#
#      Process Parts
#
#===================================
'''
        f.write(title)
        for processPart in self.processParts:
            f.write(processPart.generatePyomoModel())
        # 产生Case Depend 的参数
        title = '''
#===================================
#
#       Case Depend Paras
#
#===================================
'''
        f.write(title)
        for i in range(self.number_of_case):
            for device in self.devices.values():
                for spec, value in device.specifications.items():
                    if type(value) == ModularTask.PE.CaseDependSpec:
                        para_name = device.primitive_name + "PE%d" % i + spec
                        f.write(self.name + "." + para_name + " = Param(initialize = %f)\n"%self.case_depend_params[para_name])
        # 写入集合、参数、变量、表达式、约束的定义
        for i in range(self.number_of_case):
            title = '''
#===========================================
#===========================================
#===                                     ===
#===        PE MODEL SECTION %2d          ===
#===                                     ===
#===========================================
#===========================================
''' % i
            f.write(title)
            for device in self.devices.values():
                device.rename(device.name, device.primitive_name + "PE%d" % i)
            self.setNeedOutputVar()
            if self.options['ConnectionMode'] == 'CombinedMode':
                self.AdjustOutputName()  # 为了避免input, output重名
            self.write_SPVEC_to_file(f)
        if self.number_of_case > 1:
            title = '''
#===================================
#
#       Parameter Estimation
#
#===================================
'''
            f.write(title)
            for device in self.devices.values():
                f.write(device.generatePublicPEVar())
            for i in range(self.number_of_case):
                for device in self.devices.values():
                    device.rename(device.name, device.primitive_name + "PE%d" % i)
                    f.write(device.generatePEConstraint())
        obj_str = "def OBJ_func(m):\n"
        first_flag = True
        for k,v in self.obj_included_vars.items():
            if first_flag:
                obj_str += "\treturn (m."+k+" - "+str(v[0])+")**2*"+str(v[1])
                first_flag = False
            else:
                obj_str += "\\\n\t     + (m." + k + " - " + str(v[0]) + ")**2*" + str(v[1])
        obj_str += "\n"
        obj_str += self.name + ".OBJ = Objective(rule = OBJ_func)"
        f.write(obj_str)
        f.close()
