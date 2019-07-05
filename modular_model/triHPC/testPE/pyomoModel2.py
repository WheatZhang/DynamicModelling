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
#      Parameters & Sets
#
#===================================
#--------HPCFeed1---------
test_model.HPCFeed1MFlow = Param(initialize = 3100.000000)
test_model.HPCFeed1MFrac = Param(test_model.Component, initialize = {'Oxygen': 0.2095, 'Nitrogen': 0.7812, 'Argon': 0.0093})
test_model.HPCFeed1Pressure = Param(initialize = 564.000000)
test_model.HPCFeed1VF = Param(initialize = 0.980000)
#--------HPCFeed2---------
test_model.HPCFeed2MFlow = Param(initialize = 1200.000000)
test_model.HPCFeed2MFrac = Param(test_model.Component, initialize = {'Oxygen': 0.2095, 'Nitrogen': 0.7812, 'Argon': 0.0093})
test_model.HPCFeed2Pressure = Param(initialize = 562.600000)
test_model.HPCFeed2VF = Param(initialize = 0.084100)
#--------HPC---------
test_model.HPCTrays = RangeSet(1, 42)
test_model.HPCExt6MFlow = Param(initialize = 829.800000)
test_model.HPCExt22MFlow = Param(initialize = 47.290000)
test_model.HPCTopPressure = Param(initialize = 538.600000)
test_model.HPCBtmPressure = Param(initialize = 564.000000)
test_model.HPCUALeakage = Param(initialize = 10.000000)
test_model.HPCAmbientTemp = Param(initialize = 25.000000)
#--------HPCSump---------
test_model.HPCSumpLiqRho = Param(initialize = 1000.000000)
test_model.HPCSumpSumpCSArea = Param(initialize = 6.000000)
#--------HPCCond---------
test_model.HPCCondRefluxRatio = Param(initialize = 0.564650)

#===================================
#
#         Variables
#
#===================================
#--------HPCFeed1---------
test_model.HPCFeed1Temp = Var()
test_model.HPCFeed1LiqMFrac = Var(test_model.Component, bounds=(0, 1))
test_model.HPCFeed1VapMFrac = Var(test_model.Component, bounds=(0, 1))
#--------HPCFeed2---------
test_model.HPCFeed2Temp = Var()
test_model.HPCFeed2LiqMFrac = Var(test_model.Component, bounds=(0, 1))
test_model.HPCFeed2VapMFrac = Var(test_model.Component, bounds=(0, 1))
#--------HPC---------
test_model.HPCVapLvMFlow = Var(test_model.HPCTrays, within=NonNegativeReals)
test_model.HPCLiqLvMFlow = Var(test_model.HPCTrays, within=NonNegativeReals)
test_model.HPCTrayTemp = Var(test_model.HPCTrays)
test_model.HPCTrayPressure = Var(test_model.HPCTrays)
test_model.HPCLiqLvMFrac = Var(test_model.HPCTrays,test_model.Component, bounds=(0, 1))
test_model.HPCVapLvMFrac = Var(test_model.HPCTrays,test_model.Component, bounds=(0, 1))
#--------HPC's var in extractions---------
test_model.HPCExt6MFrac = Var(test_model.Component, bounds=(0,1))
test_model.HPCExt6MEtlp = Var()
test_model.HPCExt22MFrac = Var(test_model.Component, bounds=(0,1))
test_model.HPCExt22MEtlp = Var()
#--------HPCSump---------
test_model.HPCSumpOutMFlow = Var(within=NonNegativeReals)
test_model.HPCSumpHldpMFrac = Var(test_model.Component, bounds =(0,1))
#--------HPCCond---------
test_model.HPCCondRefMFlow = Var(within=NonNegativeReals)
test_model.HPCCondPrdtMFlow = Var(within=NonNegativeReals)
test_model.HPCCondMHeatOut = Var(within=NonNegativeReals)
test_model.HPCCondTemp = Var(initialize = 0)

#===================================
#
#         Expressions
#
#===================================
#--------HPCFeed1 Enthalpy---------
def HPCFeed1VapMEtlp(m):
	return triHPCThermo.HPCFeed1SelfCstmVapEtlp.VapEtlp(m.HPCFeed1Pressure, m.HPCFeed1Temp,m.HPCFeed1LiqMFrac["Nitrogen"])
test_model.HPCFeed1VapMEtlp = Expression(rule=HPCFeed1VapMEtlp)
def HPCFeed1LiqMEtlp(m):
	return triHPCThermo.HPCFeed1SelfCstmLiqEtlp.LiqEtlp(m.HPCFeed1Pressure, m.HPCFeed1Temp,m.HPCFeed1LiqMFrac["Nitrogen"])
test_model.HPCFeed1LiqMEtlp = Expression(rule=HPCFeed1LiqMEtlp)
def HPCFeed1MEtlp(m):
	return m.HPCFeed1LiqMEtlp * (1-m.HPCFeed1VF)+m.HPCFeed1VapMEtlp * m.HPCFeed1VF
test_model.HPCFeed1MEtlp = Expression(rule=HPCFeed1MEtlp)
#--------HPCFeed2 Enthalpy---------
def HPCFeed2VapMEtlp(m):
	return triHPCThermo.HPCFeed2SelfCstmVapEtlp.VapEtlp(m.HPCFeed2Pressure, m.HPCFeed2Temp,m.HPCFeed2LiqMFrac["Nitrogen"])
test_model.HPCFeed2VapMEtlp = Expression(rule=HPCFeed2VapMEtlp)
def HPCFeed2LiqMEtlp(m):
	return triHPCThermo.HPCFeed2SelfCstmLiqEtlp.LiqEtlp(m.HPCFeed2Pressure, m.HPCFeed2Temp,m.HPCFeed2LiqMFrac["Nitrogen"])
test_model.HPCFeed2LiqMEtlp = Expression(rule=HPCFeed2LiqMEtlp)
def HPCFeed2MEtlp(m):
	return m.HPCFeed2LiqMEtlp * (1-m.HPCFeed2VF)+m.HPCFeed2VapMEtlp * m.HPCFeed2VF
test_model.HPCFeed2MEtlp = Expression(rule=HPCFeed2MEtlp)
#--------HPC Component Flowrate---------
def HPCVapLvMCompFlow(m, tray, comp):
	return m.HPCVapLvMFrac[tray, comp] * m.HPCVapLvMFlow[tray]
test_model.HPCVapLvMCompFlow = Expression(test_model.HPCTrays, test_model.Component, rule=HPCVapLvMCompFlow)
def HPCLiqLvMCompFlow(m, tray, comp):
	return m.HPCLiqLvMFrac[tray, comp] * m.HPCLiqLvMFlow[tray]
