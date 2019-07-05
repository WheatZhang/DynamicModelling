#!/usr/bin/env python
#-*- coding:utf-8 -*-

from pyomo.environ import *
from pyomo.opt import SolverStatus, TerminationCondition
import numpy as np
from fit_tools import binary_cubic_polyfit

def create_binary_margules(filename, temp_span, pressure_span):
    point_density = 3
    points = (point_density+1)*(point_density+1)
    x = np.zeros(shape=(points,))
    y = np.zeros(shape=(points,))
    vap_oxygen = np.zeros(shape=(points,))
    liq_oxygen = np.zeros(shape = (points,))
    d_temp = (temp_span[1]-temp_span[0])/point_density
    d_pressure = (pressure_span[1]-pressure_span[0])/point_density
    n = 0
    for i in range(point_density+1):
        temp = temp_span[0] + i * d_temp
        for j in range(point_density+1):
            pressure = pressure_span[0] + j * d_pressure
            x[n] = pressure
            y[n] = temp
            result = margules_model(temp, pressure)
            vap_oxygen[n] = result[2]
            liq_oxygen[n] = result[0]
            n = n+1
    binary_cubic_polyfit(x, y, vap_oxygen, filename,"vap_oxygen_composition", "pressure", "temperature")
    binary_cubic_polyfit(x, y, liq_oxygen, filename, "liq_oxygen_composition", "pressure", "temperature")
    lib = __import__(filename)
    vap_oxygen_hat = np.zeros(shape=vap_oxygen.shape)
    liq_oxygen_hat = np.zeros(shape=liq_oxygen.shape)
    for i in range(vap_oxygen_hat.size):
        vap_oxygen_hat[i] = lib.vap_oxygen_composition(x[i], y[i])
        liq_oxygen_hat[i] = lib.liq_oxygen_composition(x[i], y[i])
    vap_error = np.max(np.abs(vap_oxygen - vap_oxygen_hat))
    liq_error = np.max(np.abs(liq_oxygen - liq_oxygen_hat))
    if vap_error>0.1:
        raise Exception("The vap_oxygen fitting has large error %f.\n"%vap_error)
    elif vap_error > 0.01:
        print("The vap_oxygen fitting is not very accurate with error %f.\n"%vap_error)
    if liq_error>0.1:
        raise Exception("The liq_oxygen fitting has large error %f.\n"%liq_error)
    elif liq_error > 0.01:
        print("The liq_oxygen fitting is not very accurate with error %f.\n"%liq_error)

def margules_model(temp, pressure):
    model = ConcreteModel()
    model.Component = Set(initialize=['Oxygen', 'Nitrogen'])

    model.SatPresCorA = Param(model.Component, initialize={'Oxygen':3.85845,'Nitrogen':3.63792})
    model.SatPresCorB = Param(model.Component, initialize={'Oxygen':-325.675,'Nitrogen':-257.877})
    model.SatPresCorC = Param(model.Component, initialize={'Oxygen':-5.667,'Nitrogen':-6.344})
    model.RGas = Param(initialize=8.314) #J/(mol*K)
    dict = {('Oxygen','Oxygen'):0,
    ('Oxygen','Nitrogen'):-0.012,
    ('Nitrogen','Oxygen'):-0.012,
    ('Nitrogen','Nitrogen'):0
    }
    model.MargulesItrct = Param(model.Component, model.Component, initialize=dict)

    model.LiqMFrac = Var(model.Component,bounds=(0,1),initialize={'Oxygen':0.7,'Nitrogen':0.3})
    model.VapMFrac = Var(model.Component,bounds=(0,1),initialize={'Oxygen':0.3,'Nitrogen':0.7})
    model.Pressure = Var(within=NonNegativeReals,initialize=pressure)
    model.SatPres = Var(model.Component, within=NonNegativeReals,initialize={'Oxygen':329,'Nitrogen':942})
    model.PhEquConst = Var(model.Component,initialize=1)
    model.Activity = Var(model.Component, within=NonNegativeReals,initialize=1)
    model.Temp = Var(bounds=(-273,100),initialize=temp)

    def VapSummation(m):
        return sum([m.VapMFrac[c] for c in m.Component]) == 1
    model.VapSummation = Constraint(rule = VapSummation)
    def LiqSummation(m):
        return sum([m.LiqMFrac[c] for c in m.Component]) == 1
    model.LiqSummation = Constraint(rule = LiqSummation)
    def PhEquilibruim(m, comp):
        return m.LiqMFrac[comp]*m.PhEquConst[comp]-m.VapMFrac[comp]==0
    model.PhEquilibruim = Constraint(model.Component, rule = PhEquilibruim)
    def PhEquilConstEqu(m, comp):
        return (m.PhEquConst[comp] - m.Activity[comp]*m.SatPres[comp]/m.Pressure)*1e-2 == 0
    model.PhEquilConstEqu = Constraint(model.Component, rule = PhEquilConstEqu)
    # P in kPa, T in ℃
    def SatPresSpec(m, comp):
        return log10(m.SatPres[comp]/100)-m.SatPresCorA[comp]-m.SatPresCorB[comp]/(m.SatPresCorC[comp]+m.Temp+273.15) == 0
    model.SatPresSpec = Constraint(model.Component, rule = SatPresSpec)
    def MarguleEqu(m, comp):
        return (m.RGas*m.Temp*log(m.Activity[comp]) - sum([sum([(m.MargulesItrct[c1,comp]-\
            0.5*m.MargulesItrct[c1,c2])*m.LiqMFrac[c1]*m.LiqMFrac[c2] for c2 in m.Component]) for c1 in m.Component]))*1e0 == 0
    model.MarguleEqu = Constraint(model.Component, rule = MarguleEqu)

    def TempSpec(m):
        return m.Temp == temp
    model.TempSpec = Constraint(rule = TempSpec)
    def PressureSpec(m):
        return m.Pressure == pressure
    model.PressureSpec = Constraint(rule = PressureSpec)

    solver=SolverFactory('ipopt')
    results = solver.solve(model,tee=False)
    # with open('margules_display.txt', 'w') as file:
    #     model.display(ostream=file)
    if not ((results.solver.status == SolverStatus.ok) and (results.solver.termination_condition == TerminationCondition.optimal)):
        raise Exception("The customized thermodynamic margules_model does not converge at temp %f and pressure %f" % (temp,pressure))
    liq_o = value(model.LiqMFrac['Oxygen'])
    liq_n = value(model.LiqMFrac['Nitrogen'])
    vap_o = value(model.VapMFrac['Oxygen'])
    vap_n = value(model.VapMFrac['Nitrogen'])
    return liq_o, liq_n, vap_o, vap_n

# print(margules_model(temp = -180, pressure=465))
# create_binary_margules("thermo_test",temp_span = (-176,-174),pressure_span = (530,560))