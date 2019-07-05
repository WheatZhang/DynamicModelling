from pyomo.environ import *

test_model = ConcreteModel()
test_model.Component = Set(initialize=['Oxygen', 'Nitrogen'])

#===================================
#
#      Process Parts
#
#===================================
from binary_fitting_result import vapor_oxygen_composition,liquid_oxygen_composition
from binary_fitting_result import vapor_nitrogen_enthalpy,vapor_oxygen_enthalpy
def VaporPhaseEnthalpy(temperature, pressure, oxygen, nitrogen):
	return vapor_nitrogen_enthalpy(pressure,temperature)*nitrogen+vapor_oxygen_enthalpy(pressure,temperature)*oxygen
from binary_fitting_result import liquid_nitrogen_enthalpy,liquid_oxygen_enthalpy
def LiquidPhaseEnthalpy(temperature, pressure, oxygen, nitrogen):
	return liquid_nitrogen_enthalpy(pressure,temperature)*nitrogen+liquid_oxygen_enthalpy(pressure,temperature)*oxygen

#===================================
#
#      Parameters & Sets
#
#===================================
#--------Feed---------
test_model.FeedMFlow = Param(initialize = 2000.000000)
test_model.FeedMFrac = Param(test_model.Component, initialize = {'Oxygen': 0.21, 'Nitrogen': 0.79})
test_model.FeedPressure = Param(initialize = 564.000000)
test_model.FeedVF = Param(initialize = 0.800000)
#--------Column---------
test_model.ColumnTrays = RangeSet(1, 10)
test_model.ColumnTopPressure = Param(initialize = 539.560000)
test_model.ColumnBtmPressure = Param(initialize = 564.000000)
#--------Sump---------
test_model.SumpLiqRho = Param(initialize = 1000.000000)
test_model.SumpSumpCSArea = Param(initialize = 6.000000)
#--------Condensor---------
test_model.CondensorRefluxRatio = Param(initialize = 0.930000)
#--------GNSplitter---------
test_model.GNSplitterOutARatio = Param(initialize = 0.587745)

#===================================
#
#         Variables
#
#===================================
#--------Feed---------
test_model.FeedTemp = Var()
test_model.FeedLiqMFrac = Var(test_model.Component, bounds=(0, 1))
test_model.FeedVapMFrac = Var(test_model.Component, bounds=(0, 1))
#--------Column---------
test_model.ColumnVapLvMFlow = Var(test_model.ColumnTrays, within=NonNegativeReals)
test_model.ColumnLiqLvMFlow = Var(test_model.ColumnTrays, within=NonNegativeReals)
test_model.ColumnTrayTemp = Var(test_model.ColumnTrays)
test_model.ColumnTrayPressure = Var(test_model.ColumnTrays)
test_model.ColumnLiqLvMFrac = Var(test_model.ColumnTrays,test_model.Component, bounds=(0, 1))
test_model.ColumnVapLvMFrac = Var(test_model.ColumnTrays,test_model.Component, bounds=(0, 1))
#--------Sump---------
test_model.SumpOutMFlow = Var(within=NonNegativeReals)
test_model.SumpHldpMFrac = Var(test_model.Component, bounds =(0,1))
#--------Condensor---------
test_model.CondensorRefMFlow = Var(within=NonNegativeReals)
test_model.CondensorPrdtMFlow = Var(within=NonNegativeReals)
test_model.CondensorMHeatOut = Var(within=NonNegativeReals)
test_model.CondensorTemp = Var(initialize = 0)
#--------Reboiler---------
test_model.ReboilerLiqLvMFlow = Var(within=NonNegativeReals)
test_model.ReboilerVapLvMFlow = Var(within=NonNegativeReals)
test_model.ReboilerTemp = Var()
test_model.ReboilerLiqLvMFrac = Var(test_model.Component, bounds=(0, 1))
test_model.ReboilerVapLvMFrac = Var(test_model.Component, bounds=(0, 1))
#--------GNSplitter---------
test_model.GNSplitterOutAMFlow = Var(within=NonNegativeReals)
test_model.GNSplitterOutBMFlow = Var(within=NonNegativeReals)

#===================================
#
#         Expressions
#
#===================================
#--------Feed Enthalpy---------
def FeedVapMEtlp(m):
	return VaporPhaseEnthalpy(m.FeedTemp, m.FeedPressure,m.FeedVapMFrac["Oxygen"],m.FeedVapMFrac["Nitrogen"])
test_model.FeedVapMEtlp = Expression(rule=FeedVapMEtlp)
def FeedLiqMEtlp(m):
	return LiquidPhaseEnthalpy(m.FeedTemp, m.FeedPressure,m.FeedLiqMFrac["Oxygen"],m.FeedLiqMFrac["Nitrogen"])