test_model.HPCLiqLvMCompFlow = Expression(test_model.HPCTrays, test_model.Component, rule=HPCLiqLvMCompFlow)
#--------HPC Thermo and Enthalpy---------
def HPCVapLvMEtlp(m,tray):
	if tray==1:
		return triHPCThermo.HPCAllTrays1CstmVapEtlp.VapEtlp(m.HPCTrayPressure[tray], m.HPCTrayTemp[tray],m.HPCLiqLvMFrac[tray,"Nitrogen"])
	elif tray==2:
		return triHPCThermo.HPCAllTrays2CstmVapEtlp.VapEtlp(m.HPCTrayPressure[tray], m.HPCTrayTemp[tray],m.HPCLiqLvMFrac[tray,"Nitrogen"])
	elif tray==3:
		return triHPCThermo.HPCAllTrays3CstmVapEtlp.VapEtlp(m.HPCTrayPressure[tray], m.HPCTrayTemp[tray],m.HPCLiqLvMFrac[tray,"Nitrogen"])
	elif tray==4:
		return triHPCThermo.HPCAllTrays4CstmVapEtlp.VapEtlp(m.HPCTrayPressure[tray], m.HPCTrayTemp[tray],m.HPCLiqLvMFrac[tray,"Nitrogen"])
	elif tray==5:
		return triHPCThermo.HPCAllTrays5CstmVapEtlp.VapEtlp(m.HPCTrayPressure[tray], m.HPCTrayTemp[tray],m.HPCLiqLvMFrac[tray,"Nitrogen"])
	elif tray==6:
		return triHPCThermo.HPCAllTrays6CstmVapEtlp.VapEtlp(m.HPCTrayPressure[tray], m.HPCTrayTemp[tray],m.HPCLiqLvMFrac[tray,"Nitrogen"])
	elif tray==7:
		return triHPCThermo.HPCAllTrays7CstmVapEtlp.VapEtlp(m.HPCTrayPressure[tray], m.HPCTrayTemp[tray],m.HPCLiqLvMFrac[tray,"Nitrogen"])
	elif tray==8:
		return triHPCThermo.HPCAllTrays8CstmVapEtlp.VapEtlp(m.HPCTrayPressure[tray], m.HPCTrayTemp[tray],m.HPCLiqLvMFrac[tray,"Nitrogen"])
	elif tray==9:
		return triHPCThermo.HPCAllTrays9CstmVapEtlp.VapEtlp(m.HPCTrayPressure[tray], m.HPCTrayTemp[tray],m.HPCLiqLvMFrac[tray,"Nitrogen"])
	elif tray==10:
		return triHPCThermo.HPCAllTrays10CstmVapEtlp.VapEtlp(m.HPCTrayPressure[tray], m.HPCTrayTemp[tray],m.HPCLiqLvMFrac[tray,"Nitrogen"])
	elif tray==11:
		return triHPCThermo.HPCAllTrays11CstmVapEtlp.VapEtlp(m.HPCTrayPressure[tray], m.HPCTrayTemp[tray],m.HPCLiqLvMFrac[tray,"Nitrogen"])
	elif tray==12:
		return triHPCThermo.HPCAllTrays12CstmVapEtlp.VapEtlp(m.HPCTrayPressure[tray], m.HPCTrayTemp[tray],m.HPCLiqLvMFrac[tray,"Nitrogen"])
	elif tray==13:
		return triHPCThermo.HPCAllTrays13CstmVapEtlp.VapEtlp(m.HPCTrayPressure[tray], m.HPCTrayTemp[tray],m.HPCLiqLvMFrac[tray,"Nitrogen"])
	elif tray==14:
		return triHPCThermo.HPCAllTrays14CstmVapEtlp.VapEtlp(m.HPCTrayPressure[tray], m.HPCTrayTemp[tray],m.HPCLiqLvMFrac[tray,"Nitrogen"])
	elif tray==15:
		return triHPCThermo.HPCAllTrays15CstmVapEtlp.VapEtlp(m.HPCTrayPressure[tray], m.HPCTrayTemp[tray],m.HPCLiqLvMFrac[tray,"Nitrogen"])
	elif tray==16:
		return triHPCThermo.HPCAllTrays16CstmVapEtlp.VapEtlp(m.HPCTrayPressure[tray], m.HPCTrayTemp[tray],m.HPCLiqLvMFrac[tray,"Nitrogen"])
	elif tray==17:
		return triHPCThermo.HPCAllTrays17CstmVapEtlp.VapEtlp(m.HPCTrayPressure[tray], m.HPCTrayTemp[tray],m.HPCLiqLvMFrac[tray,"Nitrogen"])
	elif tray==18:
		return triHPCThermo.HPCAllTrays18CstmVapEtlp.VapEtlp(m.HPCTrayPressure[tray], m.HPCTrayTemp[tray],m.HPCLiqLvMFrac[tray,"Nitrogen"])
	elif tray==19:
		return triHPCThermo.HPCAllTrays19CstmVapEtlp.VapEtlp(m.HPCTrayPressure[tray], m.HPCTrayTemp[tray],m.HPCLiqLvMFrac[tray,"Nitrogen"])
	elif tray==20:
		return triHPCThermo.HPCAllTrays20CstmVapEtlp.VapEtlp(m.HPCTrayPressure[tray], m.HPCTrayTemp[tray],m.HPCLiqLvMFrac[tray,"Nitrogen"])
	elif tray==21:
		return triHPCThermo.HPCAllTrays21CstmVapEtlp.VapEtlp(m.HPCTrayPressure[tray], m.HPCTrayTemp[tray],m.HPCLiqLvMFrac[tray,"Nitrogen"])
	elif tray==22:
		return triHPCThermo.HPCAllTrays22CstmVapEtlp.VapEtlp(m.HPCTrayPressure[tray], m.HPCTrayTemp[tray],m.HPCLiqLvMFrac[tray,"Nitrogen"])
	elif tray==23:
		return triHPCThermo.HPCAllTrays23CstmVapEtlp.VapEtlp(m.HPCTrayPressure[tray], m.HPCTrayTemp[tray],m.HPCLiqLvMFrac[tray,"Nitrogen"])
	elif tray==24:
		return triHPCThermo.HPCAllTrays24CstmVapEtlp.VapEtlp(m.HPCTrayPressure[tray], m.HPCTrayTemp[tray],m.HPCLiqLvMFrac[tray,"Nitrogen"])
	elif tray==25:
		return triHPCThermo.HPCAllTrays25CstmVapEtlp.VapEtlp(m.HPCTrayPressure[tray], m.HPCTrayTemp[tray],m.HPCLiqLvMFrac[tray,"Nitrogen"])
	elif tray==26:
		return triHPCThermo.HPCAllTrays26CstmVapEtlp.VapEtlp(m.HPCTrayPressure[tray], m.HPCTrayTemp[tray],m.HPCLiqLvMFrac[tray,"Nitrogen"])
	elif tray==27:
		return triHPCThermo.HPCAllTrays27CstmVapEtlp.VapEtlp(m.HPCTrayPressure[tray], m.HPCTrayTemp[tray],m.HPCLiqLvMFrac[tray,"Nitrogen"])
	elif tray==28:
		return triHPCThermo.HPCAllTrays28CstmVapEtlp.VapEtlp(m.HPCTrayPressure[tray], m.HPCTrayTemp[tray],m.HPCLiqLvMFrac[tray,"Nitrogen"])
	elif tray==29:
		return triHPCThermo.HPCAllTrays29CstmVapEtlp.VapEtlp(m.HPCTrayPressure[tray], m.HPCTrayTemp[tray],m.HPCLiqLvMFrac[tray,"Nitrogen"])
	elif tray==30:
		return triHPCThermo.HPCAllTrays30CstmVapEtlp.VapEtlp(m.HPCTrayPressure[tray], m.HPCTrayTemp[tray],m.HPCLiqLvMFrac[tray,"Nitrogen"])
	elif tray==31:
		return triHPCThermo.HPCAllTrays31CstmVapEtlp.VapEtlp(m.HPCTrayPressure[tray], m.HPCTrayTemp[tray],m.HPCLiqLvMFrac[tray,"Nitrogen"])
	elif tray==32:
		return triHPCThermo.HPCAllTrays32CstmVapEtlp.VapEtlp(m.HPCTrayPressure[tray], m.HPCTrayTemp[tray],m.HPCLiqLvMFrac[tray,"Nitrogen"])
	elif tray==33:
		return triHPCThermo.HPCAllTrays33CstmVapEtlp.VapEtlp(m.HPCTrayPressure[tray], m.HPCTrayTemp[tray],m.HPCLiqLvMFrac[tray,"Nitrogen"])
	elif tray==34:
		return triHPCThermo.HPCAllTrays34CstmVapEtlp.VapEtlp(m.HPCTrayPressure[tray], m.HPCTrayTemp[tray],m.HPCLiqLvMFrac[tray,"Nitrogen"])
	elif tray==35:
		return triHPCThermo.HPCAllTrays35CstmVapEtlp.VapEtlp(m.HPCTrayPressure[tray], m.HPCTrayTemp[tray],m.HPCLiqLvMFrac[tray,"Nitrogen"])
	elif tray==36:
		return triHPCThermo.HPCAllTrays36CstmVapEtlp.VapEtlp(m.HPCTrayPressure[tray], m.HPCTrayTemp[tray],m.HPCLiqLvMFrac[tray,"Nitrogen"])
	elif tray==37:
		return triHPCThermo.HPCAllTrays37CstmVapEtlp.VapEtlp(m.HPCTrayPressure[tray], m.HPCTrayTemp[tray],m.HPCLiqLvMFrac[tray,"Nitrogen"])
	elif tray==38:
		return triHPCThermo.HPCAllTrays38CstmVapEtlp.VapEtlp(m.HPCTrayPressure[tray], m.HPCTrayTemp[tray],m.HPCLiqLvMFrac[tray,"Nitrogen"])
	elif tray==39:
		return triHPCThermo.HPCAllTrays39CstmVapEtlp.VapEtlp(m.HPCTrayPressure[tray], m.HPCTrayTemp[tray],m.HPCLiqLvMFrac[tray,"Nitrogen"])
	elif tray==40:
		return triHPCThermo.HPCAllTrays40CstmVapEtlp.VapEtlp(m.HPCTrayPressure[tray], m.HPCTrayTemp[tray],m.HPCLiqLvMFrac[tray,"Nitrogen"])
	elif tray==41:
		return triHPCThermo.HPCAllTrays41CstmVapEtlp.VapEtlp(m.HPCTrayPressure[tray], m.HPCTrayTemp[tray],m.HPCLiqLvMFrac[tray,"Nitrogen"])
	elif tray==42:
		return triHPCThermo.HPCAllTrays42CstmVapEtlp.VapEtlp(m.HPCTrayPressure[tray], m.HPCTrayTemp[tray],m.HPCLiqLvMFrac[tray,"Nitrogen"])
