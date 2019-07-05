#!/usr/bin/env python
#-*- coding:utf-8 -*-
from pyomo.environ import *
from pyomo.dae import *
from binary_fitting_result import vapor_oxygen_composition,liquid_oxygen_composition,liquid_nitrogen_enthalpy,liquid_oxygen_enthalpy,vapor_nitrogen_enthalpy,vapor_oxygen_enthalpy
model = ConcreteModel()
#---------------物质组分指定-----------
model.Component = Set(initialize=['Oxygen','Nitrogen'])
#--------------塔设备指定--------------
model.NumberOfTrays = Param(initialize=10)
model.TopAndBottomTray = Set(initialize={1,model.NumberOfTrays.value})
model.BottomTray = Set(initialize={1})
model.trayPressure = Param(model.TopAndBottomTray,initialize={1:564,model.NumberOfTrays.value:539.56})
model.trayTemperature  = Param(model.TopAndBottomTray,initialize={1:-174.55076597225644,model.NumberOfTrays.value:-177.70902430053})
model.liquidLeavingMolarFraction = Param(model.BottomTray,model.Component,initialize=\
    {(1,'Nitrogen'):0.7009695483157175,(1,'Oxygen'):0.29903045168428255})
#--------------IRC指定-----------------
model.expandValveDeltaP = Param(initialize=400)
#-------------IRC变量定义---------------
model.ircRebTemperature=Var(bounds=(-230,-100),initialize=-188.314)
model.ircRebPressure=Var(bounds=(0,1000),initialize=564-model.expandValveDeltaP.value)
#--------------膨胀阀变量定义---------------
model.EVOutVPMolarFrac = Var(model.Component, bounds=(0,1), initialize={'Oxygen':0.09,'Nitrogen':0.90})
model.EVOutLPMolarFrac = Var(model.Component, bounds=(0,1), initialize={'Oxygen':0.25,'Nitrogen':0.75})
model.EVOutVaporFraction = Var(initialize=0.142881, bounds=(0,0.3))
#----------------------------------------
#     焓的热力学
#----------------------------------------
def LiquidPhaseEnthalpy(temperature, pressure, oxygen, nitrogen):
    return liquid_nitrogen_enthalpy(pressure,temperature)*nitrogen+liquid_oxygen_enthalpy(pressure,temperature)*oxygen
def VaporPhaseEnthalpy(temperature, pressure, oxygen, nitrogen):
    return vapor_nitrogen_enthalpy(pressure,temperature)*nitrogen+vapor_oxygen_enthalpy(pressure,temperature)*oxygen
#----------------------------------------
def _ircOutExpandValveMolarEnthalpy(m):
    return LiquidPhaseEnthalpy(m.ircRebTemperature, m.ircRebPressure, m.EVOutLPMolarFrac['Oxygen'],
                               m.EVOutLPMolarFrac['Nitrogen'])*(1-m.EVOutVaporFraction)+\
            VaporPhaseEnthalpy(m.ircRebTemperature, m.ircRebPressure, m.EVOutVPMolarFrac['Oxygen'],
                               m.EVOutVPMolarFrac['Nitrogen'])*m.EVOutVaporFraction
model.ircOutExpandValveMolarEnthalpy = Expression(rule=_ircOutExpandValveMolarEnthalpy)
#-------------IRC Expand Valve-------------------
def ExpandValvePressure(m):
    return (m.trayPressure[1]-m.expandValveDeltaP-m.ircRebPressure)*1e-3 == 0
model.ExpandValvePressure = Constraint(rule=ExpandValvePressure)
def ExpandValveEnthalpy(m):
    return (LiquidPhaseEnthalpy(m.trayTemperature[1], m.trayPressure[1], m.liquidLeavingMolarFraction[1, 'Oxygen'],
                               m.liquidLeavingMolarFraction[1, 'Nitrogen'])- \
                                 model.ircOutExpandValveMolarEnthalpy)*1e-4 ==0
model.ExpandValveEnthalpy = Constraint(rule=ExpandValveEnthalpy)
def EVOutMaterialBalance(m):
    return m.EVOutVaporFraction * m.EVOutVPMolarFrac['Oxygen'] + (1 - m.EVOutVaporFraction) * \
           m.EVOutLPMolarFrac['Oxygen'] \
           - m.liquidLeavingMolarFraction[1, 'Oxygen'] == 0
model.EVOutMaterialBalance = Constraint(rule = EVOutMaterialBalance)
def EVOutVaporComposition(m):
    return m.EVOutVPMolarFrac['Oxygen'] == vapor_oxygen_composition(m.ircRebPressure,m.ircRebTemperature)
model.EVOutVaporComposition = Constraint(rule = EVOutVaporComposition)
def EVOutLiquidComposition(m):
    return m.EVOutLPMolarFrac['Oxygen'] == liquid_oxygen_composition(m.ircRebPressure, m.ircRebTemperature)
model.EVOutLiquidComposition = Constraint(rule = EVOutLiquidComposition)
def EVOutVaporPhaseSummation(m):
    return sum([m.EVOutVPMolarFrac[c] for c in m.Component])==1
model.EVOutVaporPhaseSummation = Constraint(rule = EVOutVaporPhaseSummation)
def EVOutLiquidPhaseSummation(m):
    return sum([m.EVOutLPMolarFrac[c] for c in m.Component])==1
model.EVOutLiquidPhaseSummation = Constraint(rule = EVOutLiquidPhaseSummation)
#--------------
print(LiquidPhaseEnthalpy(model.trayTemperature[1], model.trayPressure[1], model.liquidLeavingMolarFraction[1, 'Oxygen'],
                          model.liquidLeavingMolarFraction[1, 'Nitrogen']))