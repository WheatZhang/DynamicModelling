#  _________________________________________________________________________
#
#  Pyomo: Python Optimization Modeling Objects
#  Copyright (c) 2014 Sandia Corporation.
#  Under the terms of Contract DE-AC04-94AL85000 with Sandia Corporation,
#  the U.S. Government retains certain rights in this software.
#  This software is distributed under the BSD License.
#  _________________________________________________________________________

from pyomo.environ import *
from pyomo.dae import *
import matplotlib.pyplot as plt
#from col_reflux_fix_feed import model,NumberOfTrays
from col_full import model

NumberOfTrays=model.NumberOfTrays.value
def obj_rule(m):
    return 1
model.OBJ = Objective(rule=obj_rule)
solver=SolverFactory('ipopt')
results = solver.solve(model,tee=True)
with open('reflux_display.txt', 'w') as file:
    model.display(ostream=file)
plt.show()
liquid_leaving_conc1 = []
liquid_leaving_conc2 = []
liquidLeavingMolarFlow = []
vaporLeavingMolarFlow = []
trayTemperature = []
vapor_leaving_conc1 = []
vapor_leaving_conc2 = []
for i in model.AllTrays:
    liquid_leaving_conc1.append(value(model.liquidLeavingMolarFraction[i,'Oxygen']))
    liquid_leaving_conc2.append(value(model.liquidLeavingMolarFraction[i, 'Nitrogen']))
    vapor_leaving_conc1.append(value(model.vaporLeavingMolarFraction[i, 'Oxygen']))
    vapor_leaving_conc2.append(value(model.vaporLeavingMolarFraction[i, 'Nitrogen']))
    liquidLeavingMolarFlow.append(value(model.liquidLeavingMolarFlow[i]))
    vaporLeavingMolarFlow.append(value(model.vaporLeavingMolarFlow[i]))
    trayTemperature.append(value(model.trayTemperature[i]))
fig, axes = plt.subplots(2,2)
axes[0,0].plot(range(1,NumberOfTrays+1),liquid_leaving_conc1, label = 'Oxygen_l')
axes[0,0].plot(range(1,NumberOfTrays+1),liquid_leaving_conc2, label = 'Nitrogen_l')
axes[0,1].plot(range(1,NumberOfTrays+1),liquidLeavingMolarFlow, label = 'liquid_leaving')
axes[0,1].plot(range(1,NumberOfTrays+1),liquidLeavingMolarFlow, label = 'vapor_leaving')
axes[1,0].plot(range(1,NumberOfTrays+1),trayTemperature, label = 'temperature')
axes[1,1].plot(range(1,NumberOfTrays+1),vapor_leaving_conc1, label = 'Oxygen_v')
axes[1,1].plot(range(1,NumberOfTrays+1),vapor_leaving_conc2, label = 'Nitrogen_v')
for ax1 in axes:
    for ax in ax1:
        ax.legend(loc="best")  #set legend location
plt.show()