test_model.FeedLiqMEtlp = Expression(rule=FeedLiqMEtlp)
def FeedMEtlp(m):
	return m.FeedLiqMEtlp * (1-m.FeedVF)+m.FeedVapMEtlp * m.FeedVF
test_model.FeedMEtlp = Expression(rule=FeedMEtlp)
#--------Column Component Flowrate---------
def ColumnVapLvMCompFlow(m, tray, comp):
	return m.ColumnVapLvMFrac[tray, comp] * m.ColumnVapLvMFlow[tray]
test_model.ColumnVapLvMCompFlow = Expression(test_model.ColumnTrays, test_model.Component, rule=ColumnVapLvMCompFlow)
def ColumnLiqLvMCompFlow(m, tray, comp):
	return m.ColumnLiqLvMFrac[tray, comp] * m.ColumnLiqLvMFlow[tray]
test_model.ColumnLiqLvMCompFlow = Expression(test_model.ColumnTrays, test_model.Component, rule=ColumnLiqLvMCompFlow)
#--------Column Thermo and Enthalpy---------
def ColumnVapLvMEtlp(m,tray):
	return VaporPhaseEnthalpy(m.ColumnTrayTemp[tray], m.ColumnTrayPressure[tray],m.ColumnVapLvMFrac[tray,"Oxygen"],m.ColumnVapLvMFrac[tray,"Nitrogen"])
test_model.ColumnVapLvMEtlp = Expression(test_model.ColumnTrays,rule=ColumnVapLvMEtlp)
def ColumnLiqLvMEtlp(m,tray):
	return LiquidPhaseEnthalpy(m.ColumnTrayTemp[tray], m.ColumnTrayPressure[tray],m.ColumnLiqLvMFrac[tray,"Oxygen"],m.ColumnLiqLvMFrac[tray,"Nitrogen"])
test_model.ColumnLiqLvMEtlp = Expression(test_model.ColumnTrays,rule=ColumnLiqLvMEtlp)
#--------Condensor Enthalpy---------
def CondensorOutMEtlp(m):
	return LiquidPhaseEnthalpy(m.CondensorTemp, m.ColumnTrayPressure[10],m.ColumnVapLvMFrac[10,"Oxygen"],m.ColumnVapLvMFrac[10,"Nitrogen"])
test_model.CondensorOutMEtlp = Expression(rule=CondensorOutMEtlp)
#--------Reboiler Enthalpy---------
def ReboilerVapLvMEtlp(m):
	return VaporPhaseEnthalpy(m.ReboilerTemp, m.ColumnTrayPressure[1],m.ReboilerVapLvMFrac["Oxygen"],m.ReboilerVapLvMFrac["Nitrogen"])
test_model.ReboilerVapLvMEtlp = Expression(rule=ReboilerVapLvMEtlp)
def ReboilerLiqLvMEtlp(m):
	return LiquidPhaseEnthalpy(m.ReboilerTemp, m.ColumnTrayPressure[1],m.ReboilerLiqLvMFrac["Oxygen"],m.ReboilerLiqLvMFrac["Nitrogen"])
test_model.ReboilerLiqLvMEtlp = Expression(rule=ReboilerLiqLvMEtlp)

#===================================
#
#         Constraints
#
#===================================

#----------------------------------
#           Feed
#----------------------------------
#--------Feed Mass Balance---------
def FeedMassBlnc(m):
	return m.FeedVF * m.FeedVapMFrac['Oxygen'] + \
(1 - m.FeedVF)*m.FeedLiqMFrac['Oxygen'] - m.FeedMFrac['Oxygen'] == 0
test_model.FeedMassBlnc = Constraint(rule=FeedMassBlnc)
#--------Feed Phase Equilibrium---------
def FeedSelfVapFrac(m):
	return m.FeedVapMFrac["Oxygen"] == vapor_oxygen_composition(m.FeedPressure,m.FeedTemp)
test_model.FeedSelfVapFrac = Constraint(rule=FeedSelfVapFrac)
def FeedSelfLiqFrac(m):
	return m.FeedLiqMFrac["Oxygen"] == liquid_oxygen_composition(m.FeedPressure,m.FeedTemp)
test_model.FeedSelfLiqFrac = Constraint(rule=FeedSelfLiqFrac)
#--------Feed Summation---------
def FeedLiqSum(m):
	return sum([m.FeedLiqMFrac[c] for c in m.Component]) == 1
test_model.FeedLiqSum = Constraint(rule=FeedLiqSum)
def FeedVapSum(m):
	return sum([m.FeedVapMFrac[c] for c in m.Component]) == 1
test_model.FeedVapSum = Constraint(rule=FeedVapSum)

