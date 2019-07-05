from pyomo.environ import *
from pyomo.dae import *

test_model3 = ConcreteModel()
test_model3.Component = Set(initialize=['Oxygen', 'Nitrogen'])

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
test_model3.FeedMFlow = Param(initialize = 2000.000000)
test_model3.FeedMFrac = Param(test_model3.Component, initialize = {'Oxygen': 0.21, 'Nitrogen': 0.79})
test_model3.FeedPressure = Param(initialize = 564.000000)
test_model3.FeedVF = Param(initialize = 0.800000)
#--------Column---------
test_model3.ColumnTrays = RangeSet(1, 10)
test_model3.ColumnTopPressure = Param(initialize = 539.560000)
test_model3.ColumnBtmPressure = Param(initialize = 564.000000)
#--------RefFlow---------
test_model3.RefFlowMFlow = Param(initialize = 586.562970)
test_model3.RefFlowMFrac = Param(test_model3.Component, initialize = {'Nitrogen': 0.9514604305969551, 'Oxygen': 0.04853956940304498})
test_model3.RefFlowPressure = Param(initialize = 539.560000)
test_model3.RefFlowTemp = Param(initialize = -176.664000)

#===================================
#
#         Variables
#
#===================================
#--------Feed---------
test_model3.FeedTemp = Var()
test_model3.FeedLiqMFrac = Var(test_model3.Component, bounds=(0, 1))
test_model3.FeedVapMFrac = Var(test_model3.Component, bounds=(0, 1))
#--------Column---------
test_model3.ColumnVapLvMFlow = Var(test_model3.ColumnTrays, within=NonNegativeReals)
test_model3.ColumnLiqLvMFlow = Var(test_model3.ColumnTrays, within=NonNegativeReals)
test_model3.ColumnTrayTemp = Var(test_model3.ColumnTrays)
test_model3.ColumnTrayPressure = Var(test_model3.ColumnTrays)
test_model3.ColumnLiqLvMFrac = Var(test_model3.ColumnTrays,test_model3.Component, bounds=(0, 1))
test_model3.ColumnVapLvMFrac = Var(test_model3.ColumnTrays,test_model3.Component, bounds=(0, 1))

#===================================
#
#         Expressions
#
#===================================
#--------Feed Enthalpy---------
def FeedVapMEtlp(m):
	return VaporPhaseEnthalpy(m.FeedTemp, m.FeedPressure,m.FeedVapMFrac["Oxygen"],m.FeedVapMFrac["Nitrogen"])
test_model3.FeedVapMEtlp = Expression(rule=FeedVapMEtlp)
def FeedLiqMEtlp(m):
	return LiquidPhaseEnthalpy(m.FeedTemp, m.FeedPressure,m.FeedLiqMFrac["Oxygen"],m.FeedLiqMFrac["Nitrogen"])
test_model3.FeedLiqMEtlp = Expression(rule=FeedLiqMEtlp)
def FeedMEtlp(m):
	return m.FeedLiqMEtlp * (1-m.FeedVF)+m.FeedVapMEtlp * m.FeedVF
test_model3.FeedMEtlp = Expression(rule=FeedMEtlp)
#--------Column Component Flowrate---------
def ColumnVapLvMCompFlow(m, tray, comp):
	return m.ColumnVapLvMFrac[tray, comp] * m.ColumnVapLvMFlow[tray]
test_model3.ColumnVapLvMCompFlow = Expression(test_model3.ColumnTrays, test_model3.Component, rule=ColumnVapLvMCompFlow)
def ColumnLiqLvMCompFlow(m, tray, comp):
	return m.ColumnLiqLvMFrac[tray, comp] * m.ColumnLiqLvMFlow[tray]
test_model3.ColumnLiqLvMCompFlow = Expression(test_model3.ColumnTrays, test_model3.Component, rule=ColumnLiqLvMCompFlow)
#--------Column Enthalpy---------
def ColumnVapLvMEtlp(m,tray):
	return VaporPhaseEnthalpy(m.ColumnTrayTemp[tray], m.ColumnTrayPressure[tray],m.ColumnVapLvMFrac[tray,"Oxygen"],m.ColumnVapLvMFrac[tray,"Nitrogen"])
test_model3.ColumnVapLvMEtlp = Expression(test_model3.ColumnTrays,rule=ColumnVapLvMEtlp)
def ColumnLiqLvMEtlp(m,tray):
	return LiquidPhaseEnthalpy(m.ColumnTrayTemp[tray], m.ColumnTrayPressure[tray],m.ColumnLiqLvMFrac[tray,"Oxygen"],m.ColumnLiqLvMFrac[tray,"Nitrogen"])
test_model3.ColumnLiqLvMEtlp = Expression(test_model3.ColumnTrays,rule=ColumnLiqLvMEtlp)
#--------RefFlow Enthalpy---------
def RefFlowMEtlp(m):
	return LiquidPhaseEnthalpy(m.RefFlowTemp, m.RefFlowPressure,m.RefFlowMFrac["Oxygen"],m.RefFlowMFrac["Nitrogen"])
test_model3.RefFlowMEtlp = Expression(rule=RefFlowMEtlp)

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
test_model3.FeedMassBlnc = Constraint(rule=FeedMassBlnc)
#--------Feed Phase Equilibrium---------
def FeedThermCompVap(m):
	return m.FeedVapMFrac["Oxygen"] == vapor_oxygen_composition(m.FeedPressure,m.FeedTemp)
