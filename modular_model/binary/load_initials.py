#!/usr/bin/env python
#-*- coding:utf-8 -*-
from pyomo.environ import *
from pyomo.dae import *
import csv
from tools import set_initials_partial_index
def load_RKinit_modified_t(model, model_path, init_set_name, new_time):
    new_time.sort()
    module = __import__(model_path)
    data = getattr(module, init_set_name)
    old_time = getattr(module, "old_time")
    for key,value in data.items():
        dict_modified = modify_time(value, new_time, old_time)
        set_initials(model, key, dict_modified)
    return model
def load_display_modified_t(model, filepath, new_time, old_time):
    new_time.sort()
    old_time.sort()
    f = open(filepath,"r")   #设置文件对象
    status = 0
    for line in f:
        line_value = line.split(':')
        if len(line_value) <= 1:
            continue
        if line_value[0].strip()[0] == '#':
            continue
        elif len(line_value) == 2:
            if status == 0:
                status = 1
                var_name = line_value[0].strip()
                dict = {}
                var_value = 0
                var_type = 0
            else:
                if var_type == 0:
                    set_initials(model, var_name, var_value)
                elif var_type == 1:
                    dict_modified = modify_time(dict,new_time, old_time)
                    set_initials(model, var_name, dict_modified)
                status = 1
                var_name=line_value[0].strip()
                dict = {}
                var_value = 0
                var_type = 0
            continue
        if status == 1:
            status = 2
            continue
        if status == 2:
            if line_value[0].strip() == 'None':
                var_type = 0
                var_value = float(line_value[2].strip())
            else:
                var_type = 1
                str = line_value[0].strip()
                if str[0] == '(':
                    dict[eval(str)] = float(line_value[2].strip())
                else:
                    if str.isdigit():
                        dict[int(str)] = float(line_value[2].strip())
                    elif type(eval(str))==float:
                        dict[float(str)] = float(line_value[2].strip())
                    else:
                        dict[str] = float(line_value[2].strip())
    f.close() #关闭文件
    return model

def modify_time(dict,new_time, old_time):
    keys = []
    for complete_key in dict.keys():
        if type(complete_key) == tuple:
            keys.append(complete_key[1:])
        else:
            keys = None
            break
    result_dict = {}
    for i in range(len(new_time)):
        time = new_time[i]
        lb_index_in_old = get_lower_bound_index(time, old_time)
        if lb_index_in_old == len(old_time) - 1:
            if keys == None:
                result_dict[new_time[i]] = dict[old_time[-1]]
            else:
                for k in keys:
                    this_old_key = [old_time[-1]]
                    this_new_key = [time]
                    for j in k:
                        this_old_key.append(j)
                        this_new_key.append(j)
                    result_dict[tuple(this_new_key)] = dict[tuple(this_old_key)]
        else:
            weight = [(time-old_time[lb_index_in_old])/(old_time[lb_index_in_old+1]-old_time[lb_index_in_old]), \
                      (old_time[lb_index_in_old+1]-time) / (old_time[lb_index_in_old + 1] - old_time[lb_index_in_old])]
            if keys == None:
                result_dict[new_time[i]] = dict[old_time[lb_index_in_old]]*weight[1]+dict[old_time[lb_index_in_old+1]]*weight[0]
            else:
                for k in keys:
                    this_old_key1 = [old_time[lb_index_in_old]]
                    this_old_key2 = [old_time[lb_index_in_old + 1]]
                    this_new_key = [time]
                    for j in k:
                        this_old_key1.append(j)
                        this_old_key2.append(j)
                        this_new_key.append(j)
                    result_dict[tuple(this_new_key)] = dict[tuple(this_old_key1)]*weight[1]+dict[tuple(this_old_key2)]*weight[0]
    return result_dict

def get_lower_bound_index(value, list):
    length = len(list)
    ub = length-1
    lb = 0
    if list[ub] <= value:
        return ub
    return _dichtomy_search_lb(value, list, ub, lb)

def _dichtomy_search_lb(value, list, ub, lb):
    if ub-lb <= 5:
        index = lb
        while(True):
            if list[index+1] < value:
                index+=1
            else:
                return index
            if index >= ub-1:
                break
        return index
    else:
        mid = int(lb+(ub-lb)/2)
        if list[mid] > value:
            return _dichtomy_search_lb(value, list, mid, lb)
        else:
            return _dichtomy_search_lb(value, list, ub, mid)


def load_from_display_filt_t(model, filepath, time):
    f = open(filepath,"r")   #设置文件对象
    status = 0
    for line in f:
        line_value = line.split(':')
        if len(line_value) <= 1:
            continue
        if line_value[0].strip()[0] == '#':
            continue
        elif len(line_value) == 2:
            if status == 0:
                status = 1
                var_name = line_value[0].strip()
                dict = {}
                var_value = 0
                var_type = 0
            else:
                if var_type == 0:
                    set_initials(model, var_name, var_value)
                elif var_type == 1:
                    set_initials(model, var_name, dict)
                status = 1
                var_name=line_value[0].strip()
                dict = {}
                var_value = 0
                var_type = 0
            continue
        if status == 1:
            status = 2
            continue
        if status == 2:
            if line_value[0].strip() == 'None':
                var_type = 0
                var_value = float(line_value[2].strip())
            else:
                var_type = 1
                str = line_value[0].strip()
                if str[0] == '(':
                    if eval(str+"[0]") in time:
                        dict[eval(str)] = float(line_value[2].strip())
                else:
                    if str.isdigit():
                        if int(str) in time:
                            dict[int(str)] = float(line_value[2].strip())
                    elif type(eval(str))==float:
                        if float(str) in time:
                            dict[float(str)] = float(line_value[2].strip())
                    else:
                        dict[str] = float(line_value[2].strip())
    f.close() #关闭文件
    return model

