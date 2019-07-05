from pyomo.environ import *

test_model = ConcreteModel()
test_model.Component = Set(initialize=['Nitrogen', 'Oxygen', 'Argon'])

#===================================
#
#      Process Parts
#
#===================================
import triHPCThermo.HPCFeed1SelfCstmVapEtlp
import triHPCThermo.HPCFeed1SelfCstmLiqEtlp
import triHPCThermo.HPCFeed1SelfCstmLiqO2
import triHPCThermo.HPCFeed1SelfCstmVapO2
import triHPCThermo.HPCFeed1SelfCstmVapN2
import triHPCThermo.HPCFeed2SelfCstmVapEtlp
import triHPCThermo.HPCFeed2SelfCstmLiqEtlp
import triHPCThermo.HPCFeed2SelfCstmLiqO2
import triHPCThermo.HPCFeed2SelfCstmVapO2
import triHPCThermo.HPCFeed2SelfCstmVapN2
import triHPCThermo.HPCAllTrays1CstmVapEtlp
import triHPCThermo.HPCAllTrays2CstmVapEtlp
import triHPCThermo.HPCAllTrays3CstmVapEtlp
import triHPCThermo.HPCAllTrays4CstmVapEtlp
import triHPCThermo.HPCAllTrays5CstmVapEtlp
import triHPCThermo.HPCAllTrays6CstmVapEtlp
import triHPCThermo.HPCAllTrays7CstmVapEtlp
import triHPCThermo.HPCAllTrays8CstmVapEtlp
import triHPCThermo.HPCAllTrays9CstmVapEtlp
import triHPCThermo.HPCAllTrays10CstmVapEtlp
import triHPCThermo.HPCAllTrays11CstmVapEtlp
import triHPCThermo.HPCAllTrays12CstmVapEtlp
import triHPCThermo.HPCAllTrays13CstmVapEtlp
import triHPCThermo.HPCAllTrays14CstmVapEtlp
import triHPCThermo.HPCAllTrays15CstmVapEtlp
import triHPCThermo.HPCAllTrays16CstmVapEtlp
import triHPCThermo.HPCAllTrays17CstmVapEtlp
import triHPCThermo.HPCAllTrays18CstmVapEtlp
import triHPCThermo.HPCAllTrays19CstmVapEtlp
import triHPCThermo.HPCAllTrays20CstmVapEtlp
import triHPCThermo.HPCAllTrays21CstmVapEtlp
import triHPCThermo.HPCAllTrays22CstmVapEtlp
import triHPCThermo.HPCAllTrays23CstmVapEtlp
import triHPCThermo.HPCAllTrays24CstmVapEtlp
import triHPCThermo.HPCAllTrays25CstmVapEtlp
import triHPCThermo.HPCAllTrays26CstmVapEtlp
import triHPCThermo.HPCAllTrays27CstmVapEtlp
import triHPCThermo.HPCAllTrays28CstmVapEtlp
import triHPCThermo.HPCAllTrays29CstmVapEtlp
import triHPCThermo.HPCAllTrays30CstmVapEtlp
import triHPCThermo.HPCAllTrays31CstmVapEtlp
import triHPCThermo.HPCAllTrays32CstmVapEtlp
import triHPCThermo.HPCAllTrays33CstmVapEtlp
import triHPCThermo.HPCAllTrays34CstmVapEtlp
import triHPCThermo.HPCAllTrays35CstmVapEtlp
import triHPCThermo.HPCAllTrays36CstmVapEtlp
import triHPCThermo.HPCAllTrays37CstmVapEtlp
import triHPCThermo.HPCAllTrays38CstmVapEtlp
import triHPCThermo.HPCAllTrays39CstmVapEtlp
import triHPCThermo.HPCAllTrays40CstmVapEtlp
import triHPCThermo.HPCAllTrays41CstmVapEtlp
import triHPCThermo.HPCAllTrays42CstmVapEtlp
import triHPCThermo.HPCAllTrays1CstmLiqEtlp
import triHPCThermo.HPCAllTrays2CstmLiqEtlp
import triHPCThermo.HPCAllTrays3CstmLiqEtlp
import triHPCThermo.HPCAllTrays4CstmLiqEtlp
import triHPCThermo.HPCAllTrays5CstmLiqEtlp
import triHPCThermo.HPCAllTrays6CstmLiqEtlp
import triHPCThermo.HPCAllTrays7CstmLiqEtlp
import triHPCThermo.HPCAllTrays8CstmLiqEtlp
import triHPCThermo.HPCAllTrays9CstmLiqEtlp
import triHPCThermo.HPCAllTrays10CstmLiqEtlp
import triHPCThermo.HPCAllTrays11CstmLiqEtlp
import triHPCThermo.HPCAllTrays12CstmLiqEtlp
import triHPCThermo.HPCAllTrays13CstmLiqEtlp
import triHPCThermo.HPCAllTrays14CstmLiqEtlp
import triHPCThermo.HPCAllTrays15CstmLiqEtlp
import triHPCThermo.HPCAllTrays16CstmLiqEtlp
import triHPCThermo.HPCAllTrays17CstmLiqEtlp
import triHPCThermo.HPCAllTrays18CstmLiqEtlp
import triHPCThermo.HPCAllTrays19CstmLiqEtlp
import triHPCThermo.HPCAllTrays20CstmLiqEtlp
import triHPCThermo.HPCAllTrays21CstmLiqEtlp
import triHPCThermo.HPCAllTrays22CstmLiqEtlp
import triHPCThermo.HPCAllTrays23CstmLiqEtlp
import triHPCThermo.HPCAllTrays24CstmLiqEtlp
import triHPCThermo.HPCAllTrays25CstmLiqEtlp
import triHPCThermo.HPCAllTrays26CstmLiqEtlp
import triHPCThermo.HPCAllTrays27CstmLiqEtlp
import triHPCThermo.HPCAllTrays28CstmLiqEtlp
import triHPCThermo.HPCAllTrays29CstmLiqEtlp
import triHPCThermo.HPCAllTrays30CstmLiqEtlp
import triHPCThermo.HPCAllTrays31CstmLiqEtlp
import triHPCThermo.HPCAllTrays32CstmLiqEtlp
import triHPCThermo.HPCAllTrays33CstmLiqEtlp
import triHPCThermo.HPCAllTrays34CstmLiqEtlp
import triHPCThermo.HPCAllTrays35CstmLiqEtlp
import triHPCThermo.HPCAllTrays36CstmLiqEtlp
import triHPCThermo.HPCAllTrays37CstmLiqEtlp
import triHPCThermo.HPCAllTrays38CstmLiqEtlp
import triHPCThermo.HPCAllTrays39CstmLiqEtlp
import triHPCThermo.HPCAllTrays40CstmLiqEtlp
import triHPCThermo.HPCAllTrays41CstmLiqEtlp
import triHPCThermo.HPCAllTrays42CstmLiqEtlp
import triHPCThermo.HPCAllTrays1CstmLiqO2
import triHPCThermo.HPCAllTrays1CstmVapO2
import triHPCThermo.HPCAllTrays1CstmVapN2
import triHPCThermo.HPCAllTrays2CstmLiqO2
import triHPCThermo.HPCAllTrays2CstmVapO2
import triHPCThermo.HPCAllTrays2CstmVapN2
import triHPCThermo.HPCAllTrays3CstmLiqO2
import triHPCThermo.HPCAllTrays3CstmVapO2
import triHPCThermo.HPCAllTrays3CstmVapN2
import triHPCThermo.HPCAllTrays4CstmLiqO2
import triHPCThermo.HPCAllTrays4CstmVapO2
import triHPCThermo.HPCAllTrays4CstmVapN2
import triHPCThermo.HPCAllTrays5CstmLiqO2
import triHPCThermo.HPCAllTrays5CstmVapO2
import triHPCThermo.HPCAllTrays5CstmVapN2
import triHPCThermo.HPCAllTrays6CstmLiqO2
import triHPCThermo.HPCAllTrays6CstmVapO2
import triHPCThermo.HPCAllTrays6CstmVapN2
import triHPCThermo.HPCAllTrays7CstmLiqO2
import triHPCThermo.HPCAllTrays7CstmVapO2
import triHPCThermo.HPCAllTrays7CstmVapN2
import triHPCThermo.HPCAllTrays8CstmLiqO2
import triHPCThermo.HPCAllTrays8CstmVapO2
import triHPCThermo.HPCAllTrays8CstmVapN2
import triHPCThermo.HPCAllTrays9CstmLiqO2
import triHPCThermo.HPCAllTrays9CstmVapO2
import triHPCThermo.HPCAllTrays9CstmVapN2
import triHPCThermo.HPCAllTrays10CstmLiqO2
import triHPCThermo.HPCAllTrays10CstmVapO2
import triHPCThermo.HPCAllTrays10CstmVapN2
import triHPCThermo.HPCAllTrays11CstmLiqO2
import triHPCThermo.HPCAllTrays11CstmVapO2
import triHPCThermo.HPCAllTrays11CstmVapN2
import triHPCThermo.HPCAllTrays12CstmLiqO2
import triHPCThermo.HPCAllTrays12CstmVapO2
import triHPCThermo.HPCAllTrays12CstmVapN2
import triHPCThermo.HPCAllTrays13CstmLiqO2
import triHPCThermo.HPCAllTrays13CstmVapO2
import triHPCThermo.HPCAllTrays13CstmVapN2
import triHPCThermo.HPCAllTrays14CstmLiqO2
import triHPCThermo.HPCAllTrays14CstmVapO2
import triHPCThermo.HPCAllTrays14CstmVapN2
import triHPCThermo.HPCAllTrays15CstmLiqO2
import triHPCThermo.HPCAllTrays15CstmVapO2
import triHPCThermo.HPCAllTrays15CstmVapN2
import triHPCThermo.HPCAllTrays16CstmLiqO2
import triHPCThermo.HPCAllTrays16CstmVapO2
import triHPCThermo.HPCAllTrays16CstmVapN2
import triHPCThermo.HPCAllTrays17CstmLiqO2
import triHPCThermo.HPCAllTrays17CstmVapO2
import triHPCThermo.HPCAllTrays17CstmVapN2
import triHPCThermo.HPCAllTrays18CstmLiqO2
import triHPCThermo.HPCAllTrays18CstmVapO2
import triHPCThermo.HPCAllTrays18CstmVapN2
import triHPCThermo.HPCAllTrays19CstmLiqO2
import triHPCThermo.HPCAllTrays19CstmVapO2
import triHPCThermo.HPCAllTrays19CstmVapN2
import triHPCThermo.HPCAllTrays20CstmLiqO2
import triHPCThermo.HPCAllTrays20CstmVapO2
import triHPCThermo.HPCAllTrays20CstmVapN2
import triHPCThermo.HPCAllTrays21CstmLiqO2
import triHPCThermo.HPCAllTrays21CstmVapO2
import triHPCThermo.HPCAllTrays21CstmVapN2
import triHPCThermo.HPCAllTrays22CstmLiqO2
import triHPCThermo.HPCAllTrays22CstmVapO2
import triHPCThermo.HPCAllTrays22CstmVapN2
import triHPCThermo.HPCAllTrays23CstmLiqO2
import triHPCThermo.HPCAllTrays23CstmVapO2
import triHPCThermo.HPCAllTrays23CstmVapN2
import triHPCThermo.HPCAllTrays24CstmLiqO2
import triHPCThermo.HPCAllTrays24CstmVapO2
import triHPCThermo.HPCAllTrays24CstmVapN2
import triHPCThermo.HPCAllTrays25CstmLiqO2
import triHPCThermo.HPCAllTrays25CstmVapO2
import triHPCThermo.HPCAllTrays25CstmVapN2
import triHPCThermo.HPCAllTrays26CstmLiqO2
import triHPCThermo.HPCAllTrays26CstmVapO2
import triHPCThermo.HPCAllTrays26CstmVapN2
import triHPCThermo.HPCAllTrays27CstmLiqO2
import triHPCThermo.HPCAllTrays27CstmVapO2
import triHPCThermo.HPCAllTrays27CstmVapN2
import triHPCThermo.HPCAllTrays28CstmLiqO2
import triHPCThermo.HPCAllTrays28CstmVapO2
import triHPCThermo.HPCAllTrays28CstmVapN2
import triHPCThermo.HPCAllTrays29CstmLiqO2
import triHPCThermo.HPCAllTrays29CstmVapO2
import triHPCThermo.HPCAllTrays29CstmVapN2
import triHPCThermo.HPCAllTrays30CstmLiqO2
import triHPCThermo.HPCAllTrays30CstmVapO2
import triHPCThermo.HPCAllTrays30CstmVapN2
import triHPCThermo.HPCAllTrays31CstmLiqO2
import triHPCThermo.HPCAllTrays31CstmVapO2
import triHPCThermo.HPCAllTrays31CstmVapN2
import triHPCThermo.HPCAllTrays32CstmLiqO2
import triHPCThermo.HPCAllTrays32CstmVapO2
import triHPCThermo.HPCAllTrays32CstmVapN2
import triHPCThermo.HPCAllTrays33CstmLiqO2
import triHPCThermo.HPCAllTrays33CstmVapO2
import triHPCThermo.HPCAllTrays33CstmVapN2
import triHPCThermo.HPCAllTrays34CstmLiqO2
import triHPCThermo.HPCAllTrays34CstmVapO2
import triHPCThermo.HPCAllTrays34CstmVapN2
import triHPCThermo.HPCAllTrays35CstmLiqO2
import triHPCThermo.HPCAllTrays35CstmVapO2
import triHPCThermo.HPCAllTrays35CstmVapN2
import triHPCThermo.HPCAllTrays36CstmLiqO2
import triHPCThermo.HPCAllTrays36CstmVapO2
import triHPCThermo.HPCAllTrays36CstmVapN2
import triHPCThermo.HPCAllTrays37CstmLiqO2
import triHPCThermo.HPCAllTrays37CstmVapO2
import triHPCThermo.HPCAllTrays37CstmVapN2
import triHPCThermo.HPCAllTrays38CstmLiqO2
import triHPCThermo.HPCAllTrays38CstmVapO2
import triHPCThermo.HPCAllTrays38CstmVapN2
import triHPCThermo.HPCAllTrays39CstmLiqO2
import triHPCThermo.HPCAllTrays39CstmVapO2
import triHPCThermo.HPCAllTrays39CstmVapN2
import triHPCThermo.HPCAllTrays40CstmLiqO2
import triHPCThermo.HPCAllTrays40CstmVapO2
import triHPCThermo.HPCAllTrays40CstmVapN2
import triHPCThermo.HPCAllTrays41CstmLiqO2
import triHPCThermo.HPCAllTrays41CstmVapO2
import triHPCThermo.HPCAllTrays41CstmVapN2
import triHPCThermo.HPCAllTrays42CstmLiqO2
import triHPCThermo.HPCAllTrays42CstmVapO2
import triHPCThermo.HPCAllTrays42CstmVapN2
import triHPCThermo.HPCCondOutletCstmLiqEtlp
import triHPCThermo.HPCCondSelfCstmLiqO2

#===================================
#
#       Case Depend Paras
#
#===================================
test_model.HPCFeed1PE0MFlow = Param(initialize = 3326.000000)
test_model.HPCFeed2PE0MFlow = Param(initialize = 1276.000000)
test_model.HPCFeed1PE1MFlow = Param(initialize = 3100.000000)
test_model.HPCFeed2PE1MFlow = Param(initialize = 1200.000000)

#===========================================
#===========================================
#===                                     ===
#===        PE MODEL SECTION  0          ===
#===                                     ===
#===========================================
#===========================================

#===================================
#
#      Parameters & Sets
#
#===================================
#--------HPCFeed1PE0---------
test_model.HPCFeed1PE0MFrac = Param(test_model.Component, initialize = {'Oxygen': 0.2095, 'Nitrogen': 0.7812, 'Argon': 0.0093})
test_model.HPCFeed1PE0Pressure = Param(initialize = 564.000000)
test_model.HPCFeed1PE0VF = Param(initialize = 0.980000)
#--------HPCFeed2PE0---------
test_model.HPCFeed2PE0MFrac = Param(test_model.Component, initialize = {'Oxygen': 0.2095, 'Nitrogen': 0.7812, 'Argon': 0.0093})
test_model.HPCFeed2PE0Pressure = Param(initialize = 562.600000)
test_model.HPCFeed2PE0VF = Param(initialize = 0.084100)
#--------HPCPE0---------
test_model.HPCPE0Trays = RangeSet(1, 42)
test_model.HPCPE0Ext6MFlow = Param(initialize = 829.800000)
test_model.HPCPE0Ext22MFlow = Param(initialize = 47.290000)
test_model.HPCPE0TopPressure = Param(initialize = 538.600000)
test_model.HPCPE0BtmPressure = Param(initialize = 564.000000)
test_model.HPCPE0UALeakage = Var(initialize = 10.000000, within=NonNegativeReals)
test_model.HPCPE0AmbientTemp = Var(initialize = 25.000000, bounds = (10,40))
#--------HPCSumpPE0---------
test_model.HPCSumpPE0LiqRho = Param(initialize = 1000.000000)
test_model.HPCSumpPE0SumpCSArea = Param(initialize = 6.000000)
#--------HPCCondPE0---------
test_model.HPCCondPE0RefluxRatio = Param(initialize = 0.564650)

#===================================
#
#         Variables
#
#===================================
#--------HPCFeed1PE0---------
test_model.HPCFeed1PE0Temp = Var()
test_model.HPCFeed1PE0LiqMFrac = Var(test_model.Component, bounds=(0, 1))
test_model.HPCFeed1PE0VapMFrac = Var(test_model.Component, bounds=(0, 1))
#--------HPCFeed2PE0---------
test_model.HPCFeed2PE0Temp = Var()
test_model.HPCFeed2PE0LiqMFrac = Var(test_model.Component, bounds=(0, 1))
test_model.HPCFeed2PE0VapMFrac = Var(test_model.Component, bounds=(0, 1))
#--------HPCPE0---------
test_model.HPCPE0VapLvMFlow = Var(test_model.HPCPE0Trays, within=NonNegativeReals)
test_model.HPCPE0LiqLvMFlow = Var(test_model.HPCPE0Trays, within=NonNegativeReals)
test_model.HPCPE0TrayTemp = Var(test_model.HPCPE0Trays)
test_model.HPCPE0TrayPressure = Var(test_model.HPCPE0Trays)
test_model.HPCPE0LiqLvMFrac = Var(test_model.HPCPE0Trays,test_model.Component, bounds=(0, 1))
test_model.HPCPE0VapLvMFrac = Var(test_model.HPCPE0Trays,test_model.Component, bounds=(0, 1))
#--------HPCPE0's var in extractions---------
test_model.HPCPE0Ext6MFrac = Var(test_model.Component, bounds=(0,1))
test_model.HPCPE0Ext6MEtlp = Var()
test_model.HPCPE0Ext22MFrac = Var(test_model.Component, bounds=(0,1))
test_model.HPCPE0Ext22MEtlp = Var()
#--------HPCSumpPE0---------
test_model.HPCSumpPE0OutMFlow = Var(within=NonNegativeReals)
test_model.HPCSumpPE0HldpMFrac = Var(test_model.Component, bounds =(0,1))
#--------HPCCondPE0---------
test_model.HPCCondPE0RefMFlow = Var(within=NonNegativeReals)
test_model.HPCCondPE0PrdtMFlow = Var(within=NonNegativeReals)
test_model.HPCCondPE0MHeatOut = Var(within=NonNegativeReals)
test_model.HPCCondPE0Temp = Var(initialize = 0)

#===================================
#
#         Expressions
#
#===================================
#--------HPCFeed1PE0 Enthalpy---------
def HPCFeed1PE0VapMEtlp(m):
	return triHPCThermo.HPCFeed1SelfCstmVapEtlp.VapEtlp(m.HPCFeed1PE0Pressure, m.HPCFeed1PE0Temp,m.HPCFeed1PE0LiqMFrac["Nitrogen"])
test_model.HPCFeed1PE0VapMEtlp = Expression(rule=HPCFeed1PE0VapMEtlp)
def HPCFeed1PE0LiqMEtlp(m):
	return triHPCThermo.HPCFeed1SelfCstmLiqEtlp.LiqEtlp(m.HPCFeed1PE0Pressure, m.HPCFeed1PE0Temp,m.HPCFeed1PE0LiqMFrac["Nitrogen"])
test_model.HPCFeed1PE0LiqMEtlp = Expression(rule=HPCFeed1PE0LiqMEtlp)
def HPCFeed1PE0MEtlp(m):
	return m.HPCFeed1PE0LiqMEtlp * (1-m.HPCFeed1PE0VF)+m.HPCFeed1PE0VapMEtlp * m.HPCFeed1PE0VF
test_model.HPCFeed1PE0MEtlp = Expression(rule=HPCFeed1PE0MEtlp)
#--------HPCFeed2PE0 Enthalpy---------
def HPCFeed2PE0VapMEtlp(m):
	return triHPCThermo.HPCFeed2SelfCstmVapEtlp.VapEtlp(m.HPCFeed2PE0Pressure, m.HPCFeed2PE0Temp,m.HPCFeed2PE0LiqMFrac["Nitrogen"])
test_model.HPCFeed2PE0VapMEtlp = Expression(rule=HPCFeed2PE0VapMEtlp)
def HPCFeed2PE0LiqMEtlp(m):
	return triHPCThermo.HPCFeed2SelfCstmLiqEtlp.LiqEtlp(m.HPCFeed2PE0Pressure, m.HPCFeed2PE0Temp,m.HPCFeed2PE0LiqMFrac["Nitrogen"])
test_model.HPCFeed2PE0LiqMEtlp = Expression(rule=HPCFeed2PE0LiqMEtlp)
def HPCFeed2PE0MEtlp(m):
	return m.HPCFeed2PE0LiqMEtlp * (1-m.HPCFeed2PE0VF)+m.HPCFeed2PE0VapMEtlp * m.HPCFeed2PE0VF
test_model.HPCFeed2PE0MEtlp = Expression(rule=HPCFeed2PE0MEtlp)
#--------HPCPE0 Component Flowrate---------
def HPCPE0VapLvMCompFlow(m, tray, comp):
	return m.HPCPE0VapLvMFrac[tray, comp] * m.HPCPE0VapLvMFlow[tray]
test_model.HPCPE0VapLvMCompFlow = Expression(test_model.HPCPE0Trays, test_model.Component, rule=HPCPE0VapLvMCompFlow)
def HPCPE0LiqLvMCompFlow(m, tray, comp):
	return m.HPCPE0LiqLvMFrac[tray, comp] * m.HPCPE0LiqLvMFlow[tray]