test_model.HPCVapLvMEtlp = Expression(test_model.HPCTrays,rule=HPCVapLvMEtlp)
def HPCLiqLvMEtlp(m,tray):
	if tray==1:
		return triHPCThermo.HPCAllTrays1CstmLiqEtlp.LiqEtlp(m.HPCTrayPressure[tray], m.HPCTrayTemp[tray],m.HPCLiqLvMFrac[tray,"Nitrogen"])
	elif tray==2:
		return triHPCThermo.HPCAllTrays2CstmLiqEtlp.LiqEtlp(m.HPCTrayPressure[tray], m.HPCTrayTemp[tray],m.HPCLiqLvMFrac[tray,"Nitrogen"])
	elif tray==3:
		return triHPCThermo.HPCAllTrays3CstmLiqEtlp.LiqEtlp(m.HPCTrayPressure[tray], m.HPCTrayTemp[tray],m.HPCLiqLvMFrac[tray,"Nitrogen"])
	elif tray==4:
		return triHPCThermo.HPCAllTrays4CstmLiqEtlp.LiqEtlp(m.HPCTrayPressure[tray], m.HPCTrayTemp[tray],m.HPCLiqLvMFrac[tray,"Nitrogen"])
	elif tray==5:
		return triHPCThermo.HPCAllTrays5CstmLiqEtlp.LiqEtlp(m.HPCTrayPressure[tray], m.HPCTrayTemp[tray],m.HPCLiqLvMFrac[tray,"Nitrogen"])
	elif tray==6:
		return triHPCThermo.HPCAllTrays6CstmLiqEtlp.LiqEtlp(m.HPCTrayPressure[tray], m.HPCTrayTemp[tray],m.HPCLiqLvMFrac[tray,"Nitrogen"])
	elif tray==7:
		return triHPCThermo.HPCAllTrays7CstmLiqEtlp.LiqEtlp(m.HPCTrayPressure[tray], m.HPCTrayTemp[tray],m.HPCLiqLvMFrac[tray,"Nitrogen"])
	elif tray==8:
		return triHPCThermo.HPCAllTrays8CstmLiqEtlp.LiqEtlp(m.HPCTrayPressure[tray], m.HPCTrayTemp[tray],m.HPCLiqLvMFrac[tray,"Nitrogen"])
	elif tray==9:
		return triHPCThermo.HPCAllTrays9CstmLiqEtlp.LiqEtlp(m.HPCTrayPressure[tray], m.HPCTrayTemp[tray],m.HPCLiqLvMFrac[tray,"Nitrogen"])
	elif tray==10:
		return triHPCThermo.HPCAllTrays10CstmLiqEtlp.LiqEtlp(m.HPCTrayPressure[tray], m.HPCTrayTemp[tray],m.HPCLiqLvMFrac[tray,"Nitrogen"])
	elif tray==11:
		return triHPCThermo.HPCAllTrays11CstmLiqEtlp.LiqEtlp(m.HPCTrayPressure[tray], m.HPCTrayTemp[tray],m.HPCLiqLvMFrac[tray,"Nitrogen"])
	elif tray==12:
		return triHPCThermo.HPCAllTrays12CstmLiqEtlp.LiqEtlp(m.HPCTrayPressure[tray], m.HPCTrayTemp[tray],m.HPCLiqLvMFrac[tray,"Nitrogen"])
	elif tray==13:
		return triHPCThermo.HPCAllTrays13CstmLiqEtlp.LiqEtlp(m.HPCTrayPressure[tray], m.HPCTrayTemp[tray],m.HPCLiqLvMFrac[tray,"Nitrogen"])
	elif tray==14:
		return triHPCThermo.HPCAllTrays14CstmLiqEtlp.LiqEtlp(m.HPCTrayPressure[tray], m.HPCTrayTemp[tray],m.HPCLiqLvMFrac[tray,"Nitrogen"])
	elif tray==15:
		return triHPCThermo.HPCAllTrays15CstmLiqEtlp.LiqEtlp(m.HPCTrayPressure[tray], m.HPCTrayTemp[tray],m.HPCLiqLvMFrac[tray,"Nitrogen"])
	elif tray==16:
		return triHPCThermo.HPCAllTrays16CstmLiqEtlp.LiqEtlp(m.HPCTrayPressure[tray], m.HPCTrayTemp[tray],m.HPCLiqLvMFrac[tray,"Nitrogen"])
	elif tray==17:
		return triHPCThermo.HPCAllTrays17CstmLiqEtlp.LiqEtlp(m.HPCTrayPressure[tray], m.HPCTrayTemp[tray],m.HPCLiqLvMFrac[tray,"Nitrogen"])
	elif tray==18:
		return triHPCThermo.HPCAllTrays18CstmLiqEtlp.LiqEtlp(m.HPCTrayPressure[tray], m.HPCTrayTemp[tray],m.HPCLiqLvMFrac[tray,"Nitrogen"])
	elif tray==19:
		return triHPCThermo.HPCAllTrays19CstmLiqEtlp.LiqEtlp(m.HPCTrayPressure[tray], m.HPCTrayTemp[tray],m.HPCLiqLvMFrac[tray,"Nitrogen"])
	elif tray==20:
		return triHPCThermo.HPCAllTrays20CstmLiqEtlp.LiqEtlp(m.HPCTrayPressure[tray], m.HPCTrayTemp[tray],m.HPCLiqLvMFrac[tray,"Nitrogen"])
	elif tray==21:
		return triHPCThermo.HPCAllTrays21CstmLiqEtlp.LiqEtlp(m.HPCTrayPressure[tray], m.HPCTrayTemp[tray],m.HPCLiqLvMFrac[tray,"Nitrogen"])
	elif tray==22:
		return triHPCThermo.HPCAllTrays22CstmLiqEtlp.LiqEtlp(m.HPCTrayPressure[tray], m.HPCTrayTemp[tray],m.HPCLiqLvMFrac[tray,"Nitrogen"])
	elif tray==23:
		return triHPCThermo.HPCAllTrays23CstmLiqEtlp.LiqEtlp(m.HPCTrayPressure[tray], m.HPCTrayTemp[tray],m.HPCLiqLvMFrac[tray,"Nitrogen"])
	elif tray==24:
		return triHPCThermo.HPCAllTrays24CstmLiqEtlp.LiqEtlp(m.HPCTrayPressure[tray], m.HPCTrayTemp[tray],m.HPCLiqLvMFrac[tray,"Nitrogen"])
	elif tray==25:
		return triHPCThermo.HPCAllTrays25CstmLiqEtlp.LiqEtlp(m.HPCTrayPressure[tray], m.HPCTrayTemp[tray],m.HPCLiqLvMFrac[tray,"Nitrogen"])
	elif tray==26:
		return triHPCThermo.HPCAllTrays26CstmLiqEtlp.LiqEtlp(m.HPCTrayPressure[tray], m.HPCTrayTemp[tray],m.HPCLiqLvMFrac[tray,"Nitrogen"])
	elif tray==27:
		return triHPCThermo.HPCAllTrays27CstmLiqEtlp.LiqEtlp(m.HPCTrayPressure[tray], m.HPCTrayTemp[tray],m.HPCLiqLvMFrac[tray,"Nitrogen"])
	elif tray==28:
		return triHPCThermo.HPCAllTrays28CstmLiqEtlp.LiqEtlp(m.HPCTrayPressure[tray], m.HPCTrayTemp[tray],m.HPCLiqLvMFrac[tray,"Nitrogen"])
	elif tray==29:
		return triHPCThermo.HPCAllTrays29CstmLiqEtlp.LiqEtlp(m.HPCTrayPressure[tray], m.HPCTrayTemp[tray],m.HPCLiqLvMFrac[tray,"Nitrogen"])
	elif tray==30:
		return triHPCThermo.HPCAllTrays30CstmLiqEtlp.LiqEtlp(m.HPCTrayPressure[tray], m.HPCTrayTemp[tray],m.HPCLiqLvMFrac[tray,"Nitrogen"])
	elif tray==31:
		return triHPCThermo.HPCAllTrays31CstmLiqEtlp.LiqEtlp(m.HPCTrayPressure[tray], m.HPCTrayTemp[tray],m.HPCLiqLvMFrac[tray,"Nitrogen"])
	elif tray==32:
		return triHPCThermo.HPCAllTrays32CstmLiqEtlp.LiqEtlp(m.HPCTrayPressure[tray], m.HPCTrayTemp[tray],m.HPCLiqLvMFrac[tray,"Nitrogen"])
	elif tray==33:
		return triHPCThermo.HPCAllTrays33CstmLiqEtlp.LiqEtlp(m.HPCTrayPressure[tray], m.HPCTrayTemp[tray],m.HPCLiqLvMFrac[tray,"Nitrogen"])
	elif tray==34:
		return triHPCThermo.HPCAllTrays34CstmLiqEtlp.LiqEtlp(m.HPCTrayPressure[tray], m.HPCTrayTemp[tray],m.HPCLiqLvMFrac[tray,"Nitrogen"])
	elif tray==35:
		return triHPCThermo.HPCAllTrays35CstmLiqEtlp.LiqEtlp(m.HPCTrayPressure[tray], m.HPCTrayTemp[tray],m.HPCLiqLvMFrac[tray,"Nitrogen"])
	elif tray==36:
		return triHPCThermo.HPCAllTrays36CstmLiqEtlp.LiqEtlp(m.HPCTrayPressure[tray], m.HPCTrayTemp[tray],m.HPCLiqLvMFrac[tray,"Nitrogen"])
	elif tray==37:
		return triHPCThermo.HPCAllTrays37CstmLiqEtlp.LiqEtlp(m.HPCTrayPressure[tray], m.HPCTrayTemp[tray],m.HPCLiqLvMFrac[tray,"Nitrogen"])
	elif tray==38:
		return triHPCThermo.HPCAllTrays38CstmLiqEtlp.LiqEtlp(m.HPCTrayPressure[tray], m.HPCTrayTemp[tray],m.HPCLiqLvMFrac[tray,"Nitrogen"])
	elif tray==39:
		return triHPCThermo.HPCAllTrays39CstmLiqEtlp.LiqEtlp(m.HPCTrayPressure[tray], m.HPCTrayTemp[tray],m.HPCLiqLvMFrac[tray,"Nitrogen"])
	elif tray==40:
		return triHPCThermo.HPCAllTrays40CstmLiqEtlp.LiqEtlp(m.HPCTrayPressure[tray], m.HPCTrayTemp[tray],m.HPCLiqLvMFrac[tray,"Nitrogen"])
	elif tray==41:
		return triHPCThermo.HPCAllTrays41CstmLiqEtlp.LiqEtlp(m.HPCTrayPressure[tray], m.HPCTrayTemp[tray],m.HPCLiqLvMFrac[tray,"Nitrogen"])
	elif tray==42:
		return triHPCThermo.HPCAllTrays42CstmLiqEtlp.LiqEtlp(m.HPCTrayPressure[tray], m.HPCTrayTemp[tray],m.HPCLiqLvMFrac[tray,"Nitrogen"])
test_model.HPCLiqLvMEtlp = Expression(test_model.HPCTrays,rule=HPCLiqLvMEtlp)
#--------HPCCond Enthalpy---------
def HPCCondOutMEtlp(m):
	return triHPCThermo.HPCCondOutletCstmLiqEtlp.LiqEtlp(m.HPCTrayPressure[42], m.HPCCondTemp,m.HPCVapLvMFrac[42,"Nitrogen"])
test_model.HPCCondOutMEtlp = Expression(rule=HPCCondOutMEtlp)

#===================================
#
#         Constraints
#
#===================================

#----------------------------------
#           HPCFeed1
#----------------------------------
#--------HPCFeed1 Mass Balance---------
def HPCFeed1MassBlnc0(m):
	return m.HPCFeed1VF * m.HPCFeed1VapMFrac['Nitrogen'] + \
(1 - m.HPCFeed1VF)*m.HPCFeed1LiqMFrac['Nitrogen'] - m.HPCFeed1MFrac['Nitrogen'] == 0
test_model.HPCFeed1MassBlnc0 = Constraint(rule=HPCFeed1MassBlnc0)
def HPCFeed1MassBlnc1(m):
	return m.HPCFeed1VF * m.HPCFeed1VapMFrac['Oxygen'] + \
(1 - m.HPCFeed1VF)*m.HPCFeed1LiqMFrac['Oxygen'] - m.HPCFeed1MFrac['Oxygen'] == 0
test_model.HPCFeed1MassBlnc1 = Constraint(rule=HPCFeed1MassBlnc1)
#--------HPCFeed1 Phase Equilibrium---------
def HPCFeed1SelfLiqO2Frac(m):
	return m.HPCFeed1LiqMFrac["Oxygen"] == triHPCThermo.HPCFeed1SelfCstmLiqO2.LiqO2(m.HPCFeed1Pressure,m.HPCFeed1Temp,m.HPCFeed1LiqMFrac["Nitrogen"])
test_model.HPCFeed1SelfLiqO2Frac = Constraint(rule=HPCFeed1SelfLiqO2Frac)
def HPCFeed1SelfVapO2Frac(m):
	return m.HPCFeed1VapMFrac["Oxygen"] == triHPCThermo.HPCFeed1SelfCstmVapO2.VapO2(m.HPCFeed1Pressure,m.HPCFeed1Temp,m.HPCFeed1LiqMFrac["Nitrogen"])
test_model.HPCFeed1SelfVapO2Frac = Constraint(rule=HPCFeed1SelfVapO2Frac)
def HPCFeed1SelfVapN2Frac(m):
	return m.HPCFeed1VapMFrac["Nitrogen"] == triHPCThermo.HPCFeed1SelfCstmVapN2.VapN2(m.HPCFeed1Pressure,m.HPCFeed1Temp,m.HPCFeed1LiqMFrac["Nitrogen"])
test_model.HPCFeed1SelfVapN2Frac = Constraint(rule=HPCFeed1SelfVapN2Frac)
#--------HPCFeed1 Summation---------
def HPCFeed1LiqSum(m):
	return sum([m.HPCFeed1LiqMFrac[c] for c in m.Component]) == 1
test_model.HPCFeed1LiqSum = Constraint(rule=HPCFeed1LiqSum)
def HPCFeed1VapSum(m):
	return sum([m.HPCFeed1VapMFrac[c] for c in m.Component]) == 1
