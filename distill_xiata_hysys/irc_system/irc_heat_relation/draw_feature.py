#!/usr/bin/env python
#-*- coding:utf-8 -*-
from pyomo.environ import *
from pyomo.dae import *
import reb_side
import cond_side
import matplotlib.pyplot as plt

# reb_m = reb_side.reb_model(1.6e7)
# solver=SolverFactory('ipopt')
# solver.solve(reb_m, tee=False)
# with open('reb_model.txt', 'w') as file:
#     reb_m.display(ostream=file)
#
# cond_m = cond_side.cond_model(22e6)
# solver=SolverFactory('ipopt')
# solver.solve(cond_m, tee=False)
# with open('cond_model.txt', 'w') as file:
#     cond_m.display(ostream=file)

solver=SolverFactory('ipopt')
heat_transfer = range(15000000,15800000,200000)
reb_temp = []
cond_temp = []
for ht in heat_transfer:
    reb_m = reb_side.reb_model(ht)
    solver.solve(reb_m, tee=False)
    reb_temp.append(reb_m.ircRebTemperature.value)
for ht in heat_transfer:
    cond_m = cond_side.cond_model(ht)
    solver.solve(cond_m, tee=False)
    cond_temp.append(cond_m.ircCondTemperature.value)
fig, axes = plt.subplots(2,1)
axes[0].plot(heat_transfer,reb_temp, label = 'ircRebTemperature')
axes[0].plot(heat_transfer,cond_temp, label = 'ircCondTemperature')

heatTransferConstant = 238616
ircHeatExchangeByCal = []
for i in range(len(heat_transfer)):
    ircHeatExchangeByCal.append((cond_temp[i]-reb_temp[i])*heatTransferConstant)
axes[1].plot(heat_transfer,heat_transfer, label = 'ircHeatExchangeBySpec')
axes[1].plot(heat_transfer,ircHeatExchangeByCal, label = 'ircHeatExchangeByCal')

for ax in axes:
    ax.legend(loc="best")  #set legend location
plt.show()