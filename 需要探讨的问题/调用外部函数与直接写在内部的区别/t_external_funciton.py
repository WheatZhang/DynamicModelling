#!/usr/bin/env python
#-*- coding:utf-8 -*-
from pyomo.environ import *
from pyomo.dae import *

solver=SolverFactory('ipopt')
model = ConcreteModel()
def func(x):
    return x*x*x
model.x = Var(initialize=1)
def mainConstraint(m):
    return func(m.x) >= -4
model.mainConstraint = Constraint(rule=mainConstraint)
def obj(m):
    return m.x*4
model.obj = Objective(rule=obj)
model.write('test_external_function.nl')
solver.solve(model)

model2 =  ConcreteModel()
model2.x = Var(initialize=1)
def mainConstraint(m):
    return m.x >= -4
model2.mainConstraint = Constraint(rule=mainConstraint)
def obj(m):
    return m.x*4
model2.obj = Objective(rule=obj)
model2.write('test_internal_function.nl')