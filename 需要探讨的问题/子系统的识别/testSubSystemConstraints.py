#!/usr/bin/env python
#-*- coding:utf-8 -*-

from pyomo.environ import *
from pyomo.dae import *

solver=SolverFactory('ipopt')
paramVar_init = -2
mainVar_init = 0

model = ConcreteModel()
model.paramVar = Var(initialize=paramVar_init)
model.mainVar = Var(initialize=mainVar_init)
def mainConstraint(m):
    return (m.mainVar-m.paramVar) * (m.mainVar-m.paramVar) == 400
model.mainConstraint = Constraint(rule=mainConstraint)
def paramConstraint1(m):
    return m.paramVar * m.paramVar == 4
model.paramConstraint1 = Constraint(rule=paramConstraint1)
def paramConstraint2(m):
    return m.paramVar*10 >= 0
model.paramConstraint2 = Constraint(rule=paramConstraint2)
solver.solve(model)

print("----Without Subsystem Priority----")
print("mainVar:",model.mainVar.value)
print("paramVar:",model.paramVar.value)

#--------------------------------------------------

model1 = ConcreteModel()
model1.paramVar = Var(initialize=paramVar_init)
def paramConstraint1Model1(m):
    return m.paramVar * m.paramVar == 4
model1.paramConstraint1 = Constraint(rule=paramConstraint1Model1)
def paramConstraint2Model1(m):
    return m.paramVar*10 >= 0
model1.paramConstraint2 = Constraint(rule=paramConstraint2Model1)
solver.solve(model1)
paramVar = model1.paramVar.value
model2 = ConcreteModel()
model2.mainVar = Var(initialize=mainVar_init)
def mainConstraintModel2(m):
    return (m.mainVar-paramVar) * (m.mainVar-paramVar) == 400
model2.mainConstraint = Constraint(rule=mainConstraintModel2)
solver.solve(model2)

print("----With Subsystem Priority----")
print("mainVar:",model2.mainVar.value)
print("paramVar:",paramVar)

