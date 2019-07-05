from pyomo.environ import *
from pyomo.dae import *

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
ColumnTopPressure = 539.56
ColumnBottomPressure = 564
NumberOfTrays = 5
model.TopTray = Set(initialize={NumberOfTrays})
model.BottomTray = Set(initialize={1})
model.TopAndBottomTray = Set(initialize={1,NumberOfTrays})
model.liquidLeavingMolarFlow = Param(model.BottomTray,initialize={1:325.5310557150179})
model.liquidLeavingMolarFraction = Param(model.BottomTray,model.Component,initialize=\
    {(1,'Nitrogen'):0.42577771418273724,(1,'Oxygen'):0.5742222858172628})
model.vaporLeavingMolarFlow = Param(model.TopTray,initialize={NumberOfTrays:4186.17236071245})
model.vaporLeavingMolarFraction = Param(model.TopTray,model.Component,initialize=\
    {(NumberOfTrays,'Nitrogen'):0.8608079212945091,(NumberOfTrays,'Oxygen'):0.13919207870549097})
model.trayPressure = Param(model.TopAndBottomTray,initialize={1:564,NumberOfTrays:539.56})
model.trayTemperature  = Param(model.TopAndBottomTray,initialize={1:-173.752,NumberOfTrays:-175.51168})
#--------------IRC指定-----------------
GasDrawRatio = 0.587744831
MinimalTempDiff = 0.1
model.expandValveDeltaP = Param(initialize=100)
model.ircLNProductMolarFlow = Param(initialize=39.9979154)
model.heatTransferConstant = Param(initialize=238616) #Q=k*\deltaT
model.ircHeatExchange = Param(initialize=3400000)
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
model.expandValveOutTemperature=Var(bounds=(-230,-100),initialize=0)
model.ircWasteMolarFlow=Var(within=NonNegativeReals,initialize=0)
model.ircDrainMolarFlow=Var(within=NonNegativeReals,initialize=0)
model.ircBottomLiquidMolarFlow=Var(within=NonNegativeReals,initialize=0)
model.ircRebTemperature=Var(bounds=(-230,-100),initialize=0)
model.ircRebPressure=Var(bounds=(0,1000),initialize=0)
model.ircDrainMolarFraction=Var(model.Component,bounds=(0,1),initialize={"Nitrogen":0.733749769,"Oxygen":0.266250231})
model.ircWNMolarFraction=Var(model.Component,bounds=(0,1),initialize={"Nitrogen":0.436531416,"Oxygen":0.563468584})
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
                                 model.ircOutExpandValveMolarEnthalpy)*1e-5 ==0
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