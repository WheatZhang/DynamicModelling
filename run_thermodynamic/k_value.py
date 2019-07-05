#!/usr/bin/env python
#-*- coding:utf-8 -*-
import numpy as np

R=8.314 #J/mol/k
# water
# ln(p_sat)=A+B/(T+C)
class Material(object):
    def __init__(self,name):
        self.name = name

water = Material("water")
water.Tc=647.3 #K
water.Pc=22.048 #MPa
water.omega=0.344

A=7.96681
B=-1730.63
C=233.426


def PR_calculate_p(V,T,mater):
    a=R*R*mater.Tc*mater.Tc/mater.Pc*\
      (1+(0.37464+1.54226*mater.omega-0.26992*mater.omega*mater.omega)*(1-np.sqrt(T/mater.Tc)))^2
    b=0.0778*R*mater.Tc/mater.Pc
    return R*T/(V-b) - a/(V*(V+b)+b(V-b))

def PR_caculate_p_mix2(V,T,x1,k12,mater1,mater2):
    a1 = R * R * mater1.Tc * mater1.Tc / mater1.Pc * \
        (1 + (0.37464 + 1.54226 * mater1.omega - 0.26992 * mater1.omega * mater1.omega) * (1 - np.sqrt(T / mater1.Tc))) ^ 2
    b1 = 0.0778 * R * mater1.Tc / mater1.Pc
    a2 = R * R * mater2.Tc * mater2.Tc / mater2.Pc * \
         (1 + (0.37464 + 1.54226 * mater2.omega - 0.26992 * mater2.omega * mater2.omega) * (1 - np.sqrt(T / mater2.Tc))) ^ 2
    b2 = 0.0778 * R * mater2.Tc / mater2.Pc
    a = x1*x1+2*x1*(1-x1)+(1-x1)*(1-x1)

    return R * T / (V - b) - a / (V * (V + b) + b(V - b))