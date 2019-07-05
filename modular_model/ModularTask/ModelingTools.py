#!/usr/bin/env python
#-*- coding:utf-8 -*-
import ModularTask.Task as Task
import ModularTask.PE
from types import FunctionType

def gen_dynamic_para(task, para_name, value, index_list=[]):
    if not isinstance(index_list, list):
        raise Exception("The index list must be a list.")
    if not isinstance(task, Task.PyomoDynamicTask):
        raise Exception("The task %s is not a pyomo dynamic task."%task.name)
    para_str = ""
    if isinstance(value, int) or isinstance(value, float):
        para_str += "#model_name#.#device_name#%s = Param(#model_name#.ParaTime, initialize = %f)\n" \
                    % (para_name,value)
    elif isinstance(value, dict):
        # 如果是dict类型，表明为缺省的情况，并且只允许时间缺省
        if len(index_list) == 0:
            raise Exception("Illegal specification. The parameter %s is not indexed."%para_name)
        if len(index_list) == 1:
            para_str += "old_dict = {}\n"
            para_str += "for i in #model_name#.ParaTime.value:\n"
            for k, v in value.items():
                para_str += "\told_dict[i,"+my_to_str(k)+"] = "+str(v)+"\n"
            para_str += "#model_name#.#device_name#%s = Param(#model_name#.ParaTime, #model_name#."%para_name\
                        +index_list[0]+", initialize = old_dict)\n"
        else:
            para_str += "old_dict = {}\n"
            para_str += "for i in #model_name#.ParaTime.value:\n"
            for k, v in value.items():
                para_str += "\told_dict[i,"+my_to_str(k)+"] = " + str(v) + "\n"
            index_str = ""
            for i in index_list:
                index_str+=", #model_name#."+i
            para_str += "#model_name#.#device_name#%s = Param(#model_name#.ParaTime"%para_name+ index_str\
                        + ", initialize = old_dict)\n"
    elif isinstance(value, list):
        # 如果是list类型，表明不是缺省的情况,而是设置转折点的模式
        def takeFirst(elem):
            return elem[0]
        value.sort(key = takeFirst)
        old_time = []
        for i in value:
            old_time.append(i[0])
        para_str+="old_time = "+str(old_time)+"\n"
        old_dict = {}
        for i in value:
            complete_key = [i[0]]
            if isinstance(i[1],float) or isinstance(i[1],int):
                complete_value = i[1]
                old_dict[complete_key[0]] = complete_value
            elif isinstance(i[1], old_dict):
                for k,v in old_dict.items():
                    if isinstance(k, tuple):
                        for j in k:
                            complete_key.append(j)
                            complete_value = v
                            old_dict[tuple(complete_key)] = complete_value
                    else:
                        complete_key.append(k)
                        complete_value = v
                        old_dict[tuple(complete_key)] = complete_value
            else:
                raise Exception("Unsupport type of para spec %s." % type(i[1]))
        para_str +=  "old_dict = "+str(old_dict)+"\n"
        para_str+="new_dict = ModularTask.RuntimeTools.modify_time(old_dict, pe_list, old_time)\n"
        index_str = ""
        for i in index_list:
            index_str += ", #model_name#." + i
        para_str += "#model_name#.#device_name#%s = Param(#model_name#.ParaTime" % para_name + index_str \
                    + ", initialize = new_dict)\n"
    elif isinstance(value,FunctionType):
        # 如果是function类型，表明不是缺省的情况,而是设置函数模式
        paratime= task.time_list
        first_item_flag = True
        for t in paratime:
            if first_item_flag:
                para_str += "dict = {\n    "+str(t)+":"+str(value(t))
                first_item_flag = False
            else:
                para_str += ",\n    " + str(t) + ":" + str(value(t))
        para_str+="}\n"
        index_str = ""
        for i in index_list:
            index_str += ", #model_name#." + i
        para_str += "#model_name#.#device_name#%s = Param(#model_name#.ParaTime" % para_name + index_str \
                    + ", initialize = dict)\n"
    else:
        raise Exception("Unsupport type of para spec %s."%type(value))
    return para_str

