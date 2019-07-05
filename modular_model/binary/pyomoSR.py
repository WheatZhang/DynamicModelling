from pyomo.environ import *
from pyomo.dae import *
import ModularTask

test_model = ConcreteModel()
test_model.Component = Set(initialize=['Oxygen', 'Nitrogen'])

#===================================
#
#      Modelling Time
#
#===================================
Discretizer = ModularTask.RuntimeTools.TimeDiscretizer(nfe=10, ncp=3, bounds=(0, 10))
Discretizer.set_fe_point(None)
Discretizer.initialize_time(test_model, 'Time')
pe_list = Discretizer.get_para_time()
test_model.ParaTime = Set(initialize=pe_list)

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
from binary_fitting_gradient import liquid_nitrogen_enthalpy_DT,liquid_oxygen_enthalpy_DT,liquid_oxygen_composition_DP,liquid_oxygen_composition_DT
def LiquidPhaseEnthalpyPartialT(temperature, pressure, oxygen, nitrogen):
	return liquid_nitrogen_enthalpy_DT(pressure, temperature) * nitrogen + liquid_oxygen_enthalpy_DT(pressure,temperature) * oxygen

#===================================
#
#      Parameters & Sets
#
#===================================
#--------Feed---------
test_model.FeedMFlow = Param(test_model.ParaTime, initialize = 2100.000000)
dict = {}
for i in test_model.ParaTime.value:
	dict[i,"Oxygen"] = 0.210000
	dict[i,"Nitrogen"] = 0.790000
test_model.FeedMFrac = Param(test_model.ParaTime, test_model.Component, initialize = dict)
test_model.FeedPressure = Param(test_model.ParaTime, initialize = 564.000000)
test_model.FeedVF = Param(test_model.ParaTime, initialize = 0.800000)
#--------Column---------
test_model.ColumnTrays = RangeSet(1, 10)
test_model.ColumnTopPressure = Param(initialize = 539.560000)
test_model.ColumnBtmPressure = Param(test_model.ParaTime, initialize = 564.000000)
test_model.ColumnHydrlParak = Param(initialize=10.000000)
#--------Condensor---------
test_model.CondensorRefluxRatio = Param(test_model.ParaTime, initialize = 0.930000)
#--------GNSplitter---------
test_model.GNSplitterOutARatio = Param(test_model.ParaTime, initialize = 0.587745)

#===================================
#
#         Variables
#
#===================================
#--------Feed---------
test_model.FeedTemp = Var(test_model.Time)
test_model.FeedLiqMFrac = Var(test_model.Time,test_model.Component, bounds=(0, 1))
test_model.FeedVapMFrac = Var(test_model.Time,test_model.Component, bounds=(0, 1))
#--------Column---------
test_model.ColumnVapLvMFlow = Var(test_model.Time, test_model.ColumnTrays, within=NonNegativeReals)
test_model.ColumnLiqLvMFlow = Var(test_model.Time, test_model.ColumnTrays, within=NonNegativeReals)
test_model.ColumnTrayTemp = Var(test_model.Time, test_model.ColumnTrays)
test_model.ColumnTrayPressure = Var(test_model.Time, test_model.ColumnTrays)
test_model.ColumnLiqLvMFrac = Var(test_model.Time,test_model.ColumnTrays,test_model.Component, bounds=(0, 1))
test_model.ColumnVapLvMFrac = Var(test_model.Time,test_model.ColumnTrays,test_model.Component, bounds=(0, 1))
#--------Column's var in differential equations---------
test_model.ColumnTrayMHldp = Var(test_model.Time, test_model.ColumnTrays, within=NonNegativeReals)
test_model.ColumnDtTrayMHldp = DerivativeVar(test_model.ColumnTrayMHldp)
test_model.ColumnTrayMCompHldp = Var(test_model.Time, test_model.ColumnTrays, test_model.Component, within=NonNegativeReals)
test_model.ColumnDtTrayMCompHldp = DerivativeVar(test_model.ColumnTrayMCompHldp)
test_model.ColumnDtTrayMEtlpHldp = Var(test_model.Time, test_model.ColumnTrays)
test_model.ColumnDtTrayPressure = DerivativeVar(test_model.ColumnTrayPressure)
#--------Condensor---------
test_model.CondensorRefMFlow = Var(test_model.Time, within=NonNegativeReals)
test_model.CondensorPrdtMFlow = Var(test_model.Time, within=NonNegativeReals)
test_model.CondensorMHeatOut = Var(test_model.Time, within=NonNegativeReals)
test_model.CondensorTemp = Var(test_model.Time,)
#--------Reboiler---------
test_model.ReboilerLiqLvMFlow = Var(test_model.Time, within=NonNegativeReals)
test_model.ReboilerVapLvMFlow = Var(test_model.Time, within=NonNegativeReals)
test_model.ReboilerTemp = Var(test_model.Time)
test_model.ReboilerLiqLvMFrac = Var(test_model.Time,test_model.Component, bounds=(0, 1))
test_model.ReboilerVapLvMFrac = Var(test_model.Time,test_model.Component, bounds=(0, 1))
#--------GNSplitter---------
test_model.GNSplitterOutAMFlow = Var(test_model.Time, within=NonNegativeReals)
test_model.GNSplitterOutBMFlow = Var(test_model.Time, within=NonNegativeReals)

