#!/usr/bin/env python
#-*- coding:utf-8 -*-
from pyomo.environ import *

model = ConcreteModel()
model.v = Var(initialize=20)

def con(m):
    return log10(m.v) - exp(1) == 0
model.con = Constraint(rule=con)

from pyomo.environ import *
solver=SolverFactory('ipopt')
results = solver.solve(model,tee=True)
with open('result_dynamic_display.txt', 'w') as file:
    model.display(ostream=file)
