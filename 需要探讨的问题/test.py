#!/usr/bin/env python
#-*- coding:utf-8 -*-
from pyomo.environ import *
import numpy as np

model =  ConcreteModel()

#index
model.I = range(10)

#待估计参数
model.K = Var(model.I,bounds=(1,None),initialize=2)

#第一个用到这个参数的中间变量计算函数
F_x = {}
F_x_2 = {}
F_x_3 = {}

for i in model.I:
    F_x[i] = model.K._data[i]

print(F_x[i]._value)
#for i in model.I:
#    F_x_2[i] = F_x[i] * 2
#for i in model.I:
#    F_x_3[i] = F_x_2[i] * 3


#def con(m):
#    return sum(F_x_3[i] for i in model.I)
#model.obj = Objective(rule = con)