test_model.HPCFeed1VapSum = Constraint(rule=HPCFeed1VapSum)

#----------------------------------
#           HPCFeed2
#----------------------------------
#--------HPCFeed2 Mass Balance---------
def HPCFeed2MassBlnc0(m):
	return m.HPCFeed2VF * m.HPCFeed2VapMFrac['Nitrogen'] + \
(1 - m.HPCFeed2VF)*m.HPCFeed2LiqMFrac['Nitrogen'] - m.HPCFeed2MFrac['Nitrogen'] == 0
test_model.HPCFeed2MassBlnc0 = Constraint(rule=HPCFeed2MassBlnc0)
def HPCFeed2MassBlnc1(m):
	return m.HPCFeed2VF * m.HPCFeed2VapMFrac['Oxygen'] + \
(1 - m.HPCFeed2VF)*m.HPCFeed2LiqMFrac['Oxygen'] - m.HPCFeed2MFrac['Oxygen'] == 0
test_model.HPCFeed2MassBlnc1 = Constraint(rule=HPCFeed2MassBlnc1)
#--------HPCFeed2 Phase Equilibrium---------
def HPCFeed2SelfLiqO2Frac(m):
	return m.HPCFeed2LiqMFrac["Oxygen"] == triHPCThermo.HPCFeed2SelfCstmLiqO2.LiqO2(m.HPCFeed2Pressure,m.HPCFeed2Temp,m.HPCFeed2LiqMFrac["Nitrogen"])
test_model.HPCFeed2SelfLiqO2Frac = Constraint(rule=HPCFeed2SelfLiqO2Frac)
def HPCFeed2SelfVapO2Frac(m):
	return m.HPCFeed2VapMFrac["Oxygen"] == triHPCThermo.HPCFeed2SelfCstmVapO2.VapO2(m.HPCFeed2Pressure,m.HPCFeed2Temp,m.HPCFeed2LiqMFrac["Nitrogen"])
test_model.HPCFeed2SelfVapO2Frac = Constraint(rule=HPCFeed2SelfVapO2Frac)
def HPCFeed2SelfVapN2Frac(m):
	return m.HPCFeed2VapMFrac["Nitrogen"] == triHPCThermo.HPCFeed2SelfCstmVapN2.VapN2(m.HPCFeed2Pressure,m.HPCFeed2Temp,m.HPCFeed2LiqMFrac["Nitrogen"])
test_model.HPCFeed2SelfVapN2Frac = Constraint(rule=HPCFeed2SelfVapN2Frac)
#--------HPCFeed2 Summation---------
def HPCFeed2LiqSum(m):
	return sum([m.HPCFeed2LiqMFrac[c] for c in m.Component]) == 1
test_model.HPCFeed2LiqSum = Constraint(rule=HPCFeed2LiqSum)
def HPCFeed2VapSum(m):
	return sum([m.HPCFeed2VapMFrac[c] for c in m.Component]) == 1
test_model.HPCFeed2VapSum = Constraint(rule=HPCFeed2VapSum)

#----------------------------------
#           HPC
#----------------------------------
#--------HPC Mass Balance---------
def HPCMassBlnc(m,tray, comp):
	if tray == 1:
		return (m.HPCLiqLvMCompFlow[tray + 1, comp]- m.HPCLiqLvMCompFlow[tray, comp] - m.HPCVapLvMCompFlow[tray, comp]+m.HPCFeed1MFlow*m.HPCFeed1MFrac[comp])*0.001000 == 0
	elif tray == 4:
		return (m.HPCLiqLvMCompFlow[tray + 1, comp] + m.HPCVapLvMCompFlow[tray - 1, comp] - m.HPCLiqLvMCompFlow[tray, comp] - m.HPCVapLvMCompFlow[tray, comp]+m.HPCFeed2MFlow*m.HPCFeed2MFrac[comp])*0.001000 == 0
	elif tray == 6:
		return (m.HPCLiqLvMCompFlow[tray + 1, comp] + m.HPCVapLvMCompFlow[tray - 1, comp] - m.HPCLiqLvMCompFlow[tray, comp] - m.HPCVapLvMCompFlow[tray, comp]-m.HPCExt6MFlow*m.HPCExt6MFrac[comp])*0.001000 == 0
	elif tray == 22:
		return (m.HPCLiqLvMCompFlow[tray + 1, comp] + m.HPCVapLvMCompFlow[tray - 1, comp] - m.HPCLiqLvMCompFlow[tray, comp] - m.HPCVapLvMCompFlow[tray, comp]-m.HPCExt22MFlow*m.HPCExt22MFrac[comp])*0.001000 == 0
	elif tray == 42:
		return (m.HPCCondRefMFlow*m.HPCVapLvMFrac[42,comp] + m.HPCVapLvMCompFlow[tray - 1, comp] - m.HPCLiqLvMCompFlow[tray, comp] - m.HPCVapLvMCompFlow[tray, comp])*0.001000 == 0
	else:
		return (m.HPCLiqLvMCompFlow[tray + 1, comp] + m.HPCVapLvMCompFlow[tray - 1, comp] - m.HPCLiqLvMCompFlow[tray, comp] - m.HPCVapLvMCompFlow[tray, comp])*0.001000 == 0
test_model.HPCMassBlnc = Constraint(test_model.HPCTrays, test_model.Component, rule=HPCMassBlnc)
#--------HPC Energy Balance---------
def HPCEngBlnc(m,tray):
	if tray == 1:
		return (m.HPCLiqLvMFlow[tray + 1] * m.HPCLiqLvMEtlp[tray+1] \
		        - m.HPCLiqLvMFlow[tray] * m.HPCLiqLvMEtlp[tray] \
		        - m.HPCVapLvMFlow[tray] * m.HPCVapLvMEtlp[tray]\
		        +m.HPCFeed1MFlow*m.HPCFeed1MEtlp-m.HPCUALeakage*(m.HPCAmbientTemp-m.HPCTrayTemp[tray]))*0.000010 == 0
	elif tray == 4:
		return (m.HPCLiqLvMFlow[tray + 1] * m.HPCLiqLvMEtlp[tray+1] \
		        + m.HPCVapLvMFlow[tray-1] * m.HPCVapLvMEtlp[tray-1] \
		        - m.HPCLiqLvMFlow[tray] * m.HPCLiqLvMEtlp[tray] \
		        - m.HPCVapLvMFlow[tray] * m.HPCVapLvMEtlp[tray]\
		        +m.HPCFeed2MFlow*m.HPCFeed2MEtlp-m.HPCUALeakage*(m.HPCAmbientTemp-m.HPCTrayTemp[tray]))*0.000010 == 0
	elif tray == 6:
		return (m.HPCLiqLvMFlow[tray + 1] * m.HPCLiqLvMEtlp[tray+1] \
		        + m.HPCVapLvMFlow[tray-1] * m.HPCVapLvMEtlp[tray-1] \
		        - m.HPCLiqLvMFlow[tray] * m.HPCLiqLvMEtlp[tray] \
		        - m.HPCVapLvMFlow[tray] * m.HPCVapLvMEtlp[tray]\
		        -m.HPCExt6MFlow*m.HPCExt6MEtlp-m.HPCUALeakage*(m.HPCAmbientTemp-m.HPCTrayTemp[tray]))*0.000010 == 0
	elif tray == 22:
		return (m.HPCLiqLvMFlow[tray + 1] * m.HPCLiqLvMEtlp[tray+1] \
		        + m.HPCVapLvMFlow[tray-1] * m.HPCVapLvMEtlp[tray-1] \
		        - m.HPCLiqLvMFlow[tray] * m.HPCLiqLvMEtlp[tray] \
		        - m.HPCVapLvMFlow[tray] * m.HPCVapLvMEtlp[tray]\
		        -m.HPCExt22MFlow*m.HPCExt22MEtlp-m.HPCUALeakage*(m.HPCAmbientTemp-m.HPCTrayTemp[tray]))*0.000010 == 0
	elif tray == 42:
		return (m.HPCCondRefMFlow * m.HPCCondOutMEtlp \
		        + m.HPCVapLvMFlow[tray-1] * m.HPCVapLvMEtlp[tray-1] \
		        - m.HPCLiqLvMFlow[tray] * m.HPCLiqLvMEtlp[tray] \
		        - m.HPCVapLvMFlow[tray] * m.HPCVapLvMEtlp[tray]-m.HPCUALeakage*(m.HPCAmbientTemp-m.HPCTrayTemp[tray]))*0.000010 == 0
	else:
		return (m.HPCLiqLvMFlow[tray + 1] * m.HPCLiqLvMEtlp[tray+1] \
		        + m.HPCVapLvMFlow[tray-1] * m.HPCVapLvMEtlp[tray-1] \
		        - m.HPCLiqLvMFlow[tray] * m.HPCLiqLvMEtlp[tray] \
		        - m.HPCVapLvMFlow[tray] * m.HPCVapLvMEtlp[tray]-m.HPCUALeakage*(m.HPCAmbientTemp-m.HPCTrayTemp[tray]))*0.000010 == 0
