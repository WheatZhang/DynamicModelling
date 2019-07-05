#!/usr/bin/env python
#-*- coding:utf-8 -*-
from pyomo.environ import *
from pyomo.dae import *
from binary_fitting_result import vapor_oxygen_composition,liquid_oxygen_composition,liquid_nitrogen_enthalpy,liquid_oxygen_enthalpy,vapor_nitrogen_enthalpy,vapor_oxygen_enthalpy
import matplotlib.pyplot as plt
import numpy as np

def LiquidPhaseEnthalpy(temperature, pressure, oxygen, nitrogen):
    return liquid_nitrogen_enthalpy(pressure,temperature)*nitrogen+liquid_oxygen_enthalpy(pressure,temperature)*oxygen
def VaporPhaseEnthalpy(temperature, pressure, oxygen, nitrogen):
    return vapor_nitrogen_enthalpy(pressure,temperature)*nitrogen+vapor_oxygen_enthalpy(pressure,temperature)*oxygen

temp_profile = []
enthalpy_profile = []
vapor_frac = []
for ircRebTemperature in np.arange(-190,-186,0.1):
    temp_profile.append(ircRebTemperature)
    ircRebPressure =  564-400
    total_nitrogen = 0.7009695483157175
    total_oxygen = 0.29903045168428255
    EVOutVPMolarFrac_oxygen = vapor_oxygen_composition(ircRebPressure, ircRebTemperature)
    EVOutLPMolarFrac_oxygen= liquid_oxygen_composition(ircRebPressure, ircRebTemperature)
    EVOutVaporFraction = (EVOutLPMolarFrac_oxygen-total_oxygen)/(EVOutLPMolarFrac_oxygen-EVOutVPMolarFrac_oxygen)
    enthalpy =  LiquidPhaseEnthalpy(ircRebTemperature, ircRebPressure, EVOutLPMolarFrac_oxygen,
                                  1-EVOutLPMolarFrac_oxygen)*(1-EVOutVaporFraction)+\
                VaporPhaseEnthalpy(ircRebTemperature, ircRebPressure, EVOutVPMolarFrac_oxygen,
                                   1-EVOutVPMolarFrac_oxygen)*EVOutVaporFraction
    enthalpy_profile.append(enthalpy)
    vapor_frac.append(EVOutVaporFraction)

fig, axes = plt.subplots(1,2)
axes[0].plot(temp_profile,enthalpy_profile,c='r')
axes[1].plot(temp_profile,vapor_frac,c='b')
plt.show()