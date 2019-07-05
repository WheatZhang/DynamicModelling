#!/usr/bin/env python
#-*- coding:utf-8 -*-
from pyomo.environ import *
from pyomo.dae import *
from pyomo.opt import SolverStatus, TerminationCondition

def pre_setting(model):
	#----------单位-----------
	#  温度：℃，
	#  温差：K
	#  压力：kPa
	#  物质的量：kmol
	#  流量：kmol/h
	#  摩尔焓：kJ/kmol
	#---------------物质组分指定-----------
	model.Component = Set(initialize=['Oxygen','Nitrogen'])
	#--------------塔输出指定--------------
	# model.ColumnTopPressure = Param(initialize = 539.56)
	# model.ColumnBottomPressure = Param(initialize = 564)
	model.NumberOfTrays = Param(initialize=5)
	model.TopTray = Set(initialize={model.NumberOfTrays.value})
	model.BottomTray = Set(initialize={1})
	model.TopAndBottomTray = Set(initialize={1,model.NumberOfTrays.value})
	model.liquidLeavingMolarFlow = Param(model.BottomTray,initialize={1:273.93947880149295})
	model.liquidLeavingMolarFraction = Param(model.BottomTray,model.Component,initialize=\
		{(1,'Nitrogen'):0.3696311468392572,(1,'Oxygen'):0.6303688531607429})
	model.vaporLeavingMolarFlow = Param(model.TopTray,initialize={model.NumberOfTrays.value:4315.151302996267})
	model.vaporLeavingMolarFraction = Param(model.TopTray,model.Component,initialize=\
		{(model.NumberOfTrays.value,'Nitrogen'):0.8567158672293502,(model.NumberOfTrays.value,'Oxygen'):0.1432841327706497})
	model.trayPressure = Param(model.TopAndBottomTray,initialize={1:564,model.NumberOfTrays.value:539.56})
	model.trayTemperature  = Param(model.TopAndBottomTray,initialize={1:-173.75200000000004,model.NumberOfTrays.value:-175.51168000000004})
	#--------------IRC指定-----------------
	model.GasDrawRatio = Param(initialize=0.587744831)
	model.MinimalTempDiff =  Param(initialize=0.1)
	model.expandValveDeltaP = Param(initialize=100)
	model.ircLNProductMolarFlow = Param(initialize=39.9979154)
	model.heatTransferConstant = Param(initialize=238616) #Q=k*\deltaT
	model.ircWasteMolarFlow=Param(initialize=142.412308)
	#--------------VLE热力学指定----------------
	reb_ec = {}
	for c in model.Component:
		if c == 'Oxygen':
			reb_ec[c] = 0.502560524364477
		elif c=='Nitrogen':
			reb_ec[c] = 1.266452521398482
	model.rebEquilibriumConstant = Var(model.Component,initialize=reb_ec)
	model.rebEquilConstantRatio = Param(initialize=0.5/1.26)
	# 加入bound是必要的，否则不能收敛到一个合理的结果
	#-------------IRC变量定义---------------
	model.expandValveOutTemperature=Var(bounds=(-230,-100),initialize=-178.127)
	model.ircGNProductMolarFlow=Var(within=NonNegativeReals,initialize=2460.4011666837564)
	model.ircTopTrayVaporMolarFlow=Var(within=NonNegativeReals,initialize=4186.17236071245)
	model.ircDrainMolarFlow=Var(within=NonNegativeReals,initialize=180.70551815285762)
	model.ircBottomLiquidMolarFlow=Var(within=NonNegativeReals,initialize=325.5310557150179)
	model.ircRefluxMolarFlow=Var(within=NonNegativeReals,initialize=1685.7732786301506)
	model.ircCondTemperature=Var(bounds=(-230,-100),initialize=-166)
	model.ircCondPressure=Var(bounds=(0,1000),initialize=450)
	model.ircRebTemperature=Var(bounds=(-230,-100),initialize=-173)
	model.ircRebPressure=Var(bounds=(0,1000),initialize=564-model.expandValveDeltaP.value)
	model.ircHeatExchange=Var(within=NonNegativeReals,initialize=1.52e6)
	model.ircDrainMolarFraction=Var(model.Component,bounds=(0,1),initialize={"Nitrogen":0.733749769,"Oxygen":0.266250231})
	model.ircWNMolarFraction=Var(model.Component,bounds=(0,1),initialize={"Nitrogen":0.436531416,"Oxygen":0.563468584})


