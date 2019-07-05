#!/usr/bin/env python
#-*- coding:utf-8 -*-
import sys
sys.path.append("../")
from pyomoSR import test_model

from pyomo.environ import *
solver=SolverFactory('ipopt')
results = solver.solve(test_model,tee=True)
with open('SR_display.txt', 'w') as file:
    test_model.display(ostream=file)