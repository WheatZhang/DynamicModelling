#!/usr/bin/env python
#-*- coding:utf-8 -*-
from pyomo.environ import *
from pyomo.dae import *

class TimeDiscretizer(object):
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

#--------------------------------------------
    # 示例程序：
    # dict = {0:0,1:2,3:4}
    # dict = {(0,'a'):0,(0,'b'):2,
    #         (1,'a'):2,(1,'b'):2,
    #         (3,'a'):3,(3,'b'):5}
    # 其中dict键名的第一个数字为old_time中的时间
    # new_time = [0,1,2,5,2,2,5]
    # new_time为新离散的时间点
    # old_time = [0,1,3]
    # old_time为旧离散的时间点
#--------------------------------------------
def modify_time(dict,new_time, old_time):
    keys = []
    first_item_flag = True
    for complete_key in dict.keys():
        if type(complete_key) == tuple:
            if first_item_flag:
                first_item_flag = False
                first_time = complete_key[0]
                keys.append(complete_key[1:])
            else:
                if complete_key[0] == first_time:
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