#===================================
#
#         Expressions
#
#===================================
#--------Feed Enthalpy---------
def FeedVapMEtlp(m,time):
	return VaporPhaseEnthalpy(m.FeedTemp[time], m.FeedPressure[time],m.FeedVapMFrac[time,"Oxygen"],m.FeedVapMFrac[time,"Nitrogen"])
test_model.FeedVapMEtlp = Expression(test_model.Time,rule=FeedVapMEtlp)
def FeedLiqMEtlp(m,time):
	return LiquidPhaseEnthalpy(m.FeedTemp[time], m.FeedPressure[time],m.FeedLiqMFrac[time,"Oxygen"],m.FeedLiqMFrac[time,"Nitrogen"])
test_model.FeedLiqMEtlp = Expression(test_model.Time,rule=FeedLiqMEtlp)
def FeedMEtlp(m, time):
	return m.FeedLiqMEtlp[time] * (1-m.FeedVF[time])+m.FeedVapMEtlp[time] * m.FeedVF[time]
test_model.FeedMEtlp = Expression(test_model.Time, rule=FeedMEtlp)
#--------Column Component Flowrate---------
def ColumnVapLvMCompFlow(m, time, tray, comp):
	return m.ColumnVapLvMFrac[time, tray, comp] * m.ColumnVapLvMFlow[time, tray]
test_model.ColumnVapLvMCompFlow = Expression(test_model.Time, test_model.ColumnTrays, test_model.Component, rule=ColumnVapLvMCompFlow)
def ColumnLiqLvMCompFlow(m, time, tray, comp):
	return m.ColumnLiqLvMFrac[time, tray, comp] * m.ColumnLiqLvMFlow[time, tray]
test_model.ColumnLiqLvMCompFlow = Expression(test_model.Time, test_model.ColumnTrays, test_model.Component, rule=ColumnLiqLvMCompFlow)
#--------Column Thermo and Enthalpy---------
def ColumnVapLvMEtlp(m,time,tray):
	return VaporPhaseEnthalpy(m.ColumnTrayTemp[time,tray], m.ColumnTrayPressure[time,tray],m.ColumnVapLvMFrac[time,tray,"Oxygen"],m.ColumnVapLvMFrac[time,tray,"Nitrogen"])
test_model.ColumnVapLvMEtlp = Expression(test_model.Time,test_model.ColumnTrays,rule=ColumnVapLvMEtlp)
def ColumnLiqLvMEtlp(m,time,tray):
	return LiquidPhaseEnthalpy(m.ColumnTrayTemp[time,tray], m.ColumnTrayPressure[time,tray],m.ColumnLiqLvMFrac[time,tray,"Oxygen"],m.ColumnLiqLvMFrac[time,tray,"Nitrogen"])
test_model.ColumnLiqLvMEtlp = Expression(test_model.Time,test_model.ColumnTrays,rule=ColumnLiqLvMEtlp)
#--------Column Dynamic Related---------
def ColumnDtLiqLvMFrac(m, time, tray, comp):
	return (m.ColumnDtTrayMCompHldp[time, tray, comp] - m.ColumnLiqLvMFrac[time, tray, comp] *\
	      m.ColumnDtTrayMHldp[time, tray]) / m.ColumnTrayMHldp[time, tray]
