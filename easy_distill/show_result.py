#!/usr/bin/env python
#-*- coding:utf-8 -*-
from pyomo.environ import *
from pyomo.dae import *

def print_var(model, var_name):
    if isinstance(getattr(model, var_name), pyomo.core.base.var.SimpleVar):
        result = getattr(model,var_name)._value
    elif isinstance(getattr(model, var_name), pyomo.core.base.var.IndexedVar):
        result = {}
        for key, value in getattr(model, var_name)._data.items():
            result[key]=value._value
    else:
        raise Exception('Cannot handle a var which is neither IndexedVar nor SimpleVar')
    print(result)

def print_all_var(model, file_name):
    all_attr = dir(model)
    f = open(file_name, "w")
    for attr in all_attr:
        if isinstance(getattr(model, attr), pyomo.core.base.var.SimpleVar):
            f.write(attr+'\t')
            f.write(str(getattr(model,attr)._value))
            f.write('\n\n')
        elif isinstance(getattr(model, attr), pyomo.core.base.var.IndexedVar):
            f.write(attr + '\n')
            for key, value in getattr(model, attr)._data.items():
                f.write(str(key) + '\t')
                f.write(str(value._value)+'\n')
            f.write('\n')
    f.close()