#!/usr/bin/env python
#-*- coding:utf-8 -*-
from pyomo.environ import *
from pyomo.dae import *
import re
import ModularTask

class CaseDependSpec(object):
    def __init__(self, params = {}):
        self.params = params

class EstimatedSpec(object):
    def __init__(self, params = {}):
        self.params = params

    def get_init(self):
        if 'init' in self.params.keys():
            return self.params['init']
        else:
            return None

    def generate_domain_str(self):
        domain_str = ""
        if 'within' in self.params.keys():
            if self.params['within'] == 'Nonnegative':
                domain_str += ", within=NonNegativeReals"
            elif self.params['within'] == 'Negative':
                domain_str += ", within=NegativeReals"
            if type(self.params['within']) == list or type(self.params['within']) == tuple:
                domain_str += ", bounds = ("+str(self.params['within'][0])+","+str(self.params['within'][1])+")"
        return domain_str

def to_setting_template(model, task, file_name):
    all_attr = dir(model)
    if task.number_of_case == 1:
        f = open(file_name, "w")
        f.write("#------------------------#\n# Case Depend Parameters #\n#------------------------#\n@para\n\n")
        cd_specifications = []
        for device in task.devices.values():
            for spec, value in device.specifications.items():
                if type(value) == CaseDependSpec:
                    cd_specifications.append(device.primitive_name + spec)
        for name in cd_specifications:
            f.write(name + "\tNone\n\n")
        f.write("#------------------------#\n#      PE Used Data      #\n#------------------------#\n@data\n\n")
        for attr in all_attr:
            if attr in cd_specifications:
                continue
            if isinstance(getattr(model, attr), pyomo.core.base.var.SimpleVar):
                f.write(attr + '\t')
                f.write(str(getattr(model, attr)._value))
                f.write('\t1')
                f.write('\n\n')
            elif isinstance(getattr(model, attr), pyomo.core.base.var.IndexedVar):
                f.write(attr + '\n')
                for key, value in getattr(model, attr)._data.items():
                    f.write(str(key) + '\t')
                    f.write(str(value._value) + '\t1\n')
                f.write('\n')
        f.close()
    else:
        fs = []
        for i in range(task.number_of_case):
            fs.append(open(re.match(r"(.+)\.",file_name).group(1)+str(i)+".txt", "w"))
        for i in range(task.number_of_case):
            fs[i].write("#------------------------#\n# Case Depend Parameters #\n#------------------------#\n@para\n\n")
        cd_specifications = []
        for device in task.devices.values():
            for spec, value in device.specifications.items():
                if type(value) == CaseDependSpec:
                    cd_specifications.append(device.primitive_name + "PE%d" + spec)
        for i in range(task.number_of_case):
            for name in cd_specifications:
                fs[i].write(name%i+"\tNone\n\n")
        for i in range(task.number_of_case):
            fs[i].write("#------------------------#\n#      PE Used Data      #\n#------------------------#\n@data\n\n")
        for attr in all_attr:
            if isinstance(getattr(model, attr), pyomo.core.base.var.SimpleVar) or isinstance(getattr(model, attr),
                                                                                             pyomo.core.base.var.IndexedVar):
                belong_to_case_no = None
                flag = False
                for device in task.devices.values():
                    for c_no in range(task.number_of_case):
                        if attr.startswith(device.primitive_name + "PE%d" % c_no):
                            flag = True
                            belong_to_case_no = c_no
                            break
                    if flag:
                        break
                if flag == False:
                    continue
                cd_para_flag = False
                for spec in cd_specifications:
                    if attr == spec % belong_to_case_no:
                        cd_para_flag = True
                        break
                if cd_para_flag:
                    continue
                if isinstance(getattr(model, attr), pyomo.core.base.var.SimpleVar):
                    fs[belong_to_case_no].write(attr + '\t')
                    fs[belong_to_case_no].write(str(getattr(model, attr)._value))
                    fs[belong_to_case_no].write('\t1\n\n')
                elif isinstance(getattr(model, attr), pyomo.core.base.var.IndexedVar):
                    fs[belong_to_case_no].write(attr + '\n')
                    for key, value in getattr(model, attr)._data.items():
                        fs[belong_to_case_no].write(str(key) + '\t')
                        fs[belong_to_case_no].write(str(value._value) + '\t1\n')
                    fs[belong_to_case_no].write('\n')
        for f in fs:
            f.close()