test_model.ColumnDtLiqLvMFrac = Expression(test_model.Time, test_model.ColumnTrays, test_model.Component, rule=ColumnDtLiqLvMFrac)
def ColumnPTTrayMEtlpHldp(m,time,tray):
	return LiquidPhaseEnthalpyPartialT(m.ColumnTrayTemp[time,tray], m.ColumnTrayPressure[time,tray],m.ColumnLiqLvMFrac[time,tray,"Oxygen"],m.ColumnLiqLvMFrac[time,tray,"Nitrogen"]) 
test_model.ColumnPTTrayMEtlpHldp = Expression(test_model.Time,test_model.ColumnTrays,rule=ColumnPTTrayMEtlpHldp)
def ColumnPxTrayMEtlpHldp(m,time,tray, comp):
	if comp == 'Oxygen':
		return liquid_oxygen_enthalpy(m.ColumnTrayPressure[time,tray], m.ColumnTrayTemp[time,tray])
	elif comp == 'Nitrogen':
		return liquid_nitrogen_enthalpy(m.ColumnTrayPressure[time,tray], m.ColumnTrayTemp[time,tray])
test_model.ColumnPxTrayMEtlpHldp = Expression(test_model.Time,test_model.ColumnTrays,test_model.Component, rule=ColumnPxTrayMEtlpHldp)
def ColumnDtTrayTemp(m,time,tray):
	return (m.ColumnDtLiqLvMFrac[time,tray,"Oxygen"] - liquid_oxygen_composition_DP(m.ColumnTrayPressure[time,tray],m.ColumnTrayTemp[time,tray]) *m.ColumnDtTrayPressure[time,tray]) / liquid_oxygen_composition_DT(m.ColumnTrayPressure[time,tray], m.ColumnTrayTemp[time,tray])
test_model.ColumnDtTrayTemp = Expression(test_model.Time,test_model.ColumnTrays,rule=ColumnDtTrayTemp)
#--------Condensor Enthalpy---------
def CondensorOutMEtlp(m,time):
	return LiquidPhaseEnthalpy(m.CondensorTemp[time], m.ColumnTrayPressure[time,10],m.ColumnVapLvMFrac[time,10,"Oxygen"],m.ColumnVapLvMFrac[time,10,"Nitrogen"])
test_model.CondensorOutMEtlp = Expression(test_model.Time,rule=CondensorOutMEtlp)
#--------Reboiler Enthalpy---------
def ReboilerVapLvMEtlp(m,time):
	return VaporPhaseEnthalpy(m.ReboilerTemp[time], m.ColumnTrayPressure[time,1],m.ReboilerVapLvMFrac[time,"Oxygen"],m.ReboilerVapLvMFrac[time,"Nitrogen"])
test_model.ReboilerVapLvMEtlp = Expression(test_model.Time,rule=ReboilerVapLvMEtlp)
def ReboilerLiqLvMEtlp(m,time):
	return LiquidPhaseEnthalpy(m.ReboilerTemp[time], m.ColumnTrayPressure[time,1],m.ReboilerLiqLvMFrac[time,"Oxygen"],m.ReboilerLiqLvMFrac[time,"Nitrogen"])
test_model.ReboilerLiqLvMEtlp = Expression(test_model.Time,rule=ReboilerLiqLvMEtlp)

#===================================
#
#         Constraints
#
#===================================

#----------------------------------
#           Feed
#----------------------------------
#--------Feed Mass Balance---------
def FeedMassBlnc(m, time):
	return m.FeedVF[time] * m.FeedVapMFrac[time, 'Oxygen'] + \
(1 - m.FeedVF[time])*m.FeedLiqMFrac[time, 'Oxygen'] - m.FeedMFrac[time, 'Oxygen'] == 0
test_model.FeedMassBlnc = Constraint(test_model.Time, rule=FeedMassBlnc)
#--------Feed Phase Equilibrium---------
def FeedThermCompVap(m,time):
	return m.FeedVapMFrac[time,"Oxygen"] == vapor_oxygen_composition(m.FeedPressure[time],m.FeedTemp[time])