test_model.HPCEngBlnc = Constraint(test_model.HPCTrays,rule=HPCEngBlnc)
#--------HPC Phase Equilibrium & System Parts---------
def HPCAllTraysLiqO2Frac(m,tray):
	if tray==1:
		return m.HPCLiqLvMFrac[tray,"Oxygen"] == triHPCThermo.HPCAllTrays1CstmLiqO2.LiqO2(m.HPCTrayPressure[tray],m.HPCTrayTemp[tray],m.HPCLiqLvMFrac[tray,"Nitrogen"])
	elif tray==2:
		return m.HPCLiqLvMFrac[tray,"Oxygen"] == triHPCThermo.HPCAllTrays2CstmLiqO2.LiqO2(m.HPCTrayPressure[tray],m.HPCTrayTemp[tray],m.HPCLiqLvMFrac[tray,"Nitrogen"])
	elif tray==3:
		return m.HPCLiqLvMFrac[tray,"Oxygen"] == triHPCThermo.HPCAllTrays3CstmLiqO2.LiqO2(m.HPCTrayPressure[tray],m.HPCTrayTemp[tray],m.HPCLiqLvMFrac[tray,"Nitrogen"])
	elif tray==4:
		return m.HPCLiqLvMFrac[tray,"Oxygen"] == triHPCThermo.HPCAllTrays4CstmLiqO2.LiqO2(m.HPCTrayPressure[tray],m.HPCTrayTemp[tray],m.HPCLiqLvMFrac[tray,"Nitrogen"])
	elif tray==5:
		return m.HPCLiqLvMFrac[tray,"Oxygen"] == triHPCThermo.HPCAllTrays5CstmLiqO2.LiqO2(m.HPCTrayPressure[tray],m.HPCTrayTemp[tray],m.HPCLiqLvMFrac[tray,"Nitrogen"])
	elif tray==6:
		return m.HPCLiqLvMFrac[tray,"Oxygen"] == triHPCThermo.HPCAllTrays6CstmLiqO2.LiqO2(m.HPCTrayPressure[tray],m.HPCTrayTemp[tray],m.HPCLiqLvMFrac[tray,"Nitrogen"])
	elif tray==7:
		return m.HPCLiqLvMFrac[tray,"Oxygen"] == triHPCThermo.HPCAllTrays7CstmLiqO2.LiqO2(m.HPCTrayPressure[tray],m.HPCTrayTemp[tray],m.HPCLiqLvMFrac[tray,"Nitrogen"])
	elif tray==8:
		return m.HPCLiqLvMFrac[tray,"Oxygen"] == triHPCThermo.HPCAllTrays8CstmLiqO2.LiqO2(m.HPCTrayPressure[tray],m.HPCTrayTemp[tray],m.HPCLiqLvMFrac[tray,"Nitrogen"])
	elif tray==9:
		return m.HPCLiqLvMFrac[tray,"Oxygen"] == triHPCThermo.HPCAllTrays9CstmLiqO2.LiqO2(m.HPCTrayPressure[tray],m.HPCTrayTemp[tray],m.HPCLiqLvMFrac[tray,"Nitrogen"])
	elif tray==10:
		return m.HPCLiqLvMFrac[tray,"Oxygen"] == triHPCThermo.HPCAllTrays10CstmLiqO2.LiqO2(m.HPCTrayPressure[tray],m.HPCTrayTemp[tray],m.HPCLiqLvMFrac[tray,"Nitrogen"])
	elif tray==11:
		return m.HPCLiqLvMFrac[tray,"Oxygen"] == triHPCThermo.HPCAllTrays11CstmLiqO2.LiqO2(m.HPCTrayPressure[tray],m.HPCTrayTemp[tray],m.HPCLiqLvMFrac[tray,"Nitrogen"])
	elif tray==12:
		return m.HPCLiqLvMFrac[tray,"Oxygen"] == triHPCThermo.HPCAllTrays12CstmLiqO2.LiqO2(m.HPCTrayPressure[tray],m.HPCTrayTemp[tray],m.HPCLiqLvMFrac[tray,"Nitrogen"])
	elif tray==13:
		return m.HPCLiqLvMFrac[tray,"Oxygen"] == triHPCThermo.HPCAllTrays13CstmLiqO2.LiqO2(m.HPCTrayPressure[tray],m.HPCTrayTemp[tray],m.HPCLiqLvMFrac[tray,"Nitrogen"])
	elif tray==14:
		return m.HPCLiqLvMFrac[tray,"Oxygen"] == triHPCThermo.HPCAllTrays14CstmLiqO2.LiqO2(m.HPCTrayPressure[tray],m.HPCTrayTemp[tray],m.HPCLiqLvMFrac[tray,"Nitrogen"])
	elif tray==15:
		return m.HPCLiqLvMFrac[tray,"Oxygen"] == triHPCThermo.HPCAllTrays15CstmLiqO2.LiqO2(m.HPCTrayPressure[tray],m.HPCTrayTemp[tray],m.HPCLiqLvMFrac[tray,"Nitrogen"])
	elif tray==16:
		return m.HPCLiqLvMFrac[tray,"Oxygen"] == triHPCThermo.HPCAllTrays16CstmLiqO2.LiqO2(m.HPCTrayPressure[tray],m.HPCTrayTemp[tray],m.HPCLiqLvMFrac[tray,"Nitrogen"])
	elif tray==17:
		return m.HPCLiqLvMFrac[tray,"Oxygen"] == triHPCThermo.HPCAllTrays17CstmLiqO2.LiqO2(m.HPCTrayPressure[tray],m.HPCTrayTemp[tray],m.HPCLiqLvMFrac[tray,"Nitrogen"])
	elif tray==18:
		return m.HPCLiqLvMFrac[tray,"Oxygen"] == triHPCThermo.HPCAllTrays18CstmLiqO2.LiqO2(m.HPCTrayPressure[tray],m.HPCTrayTemp[tray],m.HPCLiqLvMFrac[tray,"Nitrogen"])
	elif tray==19:
		return m.HPCLiqLvMFrac[tray,"Oxygen"] == triHPCThermo.HPCAllTrays19CstmLiqO2.LiqO2(m.HPCTrayPressure[tray],m.HPCTrayTemp[tray],m.HPCLiqLvMFrac[tray,"Nitrogen"])
	elif tray==20:
		return m.HPCLiqLvMFrac[tray,"Oxygen"] == triHPCThermo.HPCAllTrays20CstmLiqO2.LiqO2(m.HPCTrayPressure[tray],m.HPCTrayTemp[tray],m.HPCLiqLvMFrac[tray,"Nitrogen"])
	elif tray==21:
		return m.HPCLiqLvMFrac[tray,"Oxygen"] == triHPCThermo.HPCAllTrays21CstmLiqO2.LiqO2(m.HPCTrayPressure[tray],m.HPCTrayTemp[tray],m.HPCLiqLvMFrac[tray,"Nitrogen"])
	elif tray==22:
		return m.HPCLiqLvMFrac[tray,"Oxygen"] == triHPCThermo.HPCAllTrays22CstmLiqO2.LiqO2(m.HPCTrayPressure[tray],m.HPCTrayTemp[tray],m.HPCLiqLvMFrac[tray,"Nitrogen"])
	elif tray==23:
		return m.HPCLiqLvMFrac[tray,"Oxygen"] == triHPCThermo.HPCAllTrays23CstmLiqO2.LiqO2(m.HPCTrayPressure[tray],m.HPCTrayTemp[tray],m.HPCLiqLvMFrac[tray,"Nitrogen"])
	elif tray==24:
		return m.HPCLiqLvMFrac[tray,"Oxygen"] == triHPCThermo.HPCAllTrays24CstmLiqO2.LiqO2(m.HPCTrayPressure[tray],m.HPCTrayTemp[tray],m.HPCLiqLvMFrac[tray,"Nitrogen"])
	elif tray==25:
		return m.HPCLiqLvMFrac[tray,"Oxygen"] == triHPCThermo.HPCAllTrays25CstmLiqO2.LiqO2(m.HPCTrayPressure[tray],m.HPCTrayTemp[tray],m.HPCLiqLvMFrac[tray,"Nitrogen"])
	elif tray==26:
		return m.HPCLiqLvMFrac[tray,"Oxygen"] == triHPCThermo.HPCAllTrays26CstmLiqO2.LiqO2(m.HPCTrayPressure[tray],m.HPCTrayTemp[tray],m.HPCLiqLvMFrac[tray,"Nitrogen"])
	elif tray==27:
		return m.HPCLiqLvMFrac[tray,"Oxygen"] == triHPCThermo.HPCAllTrays27CstmLiqO2.LiqO2(m.HPCTrayPressure[tray],m.HPCTrayTemp[tray],m.HPCLiqLvMFrac[tray,"Nitrogen"])
	elif tray==28:
		return m.HPCLiqLvMFrac[tray,"Oxygen"] == triHPCThermo.HPCAllTrays28CstmLiqO2.LiqO2(m.HPCTrayPressure[tray],m.HPCTrayTemp[tray],m.HPCLiqLvMFrac[tray,"Nitrogen"])
	elif tray==29:
		return m.HPCLiqLvMFrac[tray,"Oxygen"] == triHPCThermo.HPCAllTrays29CstmLiqO2.LiqO2(m.HPCTrayPressure[tray],m.HPCTrayTemp[tray],m.HPCLiqLvMFrac[tray,"Nitrogen"])
	elif tray==30:
		return m.HPCLiqLvMFrac[tray,"Oxygen"] == triHPCThermo.HPCAllTrays30CstmLiqO2.LiqO2(m.HPCTrayPressure[tray],m.HPCTrayTemp[tray],m.HPCLiqLvMFrac[tray,"Nitrogen"])
	elif tray==31:
		return m.HPCLiqLvMFrac[tray,"Oxygen"] == triHPCThermo.HPCAllTrays31CstmLiqO2.LiqO2(m.HPCTrayPressure[tray],m.HPCTrayTemp[tray],m.HPCLiqLvMFrac[tray,"Nitrogen"])
	elif tray==32:
		return m.HPCLiqLvMFrac[tray,"Oxygen"] == triHPCThermo.HPCAllTrays32CstmLiqO2.LiqO2(m.HPCTrayPressure[tray],m.HPCTrayTemp[tray],m.HPCLiqLvMFrac[tray,"Nitrogen"])
	elif tray==33:
		return m.HPCLiqLvMFrac[tray,"Oxygen"] == triHPCThermo.HPCAllTrays33CstmLiqO2.LiqO2(m.HPCTrayPressure[tray],m.HPCTrayTemp[tray],m.HPCLiqLvMFrac[tray,"Nitrogen"])
	elif tray==34:
		return m.HPCLiqLvMFrac[tray,"Oxygen"] == triHPCThermo.HPCAllTrays34CstmLiqO2.LiqO2(m.HPCTrayPressure[tray],m.HPCTrayTemp[tray],m.HPCLiqLvMFrac[tray,"Nitrogen"])
	elif tray==35:
		return m.HPCLiqLvMFrac[tray,"Oxygen"] == triHPCThermo.HPCAllTrays35CstmLiqO2.LiqO2(m.HPCTrayPressure[tray],m.HPCTrayTemp[tray],m.HPCLiqLvMFrac[tray,"Nitrogen"])
	elif tray==36:
		return m.HPCLiqLvMFrac[tray,"Oxygen"] == triHPCThermo.HPCAllTrays36CstmLiqO2.LiqO2(m.HPCTrayPressure[tray],m.HPCTrayTemp[tray],m.HPCLiqLvMFrac[tray,"Nitrogen"])
	elif tray==37:
		return m.HPCLiqLvMFrac[tray,"Oxygen"] == triHPCThermo.HPCAllTrays37CstmLiqO2.LiqO2(m.HPCTrayPressure[tray],m.HPCTrayTemp[tray],m.HPCLiqLvMFrac[tray,"Nitrogen"])
	elif tray==38:
		return m.HPCLiqLvMFrac[tray,"Oxygen"] == triHPCThermo.HPCAllTrays38CstmLiqO2.LiqO2(m.HPCTrayPressure[tray],m.HPCTrayTemp[tray],m.HPCLiqLvMFrac[tray,"Nitrogen"])
	elif tray==39:
		return m.HPCLiqLvMFrac[tray,"Oxygen"] == triHPCThermo.HPCAllTrays39CstmLiqO2.LiqO2(m.HPCTrayPressure[tray],m.HPCTrayTemp[tray],m.HPCLiqLvMFrac[tray,"Nitrogen"])
	elif tray==40:
		return m.HPCLiqLvMFrac[tray,"Oxygen"] == triHPCThermo.HPCAllTrays40CstmLiqO2.LiqO2(m.HPCTrayPressure[tray],m.HPCTrayTemp[tray],m.HPCLiqLvMFrac[tray,"Nitrogen"])
	elif tray==41:
		return m.HPCLiqLvMFrac[tray,"Oxygen"] == triHPCThermo.HPCAllTrays41CstmLiqO2.LiqO2(m.HPCTrayPressure[tray],m.HPCTrayTemp[tray],m.HPCLiqLvMFrac[tray,"Nitrogen"])
	elif tray==42:
		return m.HPCLiqLvMFrac[tray,"Oxygen"] == triHPCThermo.HPCAllTrays42CstmLiqO2.LiqO2(m.HPCTrayPressure[tray],m.HPCTrayTemp[tray],m.HPCLiqLvMFrac[tray,"Nitrogen"])