test_model.HPCPE0LiqLvMCompFlow = Expression(test_model.HPCPE0Trays, test_model.Component, rule=HPCPE0LiqLvMCompFlow)
#--------HPCPE0 Thermo and Enthalpy---------
def HPCPE0VapLvMEtlp(m,tray):
	if tray==1:
		return triHPCThermo.HPCAllTrays1CstmVapEtlp.VapEtlp(m.HPCPE0TrayPressure[tray], m.HPCPE0TrayTemp[tray],m.HPCPE0LiqLvMFrac[tray,"Nitrogen"])
	elif tray==2:
		return triHPCThermo.HPCAllTrays2CstmVapEtlp.VapEtlp(m.HPCPE0TrayPressure[tray], m.HPCPE0TrayTemp[tray],m.HPCPE0LiqLvMFrac[tray,"Nitrogen"])
	elif tray==3:
		return triHPCThermo.HPCAllTrays3CstmVapEtlp.VapEtlp(m.HPCPE0TrayPressure[tray], m.HPCPE0TrayTemp[tray],m.HPCPE0LiqLvMFrac[tray,"Nitrogen"])
	elif tray==4:
		return triHPCThermo.HPCAllTrays4CstmVapEtlp.VapEtlp(m.HPCPE0TrayPressure[tray], m.HPCPE0TrayTemp[tray],m.HPCPE0LiqLvMFrac[tray,"Nitrogen"])
	elif tray==5:
		return triHPCThermo.HPCAllTrays5CstmVapEtlp.VapEtlp(m.HPCPE0TrayPressure[tray], m.HPCPE0TrayTemp[tray],m.HPCPE0LiqLvMFrac[tray,"Nitrogen"])
	elif tray==6:
		return triHPCThermo.HPCAllTrays6CstmVapEtlp.VapEtlp(m.HPCPE0TrayPressure[tray], m.HPCPE0TrayTemp[tray],m.HPCPE0LiqLvMFrac[tray,"Nitrogen"])
	elif tray==7:
		return triHPCThermo.HPCAllTrays7CstmVapEtlp.VapEtlp(m.HPCPE0TrayPressure[tray], m.HPCPE0TrayTemp[tray],m.HPCPE0LiqLvMFrac[tray,"Nitrogen"])
	elif tray==8:
		return triHPCThermo.HPCAllTrays8CstmVapEtlp.VapEtlp(m.HPCPE0TrayPressure[tray], m.HPCPE0TrayTemp[tray],m.HPCPE0LiqLvMFrac[tray,"Nitrogen"])
	elif tray==9:
		return triHPCThermo.HPCAllTrays9CstmVapEtlp.VapEtlp(m.HPCPE0TrayPressure[tray], m.HPCPE0TrayTemp[tray],m.HPCPE0LiqLvMFrac[tray,"Nitrogen"])
	elif tray==10:
		return triHPCThermo.HPCAllTrays10CstmVapEtlp.VapEtlp(m.HPCPE0TrayPressure[tray], m.HPCPE0TrayTemp[tray],m.HPCPE0LiqLvMFrac[tray,"Nitrogen"])
	elif tray==11:
		return triHPCThermo.HPCAllTrays11CstmVapEtlp.VapEtlp(m.HPCPE0TrayPressure[tray], m.HPCPE0TrayTemp[tray],m.HPCPE0LiqLvMFrac[tray,"Nitrogen"])
	elif tray==12:
		return triHPCThermo.HPCAllTrays12CstmVapEtlp.VapEtlp(m.HPCPE0TrayPressure[tray], m.HPCPE0TrayTemp[tray],m.HPCPE0LiqLvMFrac[tray,"Nitrogen"])
	elif tray==13:
		return triHPCThermo.HPCAllTrays13CstmVapEtlp.VapEtlp(m.HPCPE0TrayPressure[tray], m.HPCPE0TrayTemp[tray],m.HPCPE0LiqLvMFrac[tray,"Nitrogen"])
	elif tray==14:
		return triHPCThermo.HPCAllTrays14CstmVapEtlp.VapEtlp(m.HPCPE0TrayPressure[tray], m.HPCPE0TrayTemp[tray],m.HPCPE0LiqLvMFrac[tray,"Nitrogen"])
	elif tray==15:
		return triHPCThermo.HPCAllTrays15CstmVapEtlp.VapEtlp(m.HPCPE0TrayPressure[tray], m.HPCPE0TrayTemp[tray],m.HPCPE0LiqLvMFrac[tray,"Nitrogen"])
	elif tray==16:
		return triHPCThermo.HPCAllTrays16CstmVapEtlp.VapEtlp(m.HPCPE0TrayPressure[tray], m.HPCPE0TrayTemp[tray],m.HPCPE0LiqLvMFrac[tray,"Nitrogen"])
	elif tray==17:
		return triHPCThermo.HPCAllTrays17CstmVapEtlp.VapEtlp(m.HPCPE0TrayPressure[tray], m.HPCPE0TrayTemp[tray],m.HPCPE0LiqLvMFrac[tray,"Nitrogen"])
	elif tray==18:
		return triHPCThermo.HPCAllTrays18CstmVapEtlp.VapEtlp(m.HPCPE0TrayPressure[tray], m.HPCPE0TrayTemp[tray],m.HPCPE0LiqLvMFrac[tray,"Nitrogen"])
	elif tray==19:
		return triHPCThermo.HPCAllTrays19CstmVapEtlp.VapEtlp(m.HPCPE0TrayPressure[tray], m.HPCPE0TrayTemp[tray],m.HPCPE0LiqLvMFrac[tray,"Nitrogen"])
	elif tray==20:
		return triHPCThermo.HPCAllTrays20CstmVapEtlp.VapEtlp(m.HPCPE0TrayPressure[tray], m.HPCPE0TrayTemp[tray],m.HPCPE0LiqLvMFrac[tray,"Nitrogen"])
	elif tray==21:
		return triHPCThermo.HPCAllTrays21CstmVapEtlp.VapEtlp(m.HPCPE0TrayPressure[tray], m.HPCPE0TrayTemp[tray],m.HPCPE0LiqLvMFrac[tray,"Nitrogen"])
	elif tray==22:
		return triHPCThermo.HPCAllTrays22CstmVapEtlp.VapEtlp(m.HPCPE0TrayPressure[tray], m.HPCPE0TrayTemp[tray],m.HPCPE0LiqLvMFrac[tray,"Nitrogen"])
	elif tray==23:
		return triHPCThermo.HPCAllTrays23CstmVapEtlp.VapEtlp(m.HPCPE0TrayPressure[tray], m.HPCPE0TrayTemp[tray],m.HPCPE0LiqLvMFrac[tray,"Nitrogen"])
	elif tray==24:
		return triHPCThermo.HPCAllTrays24CstmVapEtlp.VapEtlp(m.HPCPE0TrayPressure[tray], m.HPCPE0TrayTemp[tray],m.HPCPE0LiqLvMFrac[tray,"Nitrogen"])
	elif tray==25:
		return triHPCThermo.HPCAllTrays25CstmVapEtlp.VapEtlp(m.HPCPE0TrayPressure[tray], m.HPCPE0TrayTemp[tray],m.HPCPE0LiqLvMFrac[tray,"Nitrogen"])
	elif tray==26:
		return triHPCThermo.HPCAllTrays26CstmVapEtlp.VapEtlp(m.HPCPE0TrayPressure[tray], m.HPCPE0TrayTemp[tray],m.HPCPE0LiqLvMFrac[tray,"Nitrogen"])
	elif tray==27:
		return triHPCThermo.HPCAllTrays27CstmVapEtlp.VapEtlp(m.HPCPE0TrayPressure[tray], m.HPCPE0TrayTemp[tray],m.HPCPE0LiqLvMFrac[tray,"Nitrogen"])
	elif tray==28:
		return triHPCThermo.HPCAllTrays28CstmVapEtlp.VapEtlp(m.HPCPE0TrayPressure[tray], m.HPCPE0TrayTemp[tray],m.HPCPE0LiqLvMFrac[tray,"Nitrogen"])
	elif tray==29:
		return triHPCThermo.HPCAllTrays29CstmVapEtlp.VapEtlp(m.HPCPE0TrayPressure[tray], m.HPCPE0TrayTemp[tray],m.HPCPE0LiqLvMFrac[tray,"Nitrogen"])
	elif tray==30:
		return triHPCThermo.HPCAllTrays30CstmVapEtlp.VapEtlp(m.HPCPE0TrayPressure[tray], m.HPCPE0TrayTemp[tray],m.HPCPE0LiqLvMFrac[tray,"Nitrogen"])
	elif tray==31:
		return triHPCThermo.HPCAllTrays31CstmVapEtlp.VapEtlp(m.HPCPE0TrayPressure[tray], m.HPCPE0TrayTemp[tray],m.HPCPE0LiqLvMFrac[tray,"Nitrogen"])
	elif tray==32:
		return triHPCThermo.HPCAllTrays32CstmVapEtlp.VapEtlp(m.HPCPE0TrayPressure[tray], m.HPCPE0TrayTemp[tray],m.HPCPE0LiqLvMFrac[tray,"Nitrogen"])
	elif tray==33:
		return triHPCThermo.HPCAllTrays33CstmVapEtlp.VapEtlp(m.HPCPE0TrayPressure[tray], m.HPCPE0TrayTemp[tray],m.HPCPE0LiqLvMFrac[tray,"Nitrogen"])
	elif tray==34:
		return triHPCThermo.HPCAllTrays34CstmVapEtlp.VapEtlp(m.HPCPE0TrayPressure[tray], m.HPCPE0TrayTemp[tray],m.HPCPE0LiqLvMFrac[tray,"Nitrogen"])
	elif tray==35:
		return triHPCThermo.HPCAllTrays35CstmVapEtlp.VapEtlp(m.HPCPE0TrayPressure[tray], m.HPCPE0TrayTemp[tray],m.HPCPE0LiqLvMFrac[tray,"Nitrogen"])
	elif tray==36:
		return triHPCThermo.HPCAllTrays36CstmVapEtlp.VapEtlp(m.HPCPE0TrayPressure[tray], m.HPCPE0TrayTemp[tray],m.HPCPE0LiqLvMFrac[tray,"Nitrogen"])
	elif tray==37:
		return triHPCThermo.HPCAllTrays37CstmVapEtlp.VapEtlp(m.HPCPE0TrayPressure[tray], m.HPCPE0TrayTemp[tray],m.HPCPE0LiqLvMFrac[tray,"Nitrogen"])
	elif tray==38:
		return triHPCThermo.HPCAllTrays38CstmVapEtlp.VapEtlp(m.HPCPE0TrayPressure[tray], m.HPCPE0TrayTemp[tray],m.HPCPE0LiqLvMFrac[tray,"Nitrogen"])
	elif tray==39:
		return triHPCThermo.HPCAllTrays39CstmVapEtlp.VapEtlp(m.HPCPE0TrayPressure[tray], m.HPCPE0TrayTemp[tray],m.HPCPE0LiqLvMFrac[tray,"Nitrogen"])
	elif tray==40:
		return triHPCThermo.HPCAllTrays40CstmVapEtlp.VapEtlp(m.HPCPE0TrayPressure[tray], m.HPCPE0TrayTemp[tray],m.HPCPE0LiqLvMFrac[tray,"Nitrogen"])
	elif tray==41:
		return triHPCThermo.HPCAllTrays41CstmVapEtlp.VapEtlp(m.HPCPE0TrayPressure[tray], m.HPCPE0TrayTemp[tray],m.HPCPE0LiqLvMFrac[tray,"Nitrogen"])
	elif tray==42:
		return triHPCThermo.HPCAllTrays42CstmVapEtlp.VapEtlp(m.HPCPE0TrayPressure[tray], m.HPCPE0TrayTemp[tray],m.HPCPE0LiqLvMFrac[tray,"Nitrogen"])
test_model.HPCPE0VapLvMEtlp = Expression(test_model.HPCPE0Trays,rule=HPCPE0VapLvMEtlp)
def HPCPE0LiqLvMEtlp(m,tray):
	if tray==1:
		return triHPCThermo.HPCAllTrays1CstmLiqEtlp.LiqEtlp(m.HPCPE0TrayPressure[tray], m.HPCPE0TrayTemp[tray],m.HPCPE0LiqLvMFrac[tray,"Nitrogen"])
	elif tray==2:
		return triHPCThermo.HPCAllTrays2CstmLiqEtlp.LiqEtlp(m.HPCPE0TrayPressure[tray], m.HPCPE0TrayTemp[tray],m.HPCPE0LiqLvMFrac[tray,"Nitrogen"])
	elif tray==3:
		return triHPCThermo.HPCAllTrays3CstmLiqEtlp.LiqEtlp(m.HPCPE0TrayPressure[tray], m.HPCPE0TrayTemp[tray],m.HPCPE0LiqLvMFrac[tray,"Nitrogen"])
	elif tray==4:
		return triHPCThermo.HPCAllTrays4CstmLiqEtlp.LiqEtlp(m.HPCPE0TrayPressure[tray], m.HPCPE0TrayTemp[tray],m.HPCPE0LiqLvMFrac[tray,"Nitrogen"])
	elif tray==5:
		return triHPCThermo.HPCAllTrays5CstmLiqEtlp.LiqEtlp(m.HPCPE0TrayPressure[tray], m.HPCPE0TrayTemp[tray],m.HPCPE0LiqLvMFrac[tray,"Nitrogen"])
	elif tray==6:
		return triHPCThermo.HPCAllTrays6CstmLiqEtlp.LiqEtlp(m.HPCPE0TrayPressure[tray], m.HPCPE0TrayTemp[tray],m.HPCPE0LiqLvMFrac[tray,"Nitrogen"])
	elif tray==7:
		return triHPCThermo.HPCAllTrays7CstmLiqEtlp.LiqEtlp(m.HPCPE0TrayPressure[tray], m.HPCPE0TrayTemp[tray],m.HPCPE0LiqLvMFrac[tray,"Nitrogen"])
	elif tray==8:
		return triHPCThermo.HPCAllTrays8CstmLiqEtlp.LiqEtlp(m.HPCPE0TrayPressure[tray], m.HPCPE0TrayTemp[tray],m.HPCPE0LiqLvMFrac[tray,"Nitrogen"])
	elif tray==9:
		return triHPCThermo.HPCAllTrays9CstmLiqEtlp.LiqEtlp(m.HPCPE0TrayPressure[tray], m.HPCPE0TrayTemp[tray],m.HPCPE0LiqLvMFrac[tray,"Nitrogen"])
	elif tray==10:
		return triHPCThermo.HPCAllTrays10CstmLiqEtlp.LiqEtlp(m.HPCPE0TrayPressure[tray], m.HPCPE0TrayTemp[tray],m.HPCPE0LiqLvMFrac[tray,"Nitrogen"])
	elif tray==11:
		return triHPCThermo.HPCAllTrays11CstmLiqEtlp.LiqEtlp(m.HPCPE0TrayPressure[tray], m.HPCPE0TrayTemp[tray],m.HPCPE0LiqLvMFrac[tray,"Nitrogen"])
	elif tray==12:
		return triHPCThermo.HPCAllTrays12CstmLiqEtlp.LiqEtlp(m.HPCPE0TrayPressure[tray], m.HPCPE0TrayTemp[tray],m.HPCPE0LiqLvMFrac[tray,"Nitrogen"])
	elif tray==13:
		return triHPCThermo.HPCAllTrays13CstmLiqEtlp.LiqEtlp(m.HPCPE0TrayPressure[tray], m.HPCPE0TrayTemp[tray],m.HPCPE0LiqLvMFrac[tray,"Nitrogen"])
	elif tray==14:
		return triHPCThermo.HPCAllTrays14CstmLiqEtlp.LiqEtlp(m.HPCPE0TrayPressure[tray], m.HPCPE0TrayTemp[tray],m.HPCPE0LiqLvMFrac[tray,"Nitrogen"])
	elif tray==15:
		return triHPCThermo.HPCAllTrays15CstmLiqEtlp.LiqEtlp(m.HPCPE0TrayPressure[tray], m.HPCPE0TrayTemp[tray],m.HPCPE0LiqLvMFrac[tray,"Nitrogen"])
	elif tray==16:
		return triHPCThermo.HPCAllTrays16CstmLiqEtlp.LiqEtlp(m.HPCPE0TrayPressure[tray], m.HPCPE0TrayTemp[tray],m.HPCPE0LiqLvMFrac[tray,"Nitrogen"])
	elif tray==17:
		return triHPCThermo.HPCAllTrays17CstmLiqEtlp.LiqEtlp(m.HPCPE0TrayPressure[tray], m.HPCPE0TrayTemp[tray],m.HPCPE0LiqLvMFrac[tray,"Nitrogen"])
	elif tray==18:
		return triHPCThermo.HPCAllTrays18CstmLiqEtlp.LiqEtlp(m.HPCPE0TrayPressure[tray], m.HPCPE0TrayTemp[tray],m.HPCPE0LiqLvMFrac[tray,"Nitrogen"])
	elif tray==19:
		return triHPCThermo.HPCAllTrays19CstmLiqEtlp.LiqEtlp(m.HPCPE0TrayPressure[tray], m.HPCPE0TrayTemp[tray],m.HPCPE0LiqLvMFrac[tray,"Nitrogen"])
	elif tray==20:
		return triHPCThermo.HPCAllTrays20CstmLiqEtlp.LiqEtlp(m.HPCPE0TrayPressure[tray], m.HPCPE0TrayTemp[tray],m.HPCPE0LiqLvMFrac[tray,"Nitrogen"])
	elif tray==21:
		return triHPCThermo.HPCAllTrays21CstmLiqEtlp.LiqEtlp(m.HPCPE0TrayPressure[tray], m.HPCPE0TrayTemp[tray],m.HPCPE0LiqLvMFrac[tray,"Nitrogen"])
	elif tray==22:
		return triHPCThermo.HPCAllTrays22CstmLiqEtlp.LiqEtlp(m.HPCPE0TrayPressure[tray], m.HPCPE0TrayTemp[tray],m.HPCPE0LiqLvMFrac[tray,"Nitrogen"])
	elif tray==23:
		return triHPCThermo.HPCAllTrays23CstmLiqEtlp.LiqEtlp(m.HPCPE0TrayPressure[tray], m.HPCPE0TrayTemp[tray],m.HPCPE0LiqLvMFrac[tray,"Nitrogen"])
	elif tray==24:
		return triHPCThermo.HPCAllTrays24CstmLiqEtlp.LiqEtlp(m.HPCPE0TrayPressure[tray], m.HPCPE0TrayTemp[tray],m.HPCPE0LiqLvMFrac[tray,"Nitrogen"])
	elif tray==25:
		return triHPCThermo.HPCAllTrays25CstmLiqEtlp.LiqEtlp(m.HPCPE0TrayPressure[tray], m.HPCPE0TrayTemp[tray],m.HPCPE0LiqLvMFrac[tray,"Nitrogen"])
	elif tray==26:
		return triHPCThermo.HPCAllTrays26CstmLiqEtlp.LiqEtlp(m.HPCPE0TrayPressure[tray], m.HPCPE0TrayTemp[tray],m.HPCPE0LiqLvMFrac[tray,"Nitrogen"])
	elif tray==27:
		return triHPCThermo.HPCAllTrays27CstmLiqEtlp.LiqEtlp(m.HPCPE0TrayPressure[tray], m.HPCPE0TrayTemp[tray],m.HPCPE0LiqLvMFrac[tray,"Nitrogen"])
	elif tray==28:
		return triHPCThermo.HPCAllTrays28CstmLiqEtlp.LiqEtlp(m.HPCPE0TrayPressure[tray], m.HPCPE0TrayTemp[tray],m.HPCPE0LiqLvMFrac[tray,"Nitrogen"])
	elif tray==29:
		return triHPCThermo.HPCAllTrays29CstmLiqEtlp.LiqEtlp(m.HPCPE0TrayPressure[tray], m.HPCPE0TrayTemp[tray],m.HPCPE0LiqLvMFrac[tray,"Nitrogen"])
	elif tray==30:
		return triHPCThermo.HPCAllTrays30CstmLiqEtlp.LiqEtlp(m.HPCPE0TrayPressure[tray], m.HPCPE0TrayTemp[tray],m.HPCPE0LiqLvMFrac[tray,"Nitrogen"])
	elif tray==31:
		return triHPCThermo.HPCAllTrays31CstmLiqEtlp.LiqEtlp(m.HPCPE0TrayPressure[tray], m.HPCPE0TrayTemp[tray],m.HPCPE0LiqLvMFrac[tray,"Nitrogen"])
	elif tray==32:
		return triHPCThermo.HPCAllTrays32CstmLiqEtlp.LiqEtlp(m.HPCPE0TrayPressure[tray], m.HPCPE0TrayTemp[tray],m.HPCPE0LiqLvMFrac[tray,"Nitrogen"])
	elif tray==33:
		return triHPCThermo.HPCAllTrays33CstmLiqEtlp.LiqEtlp(m.HPCPE0TrayPressure[tray], m.HPCPE0TrayTemp[tray],m.HPCPE0LiqLvMFrac[tray,"Nitrogen"])
	elif tray==34:
		return triHPCThermo.HPCAllTrays34CstmLiqEtlp.LiqEtlp(m.HPCPE0TrayPressure[tray], m.HPCPE0TrayTemp[tray],m.HPCPE0LiqLvMFrac[tray,"Nitrogen"])
	elif tray==35:
		return triHPCThermo.HPCAllTrays35CstmLiqEtlp.LiqEtlp(m.HPCPE0TrayPressure[tray], m.HPCPE0TrayTemp[tray],m.HPCPE0LiqLvMFrac[tray,"Nitrogen"])
	elif tray==36:
		return triHPCThermo.HPCAllTrays36CstmLiqEtlp.LiqEtlp(m.HPCPE0TrayPressure[tray], m.HPCPE0TrayTemp[tray],m.HPCPE0LiqLvMFrac[tray,"Nitrogen"])
	elif tray==37:
		return triHPCThermo.HPCAllTrays37CstmLiqEtlp.LiqEtlp(m.HPCPE0TrayPressure[tray], m.HPCPE0TrayTemp[tray],m.HPCPE0LiqLvMFrac[tray,"Nitrogen"])
	elif tray==38:
		return triHPCThermo.HPCAllTrays38CstmLiqEtlp.LiqEtlp(m.HPCPE0TrayPressure[tray], m.HPCPE0TrayTemp[tray],m.HPCPE0LiqLvMFrac[tray,"Nitrogen"])
	elif tray==39:
		return triHPCThermo.HPCAllTrays39CstmLiqEtlp.LiqEtlp(m.HPCPE0TrayPressure[tray], m.HPCPE0TrayTemp[tray],m.HPCPE0LiqLvMFrac[tray,"Nitrogen"])
	elif tray==40:
		return triHPCThermo.HPCAllTrays40CstmLiqEtlp.LiqEtlp(m.HPCPE0TrayPressure[tray], m.HPCPE0TrayTemp[tray],m.HPCPE0LiqLvMFrac[tray,"Nitrogen"])
	elif tray==41:
		return triHPCThermo.HPCAllTrays41CstmLiqEtlp.LiqEtlp(m.HPCPE0TrayPressure[tray], m.HPCPE0TrayTemp[tray],m.HPCPE0LiqLvMFrac[tray,"Nitrogen"])
	elif tray==42:
		return triHPCThermo.HPCAllTrays42CstmLiqEtlp.LiqEtlp(m.HPCPE0TrayPressure[tray], m.HPCPE0TrayTemp[tray],m.HPCPE0LiqLvMFrac[tray,"Nitrogen"])
test_model.HPCPE0LiqLvMEtlp = Expression(test_model.HPCPE0Trays,rule=HPCPE0LiqLvMEtlp)
#--------HPCCondPE0 Enthalpy---------
def HPCCondPE0OutMEtlp(m):
	return triHPCThermo.HPCCondOutletCstmLiqEtlp.LiqEtlp(m.HPCPE0TrayPressure[42], m.HPCCondPE0Temp,m.HPCPE0VapLvMFrac[42,"Nitrogen"])
test_model.HPCCondPE0OutMEtlp = Expression(rule=HPCCondPE0OutMEtlp)

#===================================
#
#         Constraints
#
#===================================

#----------------------------------
#           HPCFeed1PE0
#----------------------------------
#--------HPCFeed1PE0 Mass Balance---------
def HPCFeed1PE0MassBlnc0(m):
	return m.HPCFeed1PE0VF * m.HPCFeed1PE0VapMFrac['Nitrogen'] + \
(1 - m.HPCFeed1PE0VF)*m.HPCFeed1PE0LiqMFrac['Nitrogen'] - m.HPCFeed1PE0MFrac['Nitrogen'] == 0
test_model.HPCFeed1PE0MassBlnc0 = Constraint(rule=HPCFeed1PE0MassBlnc0)
def HPCFeed1PE0MassBlnc1(m):
	return m.HPCFeed1PE0VF * m.HPCFeed1PE0VapMFrac['Oxygen'] + \
(1 - m.HPCFeed1PE0VF)*m.HPCFeed1PE0LiqMFrac['Oxygen'] - m.HPCFeed1PE0MFrac['Oxygen'] == 0
test_model.HPCFeed1PE0MassBlnc1 = Constraint(rule=HPCFeed1PE0MassBlnc1)
#--------HPCFeed1PE0 Phase Equilibrium---------
def HPCFeed1PE0SelfLiqO2Frac(m):
	return m.HPCFeed1PE0LiqMFrac["Oxygen"] == triHPCThermo.HPCFeed1SelfCstmLiqO2.LiqO2(m.HPCFeed1PE0Pressure,m.HPCFeed1PE0Temp,m.HPCFeed1PE0LiqMFrac["Nitrogen"])
test_model.HPCFeed1PE0SelfLiqO2Frac = Constraint(rule=HPCFeed1PE0SelfLiqO2Frac)
def HPCFeed1PE0SelfVapO2Frac(m):
	return m.HPCFeed1PE0VapMFrac["Oxygen"] == triHPCThermo.HPCFeed1SelfCstmVapO2.VapO2(m.HPCFeed1PE0Pressure,m.HPCFeed1PE0Temp,m.HPCFeed1PE0LiqMFrac["Nitrogen"])
test_model.HPCFeed1PE0SelfVapO2Frac = Constraint(rule=HPCFeed1PE0SelfVapO2Frac)
def HPCFeed1PE0SelfVapN2Frac(m):
	return m.HPCFeed1PE0VapMFrac["Nitrogen"] == triHPCThermo.HPCFeed1SelfCstmVapN2.VapN2(m.HPCFeed1PE0Pressure,m.HPCFeed1PE0Temp,m.HPCFeed1PE0LiqMFrac["Nitrogen"])
test_model.HPCFeed1PE0SelfVapN2Frac = Constraint(rule=HPCFeed1PE0SelfVapN2Frac)
#--------HPCFeed1PE0 Summation---------
def HPCFeed1PE0LiqSum(m):
	return sum([m.HPCFeed1PE0LiqMFrac[c] for c in m.Component]) == 1
test_model.HPCFeed1PE0LiqSum = Constraint(rule=HPCFeed1PE0LiqSum)
def HPCFeed1PE0VapSum(m):
	return sum([m.HPCFeed1PE0VapMFrac[c] for c in m.Component]) == 1
test_model.HPCFeed1PE0VapSum = Constraint(rule=HPCFeed1PE0VapSum)

#----------------------------------
#           HPCFeed2PE0
#----------------------------------
#--------HPCFeed2PE0 Mass Balance---------
def HPCFeed2PE0MassBlnc0(m):
	return m.HPCFeed2PE0VF * m.HPCFeed2PE0VapMFrac['Nitrogen'] + \
(1 - m.HPCFeed2PE0VF)*m.HPCFeed2PE0LiqMFrac['Nitrogen'] - m.HPCFeed2PE0MFrac['Nitrogen'] == 0
test_model.HPCFeed2PE0MassBlnc0 = Constraint(rule=HPCFeed2PE0MassBlnc0)
def HPCFeed2PE0MassBlnc1(m):
	return m.HPCFeed2PE0VF * m.HPCFeed2PE0VapMFrac['Oxygen'] + \
(1 - m.HPCFeed2PE0VF)*m.HPCFeed2PE0LiqMFrac['Oxygen'] - m.HPCFeed2PE0MFrac['Oxygen'] == 0
test_model.HPCFeed2PE0MassBlnc1 = Constraint(rule=HPCFeed2PE0MassBlnc1)
#--------HPCFeed2PE0 Phase Equilibrium---------
def HPCFeed2PE0SelfLiqO2Frac(m):
	return m.HPCFeed2PE0LiqMFrac["Oxygen"] == triHPCThermo.HPCFeed2SelfCstmLiqO2.LiqO2(m.HPCFeed2PE0Pressure,m.HPCFeed2PE0Temp,m.HPCFeed2PE0LiqMFrac["Nitrogen"])
test_model.HPCFeed2PE0SelfLiqO2Frac = Constraint(rule=HPCFeed2PE0SelfLiqO2Frac)
def HPCFeed2PE0SelfVapO2Frac(m):
	return m.HPCFeed2PE0VapMFrac["Oxygen"] == triHPCThermo.HPCFeed2SelfCstmVapO2.VapO2(m.HPCFeed2PE0Pressure,m.HPCFeed2PE0Temp,m.HPCFeed2PE0LiqMFrac["Nitrogen"])
test_model.HPCFeed2PE0SelfVapO2Frac = Constraint(rule=HPCFeed2PE0SelfVapO2Frac)
def HPCFeed2PE0SelfVapN2Frac(m):
	return m.HPCFeed2PE0VapMFrac["Nitrogen"] == triHPCThermo.HPCFeed2SelfCstmVapN2.VapN2(m.HPCFeed2PE0Pressure,m.HPCFeed2PE0Temp,m.HPCFeed2PE0LiqMFrac["Nitrogen"])
test_model.HPCFeed2PE0SelfVapN2Frac = Constraint(rule=HPCFeed2PE0SelfVapN2Frac)
#--------HPCFeed2PE0 Summation---------
def HPCFeed2PE0LiqSum(m):
	return sum([m.HPCFeed2PE0LiqMFrac[c] for c in m.Component]) == 1
test_model.HPCFeed2PE0LiqSum = Constraint(rule=HPCFeed2PE0LiqSum)
def HPCFeed2PE0VapSum(m):
	return sum([m.HPCFeed2PE0VapMFrac[c] for c in m.Component]) == 1
test_model.HPCFeed2PE0VapSum = Constraint(rule=HPCFeed2PE0VapSum)

#----------------------------------
#           HPCPE0
#----------------------------------
#--------HPCPE0 Mass Balance---------
def HPCPE0MassBlnc(m,tray, comp):
	if tray == 1:
		return (m.HPCPE0LiqLvMCompFlow[tray + 1, comp]- m.HPCPE0LiqLvMCompFlow[tray, comp] - m.HPCPE0VapLvMCompFlow[tray, comp]+m.HPCFeed1PE0MFlow*m.HPCFeed1PE0MFrac[comp])*0.001000 == 0
	elif tray == 4:
		return (m.HPCPE0LiqLvMCompFlow[tray + 1, comp] + m.HPCPE0VapLvMCompFlow[tray - 1, comp] - m.HPCPE0LiqLvMCompFlow[tray, comp] - m.HPCPE0VapLvMCompFlow[tray, comp]+m.HPCFeed2PE0MFlow*m.HPCFeed2PE0MFrac[comp])*0.001000 == 0
	elif tray == 6:
		return (m.HPCPE0LiqLvMCompFlow[tray + 1, comp] + m.HPCPE0VapLvMCompFlow[tray - 1, comp] - m.HPCPE0LiqLvMCompFlow[tray, comp] - m.HPCPE0VapLvMCompFlow[tray, comp]-m.HPCPE0Ext6MFlow*m.HPCPE0Ext6MFrac[comp])*0.001000 == 0
	elif tray == 22:
		return (m.HPCPE0LiqLvMCompFlow[tray + 1, comp] + m.HPCPE0VapLvMCompFlow[tray - 1, comp] - m.HPCPE0LiqLvMCompFlow[tray, comp] - m.HPCPE0VapLvMCompFlow[tray, comp]-m.HPCPE0Ext22MFlow*m.HPCPE0Ext22MFrac[comp])*0.001000 == 0
	elif tray == 42:
		return (m.HPCCondPE0RefMFlow*m.HPCPE0VapLvMFrac[42,comp] + m.HPCPE0VapLvMCompFlow[tray - 1, comp] - m.HPCPE0LiqLvMCompFlow[tray, comp] - m.HPCPE0VapLvMCompFlow[tray, comp])*0.001000 == 0
	else:
		return (m.HPCPE0LiqLvMCompFlow[tray + 1, comp] + m.HPCPE0VapLvMCompFlow[tray - 1, comp] - m.HPCPE0LiqLvMCompFlow[tray, comp] - m.HPCPE0VapLvMCompFlow[tray, comp])*0.001000 == 0