test_model.FeedThermCompVap = Constraint(test_model.Time,rule=FeedThermCompVap)
def FeedThermCompLiq(m,time):
	return m.FeedLiqMFrac[time,"Oxygen"] == liquid_oxygen_composition(m.FeedPressure[time],m.FeedTemp[time])
test_model.FeedThermCompLiq = Constraint(test_model.Time,rule=FeedThermCompLiq)
#--------Feed Summation---------
def FeedLiqSum(m, time):
	return sum([m.FeedLiqMFrac[time, c] for c in m.Component]) == 1
test_model.FeedLiqSum = Constraint(test_model.Time, rule=FeedLiqSum)
def FeedVapSum(m, time):
	return sum([m.FeedVapMFrac[time, c] for c in m.Component]) == 1
test_model.FeedVapSum = Constraint(test_model.Time, rule=FeedVapSum)

#----------------------------------
#           Column
#----------------------------------
#--------Column Mass Balance---------
def ColumnMassBlnc(m,time, tray, comp):
	if tray == 1:
		return (m.ColumnLiqLvMCompFlow[time, tray + 1, comp]- m.ColumnLiqLvMCompFlow[time, tray, comp] - m.ColumnVapLvMCompFlow[time, tray, comp]+m.FeedMFlow[time]*m.FeedMFrac[time, comp]-m.ColumnDtTrayMCompHldp[time,tray,comp])*0.001000 == 0
	elif tray == 10:
		return (m.CondensorRefMFlow[time]*m.ColumnVapLvMFrac[time,10, comp] + m.ColumnVapLvMCompFlow[time, tray - 1, comp] - m.ColumnLiqLvMCompFlow[time, tray, comp] - m.ColumnVapLvMCompFlow[time, tray, comp]-m.ColumnDtTrayMCompHldp[time,tray,comp])*0.001000 == 0
	else:
		return (m.ColumnLiqLvMCompFlow[time, tray + 1, comp] + m.ColumnVapLvMCompFlow[time, tray - 1, comp] - m.ColumnLiqLvMCompFlow[time, tray, comp] - m.ColumnVapLvMCompFlow[time, tray, comp]-m.ColumnDtTrayMCompHldp[time,tray,comp])*0.001000 == 0
test_model.ColumnMassBlnc = Constraint(test_model.Time, test_model.ColumnTrays, test_model.Component, rule=ColumnMassBlnc)
def ColumnMCompHldpEqu(m, time, tray, comp):
	return (m.ColumnTrayMCompHldp[time, tray, comp] - m.ColumnTrayMHldp[time, tray] * m.ColumnLiqLvMFrac[time, tray, comp]) * 1e-2 == 0
test_model.ColumnMCompHldpEqu = Constraint(test_model.Time, test_model.ColumnTrays, test_model.Component, rule=ColumnMCompHldpEqu)
#--------Column Energy Balance---------
def ColumnEngBlnc(m,time,tray):
	if tray == 1:
		return (m.ColumnLiqLvMFlow[time,tray + 1] * m.ColumnLiqLvMEtlp[time,tray+1] \
		        - m.ColumnLiqLvMFlow[time,tray] * m.ColumnLiqLvMEtlp[time,tray] \
		        - m.ColumnVapLvMFlow[time,tray] * m.ColumnVapLvMEtlp[time,tray]\
		        +m.FeedMFlow[time]*m.FeedMEtlp[time]-m.ColumnDtTrayMEtlpHldp[time,tray])*0.000010 == 0
	elif tray == 10:
		return (m.CondensorRefMFlow[time] * m.CondensorOutMEtlp[time] \
		        + m.ColumnVapLvMFlow[time,tray-1] * m.ColumnVapLvMEtlp[time,tray-1] \
		        - m.ColumnLiqLvMFlow[time,tray] * m.ColumnLiqLvMEtlp[time,tray] \
		        - m.ColumnVapLvMFlow[time,tray] * m.ColumnVapLvMEtlp[time,tray]-m.ColumnDtTrayMEtlpHldp[time,tray])*0.000010 == 0
	else:
		return (m.ColumnLiqLvMFlow[time,tray + 1] * m.ColumnLiqLvMEtlp[time,tray+1] \
		        + m.ColumnVapLvMFlow[time,tray-1] * m.ColumnVapLvMEtlp[time,tray-1] \
		        - m.ColumnLiqLvMFlow[time,tray] * m.ColumnLiqLvMEtlp[time,tray] \
		        - m.ColumnVapLvMFlow[time,tray] * m.ColumnVapLvMEtlp[time,tray] \
		        - m.ColumnDtTrayMEtlpHldp[time,tray])*0.000010 == 0
