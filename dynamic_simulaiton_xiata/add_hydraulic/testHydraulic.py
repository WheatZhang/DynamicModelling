#!/usr/bin/env python
#-*- coding:utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt

As=6.5
Hweir=35e-3
Lweir=1.942
g=9.8*3600
rho=29

L_list=[x*20 for x in range(50)]

M_list = []
for l in L_list:
    m = As*rho*(Hweir+1.41*(l/(np.sqrt(g)*rho*Lweir))**(2/3))
    M_list.append(m)

plt.plot(L_list, M_list, 'r')
plt.show()