test_model3.FeedThermCompVap = Constraint(rule=FeedThermCompVap)
def FeedThermCompLiq(m):
	return m.FeedLiqMFrac["Oxygen"] == liquid_oxygen_composition(m.FeedPressure,m.FeedTemp)
test_model3.FeedThermCompLiq = Constraint(rule=FeedThermCompLiq)
#--------Feed Summation---------
def FeedLiqSum(m):
	return sum([m.FeedLiqMFrac[c] for c in m.Component]) == 1
test_model3.FeedLiqSum = Constraint(rule=FeedLiqSum)
def FeedVapSum(m):
	return sum([m.FeedVapMFrac[c] for c in m.Component]) == 1
test_model3.FeedVapSum = Constraint(rule=FeedVapSum)

#----------------------------------
#           Column
#----------------------------------
#--------Column Mass Balance---------
def ColumnMassBlnc(m,tray, comp):
	if tray == 1:
		return (m.ColumnLiqLvMCompFlow[tray + 1, comp]- m.ColumnLiqLvMCompFlow[tray, comp] - m.ColumnVapLvMCompFlow[tray, comp]+m.FeedMFlow*m.FeedMFrac[comp])*0.001000 == 0
	elif tray == 10:
		return (m.RefFlowMFlow*m.RefFlowMFrac[comp] + m.ColumnVapLvMCompFlow[tray - 1, comp] - m.ColumnLiqLvMCompFlow[tray, comp] - m.ColumnVapLvMCompFlow[tray, comp])*0.001000 == 0
	else:
		return (m.ColumnLiqLvMCompFlow[tray + 1, comp] + m.ColumnVapLvMCompFlow[tray - 1, comp] - m.ColumnLiqLvMCompFlow[tray, comp] - m.ColumnVapLvMCompFlow[tray, comp])*0.001000 == 0
test_model3.ColumnMassBlnc = Constraint(test_model3.ColumnTrays, test_model3.Component, rule=ColumnMassBlnc)
#--------Column Energy Balance---------
def ColumnEngBlnc(m,tray):
	if tray == 1:
		return (m.ColumnLiqLvMFlow[tray + 1] * m.ColumnLiqLvMEtlp[tray+1] \
		        - m.ColumnLiqLvMFlow[tray] * m.ColumnLiqLvMEtlp[tray] \
		        - m.ColumnVapLvMFlow[tray] * m.ColumnVapLvMEtlp[tray]\
		        +m.FeedMFlow*m.FeedMEtlp)*0.000010 == 0
	elif tray == 10:
		return (m.RefFlowMFlow * m.RefFlowMEtlp \
		        + m.ColumnVapLvMFlow[tray-1] * m.ColumnVapLvMEtlp[tray-1] \
		        - m.ColumnLiqLvMFlow[tray] * m.ColumnLiqLvMEtlp[tray] \
		        - m.ColumnVapLvMFlow[tray] * m.ColumnVapLvMEtlp[tray])*0.000010 == 0
	else:
		return (m.ColumnLiqLvMFlow[tray + 1] * m.ColumnLiqLvMEtlp[tray+1] \
		        + m.ColumnVapLvMFlow[tray-1] * m.ColumnVapLvMEtlp[tray-1] \
		        - m.ColumnLiqLvMFlow[tray] * m.ColumnLiqLvMEtlp[tray] \
		        - m.ColumnVapLvMFlow[tray] * m.ColumnVapLvMEtlp[tray])*0.000010 == 0
test_model3.ColumnEngBlnc = Constraint(test_model3.ColumnTrays,rule=ColumnEngBlnc)
#--------Column Phase Equilibrium---------
def ColumnThermCompVap(m,tray):
	return m.ColumnVapLvMFrac[tray,"Oxygen"] == vapor_oxygen_composition(m.ColumnTrayPressure[tray],m.ColumnTrayTemp[tray])
test_model3.ColumnThermCompVap = Constraint(test_model3.ColumnTrays,rule=ColumnThermCompVap)
def ColumnThermCompLiq(m,tray):
	return m.ColumnLiqLvMFrac[tray,"Oxygen"] == liquid_oxygen_composition(m.ColumnTrayPressure[tray],m.ColumnTrayTemp[tray])
test_model3.ColumnThermCompLiq = Constraint(test_model3.ColumnTrays,rule=ColumnThermCompLiq)
#--------Column Summation---------
def ColumnLiqSum(m, tray):
	return sum([m.ColumnLiqLvMFrac[tray, c] for c in m.Component]) == 1
test_model3.ColumnLiqSum = Constraint(test_model3.ColumnTrays, rule=ColumnLiqSum)
def ColumnVapSum(m, tray):
	return sum([m.ColumnVapLvMFrac[tray, c] for c in m.Component]) == 1
test_model3.ColumnVapSum = Constraint(test_model3.ColumnTrays, rule=ColumnVapSum)
#--------Column Pressure Profile---------
def ColumnPProf(m, tray):
	return ((m.ColumnTopPressure-m.ColumnBtmPressure)/9*(tray-1)+m.ColumnBtmPressure - m.ColumnTrayPressure[tray])*0.010000 == 0
test_model3.ColumnPProf = Constraint(test_model3.ColumnTrays, rule=ColumnPProf)

#----------------------------------
#           RefFlow
#----------------------------------
