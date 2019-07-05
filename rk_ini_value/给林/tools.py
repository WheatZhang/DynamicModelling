#!/usr/bin/env python
#-*- coding:utf-8 -*-
from pyomo.environ import *
from pyomo.dae import *

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

class TimeDiscretilizer(object):
    def __init__(self, ncp, nfe,bounds,scheme = 'LAGRANGE-RADAU'):
        self.ncp = ncp
        self.nfe = nfe
        self.bounds = bounds
        self.scheme = scheme
    def set_fe_point(self, list):
        if list == None or len(list) == 0:
            list = []
            list.append(self.bounds[0])
            list.append(self.bounds[1])
        else:
            list.sort()
            if list[0] != self.bounds[0]:
                list.insert(0, self.bounds[0])
            if list[-1] != self.bounds[1]:
                list.append(self.bounds[1])
        if len(list) == self.nfe+1:
            self.list = list
        else:
            spans = []
            new_spans = []
            points = []
            for i in range(len(list)-1):
                spans.append(list[i+1]-list[i])
                new_spans.append(list[i+1]-list[i])
                points.append(0)
            unused_points = (self.nfe + 1) - len(list)
            if unused_points < 0:
                raise Exception("Too many nodes specified.")
            for i in range(unused_points):
                max_span_index = new_spans.index(max(new_spans))
                points[max_span_index] += 1
                new_spans[max_span_index] = spans[max_span_index]/(points[max_span_index]+1)
            for i in range(len(spans)):
                if points[i] > 0:
                    for j in range(points[i]):
                        list.append(list[i]+(list[i+1]-list[i])/(points[i]+1)*(j+1))
            list.sort()
            self.list = list
    def initialize_time(self, model, str_name):
        setattr(model, str_name, ContinuousSet(initialize=self.list[1:-1], bounds=self.bounds))
    def get_para_time(self):
        model = ConcreteModel()
        if not hasattr(self,"list"):
            raise Exception("Must set the nodes first.")
        model.time = ContinuousSet(bounds=self.bounds,initialize = self.list[1:-1])
        discretizer = TransformationFactory('dae.collocation')
        discretizer.apply_to(model, nfe=self.nfe, ncp=self.ncp, scheme=self.scheme)
        return model.time.value
    def discretilize(self, model):
        discretizer = TransformationFactory('dae.collocation')
        discretizer.apply_to(model, nfe=self.nfe, ncp=self.ncp, scheme=self.scheme)

def load_RKinit_modified_t(model, model_path, init_set_name, new_time):
    new_time.sort()
    module = __import__(model_path)
    data = getattr(module, init_set_name)
    old_time = getattr(module, "old_time")
    for key,value in data.items():
        dict_modified = modify_time(value, new_time, old_time)
        set_initials(model, key, dict_modified)
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