test_model.HPCPE0MassBlnc = Constraint(test_model.HPCPE0Trays, test_model.Component, rule=HPCPE0MassBlnc)
#--------HPCPE0 Energy Balance---------
def HPCPE0EngBlnc(m,tray):
	if tray == 1:
		return (m.HPCPE0LiqLvMFlow[tray + 1] * m.HPCPE0LiqLvMEtlp[tray+1] \
		        - m.HPCPE0LiqLvMFlow[tray] * m.HPCPE0LiqLvMEtlp[tray] \
		        - m.HPCPE0VapLvMFlow[tray] * m.HPCPE0VapLvMEtlp[tray]\
		        +m.HPCFeed1PE0MFlow*m.HPCFeed1PE0MEtlp-m.HPCPE0UALeakage*(m.HPCPE0AmbientTemp-m.HPCPE0TrayTemp[tray]))*0.000010 == 0
	elif tray == 4:
		return (m.HPCPE0LiqLvMFlow[tray + 1] * m.HPCPE0LiqLvMEtlp[tray+1] \
		        + m.HPCPE0VapLvMFlow[tray-1] * m.HPCPE0VapLvMEtlp[tray-1] \
		        - m.HPCPE0LiqLvMFlow[tray] * m.HPCPE0LiqLvMEtlp[tray] \
		        - m.HPCPE0VapLvMFlow[tray] * m.HPCPE0VapLvMEtlp[tray]\
		        +m.HPCFeed2PE0MFlow*m.HPCFeed2PE0MEtlp-m.HPCPE0UALeakage*(m.HPCPE0AmbientTemp-m.HPCPE0TrayTemp[tray]))*0.000010 == 0
	elif tray == 6:
		return (m.HPCPE0LiqLvMFlow[tray + 1] * m.HPCPE0LiqLvMEtlp[tray+1] \
		        + m.HPCPE0VapLvMFlow[tray-1] * m.HPCPE0VapLvMEtlp[tray-1] \
		        - m.HPCPE0LiqLvMFlow[tray] * m.HPCPE0LiqLvMEtlp[tray] \
		        - m.HPCPE0VapLvMFlow[tray] * m.HPCPE0VapLvMEtlp[tray]\
		        -m.HPCPE0Ext6MFlow*m.HPCPE0Ext6MEtlp-m.HPCPE0UALeakage*(m.HPCPE0AmbientTemp-m.HPCPE0TrayTemp[tray]))*0.000010 == 0
	elif tray == 22:
		return (m.HPCPE0LiqLvMFlow[tray + 1] * m.HPCPE0LiqLvMEtlp[tray+1] \
		        + m.HPCPE0VapLvMFlow[tray-1] * m.HPCPE0VapLvMEtlp[tray-1] \
		        - m.HPCPE0LiqLvMFlow[tray] * m.HPCPE0LiqLvMEtlp[tray] \
		        - m.HPCPE0VapLvMFlow[tray] * m.HPCPE0VapLvMEtlp[tray]\
		        -m.HPCPE0Ext22MFlow*m.HPCPE0Ext22MEtlp-m.HPCPE0UALeakage*(m.HPCPE0AmbientTemp-m.HPCPE0TrayTemp[tray]))*0.000010 == 0
	elif tray == 42:
		return (m.HPCCondPE0RefMFlow * m.HPCCondPE0OutMEtlp \
		        + m.HPCPE0VapLvMFlow[tray-1] * m.HPCPE0VapLvMEtlp[tray-1] \
		        - m.HPCPE0LiqLvMFlow[tray] * m.HPCPE0LiqLvMEtlp[tray] \
		        - m.HPCPE0VapLvMFlow[tray] * m.HPCPE0VapLvMEtlp[tray]-m.HPCPE0UALeakage*(m.HPCPE0AmbientTemp-m.HPCPE0TrayTemp[tray]))*0.000010 == 0
	else:
		return (m.HPCPE0LiqLvMFlow[tray + 1] * m.HPCPE0LiqLvMEtlp[tray+1] \
		        + m.HPCPE0VapLvMFlow[tray-1] * m.HPCPE0VapLvMEtlp[tray-1] \
		        - m.HPCPE0LiqLvMFlow[tray] * m.HPCPE0LiqLvMEtlp[tray] \
		        - m.HPCPE0VapLvMFlow[tray] * m.HPCPE0VapLvMEtlp[tray]-m.HPCPE0UALeakage*(m.HPCPE0AmbientTemp-m.HPCPE0TrayTemp[tray]))*0.000010 == 0
test_model.HPCPE0EngBlnc = Constraint(test_model.HPCPE0Trays,rule=HPCPE0EngBlnc)
#--------HPCPE0 Phase Equilibrium & System Parts---------
def HPCPE0AllTraysLiqO2Frac(m,tray):
	if tray==1:
		return m.HPCPE0LiqLvMFrac[tray,"Oxygen"] == triHPCThermo.HPCAllTrays1CstmLiqO2.LiqO2(m.HPCPE0TrayPressure[tray],m.HPCPE0TrayTemp[tray],m.HPCPE0LiqLvMFrac[tray,"Nitrogen"])
	elif tray==2:
		return m.HPCPE0LiqLvMFrac[tray,"Oxygen"] == triHPCThermo.HPCAllTrays2CstmLiqO2.LiqO2(m.HPCPE0TrayPressure[tray],m.HPCPE0TrayTemp[tray],m.HPCPE0LiqLvMFrac[tray,"Nitrogen"])
	elif tray==3:
		return m.HPCPE0LiqLvMFrac[tray,"Oxygen"] == triHPCThermo.HPCAllTrays3CstmLiqO2.LiqO2(m.HPCPE0TrayPressure[tray],m.HPCPE0TrayTemp[tray],m.HPCPE0LiqLvMFrac[tray,"Nitrogen"])
	elif tray==4:
		return m.HPCPE0LiqLvMFrac[tray,"Oxygen"] == triHPCThermo.HPCAllTrays4CstmLiqO2.LiqO2(m.HPCPE0TrayPressure[tray],m.HPCPE0TrayTemp[tray],m.HPCPE0LiqLvMFrac[tray,"Nitrogen"])
	elif tray==5:
		return m.HPCPE0LiqLvMFrac[tray,"Oxygen"] == triHPCThermo.HPCAllTrays5CstmLiqO2.LiqO2(m.HPCPE0TrayPressure[tray],m.HPCPE0TrayTemp[tray],m.HPCPE0LiqLvMFrac[tray,"Nitrogen"])
	elif tray==6:
		return m.HPCPE0LiqLvMFrac[tray,"Oxygen"] == triHPCThermo.HPCAllTrays6CstmLiqO2.LiqO2(m.HPCPE0TrayPressure[tray],m.HPCPE0TrayTemp[tray],m.HPCPE0LiqLvMFrac[tray,"Nitrogen"])
	elif tray==7:
		return m.HPCPE0LiqLvMFrac[tray,"Oxygen"] == triHPCThermo.HPCAllTrays7CstmLiqO2.LiqO2(m.HPCPE0TrayPressure[tray],m.HPCPE0TrayTemp[tray],m.HPCPE0LiqLvMFrac[tray,"Nitrogen"])
	elif tray==8:
		return m.HPCPE0LiqLvMFrac[tray,"Oxygen"] == triHPCThermo.HPCAllTrays8CstmLiqO2.LiqO2(m.HPCPE0TrayPressure[tray],m.HPCPE0TrayTemp[tray],m.HPCPE0LiqLvMFrac[tray,"Nitrogen"])
	elif tray==9:
		return m.HPCPE0LiqLvMFrac[tray,"Oxygen"] == triHPCThermo.HPCAllTrays9CstmLiqO2.LiqO2(m.HPCPE0TrayPressure[tray],m.HPCPE0TrayTemp[tray],m.HPCPE0LiqLvMFrac[tray,"Nitrogen"])
	elif tray==10:
		return m.HPCPE0LiqLvMFrac[tray,"Oxygen"] == triHPCThermo.HPCAllTrays10CstmLiqO2.LiqO2(m.HPCPE0TrayPressure[tray],m.HPCPE0TrayTemp[tray],m.HPCPE0LiqLvMFrac[tray,"Nitrogen"])
	elif tray==11:
		return m.HPCPE0LiqLvMFrac[tray,"Oxygen"] == triHPCThermo.HPCAllTrays11CstmLiqO2.LiqO2(m.HPCPE0TrayPressure[tray],m.HPCPE0TrayTemp[tray],m.HPCPE0LiqLvMFrac[tray,"Nitrogen"])
	elif tray==12:
		return m.HPCPE0LiqLvMFrac[tray,"Oxygen"] == triHPCThermo.HPCAllTrays12CstmLiqO2.LiqO2(m.HPCPE0TrayPressure[tray],m.HPCPE0TrayTemp[tray],m.HPCPE0LiqLvMFrac[tray,"Nitrogen"])
	elif tray==13:
		return m.HPCPE0LiqLvMFrac[tray,"Oxygen"] == triHPCThermo.HPCAllTrays13CstmLiqO2.LiqO2(m.HPCPE0TrayPressure[tray],m.HPCPE0TrayTemp[tray],m.HPCPE0LiqLvMFrac[tray,"Nitrogen"])
	elif tray==14:
		return m.HPCPE0LiqLvMFrac[tray,"Oxygen"] == triHPCThermo.HPCAllTrays14CstmLiqO2.LiqO2(m.HPCPE0TrayPressure[tray],m.HPCPE0TrayTemp[tray],m.HPCPE0LiqLvMFrac[tray,"Nitrogen"])
	elif tray==15:
		return m.HPCPE0LiqLvMFrac[tray,"Oxygen"] == triHPCThermo.HPCAllTrays15CstmLiqO2.LiqO2(m.HPCPE0TrayPressure[tray],m.HPCPE0TrayTemp[tray],m.HPCPE0LiqLvMFrac[tray,"Nitrogen"])
	elif tray==16:
		return m.HPCPE0LiqLvMFrac[tray,"Oxygen"] == triHPCThermo.HPCAllTrays16CstmLiqO2.LiqO2(m.HPCPE0TrayPressure[tray],m.HPCPE0TrayTemp[tray],m.HPCPE0LiqLvMFrac[tray,"Nitrogen"])
	elif tray==17:
		return m.HPCPE0LiqLvMFrac[tray,"Oxygen"] == triHPCThermo.HPCAllTrays17CstmLiqO2.LiqO2(m.HPCPE0TrayPressure[tray],m.HPCPE0TrayTemp[tray],m.HPCPE0LiqLvMFrac[tray,"Nitrogen"])
	elif tray==18:
		return m.HPCPE0LiqLvMFrac[tray,"Oxygen"] == triHPCThermo.HPCAllTrays18CstmLiqO2.LiqO2(m.HPCPE0TrayPressure[tray],m.HPCPE0TrayTemp[tray],m.HPCPE0LiqLvMFrac[tray,"Nitrogen"])
	elif tray==19:
		return m.HPCPE0LiqLvMFrac[tray,"Oxygen"] == triHPCThermo.HPCAllTrays19CstmLiqO2.LiqO2(m.HPCPE0TrayPressure[tray],m.HPCPE0TrayTemp[tray],m.HPCPE0LiqLvMFrac[tray,"Nitrogen"])
	elif tray==20:
		return m.HPCPE0LiqLvMFrac[tray,"Oxygen"] == triHPCThermo.HPCAllTrays20CstmLiqO2.LiqO2(m.HPCPE0TrayPressure[tray],m.HPCPE0TrayTemp[tray],m.HPCPE0LiqLvMFrac[tray,"Nitrogen"])
	elif tray==21:
		return m.HPCPE0LiqLvMFrac[tray,"Oxygen"] == triHPCThermo.HPCAllTrays21CstmLiqO2.LiqO2(m.HPCPE0TrayPressure[tray],m.HPCPE0TrayTemp[tray],m.HPCPE0LiqLvMFrac[tray,"Nitrogen"])
	elif tray==22:
		return m.HPCPE0LiqLvMFrac[tray,"Oxygen"] == triHPCThermo.HPCAllTrays22CstmLiqO2.LiqO2(m.HPCPE0TrayPressure[tray],m.HPCPE0TrayTemp[tray],m.HPCPE0LiqLvMFrac[tray,"Nitrogen"])
	elif tray==23:
		return m.HPCPE0LiqLvMFrac[tray,"Oxygen"] == triHPCThermo.HPCAllTrays23CstmLiqO2.LiqO2(m.HPCPE0TrayPressure[tray],m.HPCPE0TrayTemp[tray],m.HPCPE0LiqLvMFrac[tray,"Nitrogen"])
	elif tray==24:
		return m.HPCPE0LiqLvMFrac[tray,"Oxygen"] == triHPCThermo.HPCAllTrays24CstmLiqO2.LiqO2(m.HPCPE0TrayPressure[tray],m.HPCPE0TrayTemp[tray],m.HPCPE0LiqLvMFrac[tray,"Nitrogen"])
	elif tray==25:
		return m.HPCPE0LiqLvMFrac[tray,"Oxygen"] == triHPCThermo.HPCAllTrays25CstmLiqO2.LiqO2(m.HPCPE0TrayPressure[tray],m.HPCPE0TrayTemp[tray],m.HPCPE0LiqLvMFrac[tray,"Nitrogen"])
	elif tray==26:
		return m.HPCPE0LiqLvMFrac[tray,"Oxygen"] == triHPCThermo.HPCAllTrays26CstmLiqO2.LiqO2(m.HPCPE0TrayPressure[tray],m.HPCPE0TrayTemp[tray],m.HPCPE0LiqLvMFrac[tray,"Nitrogen"])
	elif tray==27:
		return m.HPCPE0LiqLvMFrac[tray,"Oxygen"] == triHPCThermo.HPCAllTrays27CstmLiqO2.LiqO2(m.HPCPE0TrayPressure[tray],m.HPCPE0TrayTemp[tray],m.HPCPE0LiqLvMFrac[tray,"Nitrogen"])
	elif tray==28:
		return m.HPCPE0LiqLvMFrac[tray,"Oxygen"] == triHPCThermo.HPCAllTrays28CstmLiqO2.LiqO2(m.HPCPE0TrayPressure[tray],m.HPCPE0TrayTemp[tray],m.HPCPE0LiqLvMFrac[tray,"Nitrogen"])
	elif tray==29:
		return m.HPCPE0LiqLvMFrac[tray,"Oxygen"] == triHPCThermo.HPCAllTrays29CstmLiqO2.LiqO2(m.HPCPE0TrayPressure[tray],m.HPCPE0TrayTemp[tray],m.HPCPE0LiqLvMFrac[tray,"Nitrogen"])
	elif tray==30:
		return m.HPCPE0LiqLvMFrac[tray,"Oxygen"] == triHPCThermo.HPCAllTrays30CstmLiqO2.LiqO2(m.HPCPE0TrayPressure[tray],m.HPCPE0TrayTemp[tray],m.HPCPE0LiqLvMFrac[tray,"Nitrogen"])
	elif tray==31:
		return m.HPCPE0LiqLvMFrac[tray,"Oxygen"] == triHPCThermo.HPCAllTrays31CstmLiqO2.LiqO2(m.HPCPE0TrayPressure[tray],m.HPCPE0TrayTemp[tray],m.HPCPE0LiqLvMFrac[tray,"Nitrogen"])
	elif tray==32:
		return m.HPCPE0LiqLvMFrac[tray,"Oxygen"] == triHPCThermo.HPCAllTrays32CstmLiqO2.LiqO2(m.HPCPE0TrayPressure[tray],m.HPCPE0TrayTemp[tray],m.HPCPE0LiqLvMFrac[tray,"Nitrogen"])
	elif tray==33:
		return m.HPCPE0LiqLvMFrac[tray,"Oxygen"] == triHPCThermo.HPCAllTrays33CstmLiqO2.LiqO2(m.HPCPE0TrayPressure[tray],m.HPCPE0TrayTemp[tray],m.HPCPE0LiqLvMFrac[tray,"Nitrogen"])
	elif tray==34:
		return m.HPCPE0LiqLvMFrac[tray,"Oxygen"] == triHPCThermo.HPCAllTrays34CstmLiqO2.LiqO2(m.HPCPE0TrayPressure[tray],m.HPCPE0TrayTemp[tray],m.HPCPE0LiqLvMFrac[tray,"Nitrogen"])
	elif tray==35:
		return m.HPCPE0LiqLvMFrac[tray,"Oxygen"] == triHPCThermo.HPCAllTrays35CstmLiqO2.LiqO2(m.HPCPE0TrayPressure[tray],m.HPCPE0TrayTemp[tray],m.HPCPE0LiqLvMFrac[tray,"Nitrogen"])
	elif tray==36:
		return m.HPCPE0LiqLvMFrac[tray,"Oxygen"] == triHPCThermo.HPCAllTrays36CstmLiqO2.LiqO2(m.HPCPE0TrayPressure[tray],m.HPCPE0TrayTemp[tray],m.HPCPE0LiqLvMFrac[tray,"Nitrogen"])
	elif tray==37:
		return m.HPCPE0LiqLvMFrac[tray,"Oxygen"] == triHPCThermo.HPCAllTrays37CstmLiqO2.LiqO2(m.HPCPE0TrayPressure[tray],m.HPCPE0TrayTemp[tray],m.HPCPE0LiqLvMFrac[tray,"Nitrogen"])
	elif tray==38:
		return m.HPCPE0LiqLvMFrac[tray,"Oxygen"] == triHPCThermo.HPCAllTrays38CstmLiqO2.LiqO2(m.HPCPE0TrayPressure[tray],m.HPCPE0TrayTemp[tray],m.HPCPE0LiqLvMFrac[tray,"Nitrogen"])
	elif tray==39:
		return m.HPCPE0LiqLvMFrac[tray,"Oxygen"] == triHPCThermo.HPCAllTrays39CstmLiqO2.LiqO2(m.HPCPE0TrayPressure[tray],m.HPCPE0TrayTemp[tray],m.HPCPE0LiqLvMFrac[tray,"Nitrogen"])
	elif tray==40:
		return m.HPCPE0LiqLvMFrac[tray,"Oxygen"] == triHPCThermo.HPCAllTrays40CstmLiqO2.LiqO2(m.HPCPE0TrayPressure[tray],m.HPCPE0TrayTemp[tray],m.HPCPE0LiqLvMFrac[tray,"Nitrogen"])
	elif tray==41:
		return m.HPCPE0LiqLvMFrac[tray,"Oxygen"] == triHPCThermo.HPCAllTrays41CstmLiqO2.LiqO2(m.HPCPE0TrayPressure[tray],m.HPCPE0TrayTemp[tray],m.HPCPE0LiqLvMFrac[tray,"Nitrogen"])
	elif tray==42:
		return m.HPCPE0LiqLvMFrac[tray,"Oxygen"] == triHPCThermo.HPCAllTrays42CstmLiqO2.LiqO2(m.HPCPE0TrayPressure[tray],m.HPCPE0TrayTemp[tray],m.HPCPE0LiqLvMFrac[tray,"Nitrogen"])
test_model.HPCPE0AllTraysLiqO2Frac = Constraint(test_model.HPCPE0Trays,rule=HPCPE0AllTraysLiqO2Frac)
def HPCPE0AllTraysVapO2Frac(m,tray):
	if tray==1:
		return m.HPCPE0VapLvMFrac[tray,"Oxygen"] == triHPCThermo.HPCAllTrays1CstmVapO2.VapO2(m.HPCPE0TrayPressure[tray],m.HPCPE0TrayTemp[tray],m.HPCPE0LiqLvMFrac[tray,"Nitrogen"])
	elif tray==2:
		return m.HPCPE0VapLvMFrac[tray,"Oxygen"] == triHPCThermo.HPCAllTrays2CstmVapO2.VapO2(m.HPCPE0TrayPressure[tray],m.HPCPE0TrayTemp[tray],m.HPCPE0LiqLvMFrac[tray,"Nitrogen"])
	elif tray==3:
		return m.HPCPE0VapLvMFrac[tray,"Oxygen"] == triHPCThermo.HPCAllTrays3CstmVapO2.VapO2(m.HPCPE0TrayPressure[tray],m.HPCPE0TrayTemp[tray],m.HPCPE0LiqLvMFrac[tray,"Nitrogen"])
	elif tray==4:
		return m.HPCPE0VapLvMFrac[tray,"Oxygen"] == triHPCThermo.HPCAllTrays4CstmVapO2.VapO2(m.HPCPE0TrayPressure[tray],m.HPCPE0TrayTemp[tray],m.HPCPE0LiqLvMFrac[tray,"Nitrogen"])
	elif tray==5:
		return m.HPCPE0VapLvMFrac[tray,"Oxygen"] == triHPCThermo.HPCAllTrays5CstmVapO2.VapO2(m.HPCPE0TrayPressure[tray],m.HPCPE0TrayTemp[tray],m.HPCPE0LiqLvMFrac[tray,"Nitrogen"])
	elif tray==6:
		return m.HPCPE0VapLvMFrac[tray,"Oxygen"] == triHPCThermo.HPCAllTrays6CstmVapO2.VapO2(m.HPCPE0TrayPressure[tray],m.HPCPE0TrayTemp[tray],m.HPCPE0LiqLvMFrac[tray,"Nitrogen"])
	elif tray==7:
		return m.HPCPE0VapLvMFrac[tray,"Oxygen"] == triHPCThermo.HPCAllTrays7CstmVapO2.VapO2(m.HPCPE0TrayPressure[tray],m.HPCPE0TrayTemp[tray],m.HPCPE0LiqLvMFrac[tray,"Nitrogen"])
	elif tray==8:
		return m.HPCPE0VapLvMFrac[tray,"Oxygen"] == triHPCThermo.HPCAllTrays8CstmVapO2.VapO2(m.HPCPE0TrayPressure[tray],m.HPCPE0TrayTemp[tray],m.HPCPE0LiqLvMFrac[tray,"Nitrogen"])
	elif tray==9:
		return m.HPCPE0VapLvMFrac[tray,"Oxygen"] == triHPCThermo.HPCAllTrays9CstmVapO2.VapO2(m.HPCPE0TrayPressure[tray],m.HPCPE0TrayTemp[tray],m.HPCPE0LiqLvMFrac[tray,"Nitrogen"])
	elif tray==10:
		return m.HPCPE0VapLvMFrac[tray,"Oxygen"] == triHPCThermo.HPCAllTrays10CstmVapO2.VapO2(m.HPCPE0TrayPressure[tray],m.HPCPE0TrayTemp[tray],m.HPCPE0LiqLvMFrac[tray,"Nitrogen"])
	elif tray==11:
		return m.HPCPE0VapLvMFrac[tray,"Oxygen"] == triHPCThermo.HPCAllTrays11CstmVapO2.VapO2(m.HPCPE0TrayPressure[tray],m.HPCPE0TrayTemp[tray],m.HPCPE0LiqLvMFrac[tray,"Nitrogen"])
	elif tray==12:
		return m.HPCPE0VapLvMFrac[tray,"Oxygen"] == triHPCThermo.HPCAllTrays12CstmVapO2.VapO2(m.HPCPE0TrayPressure[tray],m.HPCPE0TrayTemp[tray],m.HPCPE0LiqLvMFrac[tray,"Nitrogen"])
	elif tray==13:
		return m.HPCPE0VapLvMFrac[tray,"Oxygen"] == triHPCThermo.HPCAllTrays13CstmVapO2.VapO2(m.HPCPE0TrayPressure[tray],m.HPCPE0TrayTemp[tray],m.HPCPE0LiqLvMFrac[tray,"Nitrogen"])
	elif tray==14:
		return m.HPCPE0VapLvMFrac[tray,"Oxygen"] == triHPCThermo.HPCAllTrays14CstmVapO2.VapO2(m.HPCPE0TrayPressure[tray],m.HPCPE0TrayTemp[tray],m.HPCPE0LiqLvMFrac[tray,"Nitrogen"])
	elif tray==15:
		return m.HPCPE0VapLvMFrac[tray,"Oxygen"] == triHPCThermo.HPCAllTrays15CstmVapO2.VapO2(m.HPCPE0TrayPressure[tray],m.HPCPE0TrayTemp[tray],m.HPCPE0LiqLvMFrac[tray,"Nitrogen"])
	elif tray==16:
		return m.HPCPE0VapLvMFrac[tray,"Oxygen"] == triHPCThermo.HPCAllTrays16CstmVapO2.VapO2(m.HPCPE0TrayPressure[tray],m.HPCPE0TrayTemp[tray],m.HPCPE0LiqLvMFrac[tray,"Nitrogen"])
	elif tray==17:
		return m.HPCPE0VapLvMFrac[tray,"Oxygen"] == triHPCThermo.HPCAllTrays17CstmVapO2.VapO2(m.HPCPE0TrayPressure[tray],m.HPCPE0TrayTemp[tray],m.HPCPE0LiqLvMFrac[tray,"Nitrogen"])
	elif tray==18:
		return m.HPCPE0VapLvMFrac[tray,"Oxygen"] == triHPCThermo.HPCAllTrays18CstmVapO2.VapO2(m.HPCPE0TrayPressure[tray],m.HPCPE0TrayTemp[tray],m.HPCPE0LiqLvMFrac[tray,"Nitrogen"])
	elif tray==19:
		return m.HPCPE0VapLvMFrac[tray,"Oxygen"] == triHPCThermo.HPCAllTrays19CstmVapO2.VapO2(m.HPCPE0TrayPressure[tray],m.HPCPE0TrayTemp[tray],m.HPCPE0LiqLvMFrac[tray,"Nitrogen"])
	elif tray==20:
		return m.HPCPE0VapLvMFrac[tray,"Oxygen"] == triHPCThermo.HPCAllTrays20CstmVapO2.VapO2(m.HPCPE0TrayPressure[tray],m.HPCPE0TrayTemp[tray],m.HPCPE0LiqLvMFrac[tray,"Nitrogen"])
	elif tray==21:
		return m.HPCPE0VapLvMFrac[tray,"Oxygen"] == triHPCThermo.HPCAllTrays21CstmVapO2.VapO2(m.HPCPE0TrayPressure[tray],m.HPCPE0TrayTemp[tray],m.HPCPE0LiqLvMFrac[tray,"Nitrogen"])
	elif tray==22:
		return m.HPCPE0VapLvMFrac[tray,"Oxygen"] == triHPCThermo.HPCAllTrays22CstmVapO2.VapO2(m.HPCPE0TrayPressure[tray],m.HPCPE0TrayTemp[tray],m.HPCPE0LiqLvMFrac[tray,"Nitrogen"])
	elif tray==23:
		return m.HPCPE0VapLvMFrac[tray,"Oxygen"] == triHPCThermo.HPCAllTrays23CstmVapO2.VapO2(m.HPCPE0TrayPressure[tray],m.HPCPE0TrayTemp[tray],m.HPCPE0LiqLvMFrac[tray,"Nitrogen"])
	elif tray==24:
		return m.HPCPE0VapLvMFrac[tray,"Oxygen"] == triHPCThermo.HPCAllTrays24CstmVapO2.VapO2(m.HPCPE0TrayPressure[tray],m.HPCPE0TrayTemp[tray],m.HPCPE0LiqLvMFrac[tray,"Nitrogen"])
	elif tray==25:
		return m.HPCPE0VapLvMFrac[tray,"Oxygen"] == triHPCThermo.HPCAllTrays25CstmVapO2.VapO2(m.HPCPE0TrayPressure[tray],m.HPCPE0TrayTemp[tray],m.HPCPE0LiqLvMFrac[tray,"Nitrogen"])
	elif tray==26:
		return m.HPCPE0VapLvMFrac[tray,"Oxygen"] == triHPCThermo.HPCAllTrays26CstmVapO2.VapO2(m.HPCPE0TrayPressure[tray],m.HPCPE0TrayTemp[tray],m.HPCPE0LiqLvMFrac[tray,"Nitrogen"])
	elif tray==27:
		return m.HPCPE0VapLvMFrac[tray,"Oxygen"] == triHPCThermo.HPCAllTrays27CstmVapO2.VapO2(m.HPCPE0TrayPressure[tray],m.HPCPE0TrayTemp[tray],m.HPCPE0LiqLvMFrac[tray,"Nitrogen"])
	elif tray==28:
		return m.HPCPE0VapLvMFrac[tray,"Oxygen"] == triHPCThermo.HPCAllTrays28CstmVapO2.VapO2(m.HPCPE0TrayPressure[tray],m.HPCPE0TrayTemp[tray],m.HPCPE0LiqLvMFrac[tray,"Nitrogen"])
	elif tray==29:
		return m.HPCPE0VapLvMFrac[tray,"Oxygen"] == triHPCThermo.HPCAllTrays29CstmVapO2.VapO2(m.HPCPE0TrayPressure[tray],m.HPCPE0TrayTemp[tray],m.HPCPE0LiqLvMFrac[tray,"Nitrogen"])
	elif tray==30:
		return m.HPCPE0VapLvMFrac[tray,"Oxygen"] == triHPCThermo.HPCAllTrays30CstmVapO2.VapO2(m.HPCPE0TrayPressure[tray],m.HPCPE0TrayTemp[tray],m.HPCPE0LiqLvMFrac[tray,"Nitrogen"])
	elif tray==31:
		return m.HPCPE0VapLvMFrac[tray,"Oxygen"] == triHPCThermo.HPCAllTrays31CstmVapO2.VapO2(m.HPCPE0TrayPressure[tray],m.HPCPE0TrayTemp[tray],m.HPCPE0LiqLvMFrac[tray,"Nitrogen"])
	elif tray==32:
		return m.HPCPE0VapLvMFrac[tray,"Oxygen"] == triHPCThermo.HPCAllTrays32CstmVapO2.VapO2(m.HPCPE0TrayPressure[tray],m.HPCPE0TrayTemp[tray],m.HPCPE0LiqLvMFrac[tray,"Nitrogen"])
	elif tray==33:
		return m.HPCPE0VapLvMFrac[tray,"Oxygen"] == triHPCThermo.HPCAllTrays33CstmVapO2.VapO2(m.HPCPE0TrayPressure[tray],m.HPCPE0TrayTemp[tray],m.HPCPE0LiqLvMFrac[tray,"Nitrogen"])
	elif tray==34:
		return m.HPCPE0VapLvMFrac[tray,"Oxygen"] == triHPCThermo.HPCAllTrays34CstmVapO2.VapO2(m.HPCPE0TrayPressure[tray],m.HPCPE0TrayTemp[tray],m.HPCPE0LiqLvMFrac[tray,"Nitrogen"])
	elif tray==35:
		return m.HPCPE0VapLvMFrac[tray,"Oxygen"] == triHPCThermo.HPCAllTrays35CstmVapO2.VapO2(m.HPCPE0TrayPressure[tray],m.HPCPE0TrayTemp[tray],m.HPCPE0LiqLvMFrac[tray,"Nitrogen"])
	elif tray==36:
		return m.HPCPE0VapLvMFrac[tray,"Oxygen"] == triHPCThermo.HPCAllTrays36CstmVapO2.VapO2(m.HPCPE0TrayPressure[tray],m.HPCPE0TrayTemp[tray],m.HPCPE0LiqLvMFrac[tray,"Nitrogen"])
	elif tray==37:
		return m.HPCPE0VapLvMFrac[tray,"Oxygen"] == triHPCThermo.HPCAllTrays37CstmVapO2.VapO2(m.HPCPE0TrayPressure[tray],m.HPCPE0TrayTemp[tray],m.HPCPE0LiqLvMFrac[tray,"Nitrogen"])
	elif tray==38:
		return m.HPCPE0VapLvMFrac[tray,"Oxygen"] == triHPCThermo.HPCAllTrays38CstmVapO2.VapO2(m.HPCPE0TrayPressure[tray],m.HPCPE0TrayTemp[tray],m.HPCPE0LiqLvMFrac[tray,"Nitrogen"])
	elif tray==39:
		return m.HPCPE0VapLvMFrac[tray,"Oxygen"] == triHPCThermo.HPCAllTrays39CstmVapO2.VapO2(m.HPCPE0TrayPressure[tray],m.HPCPE0TrayTemp[tray],m.HPCPE0LiqLvMFrac[tray,"Nitrogen"])
	elif tray==40:
		return m.HPCPE0VapLvMFrac[tray,"Oxygen"] == triHPCThermo.HPCAllTrays40CstmVapO2.VapO2(m.HPCPE0TrayPressure[tray],m.HPCPE0TrayTemp[tray],m.HPCPE0LiqLvMFrac[tray,"Nitrogen"])
	elif tray==41:
		return m.HPCPE0VapLvMFrac[tray,"Oxygen"] == triHPCThermo.HPCAllTrays41CstmVapO2.VapO2(m.HPCPE0TrayPressure[tray],m.HPCPE0TrayTemp[tray],m.HPCPE0LiqLvMFrac[tray,"Nitrogen"])
	elif tray==42:
		return m.HPCPE0VapLvMFrac[tray,"Oxygen"] == triHPCThermo.HPCAllTrays42CstmVapO2.VapO2(m.HPCPE0TrayPressure[tray],m.HPCPE0TrayTemp[tray],m.HPCPE0LiqLvMFrac[tray,"Nitrogen"])