def to_init_template(model, task, file_name):
    all_attr = dir(model)
    if task.number_of_case == 1:
        f = open(file_name, "w")
        for attr in all_attr:
            if isinstance(getattr(model, attr), pyomo.core.base.var.SimpleVar):
                f.write(attr + '\t')
                f.write(str(getattr(model, attr)._value))
                f.write('\n\n')
            elif isinstance(getattr(model, attr), pyomo.core.base.var.IndexedVar):
                f.write(attr + '\n')
                for key, value in getattr(model, attr)._data.items():
                    f.write(str(key) + '\t')
                    f.write(str(value._value) + '\n')
                f.write('\n')
        f.close()
    else:
        fs = []
        for i in range(task.number_of_case):
            fs.append(open(re.match(r"(.+)\.",file_name).group(1)+str(i)+".txt", "w")) #file_name+str(i)
        for attr in all_attr:
            if isinstance(getattr(model, attr), pyomo.core.base.var.SimpleVar) or isinstance(getattr(model, attr), pyomo.core.base.var.IndexedVar):
                belong_to_case_no = None
                flag = False
                for device in task.devices.values():
                    for c_no in range(task.number_of_case):
                        if attr.startswith(device.primitive_name+"PE%d"%c_no):
                            flag = True
                            belong_to_case_no = c_no
                            break
                    if flag:
                        break
                if flag == False:
                    continue
                if isinstance(getattr(model, attr), pyomo.core.base.var.SimpleVar):
                    fs[belong_to_case_no].write(attr + '\t')
                    fs[belong_to_case_no].write(str(getattr(model, attr)._value))
                    fs[belong_to_case_no].write('\n\n')
                elif isinstance(getattr(model, attr), pyomo.core.base.var.IndexedVar):
                    fs[belong_to_case_no].write(attr + '\n')
                    for key, value in getattr(model, attr)._data.items():
                        fs[belong_to_case_no].write(str(key) + '\t')
                        fs[belong_to_case_no].write(str(value._value) + '\n')
                    fs[belong_to_case_no].write('\n')
        for f in fs:
            f.close()

