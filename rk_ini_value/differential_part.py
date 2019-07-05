#!/usr/bin/env python
#-*- coding:utf-8 -*-
from pyomo.environ import *
from pyomo.dae import *

model = ConcreteModel()
#-------------------------------
#  Deficition of Sets
#-------------------------------
model.time = Set(initialize=[0,1])
model.ParaTime = Set(initialize=[0,1])
model.StateSet = Set(initialize=[0,1,2,3])
model.InputSet = Set(initialize=[0,1])
model.OutputSet = Set(initialize=[0,1])
#-------------------------------
#  Math Model
#-------------------------------
A=[[0,1,0,0],
   [-15,-0.75,5,0.25],
   [0,0,0,1],
   [10,0.5,-10,-0.5]]
B=[[0,0],
   [0.025,0],
   [0,0],
   [0,0.05]]
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
model.dxdt = Var(model.time, model.StateSet,initialize=0)
#--------------------------------
#  Differential Constraints
#--------------------------------
def StateEquation(m,t,x):
    return m.dxdt[t,x] == sum([m.x[t,j]*A[x][j] for j in m.StateSet]) + sum([m.u[t,j]*B[x][j] for j in m.InputSet])
model.StateEquation = Constraint(model.time, model.StateSet,rule = StateEquation)