test_model.HPCAllTraysLiqO2Frac = Constraint(test_model.HPCTrays,rule=HPCAllTraysLiqO2Frac)
def HPCAllTraysVapO2Frac(m,tray):
	if tray==1:
		return m.HPCVapLvMFrac[tray,"Oxygen"] == triHPCThermo.HPCAllTrays1CstmVapO2.VapO2(m.HPCTrayPressure[tray],m.HPCTrayTemp[tray],m.HPCLiqLvMFrac[tray,"Nitrogen"])
	elif tray==2:
		return m.HPCVapLvMFrac[tray,"Oxygen"] == triHPCThermo.HPCAllTrays2CstmVapO2.VapO2(m.HPCTrayPressure[tray],m.HPCTrayTemp[tray],m.HPCLiqLvMFrac[tray,"Nitrogen"])
	elif tray==3:
		return m.HPCVapLvMFrac[tray,"Oxygen"] == triHPCThermo.HPCAllTrays3CstmVapO2.VapO2(m.HPCTrayPressure[tray],m.HPCTrayTemp[tray],m.HPCLiqLvMFrac[tray,"Nitrogen"])
	elif tray==4:
		return m.HPCVapLvMFrac[tray,"Oxygen"] == triHPCThermo.HPCAllTrays4CstmVapO2.VapO2(m.HPCTrayPressure[tray],m.HPCTrayTemp[tray],m.HPCLiqLvMFrac[tray,"Nitrogen"])
	elif tray==5:
		return m.HPCVapLvMFrac[tray,"Oxygen"] == triHPCThermo.HPCAllTrays5CstmVapO2.VapO2(m.HPCTrayPressure[tray],m.HPCTrayTemp[tray],m.HPCLiqLvMFrac[tray,"Nitrogen"])
	elif tray==6:
		return m.HPCVapLvMFrac[tray,"Oxygen"] == triHPCThermo.HPCAllTrays6CstmVapO2.VapO2(m.HPCTrayPressure[tray],m.HPCTrayTemp[tray],m.HPCLiqLvMFrac[tray,"Nitrogen"])
	elif tray==7:
		return m.HPCVapLvMFrac[tray,"Oxygen"] == triHPCThermo.HPCAllTrays7CstmVapO2.VapO2(m.HPCTrayPressure[tray],m.HPCTrayTemp[tray],m.HPCLiqLvMFrac[tray,"Nitrogen"])
	elif tray==8:
		return m.HPCVapLvMFrac[tray,"Oxygen"] == triHPCThermo.HPCAllTrays8CstmVapO2.VapO2(m.HPCTrayPressure[tray],m.HPCTrayTemp[tray],m.HPCLiqLvMFrac[tray,"Nitrogen"])
	elif tray==9:
		return m.HPCVapLvMFrac[tray,"Oxygen"] == triHPCThermo.HPCAllTrays9CstmVapO2.VapO2(m.HPCTrayPressure[tray],m.HPCTrayTemp[tray],m.HPCLiqLvMFrac[tray,"Nitrogen"])
	elif tray==10:
		return m.HPCVapLvMFrac[tray,"Oxygen"] == triHPCThermo.HPCAllTrays10CstmVapO2.VapO2(m.HPCTrayPressure[tray],m.HPCTrayTemp[tray],m.HPCLiqLvMFrac[tray,"Nitrogen"])
	elif tray==11:
		return m.HPCVapLvMFrac[tray,"Oxygen"] == triHPCThermo.HPCAllTrays11CstmVapO2.VapO2(m.HPCTrayPressure[tray],m.HPCTrayTemp[tray],m.HPCLiqLvMFrac[tray,"Nitrogen"])
	elif tray==12:
		return m.HPCVapLvMFrac[tray,"Oxygen"] == triHPCThermo.HPCAllTrays12CstmVapO2.VapO2(m.HPCTrayPressure[tray],m.HPCTrayTemp[tray],m.HPCLiqLvMFrac[tray,"Nitrogen"])
	elif tray==13:
		return m.HPCVapLvMFrac[tray,"Oxygen"] == triHPCThermo.HPCAllTrays13CstmVapO2.VapO2(m.HPCTrayPressure[tray],m.HPCTrayTemp[tray],m.HPCLiqLvMFrac[tray,"Nitrogen"])
	elif tray==14:
		return m.HPCVapLvMFrac[tray,"Oxygen"] == triHPCThermo.HPCAllTrays14CstmVapO2.VapO2(m.HPCTrayPressure[tray],m.HPCTrayTemp[tray],m.HPCLiqLvMFrac[tray,"Nitrogen"])
	elif tray==15:
		return m.HPCVapLvMFrac[tray,"Oxygen"] == triHPCThermo.HPCAllTrays15CstmVapO2.VapO2(m.HPCTrayPressure[tray],m.HPCTrayTemp[tray],m.HPCLiqLvMFrac[tray,"Nitrogen"])
	elif tray==16:
		return m.HPCVapLvMFrac[tray,"Oxygen"] == triHPCThermo.HPCAllTrays16CstmVapO2.VapO2(m.HPCTrayPressure[tray],m.HPCTrayTemp[tray],m.HPCLiqLvMFrac[tray,"Nitrogen"])
	elif tray==17:
		return m.HPCVapLvMFrac[tray,"Oxygen"] == triHPCThermo.HPCAllTrays17CstmVapO2.VapO2(m.HPCTrayPressure[tray],m.HPCTrayTemp[tray],m.HPCLiqLvMFrac[tray,"Nitrogen"])
	elif tray==18:
		return m.HPCVapLvMFrac[tray,"Oxygen"] == triHPCThermo.HPCAllTrays18CstmVapO2.VapO2(m.HPCTrayPressure[tray],m.HPCTrayTemp[tray],m.HPCLiqLvMFrac[tray,"Nitrogen"])
	elif tray==19:
		return m.HPCVapLvMFrac[tray,"Oxygen"] == triHPCThermo.HPCAllTrays19CstmVapO2.VapO2(m.HPCTrayPressure[tray],m.HPCTrayTemp[tray],m.HPCLiqLvMFrac[tray,"Nitrogen"])
	elif tray==20:
		return m.HPCVapLvMFrac[tray,"Oxygen"] == triHPCThermo.HPCAllTrays20CstmVapO2.VapO2(m.HPCTrayPressure[tray],m.HPCTrayTemp[tray],m.HPCLiqLvMFrac[tray,"Nitrogen"])
	elif tray==21:
		return m.HPCVapLvMFrac[tray,"Oxygen"] == triHPCThermo.HPCAllTrays21CstmVapO2.VapO2(m.HPCTrayPressure[tray],m.HPCTrayTemp[tray],m.HPCLiqLvMFrac[tray,"Nitrogen"])
	elif tray==22:
		return m.HPCVapLvMFrac[tray,"Oxygen"] == triHPCThermo.HPCAllTrays22CstmVapO2.VapO2(m.HPCTrayPressure[tray],m.HPCTrayTemp[tray],m.HPCLiqLvMFrac[tray,"Nitrogen"])
	elif tray==23:
		return m.HPCVapLvMFrac[tray,"Oxygen"] == triHPCThermo.HPCAllTrays23CstmVapO2.VapO2(m.HPCTrayPressure[tray],m.HPCTrayTemp[tray],m.HPCLiqLvMFrac[tray,"Nitrogen"])
	elif tray==24:
		return m.HPCVapLvMFrac[tray,"Oxygen"] == triHPCThermo.HPCAllTrays24CstmVapO2.VapO2(m.HPCTrayPressure[tray],m.HPCTrayTemp[tray],m.HPCLiqLvMFrac[tray,"Nitrogen"])
	elif tray==25:
		return m.HPCVapLvMFrac[tray,"Oxygen"] == triHPCThermo.HPCAllTrays25CstmVapO2.VapO2(m.HPCTrayPressure[tray],m.HPCTrayTemp[tray],m.HPCLiqLvMFrac[tray,"Nitrogen"])
	elif tray==26:
		return m.HPCVapLvMFrac[tray,"Oxygen"] == triHPCThermo.HPCAllTrays26CstmVapO2.VapO2(m.HPCTrayPressure[tray],m.HPCTrayTemp[tray],m.HPCLiqLvMFrac[tray,"Nitrogen"])
	elif tray==27:
		return m.HPCVapLvMFrac[tray,"Oxygen"] == triHPCThermo.HPCAllTrays27CstmVapO2.VapO2(m.HPCTrayPressure[tray],m.HPCTrayTemp[tray],m.HPCLiqLvMFrac[tray,"Nitrogen"])
	elif tray==28:
		return m.HPCVapLvMFrac[tray,"Oxygen"] == triHPCThermo.HPCAllTrays28CstmVapO2.VapO2(m.HPCTrayPressure[tray],m.HPCTrayTemp[tray],m.HPCLiqLvMFrac[tray,"Nitrogen"])
	elif tray==29:
		return m.HPCVapLvMFrac[tray,"Oxygen"] == triHPCThermo.HPCAllTrays29CstmVapO2.VapO2(m.HPCTrayPressure[tray],m.HPCTrayTemp[tray],m.HPCLiqLvMFrac[tray,"Nitrogen"])
	elif tray==30:
		return m.HPCVapLvMFrac[tray,"Oxygen"] == triHPCThermo.HPCAllTrays30CstmVapO2.VapO2(m.HPCTrayPressure[tray],m.HPCTrayTemp[tray],m.HPCLiqLvMFrac[tray,"Nitrogen"])
	elif tray==31:
		return m.HPCVapLvMFrac[tray,"Oxygen"] == triHPCThermo.HPCAllTrays31CstmVapO2.VapO2(m.HPCTrayPressure[tray],m.HPCTrayTemp[tray],m.HPCLiqLvMFrac[tray,"Nitrogen"])
	elif tray==32:
		return m.HPCVapLvMFrac[tray,"Oxygen"] == triHPCThermo.HPCAllTrays32CstmVapO2.VapO2(m.HPCTrayPressure[tray],m.HPCTrayTemp[tray],m.HPCLiqLvMFrac[tray,"Nitrogen"])
	elif tray==33:
		return m.HPCVapLvMFrac[tray,"Oxygen"] == triHPCThermo.HPCAllTrays33CstmVapO2.VapO2(m.HPCTrayPressure[tray],m.HPCTrayTemp[tray],m.HPCLiqLvMFrac[tray,"Nitrogen"])
	elif tray==34:
		return m.HPCVapLvMFrac[tray,"Oxygen"] == triHPCThermo.HPCAllTrays34CstmVapO2.VapO2(m.HPCTrayPressure[tray],m.HPCTrayTemp[tray],m.HPCLiqLvMFrac[tray,"Nitrogen"])
	elif tray==35:
		return m.HPCVapLvMFrac[tray,"Oxygen"] == triHPCThermo.HPCAllTrays35CstmVapO2.VapO2(m.HPCTrayPressure[tray],m.HPCTrayTemp[tray],m.HPCLiqLvMFrac[tray,"Nitrogen"])
	elif tray==36:
		return m.HPCVapLvMFrac[tray,"Oxygen"] == triHPCThermo.HPCAllTrays36CstmVapO2.VapO2(m.HPCTrayPressure[tray],m.HPCTrayTemp[tray],m.HPCLiqLvMFrac[tray,"Nitrogen"])
	elif tray==37:
		return m.HPCVapLvMFrac[tray,"Oxygen"] == triHPCThermo.HPCAllTrays37CstmVapO2.VapO2(m.HPCTrayPressure[tray],m.HPCTrayTemp[tray],m.HPCLiqLvMFrac[tray,"Nitrogen"])
	elif tray==38:
		return m.HPCVapLvMFrac[tray,"Oxygen"] == triHPCThermo.HPCAllTrays38CstmVapO2.VapO2(m.HPCTrayPressure[tray],m.HPCTrayTemp[tray],m.HPCLiqLvMFrac[tray,"Nitrogen"])
	elif tray==39:
		return m.HPCVapLvMFrac[tray,"Oxygen"] == triHPCThermo.HPCAllTrays39CstmVapO2.VapO2(m.HPCTrayPressure[tray],m.HPCTrayTemp[tray],m.HPCLiqLvMFrac[tray,"Nitrogen"])
	elif tray==40:
		return m.HPCVapLvMFrac[tray,"Oxygen"] == triHPCThermo.HPCAllTrays40CstmVapO2.VapO2(m.HPCTrayPressure[tray],m.HPCTrayTemp[tray],m.HPCLiqLvMFrac[tray,"Nitrogen"])
	elif tray==41:
		return m.HPCVapLvMFrac[tray,"Oxygen"] == triHPCThermo.HPCAllTrays41CstmVapO2.VapO2(m.HPCTrayPressure[tray],m.HPCTrayTemp[tray],m.HPCLiqLvMFrac[tray,"Nitrogen"])
	elif tray==42:
		return m.HPCVapLvMFrac[tray,"Oxygen"] == triHPCThermo.HPCAllTrays42CstmVapO2.VapO2(m.HPCTrayPressure[tray],m.HPCTrayTemp[tray],m.HPCLiqLvMFrac[tray,"Nitrogen"])
