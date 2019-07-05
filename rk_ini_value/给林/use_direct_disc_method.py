#!/usr/bin/env python
#-*- coding:utf-8 -*-
from pyomo.environ import *
from pyomo.dae import *
import matplotlib.pyplot as plt
import tools

model = ConcreteModel()
disc = tools.TimeDiscretilizer(nfe=100, ncp = 3, bounds = (0,20))
disc.set_fe_point(list = None)
disc.initialize_time(model, 'time')
#-------------------------------
#  Deficition of Sets
#-------------------------------
pe_list =disc.get_para_time()
model.ParaTime = Set(initialize=pe_list)
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
model.dxdt = DerivativeVar(model.x, withrespectto=model.time,initialize=0)
#--------------------------------
#  Differential Constraints
#--------------------------------
def StateEquation(m,t,x):
    return m.dxdt[t,x] == sum([m.x[t,j]*A[x][j] for j in m.StateSet]) + sum([m.u[t,j]*B[x][j] for j in m.InputSet])
model.StateEquation = Constraint(model.time, model.StateSet,rule = StateEquation)
#--------------------------------
#  Algebraic Constraints
#--------------------------------
def OutputEquation(m,t,y):
    return m.y[t,y] == sum([m.x[t,j]*C[y][j] for j in m.StateSet]) + sum([m.u[t,j]*D[y][j] for j in m.InputSet])
model.OutputEquation = Constraint(model.time, model.OutputSet,rule = OutputEquation)
#-------------------------------------------
#      Integration Initial Condition
#-------------------------------------------
x0 = [0,0,0,0]
def systemStateInitCond(m):
    for i in range(len(x0)):
        yield m.x[0,i] == x0[i]
model.systemStateInitCond = ConstraintList(rule=systemStateInitCond)
#-------------------------------------------
#       discretilization
#-------------------------------------------
disc.discretilize(model)
#-------------------------------------------
#      Solve
#-------------------------------------------
solver=SolverFactory('ipopt')
results = solver.solve(model,tee=True)
#-------------------------------------------
#      Show Result
#-------------------------------------------
time = []
y1 = []
y2 = []
for i in model.time:
    time.append(i)
    y1.append(value(model.y[i,0]))
    y2.append(value(model.y[i,1]))
# fig, axes = plt.subplots(1,2)
# axes[0].plot(time,y1, label = 'y1')
# axes[1].plot(time,y2, label = 'y2')
# for ax in axes:
#     ax.legend(loc="best")  #set legend location
# plt.show()