def load_PE_setting(task, file_name):
    status = "None"
    file = open(file_name)
    for line in file:
        line_split = line.split('\t')
        # print(line_split)
        for i in range(len(line_split)):
            line_split[i] = line_split[i].strip()
        if len(line_split) >=1 and line_split[0].startswith("#"):
            continue
        if status == 'None':
            if len(line_split) >= 1 and line_split[0] == '@para':
                status = "WaitPara"
                continue
        elif status == 'WaitPara':
            if len(line_split) == 0:
                continue
            elif len(line_split) >= 1 and line_split[0] == '@data':
                status = "WaitData"
                continue
            elif len(line_split) >= 2:
                if line_split[0] == "":
                    continue
                task.case_depend_params[line_split[0]] = float(line_split[1])
            else:
                raise Exception("Wrong template format.")
        elif status == "WaitData":
            if len(line_split) == 0:
                continue
            elif len(line_split) == 1 or len(line_split) == 2:
                if line_split[0] == "":
                    continue
                else:
                    status = "IndexedVarStart"
                    var_name = line_split[0]
                    dict = {}
                    continue
            elif len(line_split) == 3:
                if line_split[0] == "":
                    continue
                elif line_split[1] == "":
                    status = "IndexedVarStart"
                    var_name = line_split[0]
                    dict = {}
                    continue
                else:
                    # 简单变量
                    set_up_one_data(task, line_split[0], float(line_split[1]), float(line_split[2]))
                    continue
            else:
                raise Exception("Wrong template format.")
        elif status == 'IndexedVarStart':
            if len(line_split) == 0:
                status = "WaitData"
                continue
            elif len(line_split) == 1 or len(line_split) == 2:
                if line_split[0] == "":
                    status = "WaitData"
                    continue
                else:
                    status = "IndexedVarStart"
                    var_name = line_split[0]
                    continue
            elif len(line_split) == 3:
                if line_split[0] == "":
                    status = "WaitData"
                    continue
                else:
                    str = line_split[0]
                    if str[0] == "\"" or str[0] == "\'":
                        index_str = "["+str+"]"
                    elif str[0] == '(':
                        index_str = str.replace('(','[').replace(')',']')
                    else:
                        if str.isdigit():
                            index_str = "[" + str + "]"
                        elif re.match(r'[a-zA-Z]', str) == None:
                            if type(eval(str)) == float:
                                index_str = "[" + str + "]"
                            else:
                                raise Exception("Wrong index format.")
                        else:#不带引号的字符串
                            dict[str] = index_str = "["+str+"]"
                    set_up_one_data(task, var_name + index_str, float(line_split[1]), float(line_split[2]))
            else:
                raise Exception("Wrong template format.")
    file.close()

def set_up_one_data(task, var_name, value_str, weight_str):
    task.obj_included_vars[var_name] = [value_str,weight_str]

def load_PE_init_from_templ(model, task):
    for file_name in task.PE_init_file:
        ModularTask.InitValueTools.load_init_from_template(model, file_name)
    if task.number_of_case > 1:
        for device in task.devices.values():
            for spec, v in device.specifications.items():
                if type(v) == ModularTask.PE.EstimatedSpec:
                    ModularTask.InitValueTools.set_initials(model, device.primitive_name+spec, v.params['init'])
                    for no_c in range(task.number_of_case):
                        ModularTask.InitValueTools.set_initials(model, device.primitive_name + 'PE%d'%no_c+spec, v.params['init'])
    elif task.number_of_case == 1:
        for device in task.devices.values():
            for spec, v in device.specifications.items():
                if type(v) == ModularTask.PE.EstimatedSpec:
                    ModularTask.InitValueTools.set_initials(model, device.primitive_name+spec, v.params['init'])
    # 保存初始误差
    task.obj_related_init = {}
    for c_no in range(task.number_of_case):
        for k in task.obj_included_vars.keys():
            task.obj_related_init[k] = value(eval("model."+k))

def write_PE_report(model, task, file_name):
    f = open(file_name, "w")
    f.write("Parameter Estimation Result:\n\n")
    for device in task.devices.values():
        for spec, v in device.specifications.items():
            if type(v) == ModularTask.PE.EstimatedSpec:
                f.write(device.primitive_name+spec+'\t'+str(value(getattr(model, device.primitive_name+spec)))+"\n")
    title = ""
    title +="""
#-----------------------------
#       Error Case %2d
#-----------------------------
var\ttrue_value\tafter\tbefore\terror_after\terror_before
"""
    for c_no in range(task.number_of_case):
        f.write(title%c_no)
        for k,v in task.obj_included_vars.items():
            if "PE%d"%c_no in k:
                v1 = v[0]  #真值
                v2 = value(eval("model."+k))  #参数估计后
                v3 = task.obj_related_init[k]  #参数估计前
                error = (v2-v1)/v1   #参数估计后
                error2 = (v3-v1)/v1  #参数估计前
                f.write(k+"\t")
                f.write(str(v1)+'\t')
                f.write(str(v2)+'\t')
                f.write(str(v3) + '\t')
                f.write("%2f" % (error * 100) + "%" + '\t')
                f.write("%2f"%(error2*100)+"%" + '\n')
    f.close()