#----------------------------------
#           Column
#----------------------------------
#--------Column Mass Balance---------
def ColumnMassBlnc(m,tray, comp):
	if tray == 1:
		return (m.ColumnLiqLvMCompFlow[tray + 1, comp]- m.ColumnLiqLvMCompFlow[tray, comp] - m.ColumnVapLvMCompFlow[tray, comp]+m.FeedMFlow*m.FeedMFrac[comp])*0.001000 == 0
	elif tray == 10:
		return (m.CondensorRefMFlow*m.ColumnVapLvMFrac[10,comp] + m.ColumnVapLvMCompFlow[tray - 1, comp] - m.ColumnLiqLvMCompFlow[tray, comp] - m.ColumnVapLvMCompFlow[tray, comp])*0.001000 == 0
	else:
		return (m.ColumnLiqLvMCompFlow[tray + 1, comp] + m.ColumnVapLvMCompFlow[tray - 1, comp] - m.ColumnLiqLvMCompFlow[tray, comp] - m.ColumnVapLvMCompFlow[tray, comp])*0.001000 == 0
test_model.ColumnMassBlnc = Constraint(test_model.ColumnTrays, test_model.Component, rule=ColumnMassBlnc)
#--------Column Energy Balance---------
def ColumnEngBlnc(m,tray):
	if tray == 1:
		return (m.ColumnLiqLvMFlow[tray + 1] * m.ColumnLiqLvMEtlp[tray+1] \
		        - m.ColumnLiqLvMFlow[tray] * m.ColumnLiqLvMEtlp[tray] \
		        - m.ColumnVapLvMFlow[tray] * m.ColumnVapLvMEtlp[tray]\
		        +m.FeedMFlow*m.FeedMEtlp)*0.000010 == 0
	elif tray == 10:
		return (m.CondensorRefMFlow * m.CondensorOutMEtlp \
		        + m.ColumnVapLvMFlow[tray-1] * m.ColumnVapLvMEtlp[tray-1] \
		        - m.ColumnLiqLvMFlow[tray] * m.ColumnLiqLvMEtlp[tray] \
		        - m.ColumnVapLvMFlow[tray] * m.ColumnVapLvMEtlp[tray])*0.000010 == 0
	else:
		return (m.ColumnLiqLvMFlow[tray + 1] * m.ColumnLiqLvMEtlp[tray+1] \
		        + m.ColumnVapLvMFlow[tray-1] * m.ColumnVapLvMEtlp[tray-1] \
		        - m.ColumnLiqLvMFlow[tray] * m.ColumnLiqLvMEtlp[tray] \
		        - m.ColumnVapLvMFlow[tray] * m.ColumnVapLvMEtlp[tray])*0.000010 == 0
test_model.ColumnEngBlnc = Constraint(test_model.ColumnTrays,rule=ColumnEngBlnc)
#--------Column Phase Equilibrium & System Parts---------
def ColumnAllTraysVapFrac(m,tray):
	return m.ColumnVapLvMFrac[tray,"Oxygen"] == vapor_oxygen_composition(m.ColumnTrayPressure[tray],m.ColumnTrayTemp[tray])
test_model.ColumnAllTraysVapFrac = Constraint(test_model.ColumnTrays,rule=ColumnAllTraysVapFrac)
def ColumnAllTraysLiqFrac(m,tray):
	return m.ColumnLiqLvMFrac[tray,"Oxygen"] == liquid_oxygen_composition(m.ColumnTrayPressure[tray],m.ColumnTrayTemp[tray])
test_model.ColumnAllTraysLiqFrac = Constraint(test_model.ColumnTrays,rule=ColumnAllTraysLiqFrac)
#--------Column Summation---------
def ColumnLiqSum(m, tray):
	return sum([m.ColumnLiqLvMFrac[tray, c] for c in m.Component]) == 1
test_model.ColumnLiqSum = Constraint(test_model.ColumnTrays, rule=ColumnLiqSum)
def ColumnVapSum(m, tray):
	return sum([m.ColumnVapLvMFrac[tray, c] for c in m.Component]) == 1
test_model.ColumnVapSum = Constraint(test_model.ColumnTrays, rule=ColumnVapSum)
#--------Column Pressure Profile---------
def ColumnPProf(m, tray):
	return ((m.ColumnTopPressure-m.ColumnBtmPressure)/9*(tray-1)+m.ColumnBtmPressure - m.ColumnTrayPressure[tray])*0.010000 == 0
test_model.ColumnPProf = Constraint(test_model.ColumnTrays, rule=ColumnPProf)

#----------------------------------
#           Sump
#----------------------------------
#--------Sump Mass Balance---------
def SumpMassBlnc(m):
	return (m.ColumnLiqLvMFlow[1]-m.SumpOutMFlow)*0.001000==0
