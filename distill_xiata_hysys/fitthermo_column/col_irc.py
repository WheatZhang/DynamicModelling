from pyomo.environ import *
from pyomo.dae import *
from binary_fitting_result import vapor_oxygen_composition,liquid_oxygen_composition,liquid_nitrogen_enthalpy,liquid_oxygen_enthalpy,vapor_nitrogen_enthalpy,vapor_oxygen_enthalpy

model = ConcreteModel()
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
model.liquidLeavingMolarFlow = Param(model.BottomTray,initialize={1:1382.580749395402})
model.liquidLeavingMolarFraction = Param(model.BottomTray,model.Component,initialize=\
    {(1,'Nitrogen'):0.7009695483157175,(1,'Oxygen'):0.29903045168428255})
model.vaporLeavingMolarFlow = Param(model.TopTray,initialize={model.NumberOfTrays.value:1543.5481265114956})
model.vaporLeavingMolarFraction = Param(model.TopTray,model.Component,initialize=\
    {(model.NumberOfTrays.value,'Nitrogen'):0.9893649995333493,(model.NumberOfTrays.value,'Oxygen'):0.010635000466650661})
model.trayPressure = Param(model.TopAndBottomTray,initialize={1:564,model.NumberOfTrays.value:539.56})
model.trayTemperature  = Param(model.TopAndBottomTray,initialize={1:-174.55076597225644,model.NumberOfTrays.value:-177.70902430053})
#--------------IRC指定-----------------
GasDrawRatio = 0.587744831
MinimalTempDiff = 0.1
model.expandValveDeltaP = Param(initialize=400)
model.heatTransferConstant = Param(initialize=1736458) #Q=k*\deltaT
model.ircLNProductMolarFlow = Param(initialize=39.9979154)

#-------------IRC变量定义---------------
model.ircWasteMolarFlow=Var(initialize=726.0305)
model.expandValveOutTemperature=Var(bounds=(-230,-100),initialize=-188.314)
model.ircGNProductMolarFlow=Var(within=NonNegativeReals,initialize=960)
model.ircTopTrayVaporMolarFlow=Var(within=NonNegativeReals,initialize=1633)
model.ircDrainMolarFlow=Var(within=NonNegativeReals,initialize=274)
model.ircBottomLiquidMolarFlow=Var(within=NonNegativeReals,initialize=1000)
model.ircRefluxMolarFlow=Var(within=NonNegativeReals,initialize=633)
model.ircCondTemperature=Var(bounds=(-230,-100),initialize=-186.348)
model.ircCondPressure=Var(bounds=(0,1000),initialize=164)
model.ircRebTemperature=Var(bounds=(-230,-100),initialize=-188.314)
model.ircRebPressure=Var(bounds=(0,1000),initialize=564-model.expandValveDeltaP.value)
model.ircHeatExchange=Var(within=NonNegativeReals,initialize=3.413876e6)
model.ircDrainMolarFraction=Var(model.Component,bounds=(0,1),initialize={"Nitrogen":0.4365,"Oxygen":0.5635})
model.ircWNMolarFraction=Var(model.Component,bounds=(0,1),initialize={"Nitrogen":0.7337,"Oxygen":0.2663})
#----------------------------------------
#     焓的热力学
#----------------------------------------
def LiquidPhaseEnthalpy(temperature, pressure, oxygen, nitrogen):
    return liquid_nitrogen_enthalpy(pressure,temperature)*nitrogen+liquid_oxygen_enthalpy(pressure,temperature)*oxygen
def VaporPhaseEnthalpy(temperature, pressure, oxygen, nitrogen):
    return vapor_nitrogen_enthalpy(pressure,temperature)*nitrogen+vapor_oxygen_enthalpy(pressure,temperature)*oxygen
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
def ICondPressure(m):
    return (m.trayPressure[m.NumberOfTrays.value] - m.ircCondPressure)*1e-3 == 0
model.ICondPressure = Constraint(rule=ICondPressure)
def deriveGNProductMolarFlow(m):
    return (m.ircGNProductMolarFlow - GasDrawRatio * m.ircTopTrayVaporMolarFlow)*1e-3 == 0
model.deriveGNProductMolarFlow = Constraint(rule = deriveGNProductMolarFlow)
def IRCCondMaterialBalance(m):
    return (m.ircTopTrayVaporMolarFlow*(1-GasDrawRatio)-m.ircLNProductMolarFlow-m.ircRefluxMolarFlow)*1e-3==0
model.ircCondMaterialBalance = Constraint(rule = IRCCondMaterialBalance)
def IRCCondEnergyBalance(m):
    return (m.ircTopTrayVaporMolarFlow*(1-GasDrawRatio)*m.ircTopTrayVaporMolarEnthalpy \
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
def rebVaporComposition(m):
    return m.ircWNMolarFraction['Oxygen'] == vapor_oxygen_composition(m.ircRebPressure,m.ircRebTemperature)
model.rebVaporComposition = Constraint(rule = rebVaporComposition)
def rebLiquidComposition(m):
    return m.ircDrainMolarFraction['Oxygen'] == liquid_oxygen_composition(m.ircRebPressure,m.ircRebTemperature)
model.rebLiquidComposition = Constraint(rule = rebLiquidComposition)
#-------------IRC Heat Transfer-----------------
def IRCTempDiff(m):
    return (m.ircCondTemperature-m.ircRebTemperature-MinimalTempDiff)*1e-2>=0
model.ircTempDiff = Constraint(rule=IRCTempDiff)
def IRCHeatTransfer(m):
    return ((m.ircCondTemperature-m.ircRebTemperature)*m.heatTransferConstant-m.ircHeatExchange)*1e-6==0
model.IRCHeatTransfer = Constraint(rule=IRCHeatTransfer)