test_model.HPCAllTraysVapO2Frac = Constraint(test_model.HPCTrays,rule=HPCAllTraysVapO2Frac)
def HPCAllTraysVapN2Frac(m,tray):
	if tray==1:
		return m.HPCVapLvMFrac[tray,"Nitrogen"] == triHPCThermo.HPCAllTrays1CstmVapN2.VapN2(m.HPCTrayPressure[tray],m.HPCTrayTemp[tray],m.HPCLiqLvMFrac[tray,"Nitrogen"])
	elif tray==2:
		return m.HPCVapLvMFrac[tray,"Nitrogen"] == triHPCThermo.HPCAllTrays2CstmVapN2.VapN2(m.HPCTrayPressure[tray],m.HPCTrayTemp[tray],m.HPCLiqLvMFrac[tray,"Nitrogen"])
	elif tray==3:
		return m.HPCVapLvMFrac[tray,"Nitrogen"] == triHPCThermo.HPCAllTrays3CstmVapN2.VapN2(m.HPCTrayPressure[tray],m.HPCTrayTemp[tray],m.HPCLiqLvMFrac[tray,"Nitrogen"])
	elif tray==4:
		return m.HPCVapLvMFrac[tray,"Nitrogen"] == triHPCThermo.HPCAllTrays4CstmVapN2.VapN2(m.HPCTrayPressure[tray],m.HPCTrayTemp[tray],m.HPCLiqLvMFrac[tray,"Nitrogen"])
	elif tray==5:
		return m.HPCVapLvMFrac[tray,"Nitrogen"] == triHPCThermo.HPCAllTrays5CstmVapN2.VapN2(m.HPCTrayPressure[tray],m.HPCTrayTemp[tray],m.HPCLiqLvMFrac[tray,"Nitrogen"])
	elif tray==6:
		return m.HPCVapLvMFrac[tray,"Nitrogen"] == triHPCThermo.HPCAllTrays6CstmVapN2.VapN2(m.HPCTrayPressure[tray],m.HPCTrayTemp[tray],m.HPCLiqLvMFrac[tray,"Nitrogen"])
	elif tray==7:
		return m.HPCVapLvMFrac[tray,"Nitrogen"] == triHPCThermo.HPCAllTrays7CstmVapN2.VapN2(m.HPCTrayPressure[tray],m.HPCTrayTemp[tray],m.HPCLiqLvMFrac[tray,"Nitrogen"])
	elif tray==8:
		return m.HPCVapLvMFrac[tray,"Nitrogen"] == triHPCThermo.HPCAllTrays8CstmVapN2.VapN2(m.HPCTrayPressure[tray],m.HPCTrayTemp[tray],m.HPCLiqLvMFrac[tray,"Nitrogen"])
	elif tray==9:
		return m.HPCVapLvMFrac[tray,"Nitrogen"] == triHPCThermo.HPCAllTrays9CstmVapN2.VapN2(m.HPCTrayPressure[tray],m.HPCTrayTemp[tray],m.HPCLiqLvMFrac[tray,"Nitrogen"])
	elif tray==10:
		return m.HPCVapLvMFrac[tray,"Nitrogen"] == triHPCThermo.HPCAllTrays10CstmVapN2.VapN2(m.HPCTrayPressure[tray],m.HPCTrayTemp[tray],m.HPCLiqLvMFrac[tray,"Nitrogen"])
	elif tray==11:
		return m.HPCVapLvMFrac[tray,"Nitrogen"] == triHPCThermo.HPCAllTrays11CstmVapN2.VapN2(m.HPCTrayPressure[tray],m.HPCTrayTemp[tray],m.HPCLiqLvMFrac[tray,"Nitrogen"])
	elif tray==12:
		return m.HPCVapLvMFrac[tray,"Nitrogen"] == triHPCThermo.HPCAllTrays12CstmVapN2.VapN2(m.HPCTrayPressure[tray],m.HPCTrayTemp[tray],m.HPCLiqLvMFrac[tray,"Nitrogen"])
	elif tray==13:
		return m.HPCVapLvMFrac[tray,"Nitrogen"] == triHPCThermo.HPCAllTrays13CstmVapN2.VapN2(m.HPCTrayPressure[tray],m.HPCTrayTemp[tray],m.HPCLiqLvMFrac[tray,"Nitrogen"])
	elif tray==14:
		return m.HPCVapLvMFrac[tray,"Nitrogen"] == triHPCThermo.HPCAllTrays14CstmVapN2.VapN2(m.HPCTrayPressure[tray],m.HPCTrayTemp[tray],m.HPCLiqLvMFrac[tray,"Nitrogen"])
	elif tray==15:
		return m.HPCVapLvMFrac[tray,"Nitrogen"] == triHPCThermo.HPCAllTrays15CstmVapN2.VapN2(m.HPCTrayPressure[tray],m.HPCTrayTemp[tray],m.HPCLiqLvMFrac[tray,"Nitrogen"])
	elif tray==16:
		return m.HPCVapLvMFrac[tray,"Nitrogen"] == triHPCThermo.HPCAllTrays16CstmVapN2.VapN2(m.HPCTrayPressure[tray],m.HPCTrayTemp[tray],m.HPCLiqLvMFrac[tray,"Nitrogen"])
	elif tray==17:
		return m.HPCVapLvMFrac[tray,"Nitrogen"] == triHPCThermo.HPCAllTrays17CstmVapN2.VapN2(m.HPCTrayPressure[tray],m.HPCTrayTemp[tray],m.HPCLiqLvMFrac[tray,"Nitrogen"])
	elif tray==18:
		return m.HPCVapLvMFrac[tray,"Nitrogen"] == triHPCThermo.HPCAllTrays18CstmVapN2.VapN2(m.HPCTrayPressure[tray],m.HPCTrayTemp[tray],m.HPCLiqLvMFrac[tray,"Nitrogen"])
	elif tray==19:
		return m.HPCVapLvMFrac[tray,"Nitrogen"] == triHPCThermo.HPCAllTrays19CstmVapN2.VapN2(m.HPCTrayPressure[tray],m.HPCTrayTemp[tray],m.HPCLiqLvMFrac[tray,"Nitrogen"])
	elif tray==20:
		return m.HPCVapLvMFrac[tray,"Nitrogen"] == triHPCThermo.HPCAllTrays20CstmVapN2.VapN2(m.HPCTrayPressure[tray],m.HPCTrayTemp[tray],m.HPCLiqLvMFrac[tray,"Nitrogen"])
	elif tray==21:
		return m.HPCVapLvMFrac[tray,"Nitrogen"] == triHPCThermo.HPCAllTrays21CstmVapN2.VapN2(m.HPCTrayPressure[tray],m.HPCTrayTemp[tray],m.HPCLiqLvMFrac[tray,"Nitrogen"])
	elif tray==22:
		return m.HPCVapLvMFrac[tray,"Nitrogen"] == triHPCThermo.HPCAllTrays22CstmVapN2.VapN2(m.HPCTrayPressure[tray],m.HPCTrayTemp[tray],m.HPCLiqLvMFrac[tray,"Nitrogen"])
	elif tray==23:
		return m.HPCVapLvMFrac[tray,"Nitrogen"] == triHPCThermo.HPCAllTrays23CstmVapN2.VapN2(m.HPCTrayPressure[tray],m.HPCTrayTemp[tray],m.HPCLiqLvMFrac[tray,"Nitrogen"])
	elif tray==24:
		return m.HPCVapLvMFrac[tray,"Nitrogen"] == triHPCThermo.HPCAllTrays24CstmVapN2.VapN2(m.HPCTrayPressure[tray],m.HPCTrayTemp[tray],m.HPCLiqLvMFrac[tray,"Nitrogen"])
	elif tray==25:
		return m.HPCVapLvMFrac[tray,"Nitrogen"] == triHPCThermo.HPCAllTrays25CstmVapN2.VapN2(m.HPCTrayPressure[tray],m.HPCTrayTemp[tray],m.HPCLiqLvMFrac[tray,"Nitrogen"])
	elif tray==26:
		return m.HPCVapLvMFrac[tray,"Nitrogen"] == triHPCThermo.HPCAllTrays26CstmVapN2.VapN2(m.HPCTrayPressure[tray],m.HPCTrayTemp[tray],m.HPCLiqLvMFrac[tray,"Nitrogen"])
	elif tray==27:
		return m.HPCVapLvMFrac[tray,"Nitrogen"] == triHPCThermo.HPCAllTrays27CstmVapN2.VapN2(m.HPCTrayPressure[tray],m.HPCTrayTemp[tray],m.HPCLiqLvMFrac[tray,"Nitrogen"])
	elif tray==28:
		return m.HPCVapLvMFrac[tray,"Nitrogen"] == triHPCThermo.HPCAllTrays28CstmVapN2.VapN2(m.HPCTrayPressure[tray],m.HPCTrayTemp[tray],m.HPCLiqLvMFrac[tray,"Nitrogen"])
	elif tray==29:
		return m.HPCVapLvMFrac[tray,"Nitrogen"] == triHPCThermo.HPCAllTrays29CstmVapN2.VapN2(m.HPCTrayPressure[tray],m.HPCTrayTemp[tray],m.HPCLiqLvMFrac[tray,"Nitrogen"])
	elif tray==30:
		return m.HPCVapLvMFrac[tray,"Nitrogen"] == triHPCThermo.HPCAllTrays30CstmVapN2.VapN2(m.HPCTrayPressure[tray],m.HPCTrayTemp[tray],m.HPCLiqLvMFrac[tray,"Nitrogen"])
	elif tray==31:
		return m.HPCVapLvMFrac[tray,"Nitrogen"] == triHPCThermo.HPCAllTrays31CstmVapN2.VapN2(m.HPCTrayPressure[tray],m.HPCTrayTemp[tray],m.HPCLiqLvMFrac[tray,"Nitrogen"])
	elif tray==32:
		return m.HPCVapLvMFrac[tray,"Nitrogen"] == triHPCThermo.HPCAllTrays32CstmVapN2.VapN2(m.HPCTrayPressure[tray],m.HPCTrayTemp[tray],m.HPCLiqLvMFrac[tray,"Nitrogen"])
	elif tray==33:
		return m.HPCVapLvMFrac[tray,"Nitrogen"] == triHPCThermo.HPCAllTrays33CstmVapN2.VapN2(m.HPCTrayPressure[tray],m.HPCTrayTemp[tray],m.HPCLiqLvMFrac[tray,"Nitrogen"])
	elif tray==34:
		return m.HPCVapLvMFrac[tray,"Nitrogen"] == triHPCThermo.HPCAllTrays34CstmVapN2.VapN2(m.HPCTrayPressure[tray],m.HPCTrayTemp[tray],m.HPCLiqLvMFrac[tray,"Nitrogen"])
	elif tray==35:
		return m.HPCVapLvMFrac[tray,"Nitrogen"] == triHPCThermo.HPCAllTrays35CstmVapN2.VapN2(m.HPCTrayPressure[tray],m.HPCTrayTemp[tray],m.HPCLiqLvMFrac[tray,"Nitrogen"])
	elif tray==36:
		return m.HPCVapLvMFrac[tray,"Nitrogen"] == triHPCThermo.HPCAllTrays36CstmVapN2.VapN2(m.HPCTrayPressure[tray],m.HPCTrayTemp[tray],m.HPCLiqLvMFrac[tray,"Nitrogen"])
	elif tray==37:
		return m.HPCVapLvMFrac[tray,"Nitrogen"] == triHPCThermo.HPCAllTrays37CstmVapN2.VapN2(m.HPCTrayPressure[tray],m.HPCTrayTemp[tray],m.HPCLiqLvMFrac[tray,"Nitrogen"])
	elif tray==38:
		return m.HPCVapLvMFrac[tray,"Nitrogen"] == triHPCThermo.HPCAllTrays38CstmVapN2.VapN2(m.HPCTrayPressure[tray],m.HPCTrayTemp[tray],m.HPCLiqLvMFrac[tray,"Nitrogen"])
	elif tray==39:
		return m.HPCVapLvMFrac[tray,"Nitrogen"] == triHPCThermo.HPCAllTrays39CstmVapN2.VapN2(m.HPCTrayPressure[tray],m.HPCTrayTemp[tray],m.HPCLiqLvMFrac[tray,"Nitrogen"])
	elif tray==40:
		return m.HPCVapLvMFrac[tray,"Nitrogen"] == triHPCThermo.HPCAllTrays40CstmVapN2.VapN2(m.HPCTrayPressure[tray],m.HPCTrayTemp[tray],m.HPCLiqLvMFrac[tray,"Nitrogen"])
	elif tray==41:
		return m.HPCVapLvMFrac[tray,"Nitrogen"] == triHPCThermo.HPCAllTrays41CstmVapN2.VapN2(m.HPCTrayPressure[tray],m.HPCTrayTemp[tray],m.HPCLiqLvMFrac[tray,"Nitrogen"])
	elif tray==42:
		return m.HPCVapLvMFrac[tray,"Nitrogen"] == triHPCThermo.HPCAllTrays42CstmVapN2.VapN2(m.HPCTrayPressure[tray],m.HPCTrayTemp[tray],m.HPCLiqLvMFrac[tray,"Nitrogen"])
