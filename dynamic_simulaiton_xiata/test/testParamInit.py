#!/usr/bin/env python
#-*- coding:utf-8 -*-
from pyomo.environ import *

model = ConcreteModel()
model.para = Param(initialize=10)
model.var = Var(initialize=0)

def con(m):
    return m.para == m.var
model.con = Constraint(rule=con)

model.para._value = 20
model.para._rule = 20

def obj_rule(m):
    return 1
model.OBJ = Objective(rule=obj_rule)
solver=SolverFactory('ipopt')
results = solver.solve(model,tee=True)
print(model.var.value)