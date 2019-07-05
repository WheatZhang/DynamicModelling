#!/usr/bin/env python
#-*- coding:utf-8 -*-
from pyomo.environ import *

def set_initials_partial_index(model, var_name, tag_index, initial_value):
    all_attr = dir(model)
    full_dict = {}
    if var_name in all_attr:
        for key in getattr(model, var_name)._data.keys():
            matched_item = []
            for i, element in enumerate(tag_index):
                matched_item.append(key[element])
            if len(matched_item) == 1:
                matched_item = matched_item[0]
            else:
                matched_item = tuple(matched_item)
            getattr(model, var_name)._data[key]._value = initial_value[matched_item]
        getattr(model, var_name)._value_init_value = None
    else:
        raise Exception("There is no variable called:"+var_name)