def load_init_from_display(model, filepath):
    f = open(filepath,"r")   #设置文件对象
    status = 0
    for line in f:
        line_value = line.split(':')
        if len(line_value) <= 1:
            continue
        if line_value[0].strip()[0] == '#':
            continue
        elif len(line_value) == 2:
            if status == 0:
                status = 1
                var_name = line_value[0].strip()
                dict = {}
                var_value = 0
                var_type = 0
            else:
                if var_type == 0:
                    set_initials(model, var_name, var_value)
                elif var_type == 1:
                    set_initials(model, var_name, dict)
                status = 1
                var_name=line_value[0].strip()
                dict = {}
                var_value = 0
                var_type = 0
            continue
        if status == 1:
            status = 2
            continue
        if status == 2:
            if line_value[0].strip() == 'None':
                var_type = 0
                var_value = float(line_value[2].strip())
            else:
                var_type = 1
                str = line_value[0].strip()
                if str[0] == '(':
                    dict[eval(str)] = float(line_value[2].strip())
                else:
                    if str.isdigit():
                        dict[int(str)] = float(line_value[2].strip())
                    elif type(eval(str))==float:
                        dict[float(str)] = float(line_value[2].strip())
                    else:
                        dict[str] = float(line_value[2].strip())
    f.close() #关闭文件
    return model

def set_initials(model, var_name, initial_value):
    all_attr = dir(model)
    if var_name in all_attr:
        if isinstance(initial_value, dict):
            if (not isinstance(getattr(model, var_name),pyomo.core.base.var.IndexedVar))\
                and (not isinstance(getattr(model, var_name),pyomo.dae.DerivativeVar)):
                raise Exception("%s is not a IndexedVar or a DerivativeVar" % var_name)
            for key, value in initial_value.items():
                getattr(model, var_name)._data[key]._value = value
            getattr(model, var_name)._value_init_value = initial_value
        else:
            if not isinstance(getattr(model, var_name),pyomo.core.base.var.SimpleVar):
                raise Exception("%s is not a SimpleVar" % var_name)
            getattr(model, var_name)._value = initial_value
            getattr(model, var_name)._value_init_value = initial_value
    else:
        raise Exception("There is no variable called:%s"%var_name)

def load_initials_from_csv(model,filepath):
    csv_file = csv.reader(open(filepath, 'r'))
    status = 0
    tags=[]
    for l in csv_file:
        line = []
        for elem in l:
            if elem != '':
                line.append(elem)
        for i in range(len(line)):
            line[i] = line[i].strip()
        if len(line) == 0 or line[0].startswith('#'): # 井号为注释
            if status == 1:
                setup_indexed_var(model, var_name, tags,dict)
            elif status == 3:
                setattr(model, var_name, Var(getattr(model, tags[0]), getattr(model, tags[1]), rule=dict))
            status = 0
            continue
        if line[0].startswith(':'):
            if status == 1:
                setup_indexed_var(model, var_name, tags,dict)
            elif status == 3:
                setattr(model, var_name, Var(getattr(model, tags[0]), getattr(model, tags[1]), rule=dict))
            if line[0].startswith(':VAR'):
                var_name = line[1]
                tags = line[2:]
                dict = {}
                status = 1
            elif line[0] == ':TABLE':
                var_name = line[1]
                tags = line[2:4]
                dict = {}
                status = 2
            else:
                raise Exception('Unidentified Tag')
            continue
        if status == 0:
            var_name = line[0]
            value = float(line[1])
            setattr(model, var_name,Var(initialize=value))
        elif status == 2:
            tag2 = line
            status = 3
            for j in range(len(tag2)):
                if tag2[j].isdigit():
                    tag2[j] = int(tag2[j])
        elif status == 1:
            if len(tags) == 0:
                raise Exception('The index must be greater than 0')
            elif len(tags) == 1:
                key = line[0]
                if key.isdigit():
                    key = int(key)
                dict[key] = float(line[1])
            else:
                key = line[:(len(line) - 1)]
                for j in range(len(key)):
                    if key[j].isdigit():
                        key[j] = int(key[j])
                key = tuple(key)
                dict[key] = float(line[-1])
        elif status == 3:
            tag1 = line[0]
            if tag1.isdigit():
                tag1 = int(tag1)
            for j in range(len(tag2)):
                key = (tag1, tag2[j])
                dict[key] = float(line[j + 1])
    if status == 1:
        setup_indexed_var(model, var_name, tags,dict)
    elif status == 3:
        setattr(model, var_name, Var(getattr(model, tags[0]), getattr(model, tags[1]), rule=dict))

def setup_indexed_var(model,var_name, tags,dict):
    if len(tags) == 0:
        raise Exception("Logic error")
    elif len(tags) == 1:
        setattr(model, var_name, Var(getattr(model, tags[0]), rule=dict))
    elif len(tags) == 2:
        setattr(model, var_name, Var(getattr(model, tags[0]), getattr(model, tags[1]), rule=dict))
    elif len(tags) == 3:
        setattr(model, var_name, Var(getattr(model, tags[0]), getattr(model, tags[1]), getattr(model, tags[2]), rule=dict))
    elif len(tags) == 4:
        setattr(model, var_name,
                Var(getattr(model, tags[0]), getattr(model, tags[1]), getattr(model, tags[2]), getattr(model, tags[3]),
                    rule=dict))
    else:
        raise Exception("Too many indexes")