test_model.HPCPE0AllTraysVapO2Frac = Constraint(test_model.HPCPE0Trays,rule=HPCPE0AllTraysVapO2Frac)
def HPCPE0AllTraysVapN2Frac(m,tray):
	if tray==1:
		return m.HPCPE0VapLvMFrac[tray,"Nitrogen"] == triHPCThermo.HPCAllTrays1CstmVapN2.VapN2(m.HPCPE0TrayPressure[tray],m.HPCPE0TrayTemp[tray],m.HPCPE0LiqLvMFrac[tray,"Nitrogen"])
	elif tray==2:
		return m.HPCPE0VapLvMFrac[tray,"Nitrogen"] == triHPCThermo.HPCAllTrays2CstmVapN2.VapN2(m.HPCPE0TrayPressure[tray],m.HPCPE0TrayTemp[tray],m.HPCPE0LiqLvMFrac[tray,"Nitrogen"])
	elif tray==3:
		return m.HPCPE0VapLvMFrac[tray,"Nitrogen"] == triHPCThermo.HPCAllTrays3CstmVapN2.VapN2(m.HPCPE0TrayPressure[tray],m.HPCPE0TrayTemp[tray],m.HPCPE0LiqLvMFrac[tray,"Nitrogen"])
	elif tray==4:
		return m.HPCPE0VapLvMFrac[tray,"Nitrogen"] == triHPCThermo.HPCAllTrays4CstmVapN2.VapN2(m.HPCPE0TrayPressure[tray],m.HPCPE0TrayTemp[tray],m.HPCPE0LiqLvMFrac[tray,"Nitrogen"])
	elif tray==5:
		return m.HPCPE0VapLvMFrac[tray,"Nitrogen"] == triHPCThermo.HPCAllTrays5CstmVapN2.VapN2(m.HPCPE0TrayPressure[tray],m.HPCPE0TrayTemp[tray],m.HPCPE0LiqLvMFrac[tray,"Nitrogen"])
	elif tray==6:
		return m.HPCPE0VapLvMFrac[tray,"Nitrogen"] == triHPCThermo.HPCAllTrays6CstmVapN2.VapN2(m.HPCPE0TrayPressure[tray],m.HPCPE0TrayTemp[tray],m.HPCPE0LiqLvMFrac[tray,"Nitrogen"])
	elif tray==7:
		return m.HPCPE0VapLvMFrac[tray,"Nitrogen"] == triHPCThermo.HPCAllTrays7CstmVapN2.VapN2(m.HPCPE0TrayPressure[tray],m.HPCPE0TrayTemp[tray],m.HPCPE0LiqLvMFrac[tray,"Nitrogen"])
	elif tray==8:
		return m.HPCPE0VapLvMFrac[tray,"Nitrogen"] == triHPCThermo.HPCAllTrays8CstmVapN2.VapN2(m.HPCPE0TrayPressure[tray],m.HPCPE0TrayTemp[tray],m.HPCPE0LiqLvMFrac[tray,"Nitrogen"])
	elif tray==9:
		return m.HPCPE0VapLvMFrac[tray,"Nitrogen"] == triHPCThermo.HPCAllTrays9CstmVapN2.VapN2(m.HPCPE0TrayPressure[tray],m.HPCPE0TrayTemp[tray],m.HPCPE0LiqLvMFrac[tray,"Nitrogen"])
	elif tray==10:
		return m.HPCPE0VapLvMFrac[tray,"Nitrogen"] == triHPCThermo.HPCAllTrays10CstmVapN2.VapN2(m.HPCPE0TrayPressure[tray],m.HPCPE0TrayTemp[tray],m.HPCPE0LiqLvMFrac[tray,"Nitrogen"])
	elif tray==11:
		return m.HPCPE0VapLvMFrac[tray,"Nitrogen"] == triHPCThermo.HPCAllTrays11CstmVapN2.VapN2(m.HPCPE0TrayPressure[tray],m.HPCPE0TrayTemp[tray],m.HPCPE0LiqLvMFrac[tray,"Nitrogen"])
	elif tray==12:
		return m.HPCPE0VapLvMFrac[tray,"Nitrogen"] == triHPCThermo.HPCAllTrays12CstmVapN2.VapN2(m.HPCPE0TrayPressure[tray],m.HPCPE0TrayTemp[tray],m.HPCPE0LiqLvMFrac[tray,"Nitrogen"])
	elif tray==13:
		return m.HPCPE0VapLvMFrac[tray,"Nitrogen"] == triHPCThermo.HPCAllTrays13CstmVapN2.VapN2(m.HPCPE0TrayPressure[tray],m.HPCPE0TrayTemp[tray],m.HPCPE0LiqLvMFrac[tray,"Nitrogen"])
	elif tray==14:
		return m.HPCPE0VapLvMFrac[tray,"Nitrogen"] == triHPCThermo.HPCAllTrays14CstmVapN2.VapN2(m.HPCPE0TrayPressure[tray],m.HPCPE0TrayTemp[tray],m.HPCPE0LiqLvMFrac[tray,"Nitrogen"])
	elif tray==15:
		return m.HPCPE0VapLvMFrac[tray,"Nitrogen"] == triHPCThermo.HPCAllTrays15CstmVapN2.VapN2(m.HPCPE0TrayPressure[tray],m.HPCPE0TrayTemp[tray],m.HPCPE0LiqLvMFrac[tray,"Nitrogen"])
	elif tray==16:
		return m.HPCPE0VapLvMFrac[tray,"Nitrogen"] == triHPCThermo.HPCAllTrays16CstmVapN2.VapN2(m.HPCPE0TrayPressure[tray],m.HPCPE0TrayTemp[tray],m.HPCPE0LiqLvMFrac[tray,"Nitrogen"])
	elif tray==17:
		return m.HPCPE0VapLvMFrac[tray,"Nitrogen"] == triHPCThermo.HPCAllTrays17CstmVapN2.VapN2(m.HPCPE0TrayPressure[tray],m.HPCPE0TrayTemp[tray],m.HPCPE0LiqLvMFrac[tray,"Nitrogen"])
	elif tray==18:
		return m.HPCPE0VapLvMFrac[tray,"Nitrogen"] == triHPCThermo.HPCAllTrays18CstmVapN2.VapN2(m.HPCPE0TrayPressure[tray],m.HPCPE0TrayTemp[tray],m.HPCPE0LiqLvMFrac[tray,"Nitrogen"])
	elif tray==19:
		return m.HPCPE0VapLvMFrac[tray,"Nitrogen"] == triHPCThermo.HPCAllTrays19CstmVapN2.VapN2(m.HPCPE0TrayPressure[tray],m.HPCPE0TrayTemp[tray],m.HPCPE0LiqLvMFrac[tray,"Nitrogen"])
	elif tray==20:
		return m.HPCPE0VapLvMFrac[tray,"Nitrogen"] == triHPCThermo.HPCAllTrays20CstmVapN2.VapN2(m.HPCPE0TrayPressure[tray],m.HPCPE0TrayTemp[tray],m.HPCPE0LiqLvMFrac[tray,"Nitrogen"])
	elif tray==21:
		return m.HPCPE0VapLvMFrac[tray,"Nitrogen"] == triHPCThermo.HPCAllTrays21CstmVapN2.VapN2(m.HPCPE0TrayPressure[tray],m.HPCPE0TrayTemp[tray],m.HPCPE0LiqLvMFrac[tray,"Nitrogen"])
	elif tray==22:
		return m.HPCPE0VapLvMFrac[tray,"Nitrogen"] == triHPCThermo.HPCAllTrays22CstmVapN2.VapN2(m.HPCPE0TrayPressure[tray],m.HPCPE0TrayTemp[tray],m.HPCPE0LiqLvMFrac[tray,"Nitrogen"])
	elif tray==23:
		return m.HPCPE0VapLvMFrac[tray,"Nitrogen"] == triHPCThermo.HPCAllTrays23CstmVapN2.VapN2(m.HPCPE0TrayPressure[tray],m.HPCPE0TrayTemp[tray],m.HPCPE0LiqLvMFrac[tray,"Nitrogen"])
	elif tray==24:
		return m.HPCPE0VapLvMFrac[tray,"Nitrogen"] == triHPCThermo.HPCAllTrays24CstmVapN2.VapN2(m.HPCPE0TrayPressure[tray],m.HPCPE0TrayTemp[tray],m.HPCPE0LiqLvMFrac[tray,"Nitrogen"])
	elif tray==25:
		return m.HPCPE0VapLvMFrac[tray,"Nitrogen"] == triHPCThermo.HPCAllTrays25CstmVapN2.VapN2(m.HPCPE0TrayPressure[tray],m.HPCPE0TrayTemp[tray],m.HPCPE0LiqLvMFrac[tray,"Nitrogen"])
	elif tray==26:
		return m.HPCPE0VapLvMFrac[tray,"Nitrogen"] == triHPCThermo.HPCAllTrays26CstmVapN2.VapN2(m.HPCPE0TrayPressure[tray],m.HPCPE0TrayTemp[tray],m.HPCPE0LiqLvMFrac[tray,"Nitrogen"])
	elif tray==27:
		return m.HPCPE0VapLvMFrac[tray,"Nitrogen"] == triHPCThermo.HPCAllTrays27CstmVapN2.VapN2(m.HPCPE0TrayPressure[tray],m.HPCPE0TrayTemp[tray],m.HPCPE0LiqLvMFrac[tray,"Nitrogen"])
	elif tray==28:
		return m.HPCPE0VapLvMFrac[tray,"Nitrogen"] == triHPCThermo.HPCAllTrays28CstmVapN2.VapN2(m.HPCPE0TrayPressure[tray],m.HPCPE0TrayTemp[tray],m.HPCPE0LiqLvMFrac[tray,"Nitrogen"])
	elif tray==29:
		return m.HPCPE0VapLvMFrac[tray,"Nitrogen"] == triHPCThermo.HPCAllTrays29CstmVapN2.VapN2(m.HPCPE0TrayPressure[tray],m.HPCPE0TrayTemp[tray],m.HPCPE0LiqLvMFrac[tray,"Nitrogen"])
	elif tray==30:
		return m.HPCPE0VapLvMFrac[tray,"Nitrogen"] == triHPCThermo.HPCAllTrays30CstmVapN2.VapN2(m.HPCPE0TrayPressure[tray],m.HPCPE0TrayTemp[tray],m.HPCPE0LiqLvMFrac[tray,"Nitrogen"])
	elif tray==31:
		return m.HPCPE0VapLvMFrac[tray,"Nitrogen"] == triHPCThermo.HPCAllTrays31CstmVapN2.VapN2(m.HPCPE0TrayPressure[tray],m.HPCPE0TrayTemp[tray],m.HPCPE0LiqLvMFrac[tray,"Nitrogen"])
	elif tray==32:
		return m.HPCPE0VapLvMFrac[tray,"Nitrogen"] == triHPCThermo.HPCAllTrays32CstmVapN2.VapN2(m.HPCPE0TrayPressure[tray],m.HPCPE0TrayTemp[tray],m.HPCPE0LiqLvMFrac[tray,"Nitrogen"])
	elif tray==33:
		return m.HPCPE0VapLvMFrac[tray,"Nitrogen"] == triHPCThermo.HPCAllTrays33CstmVapN2.VapN2(m.HPCPE0TrayPressure[tray],m.HPCPE0TrayTemp[tray],m.HPCPE0LiqLvMFrac[tray,"Nitrogen"])
	elif tray==34:
		return m.HPCPE0VapLvMFrac[tray,"Nitrogen"] == triHPCThermo.HPCAllTrays34CstmVapN2.VapN2(m.HPCPE0TrayPressure[tray],m.HPCPE0TrayTemp[tray],m.HPCPE0LiqLvMFrac[tray,"Nitrogen"])
	elif tray==35:
		return m.HPCPE0VapLvMFrac[tray,"Nitrogen"] == triHPCThermo.HPCAllTrays35CstmVapN2.VapN2(m.HPCPE0TrayPressure[tray],m.HPCPE0TrayTemp[tray],m.HPCPE0LiqLvMFrac[tray,"Nitrogen"])
	elif tray==36:
		return m.HPCPE0VapLvMFrac[tray,"Nitrogen"] == triHPCThermo.HPCAllTrays36CstmVapN2.VapN2(m.HPCPE0TrayPressure[tray],m.HPCPE0TrayTemp[tray],m.HPCPE0LiqLvMFrac[tray,"Nitrogen"])
	elif tray==37:
		return m.HPCPE0VapLvMFrac[tray,"Nitrogen"] == triHPCThermo.HPCAllTrays37CstmVapN2.VapN2(m.HPCPE0TrayPressure[tray],m.HPCPE0TrayTemp[tray],m.HPCPE0LiqLvMFrac[tray,"Nitrogen"])
	elif tray==38:
		return m.HPCPE0VapLvMFrac[tray,"Nitrogen"] == triHPCThermo.HPCAllTrays38CstmVapN2.VapN2(m.HPCPE0TrayPressure[tray],m.HPCPE0TrayTemp[tray],m.HPCPE0LiqLvMFrac[tray,"Nitrogen"])
	elif tray==39:
		return m.HPCPE0VapLvMFrac[tray,"Nitrogen"] == triHPCThermo.HPCAllTrays39CstmVapN2.VapN2(m.HPCPE0TrayPressure[tray],m.HPCPE0TrayTemp[tray],m.HPCPE0LiqLvMFrac[tray,"Nitrogen"])
	elif tray==40:
		return m.HPCPE0VapLvMFrac[tray,"Nitrogen"] == triHPCThermo.HPCAllTrays40CstmVapN2.VapN2(m.HPCPE0TrayPressure[tray],m.HPCPE0TrayTemp[tray],m.HPCPE0LiqLvMFrac[tray,"Nitrogen"])
	elif tray==41:
		return m.HPCPE0VapLvMFrac[tray,"Nitrogen"] == triHPCThermo.HPCAllTrays41CstmVapN2.VapN2(m.HPCPE0TrayPressure[tray],m.HPCPE0TrayTemp[tray],m.HPCPE0LiqLvMFrac[tray,"Nitrogen"])
	elif tray==42:
		return m.HPCPE0VapLvMFrac[tray,"Nitrogen"] == triHPCThermo.HPCAllTrays42CstmVapN2.VapN2(m.HPCPE0TrayPressure[tray],m.HPCPE0TrayTemp[tray],m.HPCPE0LiqLvMFrac[tray,"Nitrogen"])
test_model.HPCPE0AllTraysVapN2Frac = Constraint(test_model.HPCPE0Trays,rule=HPCPE0AllTraysVapN2Frac)
#--------HPCPE0 Summation---------
def HPCPE0LiqSum(m, tray):
	return sum([m.HPCPE0LiqLvMFrac[tray, c] for c in m.Component]) == 1
test_model.HPCPE0LiqSum = Constraint(test_model.HPCPE0Trays, rule=HPCPE0LiqSum)
def HPCPE0VapSum(m, tray):
	return sum([m.HPCPE0VapLvMFrac[tray, c] for c in m.Component]) == 1
test_model.HPCPE0VapSum = Constraint(test_model.HPCPE0Trays, rule=HPCPE0VapSum)
#--------HPCPE0 Pressure Profile---------
def HPCPE0PProf(m, tray):
	return ((m.HPCPE0TopPressure-m.HPCPE0BtmPressure)/41*(tray-1)+m.HPCPE0BtmPressure - m.HPCPE0TrayPressure[tray])*0.010000 == 0
test_model.HPCPE0PProf = Constraint(test_model.HPCPE0Trays, rule=HPCPE0PProf)
#--------HPCPE0 Extractions---------
def HPCPE0Ext6MFracSpec(m, comp):
	return m.HPCPE0Ext6MFrac[comp] - m.HPCPE0LiqLvMFrac[6, comp] == 0 
test_model.HPCPE0Ext6MFracSpec = Constraint(test_model.Component, rule=HPCPE0Ext6MFracSpec)
def HPCPE0Ext6MEtlpSpec(m):
	return (m.HPCPE0Ext6MEtlp - m.HPCPE0LiqLvMEtlp[6])*  0.000010 == 0
test_model.HPCPE0Ext6MEtlpSpec = Constraint(rule=HPCPE0Ext6MEtlpSpec)
def HPCPE0Ext22MFracSpec(m, comp):
	return m.HPCPE0Ext22MFrac[comp] - m.HPCPE0VapLvMFrac[22, comp] == 0 
test_model.HPCPE0Ext22MFracSpec = Constraint(test_model.Component, rule=HPCPE0Ext22MFracSpec)
def HPCPE0Ext22MEtlpSpec(m):
	return (m.HPCPE0Ext22MEtlp - m.HPCPE0VapLvMEtlp[22])*  0.000010 == 0
test_model.HPCPE0Ext22MEtlpSpec = Constraint(rule=HPCPE0Ext22MEtlpSpec)

#----------------------------------
#           HPCSumpPE0
#----------------------------------
#--------HPCSumpPE0 Mass Balance---------
def HPCSumpPE0MassBlnc(m):
	return (m.HPCPE0LiqLvMFlow[1]-m.HPCSumpPE0OutMFlow)*0.001000==0
test_model.HPCSumpPE0MassBlnc = Constraint(rule=HPCSumpPE0MassBlnc)
def HPCSumpPE0HldpMFracSpec(m, comp):
	return m.HPCSumpPE0HldpMFrac[comp] - m.HPCPE0LiqLvMFrac[1,comp] == 0
test_model.HPCSumpPE0HldpMFracSpec = Constraint(test_model.Component, rule=HPCSumpPE0HldpMFracSpec)

#----------------------------------
#           HPCCondPE0
#----------------------------------
#--------HPCCondPE0 Mass Balance---------
def HPCCondPE0MassBlnc(m):
	return (m.HPCCondPE0RefMFlow+m.HPCCondPE0PrdtMFlow-m.HPCPE0VapLvMFlow[42])*0.001000==0
test_model.HPCCondPE0MassBlnc = Constraint(rule=HPCCondPE0MassBlnc)
def HPCCondPE0RefSpec(m):
	return (m.HPCCondPE0RefMFlow-m.HPCPE0VapLvMFlow[42]*m.HPCCondPE0RefluxRatio)*0.001000==0
test_model.HPCCondPE0RefSpec = Constraint(rule=HPCCondPE0RefSpec)
#--------HPCCondPE0 Energy Balance---------
def HPCCondPE0EngBlnc(m):
	return (m.HPCPE0VapLvMFlow[42]*(m.HPCPE0VapLvMEtlp[42]-m.HPCCondPE0OutMEtlp)-m.HPCCondPE0MHeatOut)*0.000010==0
test_model.HPCCondPE0EngBlnc = Constraint(rule=HPCCondPE0EngBlnc)
#--------HPCCondPE0 Bubble Point---------
def HPCCondPE0SelfBubTemp(m):
	return m.HPCPE0VapLvMFrac[42,"Oxygen"] == triHPCThermo.HPCCondSelfCstmLiqO2.LiqO2(m.HPCPE0TrayPressure[42],m.HPCCondPE0Temp,m.HPCPE0VapLvMFrac[42,"Nitrogen"])
test_model.HPCCondPE0SelfBubTemp = Constraint(rule=HPCCondPE0SelfBubTemp)

#===========================================
#===========================================
#===                                     ===
#===        PE MODEL SECTION  1          ===
#===                                     ===
#===========================================
#===========================================

#===================================
#
#      Parameters & Sets
#
#===================================
#--------HPCFeed1PE1---------
test_model.HPCFeed1PE1MFrac = Param(test_model.Component, initialize = {'Oxygen': 0.2095, 'Nitrogen': 0.7812, 'Argon': 0.0093})
test_model.HPCFeed1PE1Pressure = Param(initialize = 564.000000)
test_model.HPCFeed1PE1VF = Param(initialize = 0.980000)
#--------HPCFeed2PE1---------
test_model.HPCFeed2PE1MFrac = Param(test_model.Component, initialize = {'Oxygen': 0.2095, 'Nitrogen': 0.7812, 'Argon': 0.0093})
test_model.HPCFeed2PE1Pressure = Param(initialize = 562.600000)
test_model.HPCFeed2PE1VF = Param(initialize = 0.084100)
#--------HPCPE1---------
test_model.HPCPE1Trays = RangeSet(1, 42)
test_model.HPCPE1Ext6MFlow = Param(initialize = 829.800000)
test_model.HPCPE1Ext22MFlow = Param(initialize = 47.290000)
test_model.HPCPE1TopPressure = Param(initialize = 538.600000)
test_model.HPCPE1BtmPressure = Param(initialize = 564.000000)
test_model.HPCPE1UALeakage = Var(initialize = 10.000000, within=NonNegativeReals)
test_model.HPCPE1AmbientTemp = Var(initialize = 25.000000, bounds = (10,40))
#--------HPCSumpPE1---------
test_model.HPCSumpPE1LiqRho = Param(initialize = 1000.000000)
test_model.HPCSumpPE1SumpCSArea = Param(initialize = 6.000000)
#--------HPCCondPE1---------
test_model.HPCCondPE1RefluxRatio = Param(initialize = 0.564650)

#===================================
#
#         Variables
#
#===================================
#--------HPCFeed1PE1---------
test_model.HPCFeed1PE1Temp = Var()
test_model.HPCFeed1PE1LiqMFrac = Var(test_model.Component, bounds=(0, 1))
test_model.HPCFeed1PE1VapMFrac = Var(test_model.Component, bounds=(0, 1))
#--------HPCFeed2PE1---------
test_model.HPCFeed2PE1Temp = Var()
test_model.HPCFeed2PE1LiqMFrac = Var(test_model.Component, bounds=(0, 1))
test_model.HPCFeed2PE1VapMFrac = Var(test_model.Component, bounds=(0, 1))
#--------HPCPE1---------
test_model.HPCPE1VapLvMFlow = Var(test_model.HPCPE1Trays, within=NonNegativeReals)
test_model.HPCPE1LiqLvMFlow = Var(test_model.HPCPE1Trays, within=NonNegativeReals)
test_model.HPCPE1TrayTemp = Var(test_model.HPCPE1Trays)
test_model.HPCPE1TrayPressure = Var(test_model.HPCPE1Trays)
test_model.HPCPE1LiqLvMFrac = Var(test_model.HPCPE1Trays,test_model.Component, bounds=(0, 1))
test_model.HPCPE1VapLvMFrac = Var(test_model.HPCPE1Trays,test_model.Component, bounds=(0, 1))
#--------HPCPE1's var in extractions---------
test_model.HPCPE1Ext6MFrac = Var(test_model.Component, bounds=(0,1))
test_model.HPCPE1Ext6MEtlp = Var()
test_model.HPCPE1Ext22MFrac = Var(test_model.Component, bounds=(0,1))
test_model.HPCPE1Ext22MEtlp = Var()
#--------HPCSumpPE1---------
test_model.HPCSumpPE1OutMFlow = Var(within=NonNegativeReals)
test_model.HPCSumpPE1HldpMFrac = Var(test_model.Component, bounds =(0,1))
#--------HPCCondPE1---------
test_model.HPCCondPE1RefMFlow = Var(within=NonNegativeReals)
test_model.HPCCondPE1PrdtMFlow = Var(within=NonNegativeReals)
test_model.HPCCondPE1MHeatOut = Var(within=NonNegativeReals)
test_model.HPCCondPE1Temp = Var(initialize = 0)

#===================================
#
#         Expressions
#
#===================================
#--------HPCFeed1PE1 Enthalpy---------
def HPCFeed1PE1VapMEtlp(m):
	return triHPCThermo.HPCFeed1SelfCstmVapEtlp.VapEtlp(m.HPCFeed1PE1Pressure, m.HPCFeed1PE1Temp,m.HPCFeed1PE1LiqMFrac["Nitrogen"])
test_model.HPCFeed1PE1VapMEtlp = Expression(rule=HPCFeed1PE1VapMEtlp)
def HPCFeed1PE1LiqMEtlp(m):
	return triHPCThermo.HPCFeed1SelfCstmLiqEtlp.LiqEtlp(m.HPCFeed1PE1Pressure, m.HPCFeed1PE1Temp,m.HPCFeed1PE1LiqMFrac["Nitrogen"])
