#!/usr/bin/env python
#-*- coding:utf-8 -*-
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
from col_irc import model

solver=SolverFactory('ipopt')
results = solver.solve(model,tee=True)
with open('irc_display.txt', 'w') as file:
    model.display(ostream=file)
