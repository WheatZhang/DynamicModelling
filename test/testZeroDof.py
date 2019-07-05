#!/usr/bin/env python
#-*- coding:utf-8 -*-
from pyomo.environ import *
from pyomo.dae import *

model = ConcreteModel()
model.x=Var(initialize=0)
model.y=Var(initialize=0)
model.z=Var(initialize=0)
def con1(m):
    return m.x+m.y+m.z==1
model.con1 = Constraint(rule=con1)
def con2(m):
    return m.x-m.y+m.z*m.z==1
model.con2 = Constraint(rule=con2)
def con3(m):
    return m.x+m.y-m.z==1
model.con3 = Constraint(rule=con3)
def obj_rule(m):
    return 1
model.OBJ = Objective(rule=obj_rule,sense=minimize)

solver=SolverFactory('ipopt')
results = solver.solve(model,tee=True)