test_model.ColumnEngBlnc = Constraint(test_model.Time, test_model.ColumnTrays,rule=ColumnEngBlnc)
def ColumnMEtlpHldpEqu(m, time, tray):
	return (m.ColumnTrayMHldp[time, tray] * (m.ColumnPTTrayMEtlpHldp[time, tray] * m.ColumnDtTrayTemp[time, tray] + \
	      sum([m.ColumnPxTrayMEtlpHldp[time, tray, c] * m.ColumnDtLiqLvMFrac[time, tray, c] for c in m.Component])) + \
	      m.ColumnLiqLvMEtlp[time, tray] * m.ColumnDtTrayMHldp[time, tray] - m.ColumnDtTrayMEtlpHldp[time, tray]) * 1e-2 == 0
test_model.ColumnMEtlpHldpEqu = Constraint(test_model.Time, test_model.ColumnTrays, rule=ColumnMEtlpHldpEqu)
#--------Column Phase Equilibrium & System Parts---------
def ColumnThermCompVap(m,time,tray):
	return m.ColumnVapLvMFrac[time,tray,"Oxygen"] == vapor_oxygen_composition(m.ColumnTrayPressure[time,tray],m.ColumnTrayTemp[time,tray])
test_model.ColumnThermCompVap = Constraint(test_model.Time,test_model.ColumnTrays,rule=ColumnThermCompVap)
def ColumnThermCompLiq(m,time,tray):
	return m.ColumnLiqLvMFrac[time,tray,"Oxygen"] == liquid_oxygen_composition(m.ColumnTrayPressure[time,tray],m.ColumnTrayTemp[time,tray])
test_model.ColumnThermCompLiq = Constraint(test_model.Time,test_model.ColumnTrays,rule=ColumnThermCompLiq)
#--------Column Hydraulics---------
def ColumnHydrlSimp(m,time,tray):
	return (m.ColumnLiqLvMFlow[time,tray] - m.ColumnHydrlParak*m.ColumnTrayMHldp[time,tray])*0.001000 == 0
test_model.ColumnHydrlSimp = Constraint(test_model.Time,test_model.ColumnTrays,rule=ColumnHydrlSimp)
#--------Column Summation---------
def ColumnLiqSum(m,time, tray):
	return sum([m.ColumnLiqLvMFrac[time, tray, c] for c in m.Component]) == 1
test_model.ColumnLiqSum = Constraint(test_model.Time, test_model.ColumnTrays, rule=ColumnLiqSum)
def ColumnVapSum(m,time, tray):
	return sum([m.ColumnVapLvMFrac[time, tray, c] for c in m.Component]) == 1
test_model.ColumnVapSum = Constraint(test_model.Time, test_model.ColumnTrays, rule=ColumnVapSum)
#--------Column Pressure Profile---------
def ColumnPProf(m, time, tray):
	return ((m.ColumnTopPressure-m.ColumnBtmPressure[time])/9*(tray-1)+m.ColumnBtmPressure[time] - m.ColumnTrayPressure[time, tray])*0.010000 == 0
test_model.ColumnPProf = Constraint(test_model.Time, test_model.ColumnTrays, rule=ColumnPProf)
#--------Column Integration Initial Condition---------
def ColumnICTrayMHldp(m):
	yield m.ColumnTrayMHldp[0, 1] == 104.329224
	yield m.ColumnTrayMHldp[0, 2] == 64.278815
	yield m.ColumnTrayMHldp[0, 3] == 64.193201
	yield m.ColumnTrayMHldp[0, 4] == 64.060577
	yield m.ColumnTrayMHldp[0, 5] == 63.860493
	yield m.ColumnTrayMHldp[0, 6] == 63.564832
	yield m.ColumnTrayMHldp[0, 7] == 63.137532
	yield m.ColumnTrayMHldp[0, 8] == 62.537492
	yield m.ColumnTrayMHldp[0, 9] == 61.727542
	yield m.ColumnTrayMHldp[0, 10] == 60.691416
