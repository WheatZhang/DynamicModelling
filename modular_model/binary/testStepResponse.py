#!/usr/bin/env python
#-*- coding:utf-8 -*-
from pyomoSR import test_model

from pyomo.environ import *
solver=SolverFactory('ipopt')
results = solver.solve(test_model,tee=True)
with open('SR_display.txt', 'w') as file:
    test_model.display(ostream=file)

#测试结果：2000->2100 OK ， 2000->2200 FAILED