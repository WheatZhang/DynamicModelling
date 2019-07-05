#!/usr/bin/env python
#-*- coding:utf-8 -*-
from pyomo.environ import *
from col_feed import model

def obj_rule(m):
    return 1
model.OBJ = Objective(rule=obj_rule)
solver=SolverFactory('ipopt')
results = solver.solve(model,tee=True)
with open('feed_display.txt', 'w') as file:
    model.display(ostream=file)