def evaluate_dyna_para(dynamic_para, time):
    para_str = ""
    if isinstance(dynamic_para, int) or isinstance(dynamic_para, float):
        return dynamic_para
    elif isinstance(dynamic_para, dict):
        # 如果是dict类型，表明为缺省的情况，并且只允许时间缺省
        return dynamic_para
    elif isinstance(dynamic_para, list):
        # 如果是list类型，表明不是缺省的情况,而是设置转折点的模式
        index = 0
        for i in dynamic_para:
            if i[0]>time:
                break
            index += 1
        return dynamic_para[index-1][1]
    elif isinstance(dynamic_para,FunctionType):
        # 如果是function类型，表明不是缺省的情况,而是设置函数模式
        return dynamic_para(time)
    else:
        raise Exception("Unsupport type of para spec %s."%type(dynamic_para))

# 用于产生稳态仿真或者稳态参数估计的Para
def ss_or_pe_para(task, para_name, value, index_list=[]):
    if not isinstance(index_list, list):
        raise Exception("The index list must be a list.")
    para_str = ""
    if type(task) == Task.PyomoStaticTask or\
            (type(task) == Task.PyomoPETask and type(value) != ModularTask.PE.EstimatedSpec):
        if isinstance(value, int) or isinstance(value, float):
            para_str += "#model_name#.#device_name#%s = Param(initialize = %f)\n" \
                        % (para_name, value)
        elif isinstance(value, dict):
            # 如果是dict类型，表明为缺省的情况，并且只允许时间缺省
            if len(index_list) == 0:
                raise Exception("Illegal specification. The parameter %s is not indexed." % para_name)
            if len(index_list) == 1:
                para_str += "dict = {}\n"
                for k, v in value.items():
                    para_str += "dict["+my_to_str(k)+"] = " + str(v) + "\n"
                para_str += "#model_name#.#device_name#%s = Param(#model_name#." % para_name \
                            + index_list[0] + ", initialize = dict)\n"
            else:
                para_str += "dict = {}\n"
                for k, v in value.items():
                    para_str += "dict[i,"+my_to_str(k)+"] = " + str(v) + "\n"
                index_str = ""
                first_flag = True
                for i in index_list:
                    if first_flag:
                        index_str += "#model_name#." + i
                        first_flag = False
                    else:
                        index_str += ", #model_name#." + i
                para_str += "#model_name#.#device_name#%s = Param(" % para_name + index_str \
                            + ", initialize = dict)\n"
    elif type(task) == Task.PyomoPETask and type(value) == ModularTask.PE.EstimatedSpec:
        para_str += "#model_name#.#device_name#%s = Var(initialize = %f%s)\n" \
                        % (para_name, value.get_init(), value.generate_domain_str())
    else:
        raise Exception("The task %s is not a suitable task."%task.name)
    return para_str

def my_to_str(obj):
    if type(obj) == str:
        return "\""+obj+"\""
    else:
        return str(obj)

def to_pe_constraint(para_name, weight):
    con_str = ""
    con_str += "def #device_name#"+para_name+"PE(m):\n"
    con_str += "\treturn (m.#device_name#"+para_name+" - m.#prim_name#"+para_name+")*%f==0\n"%weight
    con_str += "#model_name#.#device_name#"+para_name+"PE = Constraint(rule=#device_name#"+para_name+"PE)\n"
    return con_str

def to_pe_public_var(para_name, value):
    var_str = ""
    if isinstance(value, ModularTask.PE.EstimatedSpec):
        var_str += "#model_name#.#prim_name#%s = Var(initialize = %f%s)\n" \
                            % (para_name, value.get_init(), value.generate_domain_str())
    return var_str