test_model.HPCFeed1PE1LiqMEtlp = Expression(rule=HPCFeed1PE1LiqMEtlp)
def HPCFeed1PE1MEtlp(m):
	return m.HPCFeed1PE1LiqMEtlp * (1-m.HPCFeed1PE1VF)+m.HPCFeed1PE1VapMEtlp * m.HPCFeed1PE1VF
test_model.HPCFeed1PE1MEtlp = Expression(rule=HPCFeed1PE1MEtlp)
#--------HPCFeed2PE1 Enthalpy---------
def HPCFeed2PE1VapMEtlp(m):
	return triHPCThermo.HPCFeed2SelfCstmVapEtlp.VapEtlp(m.HPCFeed2PE1Pressure, m.HPCFeed2PE1Temp,m.HPCFeed2PE1LiqMFrac["Nitrogen"])
test_model.HPCFeed2PE1VapMEtlp = Expression(rule=HPCFeed2PE1VapMEtlp)
def HPCFeed2PE1LiqMEtlp(m):
	return triHPCThermo.HPCFeed2SelfCstmLiqEtlp.LiqEtlp(m.HPCFeed2PE1Pressure, m.HPCFeed2PE1Temp,m.HPCFeed2PE1LiqMFrac["Nitrogen"])
test_model.HPCFeed2PE1LiqMEtlp = Expression(rule=HPCFeed2PE1LiqMEtlp)
def HPCFeed2PE1MEtlp(m):
	return m.HPCFeed2PE1LiqMEtlp * (1-m.HPCFeed2PE1VF)+m.HPCFeed2PE1VapMEtlp * m.HPCFeed2PE1VF
test_model.HPCFeed2PE1MEtlp = Expression(rule=HPCFeed2PE1MEtlp)
#--------HPCPE1 Component Flowrate---------
def HPCPE1VapLvMCompFlow(m, tray, comp):
	return m.HPCPE1VapLvMFrac[tray, comp] * m.HPCPE1VapLvMFlow[tray]
test_model.HPCPE1VapLvMCompFlow = Expression(test_model.HPCPE1Trays, test_model.Component, rule=HPCPE1VapLvMCompFlow)
def HPCPE1LiqLvMCompFlow(m, tray, comp):
	return m.HPCPE1LiqLvMFrac[tray, comp] * m.HPCPE1LiqLvMFlow[tray]
test_model.HPCPE1LiqLvMCompFlow = Expression(test_model.HPCPE1Trays, test_model.Component, rule=HPCPE1LiqLvMCompFlow)
#--------HPCPE1 Thermo and Enthalpy---------
def HPCPE1VapLvMEtlp(m,tray):
	if tray==1:
		return triHPCThermo.HPCAllTrays1CstmVapEtlp.VapEtlp(m.HPCPE1TrayPressure[tray], m.HPCPE1TrayTemp[tray],m.HPCPE1LiqLvMFrac[tray,"Nitrogen"])
	elif tray==2:
		return triHPCThermo.HPCAllTrays2CstmVapEtlp.VapEtlp(m.HPCPE1TrayPressure[tray], m.HPCPE1TrayTemp[tray],m.HPCPE1LiqLvMFrac[tray,"Nitrogen"])
	elif tray==3:
		return triHPCThermo.HPCAllTrays3CstmVapEtlp.VapEtlp(m.HPCPE1TrayPressure[tray], m.HPCPE1TrayTemp[tray],m.HPCPE1LiqLvMFrac[tray,"Nitrogen"])
	elif tray==4:
		return triHPCThermo.HPCAllTrays4CstmVapEtlp.VapEtlp(m.HPCPE1TrayPressure[tray], m.HPCPE1TrayTemp[tray],m.HPCPE1LiqLvMFrac[tray,"Nitrogen"])
	elif tray==5:
		return triHPCThermo.HPCAllTrays5CstmVapEtlp.VapEtlp(m.HPCPE1TrayPressure[tray], m.HPCPE1TrayTemp[tray],m.HPCPE1LiqLvMFrac[tray,"Nitrogen"])
	elif tray==6:
		return triHPCThermo.HPCAllTrays6CstmVapEtlp.VapEtlp(m.HPCPE1TrayPressure[tray], m.HPCPE1TrayTemp[tray],m.HPCPE1LiqLvMFrac[tray,"Nitrogen"])
	elif tray==7:
		return triHPCThermo.HPCAllTrays7CstmVapEtlp.VapEtlp(m.HPCPE1TrayPressure[tray], m.HPCPE1TrayTemp[tray],m.HPCPE1LiqLvMFrac[tray,"Nitrogen"])
	elif tray==8:
		return triHPCThermo.HPCAllTrays8CstmVapEtlp.VapEtlp(m.HPCPE1TrayPressure[tray], m.HPCPE1TrayTemp[tray],m.HPCPE1LiqLvMFrac[tray,"Nitrogen"])
	elif tray==9:
		return triHPCThermo.HPCAllTrays9CstmVapEtlp.VapEtlp(m.HPCPE1TrayPressure[tray], m.HPCPE1TrayTemp[tray],m.HPCPE1LiqLvMFrac[tray,"Nitrogen"])
	elif tray==10:
		return triHPCThermo.HPCAllTrays10CstmVapEtlp.VapEtlp(m.HPCPE1TrayPressure[tray], m.HPCPE1TrayTemp[tray],m.HPCPE1LiqLvMFrac[tray,"Nitrogen"])
	elif tray==11:
		return triHPCThermo.HPCAllTrays11CstmVapEtlp.VapEtlp(m.HPCPE1TrayPressure[tray], m.HPCPE1TrayTemp[tray],m.HPCPE1LiqLvMFrac[tray,"Nitrogen"])
	elif tray==12:
		return triHPCThermo.HPCAllTrays12CstmVapEtlp.VapEtlp(m.HPCPE1TrayPressure[tray], m.HPCPE1TrayTemp[tray],m.HPCPE1LiqLvMFrac[tray,"Nitrogen"])
	elif tray==13:
		return triHPCThermo.HPCAllTrays13CstmVapEtlp.VapEtlp(m.HPCPE1TrayPressure[tray], m.HPCPE1TrayTemp[tray],m.HPCPE1LiqLvMFrac[tray,"Nitrogen"])
	elif tray==14:
		return triHPCThermo.HPCAllTrays14CstmVapEtlp.VapEtlp(m.HPCPE1TrayPressure[tray], m.HPCPE1TrayTemp[tray],m.HPCPE1LiqLvMFrac[tray,"Nitrogen"])
	elif tray==15:
		return triHPCThermo.HPCAllTrays15CstmVapEtlp.VapEtlp(m.HPCPE1TrayPressure[tray], m.HPCPE1TrayTemp[tray],m.HPCPE1LiqLvMFrac[tray,"Nitrogen"])
	elif tray==16:
		return triHPCThermo.HPCAllTrays16CstmVapEtlp.VapEtlp(m.HPCPE1TrayPressure[tray], m.HPCPE1TrayTemp[tray],m.HPCPE1LiqLvMFrac[tray,"Nitrogen"])
	elif tray==17:
		return triHPCThermo.HPCAllTrays17CstmVapEtlp.VapEtlp(m.HPCPE1TrayPressure[tray], m.HPCPE1TrayTemp[tray],m.HPCPE1LiqLvMFrac[tray,"Nitrogen"])
	elif tray==18:
		return triHPCThermo.HPCAllTrays18CstmVapEtlp.VapEtlp(m.HPCPE1TrayPressure[tray], m.HPCPE1TrayTemp[tray],m.HPCPE1LiqLvMFrac[tray,"Nitrogen"])
	elif tray==19:
		return triHPCThermo.HPCAllTrays19CstmVapEtlp.VapEtlp(m.HPCPE1TrayPressure[tray], m.HPCPE1TrayTemp[tray],m.HPCPE1LiqLvMFrac[tray,"Nitrogen"])
	elif tray==20:
		return triHPCThermo.HPCAllTrays20CstmVapEtlp.VapEtlp(m.HPCPE1TrayPressure[tray], m.HPCPE1TrayTemp[tray],m.HPCPE1LiqLvMFrac[tray,"Nitrogen"])
	elif tray==21:
		return triHPCThermo.HPCAllTrays21CstmVapEtlp.VapEtlp(m.HPCPE1TrayPressure[tray], m.HPCPE1TrayTemp[tray],m.HPCPE1LiqLvMFrac[tray,"Nitrogen"])
	elif tray==22:
		return triHPCThermo.HPCAllTrays22CstmVapEtlp.VapEtlp(m.HPCPE1TrayPressure[tray], m.HPCPE1TrayTemp[tray],m.HPCPE1LiqLvMFrac[tray,"Nitrogen"])
	elif tray==23:
		return triHPCThermo.HPCAllTrays23CstmVapEtlp.VapEtlp(m.HPCPE1TrayPressure[tray], m.HPCPE1TrayTemp[tray],m.HPCPE1LiqLvMFrac[tray,"Nitrogen"])
	elif tray==24:
		return triHPCThermo.HPCAllTrays24CstmVapEtlp.VapEtlp(m.HPCPE1TrayPressure[tray], m.HPCPE1TrayTemp[tray],m.HPCPE1LiqLvMFrac[tray,"Nitrogen"])
	elif tray==25:
		return triHPCThermo.HPCAllTrays25CstmVapEtlp.VapEtlp(m.HPCPE1TrayPressure[tray], m.HPCPE1TrayTemp[tray],m.HPCPE1LiqLvMFrac[tray,"Nitrogen"])
	elif tray==26:
		return triHPCThermo.HPCAllTrays26CstmVapEtlp.VapEtlp(m.HPCPE1TrayPressure[tray], m.HPCPE1TrayTemp[tray],m.HPCPE1LiqLvMFrac[tray,"Nitrogen"])
	elif tray==27:
		return triHPCThermo.HPCAllTrays27CstmVapEtlp.VapEtlp(m.HPCPE1TrayPressure[tray], m.HPCPE1TrayTemp[tray],m.HPCPE1LiqLvMFrac[tray,"Nitrogen"])
	elif tray==28:
		return triHPCThermo.HPCAllTrays28CstmVapEtlp.VapEtlp(m.HPCPE1TrayPressure[tray], m.HPCPE1TrayTemp[tray],m.HPCPE1LiqLvMFrac[tray,"Nitrogen"])
	elif tray==29:
		return triHPCThermo.HPCAllTrays29CstmVapEtlp.VapEtlp(m.HPCPE1TrayPressure[tray], m.HPCPE1TrayTemp[tray],m.HPCPE1LiqLvMFrac[tray,"Nitrogen"])
	elif tray==30:
		return triHPCThermo.HPCAllTrays30CstmVapEtlp.VapEtlp(m.HPCPE1TrayPressure[tray], m.HPCPE1TrayTemp[tray],m.HPCPE1LiqLvMFrac[tray,"Nitrogen"])
	elif tray==31:
		return triHPCThermo.HPCAllTrays31CstmVapEtlp.VapEtlp(m.HPCPE1TrayPressure[tray], m.HPCPE1TrayTemp[tray],m.HPCPE1LiqLvMFrac[tray,"Nitrogen"])
	elif tray==32:
		return triHPCThermo.HPCAllTrays32CstmVapEtlp.VapEtlp(m.HPCPE1TrayPressure[tray], m.HPCPE1TrayTemp[tray],m.HPCPE1LiqLvMFrac[tray,"Nitrogen"])
	elif tray==33:
		return triHPCThermo.HPCAllTrays33CstmVapEtlp.VapEtlp(m.HPCPE1TrayPressure[tray], m.HPCPE1TrayTemp[tray],m.HPCPE1LiqLvMFrac[tray,"Nitrogen"])
	elif tray==34:
		return triHPCThermo.HPCAllTrays34CstmVapEtlp.VapEtlp(m.HPCPE1TrayPressure[tray], m.HPCPE1TrayTemp[tray],m.HPCPE1LiqLvMFrac[tray,"Nitrogen"])
	elif tray==35:
		return triHPCThermo.HPCAllTrays35CstmVapEtlp.VapEtlp(m.HPCPE1TrayPressure[tray], m.HPCPE1TrayTemp[tray],m.HPCPE1LiqLvMFrac[tray,"Nitrogen"])
	elif tray==36:
		return triHPCThermo.HPCAllTrays36CstmVapEtlp.VapEtlp(m.HPCPE1TrayPressure[tray], m.HPCPE1TrayTemp[tray],m.HPCPE1LiqLvMFrac[tray,"Nitrogen"])
	elif tray==37:
		return triHPCThermo.HPCAllTrays37CstmVapEtlp.VapEtlp(m.HPCPE1TrayPressure[tray], m.HPCPE1TrayTemp[tray],m.HPCPE1LiqLvMFrac[tray,"Nitrogen"])
	elif tray==38:
		return triHPCThermo.HPCAllTrays38CstmVapEtlp.VapEtlp(m.HPCPE1TrayPressure[tray], m.HPCPE1TrayTemp[tray],m.HPCPE1LiqLvMFrac[tray,"Nitrogen"])
	elif tray==39:
		return triHPCThermo.HPCAllTrays39CstmVapEtlp.VapEtlp(m.HPCPE1TrayPressure[tray], m.HPCPE1TrayTemp[tray],m.HPCPE1LiqLvMFrac[tray,"Nitrogen"])
	elif tray==40:
		return triHPCThermo.HPCAllTrays40CstmVapEtlp.VapEtlp(m.HPCPE1TrayPressure[tray], m.HPCPE1TrayTemp[tray],m.HPCPE1LiqLvMFrac[tray,"Nitrogen"])
	elif tray==41:
		return triHPCThermo.HPCAllTrays41CstmVapEtlp.VapEtlp(m.HPCPE1TrayPressure[tray], m.HPCPE1TrayTemp[tray],m.HPCPE1LiqLvMFrac[tray,"Nitrogen"])
	elif tray==42:
		return triHPCThermo.HPCAllTrays42CstmVapEtlp.VapEtlp(m.HPCPE1TrayPressure[tray], m.HPCPE1TrayTemp[tray],m.HPCPE1LiqLvMFrac[tray,"Nitrogen"])
test_model.HPCPE1VapLvMEtlp = Expression(test_model.HPCPE1Trays,rule=HPCPE1VapLvMEtlp)
def HPCPE1LiqLvMEtlp(m,tray):
	if tray==1:
		return triHPCThermo.HPCAllTrays1CstmLiqEtlp.LiqEtlp(m.HPCPE1TrayPressure[tray], m.HPCPE1TrayTemp[tray],m.HPCPE1LiqLvMFrac[tray,"Nitrogen"])
	elif tray==2:
		return triHPCThermo.HPCAllTrays2CstmLiqEtlp.LiqEtlp(m.HPCPE1TrayPressure[tray], m.HPCPE1TrayTemp[tray],m.HPCPE1LiqLvMFrac[tray,"Nitrogen"])
	elif tray==3:
		return triHPCThermo.HPCAllTrays3CstmLiqEtlp.LiqEtlp(m.HPCPE1TrayPressure[tray], m.HPCPE1TrayTemp[tray],m.HPCPE1LiqLvMFrac[tray,"Nitrogen"])
	elif tray==4:
		return triHPCThermo.HPCAllTrays4CstmLiqEtlp.LiqEtlp(m.HPCPE1TrayPressure[tray], m.HPCPE1TrayTemp[tray],m.HPCPE1LiqLvMFrac[tray,"Nitrogen"])
	elif tray==5:
		return triHPCThermo.HPCAllTrays5CstmLiqEtlp.LiqEtlp(m.HPCPE1TrayPressure[tray], m.HPCPE1TrayTemp[tray],m.HPCPE1LiqLvMFrac[tray,"Nitrogen"])
	elif tray==6:
		return triHPCThermo.HPCAllTrays6CstmLiqEtlp.LiqEtlp(m.HPCPE1TrayPressure[tray], m.HPCPE1TrayTemp[tray],m.HPCPE1LiqLvMFrac[tray,"Nitrogen"])
	elif tray==7:
		return triHPCThermo.HPCAllTrays7CstmLiqEtlp.LiqEtlp(m.HPCPE1TrayPressure[tray], m.HPCPE1TrayTemp[tray],m.HPCPE1LiqLvMFrac[tray,"Nitrogen"])
	elif tray==8:
		return triHPCThermo.HPCAllTrays8CstmLiqEtlp.LiqEtlp(m.HPCPE1TrayPressure[tray], m.HPCPE1TrayTemp[tray],m.HPCPE1LiqLvMFrac[tray,"Nitrogen"])
	elif tray==9:
		return triHPCThermo.HPCAllTrays9CstmLiqEtlp.LiqEtlp(m.HPCPE1TrayPressure[tray], m.HPCPE1TrayTemp[tray],m.HPCPE1LiqLvMFrac[tray,"Nitrogen"])
	elif tray==10:
		return triHPCThermo.HPCAllTrays10CstmLiqEtlp.LiqEtlp(m.HPCPE1TrayPressure[tray], m.HPCPE1TrayTemp[tray],m.HPCPE1LiqLvMFrac[tray,"Nitrogen"])
	elif tray==11:
		return triHPCThermo.HPCAllTrays11CstmLiqEtlp.LiqEtlp(m.HPCPE1TrayPressure[tray], m.HPCPE1TrayTemp[tray],m.HPCPE1LiqLvMFrac[tray,"Nitrogen"])
	elif tray==12:
		return triHPCThermo.HPCAllTrays12CstmLiqEtlp.LiqEtlp(m.HPCPE1TrayPressure[tray], m.HPCPE1TrayTemp[tray],m.HPCPE1LiqLvMFrac[tray,"Nitrogen"])
	elif tray==13:
		return triHPCThermo.HPCAllTrays13CstmLiqEtlp.LiqEtlp(m.HPCPE1TrayPressure[tray], m.HPCPE1TrayTemp[tray],m.HPCPE1LiqLvMFrac[tray,"Nitrogen"])
	elif tray==14:
		return triHPCThermo.HPCAllTrays14CstmLiqEtlp.LiqEtlp(m.HPCPE1TrayPressure[tray], m.HPCPE1TrayTemp[tray],m.HPCPE1LiqLvMFrac[tray,"Nitrogen"])
	elif tray==15:
		return triHPCThermo.HPCAllTrays15CstmLiqEtlp.LiqEtlp(m.HPCPE1TrayPressure[tray], m.HPCPE1TrayTemp[tray],m.HPCPE1LiqLvMFrac[tray,"Nitrogen"])
	elif tray==16:
		return triHPCThermo.HPCAllTrays16CstmLiqEtlp.LiqEtlp(m.HPCPE1TrayPressure[tray], m.HPCPE1TrayTemp[tray],m.HPCPE1LiqLvMFrac[tray,"Nitrogen"])
	elif tray==17:
		return triHPCThermo.HPCAllTrays17CstmLiqEtlp.LiqEtlp(m.HPCPE1TrayPressure[tray], m.HPCPE1TrayTemp[tray],m.HPCPE1LiqLvMFrac[tray,"Nitrogen"])
	elif tray==18:
		return triHPCThermo.HPCAllTrays18CstmLiqEtlp.LiqEtlp(m.HPCPE1TrayPressure[tray], m.HPCPE1TrayTemp[tray],m.HPCPE1LiqLvMFrac[tray,"Nitrogen"])
	elif tray==19:
		return triHPCThermo.HPCAllTrays19CstmLiqEtlp.LiqEtlp(m.HPCPE1TrayPressure[tray], m.HPCPE1TrayTemp[tray],m.HPCPE1LiqLvMFrac[tray,"Nitrogen"])
	elif tray==20:
		return triHPCThermo.HPCAllTrays20CstmLiqEtlp.LiqEtlp(m.HPCPE1TrayPressure[tray], m.HPCPE1TrayTemp[tray],m.HPCPE1LiqLvMFrac[tray,"Nitrogen"])
	elif tray==21:
		return triHPCThermo.HPCAllTrays21CstmLiqEtlp.LiqEtlp(m.HPCPE1TrayPressure[tray], m.HPCPE1TrayTemp[tray],m.HPCPE1LiqLvMFrac[tray,"Nitrogen"])
	elif tray==22:
		return triHPCThermo.HPCAllTrays22CstmLiqEtlp.LiqEtlp(m.HPCPE1TrayPressure[tray], m.HPCPE1TrayTemp[tray],m.HPCPE1LiqLvMFrac[tray,"Nitrogen"])
	elif tray==23:
		return triHPCThermo.HPCAllTrays23CstmLiqEtlp.LiqEtlp(m.HPCPE1TrayPressure[tray], m.HPCPE1TrayTemp[tray],m.HPCPE1LiqLvMFrac[tray,"Nitrogen"])
	elif tray==24:
		return triHPCThermo.HPCAllTrays24CstmLiqEtlp.LiqEtlp(m.HPCPE1TrayPressure[tray], m.HPCPE1TrayTemp[tray],m.HPCPE1LiqLvMFrac[tray,"Nitrogen"])
	elif tray==25:
		return triHPCThermo.HPCAllTrays25CstmLiqEtlp.LiqEtlp(m.HPCPE1TrayPressure[tray], m.HPCPE1TrayTemp[tray],m.HPCPE1LiqLvMFrac[tray,"Nitrogen"])
	elif tray==26:
		return triHPCThermo.HPCAllTrays26CstmLiqEtlp.LiqEtlp(m.HPCPE1TrayPressure[tray], m.HPCPE1TrayTemp[tray],m.HPCPE1LiqLvMFrac[tray,"Nitrogen"])
	elif tray==27:
		return triHPCThermo.HPCAllTrays27CstmLiqEtlp.LiqEtlp(m.HPCPE1TrayPressure[tray], m.HPCPE1TrayTemp[tray],m.HPCPE1LiqLvMFrac[tray,"Nitrogen"])
	elif tray==28:
		return triHPCThermo.HPCAllTrays28CstmLiqEtlp.LiqEtlp(m.HPCPE1TrayPressure[tray], m.HPCPE1TrayTemp[tray],m.HPCPE1LiqLvMFrac[tray,"Nitrogen"])
	elif tray==29:
		return triHPCThermo.HPCAllTrays29CstmLiqEtlp.LiqEtlp(m.HPCPE1TrayPressure[tray], m.HPCPE1TrayTemp[tray],m.HPCPE1LiqLvMFrac[tray,"Nitrogen"])
	elif tray==30:
		return triHPCThermo.HPCAllTrays30CstmLiqEtlp.LiqEtlp(m.HPCPE1TrayPressure[tray], m.HPCPE1TrayTemp[tray],m.HPCPE1LiqLvMFrac[tray,"Nitrogen"])
	elif tray==31:
		return triHPCThermo.HPCAllTrays31CstmLiqEtlp.LiqEtlp(m.HPCPE1TrayPressure[tray], m.HPCPE1TrayTemp[tray],m.HPCPE1LiqLvMFrac[tray,"Nitrogen"])
	elif tray==32:
		return triHPCThermo.HPCAllTrays32CstmLiqEtlp.LiqEtlp(m.HPCPE1TrayPressure[tray], m.HPCPE1TrayTemp[tray],m.HPCPE1LiqLvMFrac[tray,"Nitrogen"])
	elif tray==33:
		return triHPCThermo.HPCAllTrays33CstmLiqEtlp.LiqEtlp(m.HPCPE1TrayPressure[tray], m.HPCPE1TrayTemp[tray],m.HPCPE1LiqLvMFrac[tray,"Nitrogen"])
	elif tray==34:
		return triHPCThermo.HPCAllTrays34CstmLiqEtlp.LiqEtlp(m.HPCPE1TrayPressure[tray], m.HPCPE1TrayTemp[tray],m.HPCPE1LiqLvMFrac[tray,"Nitrogen"])
	elif tray==35:
		return triHPCThermo.HPCAllTrays35CstmLiqEtlp.LiqEtlp(m.HPCPE1TrayPressure[tray], m.HPCPE1TrayTemp[tray],m.HPCPE1LiqLvMFrac[tray,"Nitrogen"])
	elif tray==36:
		return triHPCThermo.HPCAllTrays36CstmLiqEtlp.LiqEtlp(m.HPCPE1TrayPressure[tray], m.HPCPE1TrayTemp[tray],m.HPCPE1LiqLvMFrac[tray,"Nitrogen"])
	elif tray==37:
		return triHPCThermo.HPCAllTrays37CstmLiqEtlp.LiqEtlp(m.HPCPE1TrayPressure[tray], m.HPCPE1TrayTemp[tray],m.HPCPE1LiqLvMFrac[tray,"Nitrogen"])
	elif tray==38:
		return triHPCThermo.HPCAllTrays38CstmLiqEtlp.LiqEtlp(m.HPCPE1TrayPressure[tray], m.HPCPE1TrayTemp[tray],m.HPCPE1LiqLvMFrac[tray,"Nitrogen"])
	elif tray==39:
		return triHPCThermo.HPCAllTrays39CstmLiqEtlp.LiqEtlp(m.HPCPE1TrayPressure[tray], m.HPCPE1TrayTemp[tray],m.HPCPE1LiqLvMFrac[tray,"Nitrogen"])
	elif tray==40:
		return triHPCThermo.HPCAllTrays40CstmLiqEtlp.LiqEtlp(m.HPCPE1TrayPressure[tray], m.HPCPE1TrayTemp[tray],m.HPCPE1LiqLvMFrac[tray,"Nitrogen"])
	elif tray==41:
		return triHPCThermo.HPCAllTrays41CstmLiqEtlp.LiqEtlp(m.HPCPE1TrayPressure[tray], m.HPCPE1TrayTemp[tray],m.HPCPE1LiqLvMFrac[tray,"Nitrogen"])
	elif tray==42:
		return triHPCThermo.HPCAllTrays42CstmLiqEtlp.LiqEtlp(m.HPCPE1TrayPressure[tray], m.HPCPE1TrayTemp[tray],m.HPCPE1LiqLvMFrac[tray,"Nitrogen"])
test_model.HPCPE1LiqLvMEtlp = Expression(test_model.HPCPE1Trays,rule=HPCPE1LiqLvMEtlp)
#--------HPCCondPE1 Enthalpy---------
def HPCCondPE1OutMEtlp(m):
	return triHPCThermo.HPCCondOutletCstmLiqEtlp.LiqEtlp(m.HPCPE1TrayPressure[42], m.HPCCondPE1Temp,m.HPCPE1VapLvMFrac[42,"Nitrogen"])
test_model.HPCCondPE1OutMEtlp = Expression(rule=HPCCondPE1OutMEtlp)

#===================================
#
#         Constraints
#
#===================================

#----------------------------------
#           HPCFeed1PE1
#----------------------------------
#--------HPCFeed1PE1 Mass Balance---------
def HPCFeed1PE1MassBlnc0(m):
	return m.HPCFeed1PE1VF * m.HPCFeed1PE1VapMFrac['Nitrogen'] + \
(1 - m.HPCFeed1PE1VF)*m.HPCFeed1PE1LiqMFrac['Nitrogen'] - m.HPCFeed1PE1MFrac['Nitrogen'] == 0
test_model.HPCFeed1PE1MassBlnc0 = Constraint(rule=HPCFeed1PE1MassBlnc0)
def HPCFeed1PE1MassBlnc1(m):
	return m.HPCFeed1PE1VF * m.HPCFeed1PE1VapMFrac['Oxygen'] + \
(1 - m.HPCFeed1PE1VF)*m.HPCFeed1PE1LiqMFrac['Oxygen'] - m.HPCFeed1PE1MFrac['Oxygen'] == 0
test_model.HPCFeed1PE1MassBlnc1 = Constraint(rule=HPCFeed1PE1MassBlnc1)
#--------HPCFeed1PE1 Phase Equilibrium---------
def HPCFeed1PE1SelfLiqO2Frac(m):
	return m.HPCFeed1PE1LiqMFrac["Oxygen"] == triHPCThermo.HPCFeed1SelfCstmLiqO2.LiqO2(m.HPCFeed1PE1Pressure,m.HPCFeed1PE1Temp,m.HPCFeed1PE1LiqMFrac["Nitrogen"])
test_model.HPCFeed1PE1SelfLiqO2Frac = Constraint(rule=HPCFeed1PE1SelfLiqO2Frac)
def HPCFeed1PE1SelfVapO2Frac(m):
	return m.HPCFeed1PE1VapMFrac["Oxygen"] == triHPCThermo.HPCFeed1SelfCstmVapO2.VapO2(m.HPCFeed1PE1Pressure,m.HPCFeed1PE1Temp,m.HPCFeed1PE1LiqMFrac["Nitrogen"])
