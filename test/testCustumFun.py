#!/usr/bin/env python
#-*- coding:utf-8 -*-
from pyomo.environ import *
import numpy

model = ConcreteModel()
def myfun(x):
    x = value(x)
    y = numpy.ndarray(shape = (3,))
    y[0]=x
    y[1]=x*2
    y[2] = x+2
    return numpy.sum(y)

model.x = Var(initialize=1)
model.y = Var(initialize=10)
def con(m):
    return m.x == myfun(m.y)
model.con = Constraint(rule=con)

solver=SolverFactory('ipopt')
results = solver.solve(model,tee=True)