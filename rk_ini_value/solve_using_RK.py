#!/usr/bin/env python
#-*- coding:utf-8 -*-
from pyomo.environ import *
from pyomo.dae import *
import matplotlib.pyplot as plt
import copy
import re
import load_initials

differetial_var = ["x[*,0]","x[*,1]","x[*,2]","x[*,3]"]
derivatives = ["dxdt[*,0]","dxdt[*,1]","dxdt[*,2]","dxdt[*,3]"]
algebraic_var = ["y[*,0]","y[*,1]"]
re_expression_name = r'^(.*)\['
re_expression_index = r'\[(.*)\]'

init_result = {}
for i in differetial_var:
    name = re.search(re_expression_name, i).group(1)
    if name not in init_result:
        init_result[name] = {}
for i in derivatives:
    name = re.search(re_expression_name, i).group(1)
    if name not in init_result:
        init_result[name] = {}
for i in algebraic_var:
    name = re.search(re_expression_name, i).group(1)
    if name not in init_result:
        init_result[name] = {}

differetial_var_value = [0,0,0,0]
algebraic_var_value = [0,0]
solver=SolverFactory('ipopt')
h=0.2
start_time = 0
time = []

y1 = []
y2 = []

for k in range(100):
    try:
        a_model
    except NameError:
        pass
    else:
        del a_model
    from algebraic_part import model as a_model
    a_model = copy.deepcopy(a_model)
    for i in range(len(differetial_var_value)):
        setattr(a_model,"ICON_"+str(i),Constraint(expr=eval("a_model."+differetial_var[i].replace('*','0')+"=="+str(differetial_var_value[i]))))
    results = solver.solve(a_model,tee=False)
    for i in range(len(algebraic_var_value)):
        algebraic_var_value[i] =eval(" value(a_model."+algebraic_var[i].replace('*','0')+")\n")
        init_result[re.search(re_expression_name, algebraic_var[i]).group(1)]\
            [eval("("+re.search(re_expression_index, algebraic_var[i]).group(1).replace('*',str(start_time))+")")] = algebraic_var_value[i]

    #print(algebraic_var_value)
    y1.append(algebraic_var_value[0])
    y2.append(algebraic_var_value[1])

    try:
        d_model
    except NameError:
        pass
    else:
        del d_model
    from differential_part import model as d_model
    d_model = copy.deepcopy(d_model)
    for i in range(len(algebraic_var_value)):
        setattr(d_model,"ICON_A0_"+str(i),Constraint(expr=eval("d_model."+algebraic_var[i].replace('*','0')+"=="+str(algebraic_var_value[i]))))
        setattr(d_model, "ICON_A1_" + str(i),Constraint(expr=eval("d_model." + algebraic_var[i].replace('*', '1') + "==" + str(algebraic_var_value[i]))))
    for i in range(len(differetial_var_value)):
        setattr(d_model,"ICON_D0_"+str(i),Constraint(expr=eval("d_model."+differetial_var[i].replace('*','0')+"=="+\
                str(differetial_var_value[i])+"+0.25*"+"d_model."+derivatives[i].replace('*','0')+"*"+str(h)+ \
                "+(3+2*(3**0.5))/12*" + "d_model." + derivatives[i].replace('*', '1')+"*" + str(h))))
        setattr(d_model, "ICON_D1_" + str(i), Constraint(expr=eval("d_model." + differetial_var[i].replace('*', '1') + "==" + \
                str(differetial_var_value[i]) + "+(3-2*(3**0.5))/12*" + "d_model." + derivatives[i].replace('*', '0')+"*"+ str(h) + \
                "+0.25*" + "d_model." + derivatives[i].replace('*', '1') + "*" + str(h))))
    results = solver.solve(d_model,tee=False)
    for i in range(len(differetial_var_value)):
        differetial_var_value[i] +=h/2*(eval(" value(d_model."+derivatives[i].replace('*','0')+")\n")+ \
                                  eval(" value(d_model." + derivatives[i].replace('*', '1') + ")\n"))
        init_result[re.search(re_expression_name, differetial_var[i]).group(1)]\
            [eval("("+re.search(re_expression_index, differetial_var[i]).group(1).replace('*',str(start_time))+")")] = differetial_var_value[i]
    for i in range(len(differetial_var_value)):
        init_result[re.search(re_expression_name, derivatives[i]).group(1)]\
            [eval("("+re.search(re_expression_index, derivatives[i]).group(1).replace('*',str(start_time))+")")] = \
            eval(" value(d_model." + derivatives[i].replace('*', '1') + ")\n")

    #print(differetial_var_value)
    time.append(start_time)
    start_time += h

#-------------------------------------------
#          Save Result
#-------------------------------------------
f = open('RK_Init_Result.py', 'w')
f.write("RK_Init_For_Control_System = "+str(init_result).replace(', (',',\n(').replace(' {','\n{'))
f.write('\n')
f.write("old_time = "+str(time))
f.close()
#-------------------------------------------
#      Show Result
#-------------------------------------------
fig, axes = plt.subplots(1,2)
axes[0].plot(time,y1, label = 'y1',c='b')
axes[1].plot(time,y2, label = 'y2',c='b')

from use_direct_disc_method import time as direct_disc_time,y1 as direct_disc_y1,y2 as direct_disc_y2
axes[0].plot(direct_disc_time,direct_disc_y1, label = 'y1',c='r')
axes[1].plot(direct_disc_time,direct_disc_y2, label = 'y2',c='r')
for ax in axes:
    ax.legend(loc="best")  #set legend location
plt.show()