test_model.HPCFeed1PE1SelfVapO2Frac = Constraint(rule=HPCFeed1PE1SelfVapO2Frac)
def HPCFeed1PE1SelfVapN2Frac(m):
	return m.HPCFeed1PE1VapMFrac["Nitrogen"] == triHPCThermo.HPCFeed1SelfCstmVapN2.VapN2(m.HPCFeed1PE1Pressure,m.HPCFeed1PE1Temp,m.HPCFeed1PE1LiqMFrac["Nitrogen"])
test_model.HPCFeed1PE1SelfVapN2Frac = Constraint(rule=HPCFeed1PE1SelfVapN2Frac)
#--------HPCFeed1PE1 Summation---------
def HPCFeed1PE1LiqSum(m):
	return sum([m.HPCFeed1PE1LiqMFrac[c] for c in m.Component]) == 1
test_model.HPCFeed1PE1LiqSum = Constraint(rule=HPCFeed1PE1LiqSum)
def HPCFeed1PE1VapSum(m):
	return sum([m.HPCFeed1PE1VapMFrac[c] for c in m.Component]) == 1
test_model.HPCFeed1PE1VapSum = Constraint(rule=HPCFeed1PE1VapSum)

#----------------------------------
#           HPCFeed2PE1
#----------------------------------
#--------HPCFeed2PE1 Mass Balance---------
def HPCFeed2PE1MassBlnc0(m):
	return m.HPCFeed2PE1VF * m.HPCFeed2PE1VapMFrac['Nitrogen'] + \
(1 - m.HPCFeed2PE1VF)*m.HPCFeed2PE1LiqMFrac['Nitrogen'] - m.HPCFeed2PE1MFrac['Nitrogen'] == 0
test_model.HPCFeed2PE1MassBlnc0 = Constraint(rule=HPCFeed2PE1MassBlnc0)
def HPCFeed2PE1MassBlnc1(m):
	return m.HPCFeed2PE1VF * m.HPCFeed2PE1VapMFrac['Oxygen'] + \
(1 - m.HPCFeed2PE1VF)*m.HPCFeed2PE1LiqMFrac['Oxygen'] - m.HPCFeed2PE1MFrac['Oxygen'] == 0
test_model.HPCFeed2PE1MassBlnc1 = Constraint(rule=HPCFeed2PE1MassBlnc1)
#--------HPCFeed2PE1 Phase Equilibrium---------
def HPCFeed2PE1SelfLiqO2Frac(m):
	return m.HPCFeed2PE1LiqMFrac["Oxygen"] == triHPCThermo.HPCFeed2SelfCstmLiqO2.LiqO2(m.HPCFeed2PE1Pressure,m.HPCFeed2PE1Temp,m.HPCFeed2PE1LiqMFrac["Nitrogen"])
test_model.HPCFeed2PE1SelfLiqO2Frac = Constraint(rule=HPCFeed2PE1SelfLiqO2Frac)
def HPCFeed2PE1SelfVapO2Frac(m):
	return m.HPCFeed2PE1VapMFrac["Oxygen"] == triHPCThermo.HPCFeed2SelfCstmVapO2.VapO2(m.HPCFeed2PE1Pressure,m.HPCFeed2PE1Temp,m.HPCFeed2PE1LiqMFrac["Nitrogen"])
test_model.HPCFeed2PE1SelfVapO2Frac = Constraint(rule=HPCFeed2PE1SelfVapO2Frac)
def HPCFeed2PE1SelfVapN2Frac(m):
	return m.HPCFeed2PE1VapMFrac["Nitrogen"] == triHPCThermo.HPCFeed2SelfCstmVapN2.VapN2(m.HPCFeed2PE1Pressure,m.HPCFeed2PE1Temp,m.HPCFeed2PE1LiqMFrac["Nitrogen"])
test_model.HPCFeed2PE1SelfVapN2Frac = Constraint(rule=HPCFeed2PE1SelfVapN2Frac)
#--------HPCFeed2PE1 Summation---------
def HPCFeed2PE1LiqSum(m):
	return sum([m.HPCFeed2PE1LiqMFrac[c] for c in m.Component]) == 1
test_model.HPCFeed2PE1LiqSum = Constraint(rule=HPCFeed2PE1LiqSum)
def HPCFeed2PE1VapSum(m):
	return sum([m.HPCFeed2PE1VapMFrac[c] for c in m.Component]) == 1
test_model.HPCFeed2PE1VapSum = Constraint(rule=HPCFeed2PE1VapSum)

#----------------------------------
#           HPCPE1
#----------------------------------
#--------HPCPE1 Mass Balance---------
def HPCPE1MassBlnc(m,tray, comp):
	if tray == 1:
		return (m.HPCPE1LiqLvMCompFlow[tray + 1, comp]- m.HPCPE1LiqLvMCompFlow[tray, comp] - m.HPCPE1VapLvMCompFlow[tray, comp]+m.HPCFeed1PE1MFlow*m.HPCFeed1PE1MFrac[comp])*0.001000 == 0
	elif tray == 4:
		return (m.HPCPE1LiqLvMCompFlow[tray + 1, comp] + m.HPCPE1VapLvMCompFlow[tray - 1, comp] - m.HPCPE1LiqLvMCompFlow[tray, comp] - m.HPCPE1VapLvMCompFlow[tray, comp]+m.HPCFeed2PE1MFlow*m.HPCFeed2PE1MFrac[comp])*0.001000 == 0
	elif tray == 6:
		return (m.HPCPE1LiqLvMCompFlow[tray + 1, comp] + m.HPCPE1VapLvMCompFlow[tray - 1, comp] - m.HPCPE1LiqLvMCompFlow[tray, comp] - m.HPCPE1VapLvMCompFlow[tray, comp]-m.HPCPE1Ext6MFlow*m.HPCPE1Ext6MFrac[comp])*0.001000 == 0
	elif tray == 22:
		return (m.HPCPE1LiqLvMCompFlow[tray + 1, comp] + m.HPCPE1VapLvMCompFlow[tray - 1, comp] - m.HPCPE1LiqLvMCompFlow[tray, comp] - m.HPCPE1VapLvMCompFlow[tray, comp]-m.HPCPE1Ext22MFlow*m.HPCPE1Ext22MFrac[comp])*0.001000 == 0
	elif tray == 42:
		return (m.HPCCondPE1RefMFlow*m.HPCPE1VapLvMFrac[42,comp] + m.HPCPE1VapLvMCompFlow[tray - 1, comp] - m.HPCPE1LiqLvMCompFlow[tray, comp] - m.HPCPE1VapLvMCompFlow[tray, comp])*0.001000 == 0
	else:
		return (m.HPCPE1LiqLvMCompFlow[tray + 1, comp] + m.HPCPE1VapLvMCompFlow[tray - 1, comp] - m.HPCPE1LiqLvMCompFlow[tray, comp] - m.HPCPE1VapLvMCompFlow[tray, comp])*0.001000 == 0
test_model.HPCPE1MassBlnc = Constraint(test_model.HPCPE1Trays, test_model.Component, rule=HPCPE1MassBlnc)
#--------HPCPE1 Energy Balance---------
def HPCPE1EngBlnc(m,tray):
	if tray == 1:
		return (m.HPCPE1LiqLvMFlow[tray + 1] * m.HPCPE1LiqLvMEtlp[tray+1] \
		        - m.HPCPE1LiqLvMFlow[tray] * m.HPCPE1LiqLvMEtlp[tray] \
		        - m.HPCPE1VapLvMFlow[tray] * m.HPCPE1VapLvMEtlp[tray]\
		        +m.HPCFeed1PE1MFlow*m.HPCFeed1PE0MEtlp-m.HPCPE1UALeakage*(m.HPCPE1AmbientTemp-m.HPCPE1TrayTemp[tray]))*0.000010 == 0
	elif tray == 4:
		return (m.HPCPE1LiqLvMFlow[tray + 1] * m.HPCPE1LiqLvMEtlp[tray+1] \
		        + m.HPCPE1VapLvMFlow[tray-1] * m.HPCPE1VapLvMEtlp[tray-1] \
		        - m.HPCPE1LiqLvMFlow[tray] * m.HPCPE1LiqLvMEtlp[tray] \
		        - m.HPCPE1VapLvMFlow[tray] * m.HPCPE1VapLvMEtlp[tray]\
		        +m.HPCFeed2PE1MFlow*m.HPCFeed2PE0MEtlp-m.HPCPE1UALeakage*(m.HPCPE1AmbientTemp-m.HPCPE1TrayTemp[tray]))*0.000010 == 0
	elif tray == 6:
		return (m.HPCPE1LiqLvMFlow[tray + 1] * m.HPCPE1LiqLvMEtlp[tray+1] \
		        + m.HPCPE1VapLvMFlow[tray-1] * m.HPCPE1VapLvMEtlp[tray-1] \
		        - m.HPCPE1LiqLvMFlow[tray] * m.HPCPE1LiqLvMEtlp[tray] \
		        - m.HPCPE1VapLvMFlow[tray] * m.HPCPE1VapLvMEtlp[tray]\
		        -m.HPCPE1Ext6MFlow*m.HPCPE1Ext6MEtlp-m.HPCPE1UALeakage*(m.HPCPE1AmbientTemp-m.HPCPE1TrayTemp[tray]))*0.000010 == 0
	elif tray == 22:
		return (m.HPCPE1LiqLvMFlow[tray + 1] * m.HPCPE1LiqLvMEtlp[tray+1] \
		        + m.HPCPE1VapLvMFlow[tray-1] * m.HPCPE1VapLvMEtlp[tray-1] \
		        - m.HPCPE1LiqLvMFlow[tray] * m.HPCPE1LiqLvMEtlp[tray] \
		        - m.HPCPE1VapLvMFlow[tray] * m.HPCPE1VapLvMEtlp[tray]\
		        -m.HPCPE1Ext22MFlow*m.HPCPE1Ext22MEtlp-m.HPCPE1UALeakage*(m.HPCPE1AmbientTemp-m.HPCPE1TrayTemp[tray]))*0.000010 == 0
	elif tray == 42:
		return (m.HPCCondPE1RefMFlow * m.HPCCondPE1OutMEtlp \
		        + m.HPCPE1VapLvMFlow[tray-1] * m.HPCPE1VapLvMEtlp[tray-1] \
		        - m.HPCPE1LiqLvMFlow[tray] * m.HPCPE1LiqLvMEtlp[tray] \
		        - m.HPCPE1VapLvMFlow[tray] * m.HPCPE1VapLvMEtlp[tray]-m.HPCPE1UALeakage*(m.HPCPE1AmbientTemp-m.HPCPE1TrayTemp[tray]))*0.000010 == 0
	else:
		return (m.HPCPE1LiqLvMFlow[tray + 1] * m.HPCPE1LiqLvMEtlp[tray+1] \
		        + m.HPCPE1VapLvMFlow[tray-1] * m.HPCPE1VapLvMEtlp[tray-1] \
		        - m.HPCPE1LiqLvMFlow[tray] * m.HPCPE1LiqLvMEtlp[tray] \
		        - m.HPCPE1VapLvMFlow[tray] * m.HPCPE1VapLvMEtlp[tray]-m.HPCPE1UALeakage*(m.HPCPE1AmbientTemp-m.HPCPE1TrayTemp[tray]))*0.000010 == 0
test_model.HPCPE1EngBlnc = Constraint(test_model.HPCPE1Trays,rule=HPCPE1EngBlnc)
#--------HPCPE1 Phase Equilibrium & System Parts---------
def HPCPE1AllTraysLiqO2Frac(m,tray):
	if tray==1:
		return m.HPCPE1LiqLvMFrac[tray,"Oxygen"] == triHPCThermo.HPCAllTrays1CstmLiqO2.LiqO2(m.HPCPE1TrayPressure[tray],m.HPCPE1TrayTemp[tray],m.HPCPE1LiqLvMFrac[tray,"Nitrogen"])
	elif tray==2:
		return m.HPCPE1LiqLvMFrac[tray,"Oxygen"] == triHPCThermo.HPCAllTrays2CstmLiqO2.LiqO2(m.HPCPE1TrayPressure[tray],m.HPCPE1TrayTemp[tray],m.HPCPE1LiqLvMFrac[tray,"Nitrogen"])
	elif tray==3:
		return m.HPCPE1LiqLvMFrac[tray,"Oxygen"] == triHPCThermo.HPCAllTrays3CstmLiqO2.LiqO2(m.HPCPE1TrayPressure[tray],m.HPCPE1TrayTemp[tray],m.HPCPE1LiqLvMFrac[tray,"Nitrogen"])
	elif tray==4:
		return m.HPCPE1LiqLvMFrac[tray,"Oxygen"] == triHPCThermo.HPCAllTrays4CstmLiqO2.LiqO2(m.HPCPE1TrayPressure[tray],m.HPCPE1TrayTemp[tray],m.HPCPE1LiqLvMFrac[tray,"Nitrogen"])
	elif tray==5:
		return m.HPCPE1LiqLvMFrac[tray,"Oxygen"] == triHPCThermo.HPCAllTrays5CstmLiqO2.LiqO2(m.HPCPE1TrayPressure[tray],m.HPCPE1TrayTemp[tray],m.HPCPE1LiqLvMFrac[tray,"Nitrogen"])
	elif tray==6:
		return m.HPCPE1LiqLvMFrac[tray,"Oxygen"] == triHPCThermo.HPCAllTrays6CstmLiqO2.LiqO2(m.HPCPE1TrayPressure[tray],m.HPCPE1TrayTemp[tray],m.HPCPE1LiqLvMFrac[tray,"Nitrogen"])
	elif tray==7:
		return m.HPCPE1LiqLvMFrac[tray,"Oxygen"] == triHPCThermo.HPCAllTrays7CstmLiqO2.LiqO2(m.HPCPE1TrayPressure[tray],m.HPCPE1TrayTemp[tray],m.HPCPE1LiqLvMFrac[tray,"Nitrogen"])
	elif tray==8:
		return m.HPCPE1LiqLvMFrac[tray,"Oxygen"] == triHPCThermo.HPCAllTrays8CstmLiqO2.LiqO2(m.HPCPE1TrayPressure[tray],m.HPCPE1TrayTemp[tray],m.HPCPE1LiqLvMFrac[tray,"Nitrogen"])
	elif tray==9:
		return m.HPCPE1LiqLvMFrac[tray,"Oxygen"] == triHPCThermo.HPCAllTrays9CstmLiqO2.LiqO2(m.HPCPE1TrayPressure[tray],m.HPCPE1TrayTemp[tray],m.HPCPE1LiqLvMFrac[tray,"Nitrogen"])
	elif tray==10:
		return m.HPCPE1LiqLvMFrac[tray,"Oxygen"] == triHPCThermo.HPCAllTrays10CstmLiqO2.LiqO2(m.HPCPE1TrayPressure[tray],m.HPCPE1TrayTemp[tray],m.HPCPE1LiqLvMFrac[tray,"Nitrogen"])
	elif tray==11:
		return m.HPCPE1LiqLvMFrac[tray,"Oxygen"] == triHPCThermo.HPCAllTrays11CstmLiqO2.LiqO2(m.HPCPE1TrayPressure[tray],m.HPCPE1TrayTemp[tray],m.HPCPE1LiqLvMFrac[tray,"Nitrogen"])
	elif tray==12:
		return m.HPCPE1LiqLvMFrac[tray,"Oxygen"] == triHPCThermo.HPCAllTrays12CstmLiqO2.LiqO2(m.HPCPE1TrayPressure[tray],m.HPCPE1TrayTemp[tray],m.HPCPE1LiqLvMFrac[tray,"Nitrogen"])
	elif tray==13:
		return m.HPCPE1LiqLvMFrac[tray,"Oxygen"] == triHPCThermo.HPCAllTrays13CstmLiqO2.LiqO2(m.HPCPE1TrayPressure[tray],m.HPCPE1TrayTemp[tray],m.HPCPE1LiqLvMFrac[tray,"Nitrogen"])
	elif tray==14:
		return m.HPCPE1LiqLvMFrac[tray,"Oxygen"] == triHPCThermo.HPCAllTrays14CstmLiqO2.LiqO2(m.HPCPE1TrayPressure[tray],m.HPCPE1TrayTemp[tray],m.HPCPE1LiqLvMFrac[tray,"Nitrogen"])
	elif tray==15:
		return m.HPCPE1LiqLvMFrac[tray,"Oxygen"] == triHPCThermo.HPCAllTrays15CstmLiqO2.LiqO2(m.HPCPE1TrayPressure[tray],m.HPCPE1TrayTemp[tray],m.HPCPE1LiqLvMFrac[tray,"Nitrogen"])
	elif tray==16:
		return m.HPCPE1LiqLvMFrac[tray,"Oxygen"] == triHPCThermo.HPCAllTrays16CstmLiqO2.LiqO2(m.HPCPE1TrayPressure[tray],m.HPCPE1TrayTemp[tray],m.HPCPE1LiqLvMFrac[tray,"Nitrogen"])
	elif tray==17:
		return m.HPCPE1LiqLvMFrac[tray,"Oxygen"] == triHPCThermo.HPCAllTrays17CstmLiqO2.LiqO2(m.HPCPE1TrayPressure[tray],m.HPCPE1TrayTemp[tray],m.HPCPE1LiqLvMFrac[tray,"Nitrogen"])
	elif tray==18:
		return m.HPCPE1LiqLvMFrac[tray,"Oxygen"] == triHPCThermo.HPCAllTrays18CstmLiqO2.LiqO2(m.HPCPE1TrayPressure[tray],m.HPCPE1TrayTemp[tray],m.HPCPE1LiqLvMFrac[tray,"Nitrogen"])
	elif tray==19:
		return m.HPCPE1LiqLvMFrac[tray,"Oxygen"] == triHPCThermo.HPCAllTrays19CstmLiqO2.LiqO2(m.HPCPE1TrayPressure[tray],m.HPCPE1TrayTemp[tray],m.HPCPE1LiqLvMFrac[tray,"Nitrogen"])
	elif tray==20:
		return m.HPCPE1LiqLvMFrac[tray,"Oxygen"] == triHPCThermo.HPCAllTrays20CstmLiqO2.LiqO2(m.HPCPE1TrayPressure[tray],m.HPCPE1TrayTemp[tray],m.HPCPE1LiqLvMFrac[tray,"Nitrogen"])
	elif tray==21:
		return m.HPCPE1LiqLvMFrac[tray,"Oxygen"] == triHPCThermo.HPCAllTrays21CstmLiqO2.LiqO2(m.HPCPE1TrayPressure[tray],m.HPCPE1TrayTemp[tray],m.HPCPE1LiqLvMFrac[tray,"Nitrogen"])
	elif tray==22:
		return m.HPCPE1LiqLvMFrac[tray,"Oxygen"] == triHPCThermo.HPCAllTrays22CstmLiqO2.LiqO2(m.HPCPE1TrayPressure[tray],m.HPCPE1TrayTemp[tray],m.HPCPE1LiqLvMFrac[tray,"Nitrogen"])
	elif tray==23:
		return m.HPCPE1LiqLvMFrac[tray,"Oxygen"] == triHPCThermo.HPCAllTrays23CstmLiqO2.LiqO2(m.HPCPE1TrayPressure[tray],m.HPCPE1TrayTemp[tray],m.HPCPE1LiqLvMFrac[tray,"Nitrogen"])
	elif tray==24:
		return m.HPCPE1LiqLvMFrac[tray,"Oxygen"] == triHPCThermo.HPCAllTrays24CstmLiqO2.LiqO2(m.HPCPE1TrayPressure[tray],m.HPCPE1TrayTemp[tray],m.HPCPE1LiqLvMFrac[tray,"Nitrogen"])
	elif tray==25:
		return m.HPCPE1LiqLvMFrac[tray,"Oxygen"] == triHPCThermo.HPCAllTrays25CstmLiqO2.LiqO2(m.HPCPE1TrayPressure[tray],m.HPCPE1TrayTemp[tray],m.HPCPE1LiqLvMFrac[tray,"Nitrogen"])
	elif tray==26:
		return m.HPCPE1LiqLvMFrac[tray,"Oxygen"] == triHPCThermo.HPCAllTrays26CstmLiqO2.LiqO2(m.HPCPE1TrayPressure[tray],m.HPCPE1TrayTemp[tray],m.HPCPE1LiqLvMFrac[tray,"Nitrogen"])
	elif tray==27:
		return m.HPCPE1LiqLvMFrac[tray,"Oxygen"] == triHPCThermo.HPCAllTrays27CstmLiqO2.LiqO2(m.HPCPE1TrayPressure[tray],m.HPCPE1TrayTemp[tray],m.HPCPE1LiqLvMFrac[tray,"Nitrogen"])
	elif tray==28:
		return m.HPCPE1LiqLvMFrac[tray,"Oxygen"] == triHPCThermo.HPCAllTrays28CstmLiqO2.LiqO2(m.HPCPE1TrayPressure[tray],m.HPCPE1TrayTemp[tray],m.HPCPE1LiqLvMFrac[tray,"Nitrogen"])
	elif tray==29:
		return m.HPCPE1LiqLvMFrac[tray,"Oxygen"] == triHPCThermo.HPCAllTrays29CstmLiqO2.LiqO2(m.HPCPE1TrayPressure[tray],m.HPCPE1TrayTemp[tray],m.HPCPE1LiqLvMFrac[tray,"Nitrogen"])
	elif tray==30:
		return m.HPCPE1LiqLvMFrac[tray,"Oxygen"] == triHPCThermo.HPCAllTrays30CstmLiqO2.LiqO2(m.HPCPE1TrayPressure[tray],m.HPCPE1TrayTemp[tray],m.HPCPE1LiqLvMFrac[tray,"Nitrogen"])
	elif tray==31:
		return m.HPCPE1LiqLvMFrac[tray,"Oxygen"] == triHPCThermo.HPCAllTrays31CstmLiqO2.LiqO2(m.HPCPE1TrayPressure[tray],m.HPCPE1TrayTemp[tray],m.HPCPE1LiqLvMFrac[tray,"Nitrogen"])
	elif tray==32:
		return m.HPCPE1LiqLvMFrac[tray,"Oxygen"] == triHPCThermo.HPCAllTrays32CstmLiqO2.LiqO2(m.HPCPE1TrayPressure[tray],m.HPCPE1TrayTemp[tray],m.HPCPE1LiqLvMFrac[tray,"Nitrogen"])
	elif tray==33:
		return m.HPCPE1LiqLvMFrac[tray,"Oxygen"] == triHPCThermo.HPCAllTrays33CstmLiqO2.LiqO2(m.HPCPE1TrayPressure[tray],m.HPCPE1TrayTemp[tray],m.HPCPE1LiqLvMFrac[tray,"Nitrogen"])
	elif tray==34:
		return m.HPCPE1LiqLvMFrac[tray,"Oxygen"] == triHPCThermo.HPCAllTrays34CstmLiqO2.LiqO2(m.HPCPE1TrayPressure[tray],m.HPCPE1TrayTemp[tray],m.HPCPE1LiqLvMFrac[tray,"Nitrogen"])
	elif tray==35:
		return m.HPCPE1LiqLvMFrac[tray,"Oxygen"] == triHPCThermo.HPCAllTrays35CstmLiqO2.LiqO2(m.HPCPE1TrayPressure[tray],m.HPCPE1TrayTemp[tray],m.HPCPE1LiqLvMFrac[tray,"Nitrogen"])
	elif tray==36:
		return m.HPCPE1LiqLvMFrac[tray,"Oxygen"] == triHPCThermo.HPCAllTrays36CstmLiqO2.LiqO2(m.HPCPE1TrayPressure[tray],m.HPCPE1TrayTemp[tray],m.HPCPE1LiqLvMFrac[tray,"Nitrogen"])
	elif tray==37:
		return m.HPCPE1LiqLvMFrac[tray,"Oxygen"] == triHPCThermo.HPCAllTrays37CstmLiqO2.LiqO2(m.HPCPE1TrayPressure[tray],m.HPCPE1TrayTemp[tray],m.HPCPE1LiqLvMFrac[tray,"Nitrogen"])
	elif tray==38:
		return m.HPCPE1LiqLvMFrac[tray,"Oxygen"] == triHPCThermo.HPCAllTrays38CstmLiqO2.LiqO2(m.HPCPE1TrayPressure[tray],m.HPCPE1TrayTemp[tray],m.HPCPE1LiqLvMFrac[tray,"Nitrogen"])
	elif tray==39:
		return m.HPCPE1LiqLvMFrac[tray,"Oxygen"] == triHPCThermo.HPCAllTrays39CstmLiqO2.LiqO2(m.HPCPE1TrayPressure[tray],m.HPCPE1TrayTemp[tray],m.HPCPE1LiqLvMFrac[tray,"Nitrogen"])
	elif tray==40:
		return m.HPCPE1LiqLvMFrac[tray,"Oxygen"] == triHPCThermo.HPCAllTrays40CstmLiqO2.LiqO2(m.HPCPE1TrayPressure[tray],m.HPCPE1TrayTemp[tray],m.HPCPE1LiqLvMFrac[tray,"Nitrogen"])
	elif tray==41:
		return m.HPCPE1LiqLvMFrac[tray,"Oxygen"] == triHPCThermo.HPCAllTrays41CstmLiqO2.LiqO2(m.HPCPE1TrayPressure[tray],m.HPCPE1TrayTemp[tray],m.HPCPE1LiqLvMFrac[tray,"Nitrogen"])
	elif tray==42:
		return m.HPCPE1LiqLvMFrac[tray,"Oxygen"] == triHPCThermo.HPCAllTrays42CstmLiqO2.LiqO2(m.HPCPE1TrayPressure[tray],m.HPCPE1TrayTemp[tray],m.HPCPE1LiqLvMFrac[tray,"Nitrogen"])
