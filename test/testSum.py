#!/usr/bin/env python
#-*- coding:utf-8 -*-

from pyomo.environ import *
from pyomo.dae import *
model = ConcreteModel()
model.DataSets = RangeSet(1, 11)
model.data_simple = Var(initialize=20)
model.data = Var(getattr(model,"DataSets"),model.DataSets, initialize = 0)
def MyConstraint1(m):
    return sum([m.data[i,i]*2 for i in model.DataSets])==10
setattr(model, "MyConstraint1",Constraint(rule=MyConstraint1))
#model.MyConstraint1 = Constraint(rule=MyConstraint1)
def MyConstraint2(m,dataSet,dataSet2):
    return m.data[dataSet,dataSet2]>=0
model.MyConstraint2 = Constraint(model.DataSets,model.DataSets,rule=MyConstraint2)
def obj_rule(m):
    return sum([m.data[i,i] for i in model.DataSets])
model.OBJ = Objective(rule=obj_rule,sense=minimize)
solver=SolverFactory('ipopt')
results = solver.solve(model,tee=True)
# print(results)
all_attr = dir(model)
i = 0
for attr in all_attr:
    #print(attr)
    print(type(getattr(model,attr)))  # is pyomo.core.base.rangeset.RangeSet
    print(isinstance(getattr(model,attr),pyomo.core.base.var.IndexedVar))
    print(isinstance(getattr(model, attr), pyomo.core.base.var.SimpleVar))
    # print(isinstance(getattr(model,attr),pyomo.core.base.rangeset.RangeSet))
    # if i>8:
    #     break
keys = getattr(model.data,'__dict__')
var_data=keys['_data']
# for k in var_data:
#     print(keys['_data'][k].value)
#
print(model.data._implicit_subsets[0]._name)
print(model.data._data[(1,1)]._value)
print(model.data_simple._value)