test_model.SumpMassBlnc = Constraint(rule=SumpMassBlnc)
def SumpHldpMFracSpec(m, comp):
	return m.SumpHldpMFrac[comp] - m.ColumnLiqLvMFrac[1,comp] == 0
test_model.SumpHldpMFracSpec = Constraint(test_model.Component, rule=SumpHldpMFracSpec)

#----------------------------------
#           Condensor
#----------------------------------
#--------Condensor Mass Balance---------
def CondensorMassBlnc(m):
	return (m.CondensorRefMFlow+m.CondensorPrdtMFlow-m.GNSplitterOutBMFlow)*0.001000==0
test_model.CondensorMassBlnc = Constraint(rule=CondensorMassBlnc)
def CondensorRefSpec(m):
	return (m.CondensorRefMFlow-m.GNSplitterOutBMFlow*m.CondensorRefluxRatio)*0.001000==0
test_model.CondensorRefSpec = Constraint(rule=CondensorRefSpec)
#--------Condensor Energy Balance---------
def CondensorEngBlnc(m):
	return (m.GNSplitterOutBMFlow*(m.ColumnVapLvMEtlp[10]-m.CondensorOutMEtlp)-m.CondensorMHeatOut)*0.000010==0
test_model.CondensorEngBlnc = Constraint(rule=CondensorEngBlnc)
#--------Condensor Bubble Point---------
def CondensorSelfBubTemp(m):
	return m.ColumnVapLvMFrac[10,"Oxygen"] == liquid_oxygen_composition(m.ColumnTrayPressure[10],m.CondensorTemp)
test_model.CondensorSelfBubTemp = Constraint(rule=CondensorSelfBubTemp)

#----------------------------------
#           Reboiler
#----------------------------------
#--------Reboiler Mass Balance---------
def ReboilerMassBlnc(m,comp):
	return (m.SumpOutMFlow * m.ColumnLiqLvMFrac[1,comp]-\
	    m.ReboilerLiqLvMFlow * m.ReboilerLiqLvMFrac[comp]-\
	    m.ReboilerVapLvMFlow * m.ReboilerVapLvMFrac[comp])*0.001000==0
test_model.ReboilerMassBlnc = Constraint(test_model.Component, rule=ReboilerMassBlnc)
#--------Reboiler Energy Balance---------
def ReboilerEngBlnc(m):
	return (m.SumpOutMFlow * m.ColumnLiqLvMEtlp[1]+m.CondensorMHeatOut-\
	    m.ReboilerLiqLvMFlow * m.ReboilerLiqLvMEtlp-\
	    m.ReboilerVapLvMFlow * m.ReboilerVapLvMEtlp)*0.000010==0
test_model.ReboilerEngBlnc = Constraint(rule=ReboilerEngBlnc)
#--------Reboiler Phase Equilibrium---------
def ReboilerHdlpVapFrac(m):
	return m.ReboilerVapLvMFrac["Oxygen"] == vapor_oxygen_composition(m.ColumnTrayPressure[1],m.ReboilerTemp)
test_model.ReboilerHdlpVapFrac = Constraint(rule=ReboilerHdlpVapFrac)
def ReboilerHdlpLiqFrac(m):
	return m.ReboilerLiqLvMFrac["Oxygen"] == liquid_oxygen_composition(m.ColumnTrayPressure[1],m.ReboilerTemp)
test_model.ReboilerHdlpLiqFrac = Constraint(rule=ReboilerHdlpLiqFrac)
#--------Reboiler Summation---------
def ReboilerLiqSum(m):
	return sum([m.ReboilerLiqLvMFrac[c] for c in m.Component]) == 1
test_model.ReboilerLiqSum = Constraint(rule=ReboilerLiqSum)
def ReboilerVapSum(m):
	return sum([m.ReboilerVapLvMFrac[c] for c in m.Component]) == 1
test_model.ReboilerVapSum = Constraint(rule=ReboilerVapSum)

#----------------------------------
#           GNSplitter
#----------------------------------
#--------GNSplitter Mass Balance---------
def GNSplitterOutASpec(m):
	return (m.GNSplitterOutAMFlow-m.ColumnVapLvMFlow[10]*m.GNSplitterOutARatio)*0.001000==0
test_model.GNSplitterOutASpec = Constraint(rule=GNSplitterOutASpec)
def GNSplitterOutBSpec(m):
	return (m.GNSplitterOutBMFlow-m.ColumnVapLvMFlow[10]*(1-m.GNSplitterOutARatio))*0.001000==0
test_model.GNSplitterOutBSpec = Constraint(rule=GNSplitterOutBSpec)
