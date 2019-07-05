#!/usr/bin/env python
#-*- coding:utf-8 -*-

import test_dir.testPY as testPY
# print(testPY.myfun())

# import importlib
# lib = importlib.import_module("test_dir.testPY")
# print(lib.myfun())
from pyomo.environ import *

model = ConcreteModel()
model.x = Var()
model.y = Var(initialize=1)
def con_x(m):
    return m.x == testPY.myfun()
model.con_x = Constraint(rule = con_x)
def con_y(m):
    return m.y**3 == 8
model.con_y = Constraint(rule = con_y)

solver=SolverFactory('ipopt')
results = solver.solve(model,tee=False)
print(value(model.y))