#!/usr/bin/env python
#-*- coding:utf-8 -*-
from pyomo.environ import *
from pyomo.dae import *

model = ConcreteModel()
#-------------------------------
#  Deficition of Sets
#-------------------------------
model.time = Set(initialize=[0])
model.ParaTime = Set(initialize=[0])
model.StateSet = Set(initialize=[0,1,2,3])
model.InputSet = Set(initialize=[0,1])
model.OutputSet = Set(initialize=[0,1])
#-------------------------------
#  Math Model
#-------------------------------
C=[[1,0,0,0],
   [0,0,1,0]]
D=[[0,0],
   [0,0]]
#--------------------------------
#   Parameters
#--------------------------------
def InputSignal(m,t,u):
    if u==0:
        return 20
    elif u == 1:
        return 10
model.u = Param(model.ParaTime, model.InputSet,rule = InputSignal)
#--------------------------------
#  Variables
#--------------------------------
model.x = Var(model.time,model.StateSet,initialize=0)
model.y = Var(model.time,model.OutputSet,initialize=0)
#--------------------------------
#  Algebraic Constraints
#--------------------------------
def OutputEquation(m,t,y):
    return m.y[t,y] == sum([m.x[t,j]*C[y][j] for j in m.StateSet]) + sum([m.u[t,j]*D[y][j] for j in m.InputSet])
model.OutputEquation = Constraint(model.time, model.OutputSet,rule = OutputEquation)