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
from irc_system2 import model
#from irc_system_soft import model
import show_result

solver=SolverFactory('ipopt')
results = solver.solve(model,tee=True)
with open('irc_display2.txt', 'w') as file:
    model.display(ostream=file)