test_model.HPCAllTraysVapN2Frac = Constraint(test_model.HPCTrays,rule=HPCAllTraysVapN2Frac)
#--------HPC Summation---------
def HPCLiqSum(m, tray):
	return sum([m.HPCLiqLvMFrac[tray, c] for c in m.Component]) == 1
test_model.HPCLiqSum = Constraint(test_model.HPCTrays, rule=HPCLiqSum)
def HPCVapSum(m, tray):
	return sum([m.HPCVapLvMFrac[tray, c] for c in m.Component]) == 1
test_model.HPCVapSum = Constraint(test_model.HPCTrays, rule=HPCVapSum)
#--------HPC Pressure Profile---------
def HPCPProf(m, tray):
	return ((m.HPCTopPressure-m.HPCBtmPressure)/41*(tray-1)+m.HPCBtmPressure - m.HPCTrayPressure[tray])*0.010000 == 0
test_model.HPCPProf = Constraint(test_model.HPCTrays, rule=HPCPProf)
#--------HPC Extractions---------
def HPCExt6MFracSpec(m, comp):
	return m.HPCExt6MFrac[comp] - m.HPCLiqLvMFrac[6, comp] == 0 
test_model.HPCExt6MFracSpec = Constraint(test_model.Component, rule=HPCExt6MFracSpec)
def HPCExt6MEtlpSpec(m):
	return (m.HPCExt6MEtlp - m.HPCLiqLvMEtlp[6])*  0.000010 == 0
test_model.HPCExt6MEtlpSpec = Constraint(rule=HPCExt6MEtlpSpec)
def HPCExt22MFracSpec(m, comp):
	return m.HPCExt22MFrac[comp] - m.HPCVapLvMFrac[22, comp] == 0 
test_model.HPCExt22MFracSpec = Constraint(test_model.Component, rule=HPCExt22MFracSpec)
def HPCExt22MEtlpSpec(m):
	return (m.HPCExt22MEtlp - m.HPCVapLvMEtlp[22])*  0.000010 == 0
test_model.HPCExt22MEtlpSpec = Constraint(rule=HPCExt22MEtlpSpec)

#----------------------------------
#           HPCSump
#----------------------------------
#--------HPCSump Mass Balance---------
def HPCSumpMassBlnc(m):
	return (m.HPCLiqLvMFlow[1]-m.HPCSumpOutMFlow)*0.001000==0
test_model.HPCSumpMassBlnc = Constraint(rule=HPCSumpMassBlnc)
def HPCSumpHldpMFracSpec(m, comp):
	return m.HPCSumpHldpMFrac[comp] - m.HPCLiqLvMFrac[1,comp] == 0
test_model.HPCSumpHldpMFracSpec = Constraint(test_model.Component, rule=HPCSumpHldpMFracSpec)

#----------------------------------
#           HPCCond
#----------------------------------
#--------HPCCond Mass Balance---------
def HPCCondMassBlnc(m):
	return (m.HPCCondRefMFlow+m.HPCCondPrdtMFlow-m.HPCVapLvMFlow[42])*0.001000==0
test_model.HPCCondMassBlnc = Constraint(rule=HPCCondMassBlnc)
def HPCCondRefSpec(m):
	return (m.HPCCondRefMFlow-m.HPCVapLvMFlow[42]*m.HPCCondRefluxRatio)*0.001000==0
test_model.HPCCondRefSpec = Constraint(rule=HPCCondRefSpec)
#--------HPCCond Energy Balance---------
def HPCCondEngBlnc(m):
	return (m.HPCVapLvMFlow[42]*(m.HPCVapLvMEtlp[42]-m.HPCCondOutMEtlp)-m.HPCCondMHeatOut)*0.000010==0
test_model.HPCCondEngBlnc = Constraint(rule=HPCCondEngBlnc)
#--------HPCCond Bubble Point---------
def HPCCondSelfBubTemp(m):
	return m.HPCVapLvMFrac[42,"Oxygen"] == triHPCThermo.HPCCondSelfCstmLiqO2.LiqO2(m.HPCTrayPressure[42],m.HPCCondTemp,m.HPCVapLvMFrac[42,"Nitrogen"])
test_model.HPCCondSelfBubTemp = Constraint(rule=HPCCondSelfBubTemp)
