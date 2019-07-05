#!/usr/bin/env python
#-*- coding:utf-8 -*-
from pyomo.environ import *
from pyomo.dae import *
import csv

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
                type = 0
            else:
                if type == 0:
                    set_initials(model, var_name, var_value)
                elif type == 1:
                    set_initials(model, var_name, dict)
                status = 1
                var_name=line_value[0].strip()
                dict = {}
                var_value = 0
                type = 0
            continue
        if status == 1:
            status = 2
            continue
        if status == 2:
            if line_value[0].strip() == 'None':
                type = 0
                var_value = float(line_value[2].strip())
            else:
                type = 1
                str = line_value[0].strip()
                if str[0] == '(':
                    dict[eval(str)] = float(line_value[2].strip())
                else:
                    if str.isdigit():
                        dict[int(str)] = float(line_value[2].strip())
                    else:
                        dict[str] = float(line_value[2].strip())
    f.close() #关闭文件
    return model

def set_initials(model, var_name, initial_value):
    all_attr = dir(model)
    if var_name in all_attr:
        if isinstance(initial_value, dict):
            if not isinstance(getattr(model, var_name),pyomo.core.base.var.IndexedVar):
                raise Exception("%s is not a IndexedVar" % var_name)
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
