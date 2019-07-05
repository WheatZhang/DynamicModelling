#!/usr/bin/env python
#-*- coding:utf-8 -*-
from pyomo.environ import *
from pyomo.dae import *
import matplotlib.pyplot as plt
from expand_valve import model

NumberOfTrays=model.NumberOfTrays.value
def obj_rule(m):
    return 1
model.OBJ = Objective(rule=obj_rule)
solver=SolverFactory('ipopt')
results = solver.solve(model,tee=True)
with open('expand_valve.txt', 'w') as file:
    model.display(ostream=file)