test_model.ColumnICTrayMHldp = ConstraintList(rule=ColumnICTrayMHldp)
def ColumnICTrayMCompHldp(m):
	yield m.ColumnTrayMCompHldp[0, 1, 'Oxygen'] == 36.700746
	yield m.ColumnTrayMCompHldp[0, 2, 'Oxygen'] == 22.567986
	yield m.ColumnTrayMCompHldp[0, 3, 'Oxygen'] == 22.374393
	yield m.ColumnTrayMCompHldp[0, 4, 'Oxygen'] == 21.993554
	yield m.ColumnTrayMCompHldp[0, 5, 'Oxygen'] == 21.343238
	yield m.ColumnTrayMCompHldp[0, 6, 'Oxygen'] == 20.307010
	yield m.ColumnTrayMCompHldp[0, 7, 'Oxygen'] == 18.728308
	yield m.ColumnTrayMCompHldp[0, 8, 'Oxygen'] == 16.413406
	yield m.ColumnTrayMCompHldp[0, 9, 'Oxygen'] == 13.154986
	yield m.ColumnTrayMCompHldp[0, 10, 'Oxygen'] == 8.789893
test_model.ColumnICTrayMCompHldp = ConstraintList(rule=ColumnICTrayMCompHldp)
def ColumnICDtTrayMHldp(m):
	yield m.ColumnDtTrayMHldp[0, 1] == 0.000000
	yield m.ColumnDtTrayMHldp[0, 2] == 0.000000
	yield m.ColumnDtTrayMHldp[0, 3] == 0.000000
	yield m.ColumnDtTrayMHldp[0, 4] == 0.000000
	yield m.ColumnDtTrayMHldp[0, 5] == 0.000000
	yield m.ColumnDtTrayMHldp[0, 6] == 0.000000
	yield m.ColumnDtTrayMHldp[0, 7] == 0.000000
	yield m.ColumnDtTrayMHldp[0, 8] == 0.000000
	yield m.ColumnDtTrayMHldp[0, 9] == 0.000000
	yield m.ColumnDtTrayMHldp[0, 10] == 0.000000
test_model.ColumnICDtTrayMHldp = ConstraintList(rule=ColumnICDtTrayMHldp)
def ColumnICDtTrayMEtlpHldp(m):
	yield m.ColumnDtTrayMEtlpHldp[0, 1] == 0.000000
	yield m.ColumnDtTrayMEtlpHldp[0, 2] == 0.000000
	yield m.ColumnDtTrayMEtlpHldp[0, 3] == 0.000000
	yield m.ColumnDtTrayMEtlpHldp[0, 4] == 0.000000
	yield m.ColumnDtTrayMEtlpHldp[0, 5] == 0.000000
	yield m.ColumnDtTrayMEtlpHldp[0, 6] == 0.000000
	yield m.ColumnDtTrayMEtlpHldp[0, 7] == 0.000000
	yield m.ColumnDtTrayMEtlpHldp[0, 8] == 0.000000
	yield m.ColumnDtTrayMEtlpHldp[0, 9] == 0.000000
	yield m.ColumnDtTrayMEtlpHldp[0, 10] == 0.000000
test_model.ColumnICDtTrayMEtlpHldp = ConstraintList(rule=ColumnICDtTrayMEtlpHldp)

#----------------------------------
#           Condensor
#----------------------------------
#--------Condensor Mass Balance---------
def CondensorMassBlnc(m,time):
	return (m.CondensorRefMFlow[time]+m.CondensorPrdtMFlow[time]-m.GNSplitterOutBMFlow[time])*0.001000==0
test_model.CondensorMassBlnc = Constraint(test_model.Time, rule=CondensorMassBlnc)
def CondensorRefSpec(m,time):
	return (m.CondensorRefMFlow[time]-m.GNSplitterOutBMFlow[time]*m.CondensorRefluxRatio[time])*0.001000==0