test_model.HPCPE1AllTraysLiqO2Frac = Constraint(test_model.HPCPE1Trays,rule=HPCPE1AllTraysLiqO2Frac)
def HPCPE1AllTraysVapO2Frac(m,tray):
	if tray==1:
		return m.HPCPE1VapLvMFrac[tray,"Oxygen"] == triHPCThermo.HPCAllTrays1CstmVapO2.VapO2(m.HPCPE1TrayPressure[tray],m.HPCPE1TrayTemp[tray],m.HPCPE1LiqLvMFrac[tray,"Nitrogen"])
	elif tray==2:
		return m.HPCPE1VapLvMFrac[tray,"Oxygen"] == triHPCThermo.HPCAllTrays2CstmVapO2.VapO2(m.HPCPE1TrayPressure[tray],m.HPCPE1TrayTemp[tray],m.HPCPE1LiqLvMFrac[tray,"Nitrogen"])
	elif tray==3:
		return m.HPCPE1VapLvMFrac[tray,"Oxygen"] == triHPCThermo.HPCAllTrays3CstmVapO2.VapO2(m.HPCPE1TrayPressure[tray],m.HPCPE1TrayTemp[tray],m.HPCPE1LiqLvMFrac[tray,"Nitrogen"])
	elif tray==4:
		return m.HPCPE1VapLvMFrac[tray,"Oxygen"] == triHPCThermo.HPCAllTrays4CstmVapO2.VapO2(m.HPCPE1TrayPressure[tray],m.HPCPE1TrayTemp[tray],m.HPCPE1LiqLvMFrac[tray,"Nitrogen"])
	elif tray==5:
		return m.HPCPE1VapLvMFrac[tray,"Oxygen"] == triHPCThermo.HPCAllTrays5CstmVapO2.VapO2(m.HPCPE1TrayPressure[tray],m.HPCPE1TrayTemp[tray],m.HPCPE1LiqLvMFrac[tray,"Nitrogen"])
	elif tray==6:
		return m.HPCPE1VapLvMFrac[tray,"Oxygen"] == triHPCThermo.HPCAllTrays6CstmVapO2.VapO2(m.HPCPE1TrayPressure[tray],m.HPCPE1TrayTemp[tray],m.HPCPE1LiqLvMFrac[tray,"Nitrogen"])
	elif tray==7:
		return m.HPCPE1VapLvMFrac[tray,"Oxygen"] == triHPCThermo.HPCAllTrays7CstmVapO2.VapO2(m.HPCPE1TrayPressure[tray],m.HPCPE1TrayTemp[tray],m.HPCPE1LiqLvMFrac[tray,"Nitrogen"])
	elif tray==8:
		return m.HPCPE1VapLvMFrac[tray,"Oxygen"] == triHPCThermo.HPCAllTrays8CstmVapO2.VapO2(m.HPCPE1TrayPressure[tray],m.HPCPE1TrayTemp[tray],m.HPCPE1LiqLvMFrac[tray,"Nitrogen"])
	elif tray==9:
		return m.HPCPE1VapLvMFrac[tray,"Oxygen"] == triHPCThermo.HPCAllTrays9CstmVapO2.VapO2(m.HPCPE1TrayPressure[tray],m.HPCPE1TrayTemp[tray],m.HPCPE1LiqLvMFrac[tray,"Nitrogen"])
	elif tray==10:
		return m.HPCPE1VapLvMFrac[tray,"Oxygen"] == triHPCThermo.HPCAllTrays10CstmVapO2.VapO2(m.HPCPE1TrayPressure[tray],m.HPCPE1TrayTemp[tray],m.HPCPE1LiqLvMFrac[tray,"Nitrogen"])
	elif tray==11:
		return m.HPCPE1VapLvMFrac[tray,"Oxygen"] == triHPCThermo.HPCAllTrays11CstmVapO2.VapO2(m.HPCPE1TrayPressure[tray],m.HPCPE1TrayTemp[tray],m.HPCPE1LiqLvMFrac[tray,"Nitrogen"])
	elif tray==12:
		return m.HPCPE1VapLvMFrac[tray,"Oxygen"] == triHPCThermo.HPCAllTrays12CstmVapO2.VapO2(m.HPCPE1TrayPressure[tray],m.HPCPE1TrayTemp[tray],m.HPCPE1LiqLvMFrac[tray,"Nitrogen"])
	elif tray==13:
		return m.HPCPE1VapLvMFrac[tray,"Oxygen"] == triHPCThermo.HPCAllTrays13CstmVapO2.VapO2(m.HPCPE1TrayPressure[tray],m.HPCPE1TrayTemp[tray],m.HPCPE1LiqLvMFrac[tray,"Nitrogen"])
	elif tray==14:
		return m.HPCPE1VapLvMFrac[tray,"Oxygen"] == triHPCThermo.HPCAllTrays14CstmVapO2.VapO2(m.HPCPE1TrayPressure[tray],m.HPCPE1TrayTemp[tray],m.HPCPE1LiqLvMFrac[tray,"Nitrogen"])
	elif tray==15:
		return m.HPCPE1VapLvMFrac[tray,"Oxygen"] == triHPCThermo.HPCAllTrays15CstmVapO2.VapO2(m.HPCPE1TrayPressure[tray],m.HPCPE1TrayTemp[tray],m.HPCPE1LiqLvMFrac[tray,"Nitrogen"])
	elif tray==16:
		return m.HPCPE1VapLvMFrac[tray,"Oxygen"] == triHPCThermo.HPCAllTrays16CstmVapO2.VapO2(m.HPCPE1TrayPressure[tray],m.HPCPE1TrayTemp[tray],m.HPCPE1LiqLvMFrac[tray,"Nitrogen"])
	elif tray==17:
		return m.HPCPE1VapLvMFrac[tray,"Oxygen"] == triHPCThermo.HPCAllTrays17CstmVapO2.VapO2(m.HPCPE1TrayPressure[tray],m.HPCPE1TrayTemp[tray],m.HPCPE1LiqLvMFrac[tray,"Nitrogen"])
	elif tray==18:
		return m.HPCPE1VapLvMFrac[tray,"Oxygen"] == triHPCThermo.HPCAllTrays18CstmVapO2.VapO2(m.HPCPE1TrayPressure[tray],m.HPCPE1TrayTemp[tray],m.HPCPE1LiqLvMFrac[tray,"Nitrogen"])
	elif tray==19:
		return m.HPCPE1VapLvMFrac[tray,"Oxygen"] == triHPCThermo.HPCAllTrays19CstmVapO2.VapO2(m.HPCPE1TrayPressure[tray],m.HPCPE1TrayTemp[tray],m.HPCPE1LiqLvMFrac[tray,"Nitrogen"])
	elif tray==20:
		return m.HPCPE1VapLvMFrac[tray,"Oxygen"] == triHPCThermo.HPCAllTrays20CstmVapO2.VapO2(m.HPCPE1TrayPressure[tray],m.HPCPE1TrayTemp[tray],m.HPCPE1LiqLvMFrac[tray,"Nitrogen"])
	elif tray==21:
		return m.HPCPE1VapLvMFrac[tray,"Oxygen"] == triHPCThermo.HPCAllTrays21CstmVapO2.VapO2(m.HPCPE1TrayPressure[tray],m.HPCPE1TrayTemp[tray],m.HPCPE1LiqLvMFrac[tray,"Nitrogen"])
	elif tray==22:
		return m.HPCPE1VapLvMFrac[tray,"Oxygen"] == triHPCThermo.HPCAllTrays22CstmVapO2.VapO2(m.HPCPE1TrayPressure[tray],m.HPCPE1TrayTemp[tray],m.HPCPE1LiqLvMFrac[tray,"Nitrogen"])
	elif tray==23:
		return m.HPCPE1VapLvMFrac[tray,"Oxygen"] == triHPCThermo.HPCAllTrays23CstmVapO2.VapO2(m.HPCPE1TrayPressure[tray],m.HPCPE1TrayTemp[tray],m.HPCPE1LiqLvMFrac[tray,"Nitrogen"])
	elif tray==24:
		return m.HPCPE1VapLvMFrac[tray,"Oxygen"] == triHPCThermo.HPCAllTrays24CstmVapO2.VapO2(m.HPCPE1TrayPressure[tray],m.HPCPE1TrayTemp[tray],m.HPCPE1LiqLvMFrac[tray,"Nitrogen"])
	elif tray==25:
		return m.HPCPE1VapLvMFrac[tray,"Oxygen"] == triHPCThermo.HPCAllTrays25CstmVapO2.VapO2(m.HPCPE1TrayPressure[tray],m.HPCPE1TrayTemp[tray],m.HPCPE1LiqLvMFrac[tray,"Nitrogen"])
	elif tray==26:
		return m.HPCPE1VapLvMFrac[tray,"Oxygen"] == triHPCThermo.HPCAllTrays26CstmVapO2.VapO2(m.HPCPE1TrayPressure[tray],m.HPCPE1TrayTemp[tray],m.HPCPE1LiqLvMFrac[tray,"Nitrogen"])
	elif tray==27:
		return m.HPCPE1VapLvMFrac[tray,"Oxygen"] == triHPCThermo.HPCAllTrays27CstmVapO2.VapO2(m.HPCPE1TrayPressure[tray],m.HPCPE1TrayTemp[tray],m.HPCPE1LiqLvMFrac[tray,"Nitrogen"])
	elif tray==28:
		return m.HPCPE1VapLvMFrac[tray,"Oxygen"] == triHPCThermo.HPCAllTrays28CstmVapO2.VapO2(m.HPCPE1TrayPressure[tray],m.HPCPE1TrayTemp[tray],m.HPCPE1LiqLvMFrac[tray,"Nitrogen"])
	elif tray==29:
		return m.HPCPE1VapLvMFrac[tray,"Oxygen"] == triHPCThermo.HPCAllTrays29CstmVapO2.VapO2(m.HPCPE1TrayPressure[tray],m.HPCPE1TrayTemp[tray],m.HPCPE1LiqLvMFrac[tray,"Nitrogen"])
	elif tray==30:
		return m.HPCPE1VapLvMFrac[tray,"Oxygen"] == triHPCThermo.HPCAllTrays30CstmVapO2.VapO2(m.HPCPE1TrayPressure[tray],m.HPCPE1TrayTemp[tray],m.HPCPE1LiqLvMFrac[tray,"Nitrogen"])
	elif tray==31:
		return m.HPCPE1VapLvMFrac[tray,"Oxygen"] == triHPCThermo.HPCAllTrays31CstmVapO2.VapO2(m.HPCPE1TrayPressure[tray],m.HPCPE1TrayTemp[tray],m.HPCPE1LiqLvMFrac[tray,"Nitrogen"])
	elif tray==32:
		return m.HPCPE1VapLvMFrac[tray,"Oxygen"] == triHPCThermo.HPCAllTrays32CstmVapO2.VapO2(m.HPCPE1TrayPressure[tray],m.HPCPE1TrayTemp[tray],m.HPCPE1LiqLvMFrac[tray,"Nitrogen"])
	elif tray==33:
		return m.HPCPE1VapLvMFrac[tray,"Oxygen"] == triHPCThermo.HPCAllTrays33CstmVapO2.VapO2(m.HPCPE1TrayPressure[tray],m.HPCPE1TrayTemp[tray],m.HPCPE1LiqLvMFrac[tray,"Nitrogen"])
	elif tray==34:
		return m.HPCPE1VapLvMFrac[tray,"Oxygen"] == triHPCThermo.HPCAllTrays34CstmVapO2.VapO2(m.HPCPE1TrayPressure[tray],m.HPCPE1TrayTemp[tray],m.HPCPE1LiqLvMFrac[tray,"Nitrogen"])
	elif tray==35:
		return m.HPCPE1VapLvMFrac[tray,"Oxygen"] == triHPCThermo.HPCAllTrays35CstmVapO2.VapO2(m.HPCPE1TrayPressure[tray],m.HPCPE1TrayTemp[tray],m.HPCPE1LiqLvMFrac[tray,"Nitrogen"])
	elif tray==36:
		return m.HPCPE1VapLvMFrac[tray,"Oxygen"] == triHPCThermo.HPCAllTrays36CstmVapO2.VapO2(m.HPCPE1TrayPressure[tray],m.HPCPE1TrayTemp[tray],m.HPCPE1LiqLvMFrac[tray,"Nitrogen"])
	elif tray==37:
		return m.HPCPE1VapLvMFrac[tray,"Oxygen"] == triHPCThermo.HPCAllTrays37CstmVapO2.VapO2(m.HPCPE1TrayPressure[tray],m.HPCPE1TrayTemp[tray],m.HPCPE1LiqLvMFrac[tray,"Nitrogen"])
	elif tray==38:
		return m.HPCPE1VapLvMFrac[tray,"Oxygen"] == triHPCThermo.HPCAllTrays38CstmVapO2.VapO2(m.HPCPE1TrayPressure[tray],m.HPCPE1TrayTemp[tray],m.HPCPE1LiqLvMFrac[tray,"Nitrogen"])
	elif tray==39:
		return m.HPCPE1VapLvMFrac[tray,"Oxygen"] == triHPCThermo.HPCAllTrays39CstmVapO2.VapO2(m.HPCPE1TrayPressure[tray],m.HPCPE1TrayTemp[tray],m.HPCPE1LiqLvMFrac[tray,"Nitrogen"])
	elif tray==40:
		return m.HPCPE1VapLvMFrac[tray,"Oxygen"] == triHPCThermo.HPCAllTrays40CstmVapO2.VapO2(m.HPCPE1TrayPressure[tray],m.HPCPE1TrayTemp[tray],m.HPCPE1LiqLvMFrac[tray,"Nitrogen"])
	elif tray==41:
		return m.HPCPE1VapLvMFrac[tray,"Oxygen"] == triHPCThermo.HPCAllTrays41CstmVapO2.VapO2(m.HPCPE1TrayPressure[tray],m.HPCPE1TrayTemp[tray],m.HPCPE1LiqLvMFrac[tray,"Nitrogen"])
	elif tray==42:
		return m.HPCPE1VapLvMFrac[tray,"Oxygen"] == triHPCThermo.HPCAllTrays42CstmVapO2.VapO2(m.HPCPE1TrayPressure[tray],m.HPCPE1TrayTemp[tray],m.HPCPE1LiqLvMFrac[tray,"Nitrogen"])
test_model.HPCPE1AllTraysVapO2Frac = Constraint(test_model.HPCPE1Trays,rule=HPCPE1AllTraysVapO2Frac)
def HPCPE1AllTraysVapN2Frac(m,tray):
	if tray==1:
		return m.HPCPE1VapLvMFrac[tray,"Nitrogen"] == triHPCThermo.HPCAllTrays1CstmVapN2.VapN2(m.HPCPE1TrayPressure[tray],m.HPCPE1TrayTemp[tray],m.HPCPE1LiqLvMFrac[tray,"Nitrogen"])
	elif tray==2:
		return m.HPCPE1VapLvMFrac[tray,"Nitrogen"] == triHPCThermo.HPCAllTrays2CstmVapN2.VapN2(m.HPCPE1TrayPressure[tray],m.HPCPE1TrayTemp[tray],m.HPCPE1LiqLvMFrac[tray,"Nitrogen"])
	elif tray==3:
		return m.HPCPE1VapLvMFrac[tray,"Nitrogen"] == triHPCThermo.HPCAllTrays3CstmVapN2.VapN2(m.HPCPE1TrayPressure[tray],m.HPCPE1TrayTemp[tray],m.HPCPE1LiqLvMFrac[tray,"Nitrogen"])
	elif tray==4:
		return m.HPCPE1VapLvMFrac[tray,"Nitrogen"] == triHPCThermo.HPCAllTrays4CstmVapN2.VapN2(m.HPCPE1TrayPressure[tray],m.HPCPE1TrayTemp[tray],m.HPCPE1LiqLvMFrac[tray,"Nitrogen"])
	elif tray==5:
		return m.HPCPE1VapLvMFrac[tray,"Nitrogen"] == triHPCThermo.HPCAllTrays5CstmVapN2.VapN2(m.HPCPE1TrayPressure[tray],m.HPCPE1TrayTemp[tray],m.HPCPE1LiqLvMFrac[tray,"Nitrogen"])
	elif tray==6:
		return m.HPCPE1VapLvMFrac[tray,"Nitrogen"] == triHPCThermo.HPCAllTrays6CstmVapN2.VapN2(m.HPCPE1TrayPressure[tray],m.HPCPE1TrayTemp[tray],m.HPCPE1LiqLvMFrac[tray,"Nitrogen"])
	elif tray==7:
		return m.HPCPE1VapLvMFrac[tray,"Nitrogen"] == triHPCThermo.HPCAllTrays7CstmVapN2.VapN2(m.HPCPE1TrayPressure[tray],m.HPCPE1TrayTemp[tray],m.HPCPE1LiqLvMFrac[tray,"Nitrogen"])
	elif tray==8:
		return m.HPCPE1VapLvMFrac[tray,"Nitrogen"] == triHPCThermo.HPCAllTrays8CstmVapN2.VapN2(m.HPCPE1TrayPressure[tray],m.HPCPE1TrayTemp[tray],m.HPCPE1LiqLvMFrac[tray,"Nitrogen"])
	elif tray==9:
		return m.HPCPE1VapLvMFrac[tray,"Nitrogen"] == triHPCThermo.HPCAllTrays9CstmVapN2.VapN2(m.HPCPE1TrayPressure[tray],m.HPCPE1TrayTemp[tray],m.HPCPE1LiqLvMFrac[tray,"Nitrogen"])
	elif tray==10:
		return m.HPCPE1VapLvMFrac[tray,"Nitrogen"] == triHPCThermo.HPCAllTrays10CstmVapN2.VapN2(m.HPCPE1TrayPressure[tray],m.HPCPE1TrayTemp[tray],m.HPCPE1LiqLvMFrac[tray,"Nitrogen"])
	elif tray==11:
		return m.HPCPE1VapLvMFrac[tray,"Nitrogen"] == triHPCThermo.HPCAllTrays11CstmVapN2.VapN2(m.HPCPE1TrayPressure[tray],m.HPCPE1TrayTemp[tray],m.HPCPE1LiqLvMFrac[tray,"Nitrogen"])
	elif tray==12:
		return m.HPCPE1VapLvMFrac[tray,"Nitrogen"] == triHPCThermo.HPCAllTrays12CstmVapN2.VapN2(m.HPCPE1TrayPressure[tray],m.HPCPE1TrayTemp[tray],m.HPCPE1LiqLvMFrac[tray,"Nitrogen"])
	elif tray==13:
		return m.HPCPE1VapLvMFrac[tray,"Nitrogen"] == triHPCThermo.HPCAllTrays13CstmVapN2.VapN2(m.HPCPE1TrayPressure[tray],m.HPCPE1TrayTemp[tray],m.HPCPE1LiqLvMFrac[tray,"Nitrogen"])
	elif tray==14:
		return m.HPCPE1VapLvMFrac[tray,"Nitrogen"] == triHPCThermo.HPCAllTrays14CstmVapN2.VapN2(m.HPCPE1TrayPressure[tray],m.HPCPE1TrayTemp[tray],m.HPCPE1LiqLvMFrac[tray,"Nitrogen"])
	elif tray==15:
		return m.HPCPE1VapLvMFrac[tray,"Nitrogen"] == triHPCThermo.HPCAllTrays15CstmVapN2.VapN2(m.HPCPE1TrayPressure[tray],m.HPCPE1TrayTemp[tray],m.HPCPE1LiqLvMFrac[tray,"Nitrogen"])
	elif tray==16:
		return m.HPCPE1VapLvMFrac[tray,"Nitrogen"] == triHPCThermo.HPCAllTrays16CstmVapN2.VapN2(m.HPCPE1TrayPressure[tray],m.HPCPE1TrayTemp[tray],m.HPCPE1LiqLvMFrac[tray,"Nitrogen"])
	elif tray==17:
		return m.HPCPE1VapLvMFrac[tray,"Nitrogen"] == triHPCThermo.HPCAllTrays17CstmVapN2.VapN2(m.HPCPE1TrayPressure[tray],m.HPCPE1TrayTemp[tray],m.HPCPE1LiqLvMFrac[tray,"Nitrogen"])
	elif tray==18:
		return m.HPCPE1VapLvMFrac[tray,"Nitrogen"] == triHPCThermo.HPCAllTrays18CstmVapN2.VapN2(m.HPCPE1TrayPressure[tray],m.HPCPE1TrayTemp[tray],m.HPCPE1LiqLvMFrac[tray,"Nitrogen"])
	elif tray==19:
		return m.HPCPE1VapLvMFrac[tray,"Nitrogen"] == triHPCThermo.HPCAllTrays19CstmVapN2.VapN2(m.HPCPE1TrayPressure[tray],m.HPCPE1TrayTemp[tray],m.HPCPE1LiqLvMFrac[tray,"Nitrogen"])
	elif tray==20:
		return m.HPCPE1VapLvMFrac[tray,"Nitrogen"] == triHPCThermo.HPCAllTrays20CstmVapN2.VapN2(m.HPCPE1TrayPressure[tray],m.HPCPE1TrayTemp[tray],m.HPCPE1LiqLvMFrac[tray,"Nitrogen"])
	elif tray==21:
		return m.HPCPE1VapLvMFrac[tray,"Nitrogen"] == triHPCThermo.HPCAllTrays21CstmVapN2.VapN2(m.HPCPE1TrayPressure[tray],m.HPCPE1TrayTemp[tray],m.HPCPE1LiqLvMFrac[tray,"Nitrogen"])
	elif tray==22:
		return m.HPCPE1VapLvMFrac[tray,"Nitrogen"] == triHPCThermo.HPCAllTrays22CstmVapN2.VapN2(m.HPCPE1TrayPressure[tray],m.HPCPE1TrayTemp[tray],m.HPCPE1LiqLvMFrac[tray,"Nitrogen"])
	elif tray==23:
		return m.HPCPE1VapLvMFrac[tray,"Nitrogen"] == triHPCThermo.HPCAllTrays23CstmVapN2.VapN2(m.HPCPE1TrayPressure[tray],m.HPCPE1TrayTemp[tray],m.HPCPE1LiqLvMFrac[tray,"Nitrogen"])
	elif tray==24:
		return m.HPCPE1VapLvMFrac[tray,"Nitrogen"] == triHPCThermo.HPCAllTrays24CstmVapN2.VapN2(m.HPCPE1TrayPressure[tray],m.HPCPE1TrayTemp[tray],m.HPCPE1LiqLvMFrac[tray,"Nitrogen"])
	elif tray==25:
		return m.HPCPE1VapLvMFrac[tray,"Nitrogen"] == triHPCThermo.HPCAllTrays25CstmVapN2.VapN2(m.HPCPE1TrayPressure[tray],m.HPCPE1TrayTemp[tray],m.HPCPE1LiqLvMFrac[tray,"Nitrogen"])
	elif tray==26:
		return m.HPCPE1VapLvMFrac[tray,"Nitrogen"] == triHPCThermo.HPCAllTrays26CstmVapN2.VapN2(m.HPCPE1TrayPressure[tray],m.HPCPE1TrayTemp[tray],m.HPCPE1LiqLvMFrac[tray,"Nitrogen"])
	elif tray==27:
		return m.HPCPE1VapLvMFrac[tray,"Nitrogen"] == triHPCThermo.HPCAllTrays27CstmVapN2.VapN2(m.HPCPE1TrayPressure[tray],m.HPCPE1TrayTemp[tray],m.HPCPE1LiqLvMFrac[tray,"Nitrogen"])
	elif tray==28:
		return m.HPCPE1VapLvMFrac[tray,"Nitrogen"] == triHPCThermo.HPCAllTrays28CstmVapN2.VapN2(m.HPCPE1TrayPressure[tray],m.HPCPE1TrayTemp[tray],m.HPCPE1LiqLvMFrac[tray,"Nitrogen"])
	elif tray==29:
		return m.HPCPE1VapLvMFrac[tray,"Nitrogen"] == triHPCThermo.HPCAllTrays29CstmVapN2.VapN2(m.HPCPE1TrayPressure[tray],m.HPCPE1TrayTemp[tray],m.HPCPE1LiqLvMFrac[tray,"Nitrogen"])
	elif tray==30:
		return m.HPCPE1VapLvMFrac[tray,"Nitrogen"] == triHPCThermo.HPCAllTrays30CstmVapN2.VapN2(m.HPCPE1TrayPressure[tray],m.HPCPE1TrayTemp[tray],m.HPCPE1LiqLvMFrac[tray,"Nitrogen"])
	elif tray==31:
		return m.HPCPE1VapLvMFrac[tray,"Nitrogen"] == triHPCThermo.HPCAllTrays31CstmVapN2.VapN2(m.HPCPE1TrayPressure[tray],m.HPCPE1TrayTemp[tray],m.HPCPE1LiqLvMFrac[tray,"Nitrogen"])
	elif tray==32:
		return m.HPCPE1VapLvMFrac[tray,"Nitrogen"] == triHPCThermo.HPCAllTrays32CstmVapN2.VapN2(m.HPCPE1TrayPressure[tray],m.HPCPE1TrayTemp[tray],m.HPCPE1LiqLvMFrac[tray,"Nitrogen"])
	elif tray==33:
		return m.HPCPE1VapLvMFrac[tray,"Nitrogen"] == triHPCThermo.HPCAllTrays33CstmVapN2.VapN2(m.HPCPE1TrayPressure[tray],m.HPCPE1TrayTemp[tray],m.HPCPE1LiqLvMFrac[tray,"Nitrogen"])
	elif tray==34:
		return m.HPCPE1VapLvMFrac[tray,"Nitrogen"] == triHPCThermo.HPCAllTrays34CstmVapN2.VapN2(m.HPCPE1TrayPressure[tray],m.HPCPE1TrayTemp[tray],m.HPCPE1LiqLvMFrac[tray,"Nitrogen"])
	elif tray==35:
		return m.HPCPE1VapLvMFrac[tray,"Nitrogen"] == triHPCThermo.HPCAllTrays35CstmVapN2.VapN2(m.HPCPE1TrayPressure[tray],m.HPCPE1TrayTemp[tray],m.HPCPE1LiqLvMFrac[tray,"Nitrogen"])
	elif tray==36:
		return m.HPCPE1VapLvMFrac[tray,"Nitrogen"] == triHPCThermo.HPCAllTrays36CstmVapN2.VapN2(m.HPCPE1TrayPressure[tray],m.HPCPE1TrayTemp[tray],m.HPCPE1LiqLvMFrac[tray,"Nitrogen"])
	elif tray==37:
		return m.HPCPE1VapLvMFrac[tray,"Nitrogen"] == triHPCThermo.HPCAllTrays37CstmVapN2.VapN2(m.HPCPE1TrayPressure[tray],m.HPCPE1TrayTemp[tray],m.HPCPE1LiqLvMFrac[tray,"Nitrogen"])
	elif tray==38:
		return m.HPCPE1VapLvMFrac[tray,"Nitrogen"] == triHPCThermo.HPCAllTrays38CstmVapN2.VapN2(m.HPCPE1TrayPressure[tray],m.HPCPE1TrayTemp[tray],m.HPCPE1LiqLvMFrac[tray,"Nitrogen"])
	elif tray==39:
		return m.HPCPE1VapLvMFrac[tray,"Nitrogen"] == triHPCThermo.HPCAllTrays39CstmVapN2.VapN2(m.HPCPE1TrayPressure[tray],m.HPCPE1TrayTemp[tray],m.HPCPE1LiqLvMFrac[tray,"Nitrogen"])
	elif tray==40:
		return m.HPCPE1VapLvMFrac[tray,"Nitrogen"] == triHPCThermo.HPCAllTrays40CstmVapN2.VapN2(m.HPCPE1TrayPressure[tray],m.HPCPE1TrayTemp[tray],m.HPCPE1LiqLvMFrac[tray,"Nitrogen"])
	elif tray==41:
		return m.HPCPE1VapLvMFrac[tray,"Nitrogen"] == triHPCThermo.HPCAllTrays41CstmVapN2.VapN2(m.HPCPE1TrayPressure[tray],m.HPCPE1TrayTemp[tray],m.HPCPE1LiqLvMFrac[tray,"Nitrogen"])
	elif tray==42:
		return m.HPCPE1VapLvMFrac[tray,"Nitrogen"] == triHPCThermo.HPCAllTrays42CstmVapN2.VapN2(m.HPCPE1TrayPressure[tray],m.HPCPE1TrayTemp[tray],m.HPCPE1LiqLvMFrac[tray,"Nitrogen"])
test_model.HPCPE1AllTraysVapN2Frac = Constraint(test_model.HPCPE1Trays,rule=HPCPE1AllTraysVapN2Frac)
#--------HPCPE1 Summation---------
def HPCPE1LiqSum(m, tray):
	return sum([m.HPCPE1LiqLvMFrac[tray, c] for c in m.Component]) == 1
test_model.HPCPE1LiqSum = Constraint(test_model.HPCPE1Trays, rule=HPCPE1LiqSum)
def HPCPE1VapSum(m, tray):
	return sum([m.HPCPE1VapLvMFrac[tray, c] for c in m.Component]) == 1
test_model.HPCPE1VapSum = Constraint(test_model.HPCPE1Trays, rule=HPCPE1VapSum)
#--------HPCPE1 Pressure Profile---------
def HPCPE1PProf(m, tray):
	return ((m.HPCPE1TopPressure-m.HPCPE1BtmPressure)/41*(tray-1)+m.HPCPE1BtmPressure - m.HPCPE1TrayPressure[tray])*0.010000 == 0
test_model.HPCPE1PProf = Constraint(test_model.HPCPE1Trays, rule=HPCPE1PProf)
#--------HPCPE1 Extractions---------
def HPCPE1Ext6MFracSpec(m, comp):
	return m.HPCPE1Ext6MFrac[comp] - m.HPCPE1LiqLvMFrac[6, comp] == 0 
test_model.HPCPE1Ext6MFracSpec = Constraint(test_model.Component, rule=HPCPE1Ext6MFracSpec)
def HPCPE1Ext6MEtlpSpec(m):
	return (m.HPCPE1Ext6MEtlp - m.HPCPE1LiqLvMEtlp[6])*  0.000010 == 0
test_model.HPCPE1Ext6MEtlpSpec = Constraint(rule=HPCPE1Ext6MEtlpSpec)
def HPCPE1Ext22MFracSpec(m, comp):
	return m.HPCPE1Ext22MFrac[comp] - m.HPCPE1VapLvMFrac[22, comp] == 0 
