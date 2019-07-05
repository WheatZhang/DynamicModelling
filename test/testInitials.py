#!/usr/bin/env python
#-*- coding:utf-8 -*-

from pyomo.environ import *
from pyomo.dae import *

model = ConcreteModel()
model.DataSets = RangeSet(1,3)
model.data_simple = Var(bounds=(0,10))
model.data_indexed = Var(model.DataSets,bounds=(0,10))
#-----------------初始化----------------------
def set_initials(model, var_name, initial_value):
    all_attr = dir(model)
    if var_name in all_attr:
        if isinstance(initial_value, dict):
            for key, value in initial_value.items():
                getattr(model, var_name)._data[key]._value = value
            getattr(model, var_name)._value_init_value = initial_value
        else:
            getattr(model, var_name)._value = initial_value
            getattr(model, var_name)._value_init_value = initial_value
    else:
        raise Exception("There is no variable called:"+var_name)
#-------例子-------
set_initials(model,"data_simple",5)
set_initials(model,"data_indexed",{1:2,2:3,3:4})
#-------------------------------------------
def obj_rule(m):
    return sum([m.data_indexed[i] for i in model.DataSets])+model.data_simple
model.OBJ = Objective(rule=obj_rule,sense=minimize)

solver=SolverFactory('ipopt')
results = solver.solve(model,tee=True)

for i in range(1,4):
    print(model.data_indexed._data[i].value)
print(model.data_simple.value)