def post_setting(model):
		#----------------------------------------
	#     焓的热力学
	#----------------------------------------
	def LiquidPhaseEnthalpy(temperature, pressure, oxygen, nitrogen):
		return (8917.884 + (temperature - (-173)) * 418.68 + (pressure - 250) * -18.31725) * oxygen \
			   + (3893.724 + (temperature - (-173)) * 418.68 + (pressure - 770) * -18.31725) * nitrogen
	def VaporPhaseEnthalpy(temperature, pressure, oxygen, nitrogen):
		return (15407.424 + (temperature - (-173)) * 558.24 + (pressure - 250) * -19.43871429) * oxygen \
			   + (8457.336 + (temperature - (-173)) * 558.24 + (pressure - 770) * -19.43871429) * nitrogen
	#----------------------------------------
	###
	# Enthalpy expression
	###
	#------------------IRC------------------
	def _ircTopTrayVaporMolarEnthalpy(m):
		return VaporPhaseEnthalpy(m.trayTemperature[m.NumberOfTrays.value], m.trayPressure[m.NumberOfTrays.value], m.vaporLeavingMolarFraction[m.NumberOfTrays.value,'Oxygen'],
								  m.vaporLeavingMolarFraction[m.NumberOfTrays.value,'Nitrogen'])
	model.ircTopTrayVaporMolarEnthalpy = Expression(rule=_ircTopTrayVaporMolarEnthalpy)
	def _ircCondLiquidMolarEnthalpy(m):
		return LiquidPhaseEnthalpy(m.ircCondTemperature, m.ircCondPressure, m.vaporLeavingMolarFraction[m.NumberOfTrays.value,'Oxygen'],
								   m.vaporLeavingMolarFraction[m.NumberOfTrays.value,'Nitrogen'])
	model.ircCondLiquidMolarEnthalpy = Expression(rule=_ircCondLiquidMolarEnthalpy)
	def _ircOutExpandValveMolarEnthalpy(m):
		return LiquidPhaseEnthalpy(m.expandValveOutTemperature, m.ircRebPressure, m.liquidLeavingMolarFraction[1,'Oxygen'],
								   m.liquidLeavingMolarFraction[1,'Nitrogen'])
	model.ircOutExpandValveMolarEnthalpy = Expression(rule=_ircOutExpandValveMolarEnthalpy)
	def _ircDrainMolarEnthalpy(m):
		return LiquidPhaseEnthalpy(m.ircRebTemperature, m.ircRebPressure, m.ircDrainMolarFraction['Oxygen'],
								   m.ircDrainMolarFraction['Nitrogen'])
	model.ircDrainMolarEnthalpy = Expression(rule=_ircDrainMolarEnthalpy)
	def _ircWNMolarEnthalpy(m):
		return VaporPhaseEnthalpy(m.ircRebTemperature, m.ircRebPressure, m.ircWNMolarFraction['Oxygen'],
								  m.ircWNMolarFraction['Nitrogen'])
	model.ircWNMolarEnthalpy = Expression(rule=_ircWNMolarEnthalpy)
	#-----------------------------------
	###                             
	# Model constraints
	###
	#-------------IRC Condenser Side-----------------
	def ITopTrayVaporMolarFlow(m):
		return (m.vaporLeavingMolarFlow[m.NumberOfTrays.value] - m.ircTopTrayVaporMolarFlow)*1e-3 ==0
	model.ITopTrayVaporMolarFlow =  Constraint(rule = ITopTrayVaporMolarFlow)
	# def ICondTemperature(m):
	#     return (m.trayTemperature[m.NumberOfTrays.value] - m.ircCondTemperature)*1e-2 == 0
	# model.ICondTemperature = Constraint(rule=ICondTemperature)
	def ICondPressure(m):
		return (m.trayPressure[m.NumberOfTrays.value] - m.ircCondPressure)*1e-3 == 0
	model.ICondPressure = Constraint(rule=ICondPressure)
	def deriveGNProductMolarFlow(m):
		return (m.ircGNProductMolarFlow - m.GasDrawRatio * m.ircTopTrayVaporMolarFlow)*1e-3 == 0
	model.deriveGNProductMolarFlow = Constraint(rule = deriveGNProductMolarFlow)
	def IRCCondMaterialBalance(m):
		return (m.ircTopTrayVaporMolarFlow*(1-m.GasDrawRatio)-m.ircLNProductMolarFlow-m.ircRefluxMolarFlow)*1e-3==0
	model.ircCondMaterialBalance = Constraint(rule = IRCCondMaterialBalance)
	def IRCCondEnergyBalance(m):
		return (m.ircTopTrayVaporMolarFlow*(1-m.GasDrawRatio)*m.ircTopTrayVaporMolarEnthalpy \
			   -(m.ircLNProductMolarFlow+m.ircRefluxMolarFlow)*m.ircCondLiquidMolarEnthalpy - m.ircHeatExchange)*1e-5==0
	model.ircCondEnergyBalance = Constraint(rule = IRCCondEnergyBalance)
	#-------------IRC Reboiler Side-----------------
	def IBottomLiquidMolarFlow(m):
		return (m.liquidLeavingMolarFlow[1] - m.ircBottomLiquidMolarFlow)*1e-3 ==0
	model.IBottomLiquidMolarFlow =  Constraint(rule = IBottomLiquidMolarFlow)
	def IRCRebMaterialBalance(m, comp):
		return (m.ircBottomLiquidMolarFlow*m.liquidLeavingMolarFraction[1,comp]\
			- m.ircWasteMolarFlow*m.ircWNMolarFraction[comp]\
			- m.ircDrainMolarFlow*m.ircDrainMolarFraction[comp])*1e-3 == 0
	model.ircRebMaterialBalance = Constraint(model.Component, rule = IRCRebMaterialBalance)
	def IRCRebEnergyBalance(m):
		return (m.ircBottomLiquidMolarFlow*m.ircOutExpandValveMolarEnthalpy+m.ircHeatExchange\
			-m.ircWasteMolarFlow *m.ircWNMolarEnthalpy-m.ircDrainMolarFlow*m.ircDrainMolarEnthalpy)*1e-5==0
	model.ircRebEnergyBalance = Constraint(rule=IRCRebEnergyBalance)
	def IRCRebWNSummation(m):
		return sum([m.ircWNMolarFraction[c] for c in m.Component]) == 1
	model.IRCRebWNSummation = Constraint(rule=IRCRebWNSummation)
	def IRCRebDrainSummation(m):
		return sum([m.ircDrainMolarFraction[c] for c in m.Component]) == 1
	model.IRCRebDrainSummation = Constraint(rule=IRCRebDrainSummation)
	def ExpandValveEnthalpy(m):
		return (LiquidPhaseEnthalpy(m.trayTemperature[1], m.trayPressure[1], m.liquidLeavingMolarFraction[1, 'Oxygen'],
								   m.liquidLeavingMolarFraction[1, 'Nitrogen'])- \
									 model.ircOutExpandValveMolarEnthalpy)*1e-6 ==0
	model.ExpandValveEnthalpy = Constraint(rule=ExpandValveEnthalpy)
	def ExpandValvePressure(m):
		return (m.trayPressure[1]-m.expandValveDeltaP-m.ircRebPressure)*1e-3 == 0
	model.ExpandValvePressure = Constraint(rule=ExpandValvePressure)
	def rebEquilibrium(m):
		return m.rebEquilibriumConstant['Oxygen'] == m.rebEquilibriumConstant['Nitrogen'] * m.rebEquilConstantRatio
	model.rebEquilibrium = Constraint(rule = rebEquilibrium)
	def rebVLE(m, comp):
		return m.ircWNMolarFraction[comp] == m.ircDrainMolarFraction[comp] *m.rebEquilibriumConstant[comp]
	model.rebVLE = Constraint(model.Component, rule = rebVLE)
	#-------------IRC Heat Transfer-----------------
	def IRCTempDiff(m):
		return (m.ircCondTemperature-m.ircRebTemperature-m.MinimalTempDiff)*1e-2>=0
	model.ircTempDiff = Constraint(rule=IRCTempDiff)
	def IRCHeatTransfer(m):
		return ((m.ircCondTemperature-m.ircRebTemperature)*m.heatTransferConstant-m.ircHeatExchange)*1e-6==0
	model.IRCHeatTransfer = Constraint(rule=IRCHeatTransfer)

model_t = ConcreteModel()
pre_setting(model_t)
post_setting(model_t)

solver=SolverFactory('ipopt')
results = solver.solve(model_t,tee=True)

a=[[1,2],[1,2]]
print(a[0][0])