test_model.HPCPE1Ext22MFracSpec = Constraint(test_model.Component, rule=HPCPE1Ext22MFracSpec)
def HPCPE1Ext22MEtlpSpec(m):
	return (m.HPCPE1Ext22MEtlp - m.HPCPE1VapLvMEtlp[22])*  0.000010 == 0
test_model.HPCPE1Ext22MEtlpSpec = Constraint(rule=HPCPE1Ext22MEtlpSpec)

#----------------------------------
#           HPCSumpPE1
#----------------------------------
#--------HPCSumpPE1 Mass Balance---------
def HPCSumpPE1MassBlnc(m):
	return (m.HPCPE1LiqLvMFlow[1]-m.HPCSumpPE1OutMFlow)*0.001000==0
test_model.HPCSumpPE1MassBlnc = Constraint(rule=HPCSumpPE1MassBlnc)
def HPCSumpPE1HldpMFracSpec(m, comp):
	return m.HPCSumpPE1HldpMFrac[comp] - m.HPCPE1LiqLvMFrac[1,comp] == 0
test_model.HPCSumpPE1HldpMFracSpec = Constraint(test_model.Component, rule=HPCSumpPE1HldpMFracSpec)

#----------------------------------
#           HPCCondPE1
#----------------------------------
#--------HPCCondPE1 Mass Balance---------
def HPCCondPE1MassBlnc(m):
	return (m.HPCCondPE1RefMFlow+m.HPCCondPE1PrdtMFlow-m.HPCPE1VapLvMFlow[42])*0.001000==0
test_model.HPCCondPE1MassBlnc = Constraint(rule=HPCCondPE1MassBlnc)
def HPCCondPE1RefSpec(m):
	return (m.HPCCondPE1RefMFlow-m.HPCPE1VapLvMFlow[42]*m.HPCCondPE1RefluxRatio)*0.001000==0
test_model.HPCCondPE1RefSpec = Constraint(rule=HPCCondPE1RefSpec)
#--------HPCCondPE1 Energy Balance---------
def HPCCondPE1EngBlnc(m):
	return (m.HPCPE1VapLvMFlow[42]*(m.HPCPE1VapLvMEtlp[42]-m.HPCCondPE1OutMEtlp)-m.HPCCondPE1MHeatOut)*0.000010==0
test_model.HPCCondPE1EngBlnc = Constraint(rule=HPCCondPE1EngBlnc)
#--------HPCCondPE1 Bubble Point---------
def HPCCondPE1SelfBubTemp(m):
	return m.HPCPE1VapLvMFrac[42,"Oxygen"] == triHPCThermo.HPCCondSelfCstmLiqO2.LiqO2(m.HPCPE1TrayPressure[42],m.HPCCondPE1Temp,m.HPCPE1VapLvMFrac[42,"Nitrogen"])
test_model.HPCCondPE1SelfBubTemp = Constraint(rule=HPCCondPE1SelfBubTemp)

#===================================
#
#       Parameter Estimation
#
#===================================
#--------HPCFeed1PE1---------
#--------HPCFeed2PE1---------
#--------HPCPE1---------
test_model.HPCUALeakage = Var(initialize = 10.000000, within=NonNegativeReals)
test_model.HPCAmbientTemp = Var(initialize = 25.000000, bounds = (10,40))
#--------HPCSumpPE1---------
#--------HPCCondPE1---------
#--------HPCFeed1PE0---------
#--------HPCFeed2PE0---------
#--------HPCPE0---------
def HPCPE0UALeakagePE(m):
	return (m.HPCPE0UALeakage - m.HPCUALeakage)*0.001000==0
test_model.HPCPE0UALeakagePE = Constraint(rule=HPCPE0UALeakagePE)
def HPCPE0AmbientTempPE(m):
	return (m.HPCPE0AmbientTemp - m.HPCAmbientTemp)*0.100000==0
test_model.HPCPE0AmbientTempPE = Constraint(rule=HPCPE0AmbientTempPE)
#--------HPCSumpPE0---------
#--------HPCCondPE0---------
#--------HPCFeed1PE1---------
#--------HPCFeed2PE1---------
#--------HPCPE1---------
def HPCPE1UALeakagePE(m):
	return (m.HPCPE1UALeakage - m.HPCUALeakage)*0.001000==0
test_model.HPCPE1UALeakagePE = Constraint(rule=HPCPE1UALeakagePE)
def HPCPE1AmbientTempPE(m):
	return (m.HPCPE1AmbientTemp - m.HPCAmbientTemp)*0.100000==0
test_model.HPCPE1AmbientTempPE = Constraint(rule=HPCPE1AmbientTempPE)
#--------HPCSumpPE1---------
#--------HPCCondPE1---------
def OBJ_func(m):
	return (m.HPCPE0LiqLvMFlow[1] - 2184.0)**2*0.001\
	     + (m.HPCPE0LiqLvMFlow[2] - 2136.68662)**2*0.001\
	     + (m.HPCPE0LiqLvMFlow[3] - 2157.586671)**2*0.001\
	     + (m.HPCPE0LiqLvMFlow[4] - 2178.166928)**2*0.001\
	     + (m.HPCPE0LiqLvMFlow[5] - 1028.221435)**2*0.001\
	     + (m.HPCPE0LiqLvMFlow[6] - 1036.780804)**2*0.001\
	     + (m.HPCPE0LiqLvMFlow[7] - 1882.619668)**2*0.001\
	     + (m.HPCPE0LiqLvMFlow[8] - 1898.660873)**2*0.001\
	     + (m.HPCPE0LiqLvMFlow[9] - 1914.138391)**2*0.001\
	     + (m.HPCPE0LiqLvMFlow[10] - 1928.535583)**2*0.001\
	     + (m.HPCPE0LiqLvMFlow[11] - 1941.487748)**2*0.001\
	     + (m.HPCPE0LiqLvMFlow[12] - 1952.800484)**2*0.001\
	     + (m.HPCPE0LiqLvMFlow[13] - 1962.433354)**2*0.001\
	     + (m.HPCPE0LiqLvMFlow[14] - 1970.463026)**2*0.001\
	     + (m.HPCPE0LiqLvMFlow[15] - 1977.040714)**2*0.001\
	     + (m.HPCPE0LiqLvMFlow[16] - 1982.354315)**2*0.001\
	     + (m.HPCPE0LiqLvMFlow[17] - 1986.600007)**2*0.001\
	     + (m.HPCPE0LiqLvMFlow[18] - 1989.963922)**2*0.001\
	     + (m.HPCPE0LiqLvMFlow[19] - 1992.612186)**2*0.001\
	     + (m.HPCPE0LiqLvMFlow[20] - 1994.686985)**2*0.001\
	     + (m.HPCPE0LiqLvMFlow[21] - 1996.306415)**2*0.001\
	     + (m.HPCPE0LiqLvMFlow[22] - 1997.566443)**2*0.001\
	     + (m.HPCPE0LiqLvMFlow[23] - 1998.543759)**2*0.001\
	     + (m.HPCPE0LiqLvMFlow[24] - 1999.284)**2*0.001\
	     + (m.HPCPE0LiqLvMFlow[25] - 1999.840484)**2*0.001\
	     + (m.HPCPE0LiqLvMFlow[26] - 2000.253378)**2*0.001\
	     + (m.HPCPE0LiqLvMFlow[27] - 2000.553467)**2*0.001\
	     + (m.HPCPE0LiqLvMFlow[28] - 2000.764298)**2*0.001\
	     + (m.HPCPE0LiqLvMFlow[29] - 2000.903881)**2*0.001\
	     + (m.HPCPE0LiqLvMFlow[30] - 2000.986011)**2*0.001\
	     + (m.HPCPE0LiqLvMFlow[31] - 2001.021287)**2*0.001\
	     + (m.HPCPE0LiqLvMFlow[32] - 2001.017891)**2*0.001\
	     + (m.HPCPE0LiqLvMFlow[33] - 2000.982177)**2*0.001\
	     + (m.HPCPE0LiqLvMFlow[34] - 2000.91912)**2*0.001\
	     + (m.HPCPE0LiqLvMFlow[35] - 2000.832651)**2*0.001\
	     + (m.HPCPE0LiqLvMFlow[36] - 2000.725908)**2*0.001\
	     + (m.HPCPE0LiqLvMFlow[37] - 2000.601428)**2*0.001\
	     + (m.HPCPE0LiqLvMFlow[38] - 2000.461284)**2*0.001\
	     + (m.HPCPE0LiqLvMFlow[39] - 2000.307193)**2*0.001\
	     + (m.HPCPE0LiqLvMFlow[40] - 2000.140594)**2*0.001\
	     + (m.HPCPE0LiqLvMFlow[41] - 1999.962707)**2*0.001\
	     + (m.HPCPE0LiqLvMFlow[42] - 1999.774589)**2*0.001\
	     + (m.HPCPE0TrayTemp[1] - -173.7216905)**2*0.01\
	     + (m.HPCPE0TrayTemp[2] - -174.1353408)**2*0.01\
	     + (m.HPCPE0TrayTemp[3] - -174.5401255)**2*0.01\
	     + (m.HPCPE0TrayTemp[4] - -174.9178868)**2*0.01\
	     + (m.HPCPE0TrayTemp[5] - -175.0873053)**2*0.01\
	     + (m.HPCPE0TrayTemp[6] - -175.3910693)**2*0.01\
	     + (m.HPCPE0TrayTemp[7] - -175.6944174)**2*0.01\
	     + (m.HPCPE0TrayTemp[8] - -175.9867099)**2*0.01\
	     + (m.HPCPE0TrayTemp[9] - -176.2590873)**2*0.01\
	     + (m.HPCPE0TrayTemp[10] - -176.5054241)**2*0.01\
	     + (m.HPCPE0TrayTemp[11] - -176.7225846)**2*0.01\
	     + (m.HPCPE0TrayTemp[12] - -176.9100917)**2*0.01\
	     + (m.HPCPE0TrayTemp[13] - -177.06946)**2*0.01\
	     + (m.HPCPE0TrayTemp[14] - -177.2034502)**2*0.01\
	     + (m.HPCPE0TrayTemp[15] - -177.3154153)**2*0.01\
	     + (m.HPCPE0TrayTemp[16] - -177.408818)**2*0.01\
	     + (m.HPCPE0TrayTemp[17] - -177.4869217)**2*0.01\
	     + (m.HPCPE0TrayTemp[18] - -177.5526267)**2*0.01\
	     + (m.HPCPE0TrayTemp[19] - -177.608408)**2*0.01\
	     + (m.HPCPE0TrayTemp[20] - -177.6563171)**2*0.01\
	     + (m.HPCPE0TrayTemp[21] - -177.6980182)**2*0.01\
	     + (m.HPCPE0TrayTemp[22] - -177.7348405)**2*0.01\
	     + (m.HPCPE0TrayTemp[23] - -177.7678333)**2*0.01\
	     + (m.HPCPE0TrayTemp[24] - -177.7976166)**2*0.01\
	     + (m.HPCPE0TrayTemp[25] - -177.8248944)**2*0.01\
	     + (m.HPCPE0TrayTemp[26] - -177.8502062)**2*0.01\
	     + (m.HPCPE0TrayTemp[27] - -177.8739644)**2*0.01\
	     + (m.HPCPE0TrayTemp[28] - -177.8964844)**2*0.01\
	     + (m.HPCPE0TrayTemp[29] - -177.918008)**2*0.01\
	     + (m.HPCPE0TrayTemp[30] - -177.9387207)**2*0.01\
	     + (m.HPCPE0TrayTemp[31] - -177.9587658)**2*0.01\
	     + (m.HPCPE0TrayTemp[32] - -177.9782546)**2*0.01\
	     + (m.HPCPE0TrayTemp[33] - -177.9972743)**2*0.01\
	     + (m.HPCPE0TrayTemp[34] - -178.0158938)**2*0.01\
	     + (m.HPCPE0TrayTemp[35] - -178.034168)**2*0.01\
	     + (m.HPCPE0TrayTemp[36] - -178.0521415)**2*0.01\
	     + (m.HPCPE0TrayTemp[37] - -178.0698506)**2*0.01\
	     + (m.HPCPE0TrayTemp[38] - -178.0873257)**2*0.01\
	     + (m.HPCPE0TrayTemp[39] - -178.1045923)**2*0.01\
	     + (m.HPCPE0TrayTemp[40] - -178.1216719)**2*0.01\
	     + (m.HPCPE0TrayTemp[41] - -178.1385833)**2*0.01\
	     + (m.HPCPE0TrayTemp[42] - -178.1553429)**2*0.01\
	     + (m.HPCPE0VapLvMFlow[1] - 3278.966664)**2*0.001\
	     + (m.HPCPE0VapLvMFlow[2] - 3299.866715)**2*0.001\
	     + (m.HPCPE0VapLvMFlow[3] - 3320.446971)**2*0.001\
	     + (m.HPCPE0VapLvMFlow[4] - 3446.489701)**2*0.001\
	     + (m.HPCPE0VapLvMFlow[5] - 3455.049069)**2*0.001\
	     + (m.HPCPE0VapLvMFlow[6] - 3471.042832)**2*0.001\
	     + (m.HPCPE0VapLvMFlow[7] - 3487.084036)**2*0.001\
	     + (m.HPCPE0VapLvMFlow[8] - 3502.561554)**2*0.001\
	     + (m.HPCPE0VapLvMFlow[9] - 3516.958747)**2*0.001\
	     + (m.HPCPE0VapLvMFlow[10] - 3529.910911)**2*0.001\
	     + (m.HPCPE0VapLvMFlow[11] - 3541.223647)**2*0.001\
	     + (m.HPCPE0VapLvMFlow[12] - 3550.856518)**2*0.001\
	     + (m.HPCPE0VapLvMFlow[13] - 3558.886189)**2*0.001\
	     + (m.HPCPE0VapLvMFlow[14] - 3565.463878)**2*0.001\
	     + (m.HPCPE0VapLvMFlow[15] - 3570.777478)**2*0.001\
	     + (m.HPCPE0VapLvMFlow[16] - 3575.023171)**2*0.001\
	     + (m.HPCPE0VapLvMFlow[17] - 3578.387085)**2*0.001\
	     + (m.HPCPE0VapLvMFlow[18] - 3581.035349)**2*0.001\
	     + (m.HPCPE0VapLvMFlow[19] - 3583.110148)**2*0.001\
	     + (m.HPCPE0VapLvMFlow[20] - 3584.729578)**2*0.001\
	     + (m.HPCPE0VapLvMFlow[21] - 3585.989606)**2*0.001\
	     + (m.HPCPE0VapLvMFlow[22] - 3539.675159)**2*0.001\
	     + (m.HPCPE0VapLvMFlow[23] - 3540.4154)**2*0.001\
	     + (m.HPCPE0VapLvMFlow[24] - 3540.971883)**2*0.001\
	     + (m.HPCPE0VapLvMFlow[25] - 3541.384778)**2*0.001\
	     + (m.HPCPE0VapLvMFlow[26] - 3541.684867)**2*0.001\
	     + (m.HPCPE0VapLvMFlow[27] - 3541.895698)**2*0.001\
	     + (m.HPCPE0VapLvMFlow[28] - 3542.035281)**2*0.001\
	     + (m.HPCPE0VapLvMFlow[29] - 3542.117411)**2*0.001\
	     + (m.HPCPE0VapLvMFlow[30] - 3542.152687)**2*0.001\
	     + (m.HPCPE0VapLvMFlow[31] - 3542.14929)**2*0.001\
	     + (m.HPCPE0VapLvMFlow[32] - 3542.113576)**2*0.001\
	     + (m.HPCPE0VapLvMFlow[33] - 3542.050519)**2*0.001\
	     + (m.HPCPE0VapLvMFlow[34] - 3541.96405)**2*0.001\
	     + (m.HPCPE0VapLvMFlow[35] - 3541.857308)**2*0.001\
	     + (m.HPCPE0VapLvMFlow[36] - 3541.732828)**2*0.001\
	     + (m.HPCPE0VapLvMFlow[37] - 3541.592684)**2*0.001\
	     + (m.HPCPE0VapLvMFlow[38] - 3541.438593)**2*0.001\
	     + (m.HPCPE0VapLvMFlow[39] - 3541.271994)**2*0.001\
	     + (m.HPCPE0VapLvMFlow[40] - 3541.094106)**2*0.001\
	     + (m.HPCPE0VapLvMFlow[41] - 3540.905989)**2*0.001\
	     + (m.HPCPE0VapLvMFlow[42] - 3541.094846)**2*0.001\
	     + (m.HPCPE1LiqLvMFlow[1] - 1882.0)**2*0.001\
	     + (m.HPCPE1LiqLvMFlow[2] - 1834.037398)**2*0.001\
	     + (m.HPCPE1LiqLvMFlow[3] - 1850.887406)**2*0.001\
	     + (m.HPCPE1LiqLvMFlow[4] - 1869.213)**2*0.001\
	     + (m.HPCPE1LiqLvMFlow[5] - 788.4147033)**2*0.001\
	     + (m.HPCPE1LiqLvMFlow[6] - 790.9869725)**2*0.001\
	     + (m.HPCPE1LiqLvMFlow[7] - 1626.77056)**2*0.001\
	     + (m.HPCPE1LiqLvMFlow[8] - 1633.480043)**2*0.001\
	     + (m.HPCPE1LiqLvMFlow[9] - 1640.901197)**2*0.001\
	     + (m.HPCPE1LiqLvMFlow[10] - 1648.930942)**2*0.001\
	     + (m.HPCPE1LiqLvMFlow[11] - 1657.413339)**2*0.001\
	     + (m.HPCPE1LiqLvMFlow[12] - 1666.152299)**2*0.001\
	     + (m.HPCPE1LiqLvMFlow[13] - 1674.931672)**2*0.001\
	     + (m.HPCPE1LiqLvMFlow[14] - 1683.53835)**2*0.001\
	     + (m.HPCPE1LiqLvMFlow[15] - 1691.783357)**2*0.001\
	     + (m.HPCPE1LiqLvMFlow[16] - 1699.516923)**2*0.001\
	     + (m.HPCPE1LiqLvMFlow[17] - 1706.635715)**2*0.001\
	     + (m.HPCPE1LiqLvMFlow[18] - 1713.082678)**2*0.001\
	     + (m.HPCPE1LiqLvMFlow[19] - 1718.84145)**2*0.001\
	     + (m.HPCPE1LiqLvMFlow[20] - 1723.927862)**2*0.001\
	     + (m.HPCPE1LiqLvMFlow[21] - 1728.380683)**2*0.001\
	     + (m.HPCPE1LiqLvMFlow[22] - 1732.253104)**2*0.001\
	     + (m.HPCPE1LiqLvMFlow[23] - 1735.605714)**2*0.001\
	     + (m.HPCPE1LiqLvMFlow[24] - 1738.455299)**2*0.001\
	     + (m.HPCPE1LiqLvMFlow[25] - 1740.875979)**2*0.001\
	     + (m.HPCPE1LiqLvMFlow[26] - 1742.93435)**2*0.001\
	     + (m.HPCPE1LiqLvMFlow[27] - 1744.689485)**2*0.001\
	     + (m.HPCPE1LiqLvMFlow[28] - 1746.192651)**2*0.001\
	     + (m.HPCPE1LiqLvMFlow[29] - 1747.487593)**2*0.001\
	     + (m.HPCPE1LiqLvMFlow[30] - 1748.611115)**2*0.001\
	     + (m.HPCPE1LiqLvMFlow[31] - 1749.593832)**2*0.001\
	     + (m.HPCPE1LiqLvMFlow[32] - 1750.460959)**2*0.001\
	     + (m.HPCPE1LiqLvMFlow[33] - 1751.233088)**2*0.001\
	     + (m.HPCPE1LiqLvMFlow[34] - 1751.926911)**2*0.001\
	     + (m.HPCPE1LiqLvMFlow[35] - 1752.55586)**2*0.001\
	     + (m.HPCPE1LiqLvMFlow[36] - 1753.130676)**2*0.001\
	     + (m.HPCPE1LiqLvMFlow[37] - 1753.65989)**2*0.001\
	     + (m.HPCPE1LiqLvMFlow[38] - 1754.150239)**2*0.001\
	     + (m.HPCPE1LiqLvMFlow[39] - 1754.607008)**2*0.001\
	     + (m.HPCPE1LiqLvMFlow[40] - 1755.034313)**2*0.001\
	     + (m.HPCPE1LiqLvMFlow[41] - 1755.435341)**2*0.001\
	     + (m.HPCPE1LiqLvMFlow[42] - 1755.812544)**2*0.001\
	     + (m.HPCPE1TrayTemp[1] - -173.6429506)**2*0.01\
	     + (m.HPCPE1TrayTemp[2] - -174.0039133)**2*0.01\
	     + (m.HPCPE1TrayTemp[3] - -174.3921521)**2*0.01\
	     + (m.HPCPE1TrayTemp[4] - -174.7905387)**2*0.01\
	     + (m.HPCPE1TrayTemp[5] - -174.8559733)**2*0.01\
	     + (m.HPCPE1TrayTemp[6] - -174.9889566)**2*0.01\
	     + (m.HPCPE1TrayTemp[7] - -175.1355429)**2*0.01\
	     + (m.HPCPE1TrayTemp[8] - -175.2945475)**2*0.01\
	     + (m.HPCPE1TrayTemp[9] - -175.4639807)**2*0.01\
	     + (m.HPCPE1TrayTemp[10] - -175.6411062)**2*0.01\
	     + (m.HPCPE1TrayTemp[11] - -175.822614)**2*0.01\
	     + (m.HPCPE1TrayTemp[12] - -176.0048908)**2*0.01\
	     + (m.HPCPE1TrayTemp[13] - -176.1843406)**2*0.01\
	     + (m.HPCPE1TrayTemp[14] - -176.3576955)**2*0.01\
	     + (m.HPCPE1TrayTemp[15] - -176.5222614)**2*0.01\
	     + (m.HPCPE1TrayTemp[16] - -176.6760642)**2*0.01\
	     + (m.HPCPE1TrayTemp[17] - -176.8178895)**2*0.01\
	     + (m.HPCPE1TrayTemp[18] - -176.9472315)**2*0.01\
	     + (m.HPCPE1TrayTemp[19] - -177.0641818)**2*0.01\
	     + (m.HPCPE1TrayTemp[20] - -177.1692886)**2*0.01\
	     + (m.HPCPE1TrayTemp[21] - -177.2634132)**2*0.01\
	     + (m.HPCPE1TrayTemp[22] - -177.3476013)**2*0.01\
	     + (m.HPCPE1TrayTemp[23] - -177.4229789)**2*0.01\
	     + (m.HPCPE1TrayTemp[24] - -177.4899232)**2*0.01\
	     + (m.HPCPE1TrayTemp[25] - -177.5497139)**2*0.01\
	     + (m.HPCPE1TrayTemp[26] - -177.6035)**2*0.01\
	     + (m.HPCPE1TrayTemp[27] - -177.6522879)**2*0.01\
	     + (m.HPCPE1TrayTemp[28] - -177.6969425)**2*0.01\
	     + (m.HPCPE1TrayTemp[29] - -177.7381949)**2*0.01\
	     + (m.HPCPE1TrayTemp[30] - -177.7766561)**2*0.01\
	     + (m.HPCPE1TrayTemp[31] - -177.8128306)**2*0.01\
	     + (m.HPCPE1TrayTemp[32] - -177.8471315)**2*0.01\
	     + (m.HPCPE1TrayTemp[33] - -177.879894)**2*0.01\
	     + (m.HPCPE1TrayTemp[34] - -177.9113886)**2*0.01\
	     + (m.HPCPE1TrayTemp[35] - -177.9418313)**2*0.01\
	     + (m.HPCPE1TrayTemp[36] - -177.9713944)**2*0.01\
	     + (m.HPCPE1TrayTemp[37] - -178.0002136)**2*0.01\
	     + (m.HPCPE1TrayTemp[38] - -178.0283956)**2*0.01\
	     + (m.HPCPE1TrayTemp[39] - -178.0560236)**2*0.01\
	     + (m.HPCPE1TrayTemp[40] - -178.0831619)**2*0.01\
	     + (m.HPCPE1TrayTemp[41] - -178.1098601)**2*0.01\
	     + (m.HPCPE1TrayTemp[42] - -178.1361561)**2*0.01\
	     + (m.HPCPE1VapLvMFlow[1] - 3052.295626)**2*0.001\
	     + (m.HPCPE1VapLvMFlow[2] - 3069.145634)**2*0.001\
	     + (m.HPCPE1VapLvMFlow[3] - 3087.471228)**2*0.001\
	     + (m.HPCPE1VapLvMFlow[4] - 3206.672931)**2*0.001\
	     + (m.HPCPE1VapLvMFlow[5] - 3209.2452)**2*0.001\
	     + (m.HPCPE1VapLvMFlow[6] - 3215.195959)**2*0.001\
	     + (m.HPCPE1VapLvMFlow[7] - 3221.905442)**2*0.001\
	     + (m.HPCPE1VapLvMFlow[8] - 3229.326596)**2*0.001\
	     + (m.HPCPE1VapLvMFlow[9] - 3237.356341)**2*0.001\
	     + (m.HPCPE1VapLvMFlow[10] - 3245.838738)**2*0.001\
	     + (m.HPCPE1VapLvMFlow[11] - 3254.577698)**2*0.001\
	     + (m.HPCPE1VapLvMFlow[12] - 3263.357071)**2*0.001\
	     + (m.HPCPE1VapLvMFlow[13] - 3271.963749)**2*0.001\
	     + (m.HPCPE1VapLvMFlow[14] - 3280.208757)**2*0.001\
	     + (m.HPCPE1VapLvMFlow[15] - 3287.942322)**2*0.001\
	     + (m.HPCPE1VapLvMFlow[16] - 3295.061115)**2*0.001\
	     + (m.HPCPE1VapLvMFlow[17] - 3301.508077)**2*0.001\
	     + (m.HPCPE1VapLvMFlow[18] - 3307.266849)**2*0.001\
	     + (m.HPCPE1VapLvMFlow[19] - 3312.353261)**2*0.001\
	     + (m.HPCPE1VapLvMFlow[20] - 3316.806082)**2*0.001\
	     + (m.HPCPE1VapLvMFlow[21] - 3320.678503)**2*0.001\
	     + (m.HPCPE1VapLvMFlow[22] - 3276.736858)**2*0.001\
	     + (m.HPCPE1VapLvMFlow[23] - 3279.586444)**2*0.001\
	     + (m.HPCPE1VapLvMFlow[24] - 3282.007123)**2*0.001\
	     + (m.HPCPE1VapLvMFlow[25] - 3284.065495)**2*0.001\
	     + (m.HPCPE1VapLvMFlow[26] - 3285.820629)**2*0.001\
	     + (m.HPCPE1VapLvMFlow[27] - 3287.323796)**2*0.001\
	     + (m.HPCPE1VapLvMFlow[28] - 3288.618738)**2*0.001\
	     + (m.HPCPE1VapLvMFlow[29] - 3289.74226)**2*0.001\
	     + (m.HPCPE1VapLvMFlow[30] - 3290.724977)**2*0.001\
	     + (m.HPCPE1VapLvMFlow[31] - 3291.592103)**2*0.001\
	     + (m.HPCPE1VapLvMFlow[32] - 3292.364233)**2*0.001\
	     + (m.HPCPE1VapLvMFlow[33] - 3293.058056)**2*0.001\
	     + (m.HPCPE1VapLvMFlow[34] - 3293.687005)**2*0.001\
	     + (m.HPCPE1VapLvMFlow[35] - 3294.26182)**2*0.001\
	     + (m.HPCPE1VapLvMFlow[36] - 3294.791035)**2*0.001\
	     + (m.HPCPE1VapLvMFlow[37] - 3295.281384)**2*0.001\
	     + (m.HPCPE1VapLvMFlow[38] - 3295.738152)**2*0.001\
	     + (m.HPCPE1VapLvMFlow[39] - 3296.165457)**2*0.001\
	     + (m.HPCPE1VapLvMFlow[40] - 3296.566486)**2*0.001\
	     + (m.HPCPE1VapLvMFlow[41] - 3296.943689)**2*0.001\
	     + (m.HPCPE1VapLvMFlow[42] - 3297.637988)**2*0.001
test_model.OBJ = Objective(rule = OBJ_func)