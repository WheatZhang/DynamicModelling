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
    def __init__(self, ncp, nfe,bounds):
        self.ncp = ncp
        self.nfe = nfe
        self.bounds = bounds
    def set_fe_point(self, list):
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
            for i in range(unused_points):
                max_span_index = new_spans.index(max(new_spans))
                points[max_span_index] += 1
                new_spans[max_span_index] = spans[max_span_index]/(points[max_span_index]+1)
            for i in range(len(spans)):
                if spans[i] > 0:
                    for j in range(spans[i]+1):
                        list.append((list[i+1]-list[i])/(spans[i]+2)*(j+1))
            list.sort()
            self.list = list
    def initialize_time(self, model, str_name):
        setattr(model, str_name, ContinuousSet(initialize=self.list[1:-1], bounds=self.bounds))
    def discretilize(self, model):
        discretizer = TransformationFactory('dae.collocation')
        discretizer.apply_to(model, nfe=self.nfe, ncp=self.ncp, scheme='LAGRANGE-RADAU')
