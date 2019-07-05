#!/usr/bin/env python
#-*- coding:utf-8 -*-
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
x=[1,2,3,2]
y=[1,1,2,0]
z=[1,2,3,0]
ax.plot_trisurf(x,y,z)
plt.show()