test_model.CondensorRefSpec = Constraint(test_model.Time, rule=CondensorRefSpec)
#--------Condensor Energy Balance---------
def CondensorEngBlnc(m,time):
	return (m.GNSplitterOutBMFlow[time]*(m.ColumnVapLvMEtlp[time,10]-m.CondensorOutMEtlp[time])-m.CondensorMHeatOut[time])*0.000010==0
test_model.CondensorEngBlnc = Constraint(test_model.Time, rule=CondensorEngBlnc)
#--------Condensor Bubble Point---------
def CondensorTempBubTemp(m,time):
	return m.ColumnVapLvMFrac[time,10,"Oxygen"] == liquid_oxygen_composition(m.ColumnTrayPressure[time,10],m.CondensorTemp[time])
test_model.CondensorTempBubTemp = Constraint(test_model.Time,rule=CondensorTempBubTemp)

#----------------------------------
#           Reboiler
#----------------------------------
#--------Reboiler Mass Balance---------
def ReboilerMassBlnc(m,time,comp):
	return (m.ColumnLiqLvMFlow[time,1] * m.ColumnLiqLvMFrac[time,1,comp]-\
	    m.ReboilerLiqLvMFlow[time] * m.ReboilerLiqLvMFrac[time,comp]-\
	    m.ReboilerVapLvMFlow[time] * m.ReboilerVapLvMFrac[time,comp])*0.001000==0
test_model.ReboilerMassBlnc = Constraint(test_model.Time, test_model.Component, rule=ReboilerMassBlnc)
#--------Reboiler Energy Balance---------
def ReboilerEngBlnc(m,time):
	return (m.ColumnLiqLvMFlow[time,1] * m.ColumnLiqLvMEtlp[time,1]+m.CondensorMHeatOut[time]-\
	    m.ReboilerLiqLvMFlow[time] * m.ReboilerLiqLvMEtlp[time]-\
	    m.ReboilerVapLvMFlow[time] * m.ReboilerVapLvMEtlp[time])*0.000010==0
test_model.ReboilerEngBlnc = Constraint(test_model.Time, rule=ReboilerEngBlnc)
#--------Reboiler Phase Equilibrium---------
def ReboilerThermCompVap(m,time):
	return m.ReboilerVapLvMFrac[time,"Oxygen"] == vapor_oxygen_composition(m.ColumnTrayPressure[time,1],m.ReboilerTemp[time])
test_model.ReboilerThermCompVap = Constraint(test_model.Time,rule=ReboilerThermCompVap)
def ReboilerThermCompLiq(m,time):
	return m.ReboilerLiqLvMFrac[time,"Oxygen"] == liquid_oxygen_composition(m.ColumnTrayPressure[time,1],m.ReboilerTemp[time])
test_model.ReboilerThermCompLiq = Constraint(test_model.Time,rule=ReboilerThermCompLiq)
#--------Reboiler Summation---------
def ReboilerLiqSum(m,time):
	return sum([m.ReboilerLiqLvMFrac[time,c] for c in m.Component]) == 1
test_model.ReboilerLiqSum = Constraint(test_model.Time, rule=ReboilerLiqSum)
def ReboilerVapSum(m,time):
	return sum([m.ReboilerVapLvMFrac[time,c] for c in m.Component]) == 1
test_model.ReboilerVapSum = Constraint(test_model.Time, rule=ReboilerVapSum)

#----------------------------------
#           GNSplitter
#----------------------------------
#--------GNSplitter Mass Balance---------
def GNSplitterOutASpec(m,time):
	return (m.GNSplitterOutAMFlow[time]-m.ColumnVapLvMFlow[time,10]*m.GNSplitterOutARatio[time])*0.001000==0
test_model.GNSplitterOutASpec = Constraint(test_model.Time, rule=GNSplitterOutASpec)
def GNSplitterOutBSpec(m,time):
	return (m.GNSplitterOutBMFlow[time]-m.ColumnVapLvMFlow[time,10]*(1-m.GNSplitterOutARatio[time]))*0.001000==0
test_model.GNSplitterOutBSpec = Constraint(test_model.Time, rule=GNSplitterOutBSpec)

#===================================
#
#         Discretize
#
#===================================
Discretizer.discretilize(test_model)

#===================================
#
#     Variable Initialization
#
#===================================
ModularTask.InitValueTools.load_naive_var_init(test_model,"test_modelNaiveInit.txt")	