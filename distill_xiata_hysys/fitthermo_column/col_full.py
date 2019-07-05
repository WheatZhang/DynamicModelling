from pyomo.environ import *
from pyomo.dae import *
from binary_fitting_result import vapor_oxygen_composition,liquid_oxygen_composition,liquid_nitrogen_enthalpy,liquid_oxygen_enthalpy,vapor_nitrogen_enthalpy,vapor_oxygen_enthalpy

model = ConcreteModel()
#----------单位-----------
#  温度：℃
#  温差：K
#  压力：kPa
#  物质的量：kmol
#  流量：kmol/h
#  摩尔焓：kJ/kmol
#---------------物质组分指定-----------
model.Component = Set(initialize=['Oxygen','Nitrogen'])
#--------------塔设备指定--------------
model.NumberOfTrays = Param(initialize=10)
AirFeedTray = 1
RefluxTray = model.NumberOfTrays.value
ColumnTopPressure = 539.56
ColumnBottomPressure = 564
model.AllTrays = RangeSet(1, model.NumberOfTrays.value) # 10块塔板，下面为1
#--------------进料指定----------------
model.FeedMolarFlow = Param(initialize=2000)
model.FeedMolarFraction = Param(model.Component, initialize={'Oxygen':0.21,'Nitrogen':0.79})
model.FeedTemperature = Var(initialize = -174.0013876)
model.FeedPressure = Param(initialize = 564)
model.FeedVaporFraction = Param(initialize=0.8)
#--------------IRC指定-----------------
GasDrawRatio = 0.587744831
MinimalTempDiff = 0.1
model.expandValveDeltaP = Param(initialize=400)
model.heatTransferConstant = Param(initialize=1736458) #Q=k*\deltaT
model.ircLNProductMolarFlow = Param(initialize=39.9979154)
#--------------进料变量定义--------------
model.FeedVaporPhaseMolarFrac = Var(model.Component, bounds=(0,1), initialize={'Oxygen':0.17529771144636974,'Nitrogen':0.8247022885536303})
model.FeedLiquidPhaseMolarFrac = Var(model.Component, bounds=(0,1), initialize={'Oxygen':0.34880915421452136,'Nitrogen':0.6511908457854787})
#--------------塔板变量定义--------------
#model.trayTemperature = Param(model.AllTrays,initialize=-170)
model.trayTemperature = Var(model.AllTrays,bounds=(-230,-100),initialize=-175)
model.trayPressure = Var(model.AllTrays,bounds=(0,1000), initialize = (ColumnTopPressure+ColumnBottomPressure)/2)
model.vaporLeavingMolarFlow = Var(model.AllTrays, within=NonNegativeReals,initialize=model.FeedMolarFlow)
model.liquidLeavingMolarFlow = Var(model.AllTrays, within=NonNegativeReals,initialize=model.FeedMolarFlow)
model.vaporLeavingMolarFraction = Var(model.AllTrays, model.Component, bounds=(0,1),initialize=0.5)
model.liquidLeavingMolarFraction = Var(model.AllTrays, model.Component, bounds=(0,1),initialize=0.5)
# 之前少了这些定义
def vaporLeavingMolarFlowCompo(m,tray, comp):
    return m.vaporLeavingMolarFraction[tray,comp]*m.vaporLeavingMolarFlow[tray]
model.vaporLeavingMolarFlowCompo = Expression(model.AllTrays, model.Component,rule=vaporLeavingMolarFlowCompo)
def liquidLeavingMolarFlowCompo(m,tray, comp):
    return m.liquidLeavingMolarFraction[tray,comp]*m.liquidLeavingMolarFlow[tray]
model.liquidLeavingMolarFlowCompo = Expression(model.AllTrays, model.Component, rule=liquidLeavingMolarFlowCompo)
#-------------IRC变量定义---------------
model.ircWasteMolarFlow=Var(initialize=726.0305)
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
#--------------膨胀阀变量定义---------------
model.EVOutVPMolarFrac = Var(model.Component, bounds=(0,1), initialize={'Oxygen':0.11858191339664961,'Nitrogen':0.8814180866033504})
model.EVOutLPMolarFrac = Var(model.Component, bounds=(0,1), initialize={'Oxygen':0.32213092774934615,'Nitrogen':0.6778690722506538})
model.EVOutVaporFraction = Var(initialize=0.14, bounds=(0,0.3))
model.ircEVOutTemperature = Var(initialize=-188.314, bounds = (-200,-170))
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
#-----------------进料------------------
def _feedEnthalpy(m):
    return (1-m.FeedVaporFraction)*LiquidPhaseEnthalpy(m.FeedTemperature,m.FeedPressure,m.FeedLiquidPhaseMolarFrac['Oxygen'],m.FeedLiquidPhaseMolarFrac['Nitrogen'])\
        +m.FeedVaporFraction*VaporPhaseEnthalpy(m.FeedTemperature,m.FeedPressure,m.FeedVaporPhaseMolarFrac['Oxygen'],m.FeedVaporPhaseMolarFrac['Nitrogen'])
model.feedEnthalpy = Expression(rule= _feedEnthalpy)
#-----------------下塔------------------
def _liquidLeavingMolarEnthalpy(m, tray):
    return LiquidPhaseEnthalpy(m.trayTemperature[tray], m.trayPressure[tray], m.liquidLeavingMolarFraction[tray,'Oxygen'],\
                               m.liquidLeavingMolarFraction[tray,'Nitrogen'])
model.liquidLeavingMolarEnthalpy = Expression(model.AllTrays, rule=_liquidLeavingMolarEnthalpy)
def _vaporLeavingMolarEnthalpy(m, tray):
    return VaporPhaseEnthalpy(m.trayTemperature[tray], m.trayPressure[tray],\
                               m.vaporLeavingMolarFraction[tray, 'Oxygen'],\
                               m.vaporLeavingMolarFraction[tray, 'Nitrogen'])
model.vaporLeavingMolarEnthalpy = Expression(model.AllTrays, rule=_vaporLeavingMolarEnthalpy)
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
def _ircDrainMolarEnthalpy(m):
    return LiquidPhaseEnthalpy(m.ircRebTemperature, m.ircRebPressure, m.ircDrainMolarFraction['Oxygen'],
                               m.ircDrainMolarFraction['Nitrogen'])
model.ircDrainMolarEnthalpy = Expression(rule=_ircDrainMolarEnthalpy)
def _ircWNMolarEnthalpy(m):
    return VaporPhaseEnthalpy(m.ircRebTemperature, m.ircRebPressure, m.ircWNMolarFraction['Oxygen'],
                              m.ircWNMolarFraction['Nitrogen'])
model.ircWNMolarEnthalpy = Expression(rule=_ircWNMolarEnthalpy)
#--------------IRC Expand Valve-----------------------
def _ircOutExpandValveMolarEnthalpy(m):
    return LiquidPhaseEnthalpy(m.ircEVOutTemperature, m.ircRebPressure, m.EVOutLPMolarFrac['Oxygen'],
                               m.EVOutLPMolarFrac['Nitrogen'])*(1-m.EVOutVaporFraction)+\
VaporPhaseEnthalpy(m.ircEVOutTemperature, m.ircRebPressure, m.EVOutVPMolarFrac['Oxygen'],
                               m.EVOutVPMolarFrac['Nitrogen'])*m.EVOutVaporFraction
model.ircOutExpandValveMolarEnthalpy = Expression(rule=_ircOutExpandValveMolarEnthalpy)
#-----------------------------------
###
# Model constraints
###
#--------------feed------------------
def feedMaterialBalance(m):
    return m.FeedVaporFraction * m.FeedVaporPhaseMolarFrac['Nitrogen'] + (1 - m.FeedVaporFraction) * \
           m.FeedLiquidPhaseMolarFrac['Nitrogen'] \
           - m.FeedMolarFraction['Nitrogen'] == 0
model.feedMaterialBalance = Constraint(rule = feedMaterialBalance)
def FeedVaporComposition(m):
    return m.FeedVaporPhaseMolarFrac['Oxygen'] == vapor_oxygen_composition(m.FeedPressure,m.FeedTemperature)
model.FeedVaporComposition = Constraint(rule = FeedVaporComposition)
def FeedLiquidComposition(m):
    return m.FeedLiquidPhaseMolarFrac['Oxygen'] == liquid_oxygen_composition(m.FeedPressure,m.FeedTemperature)
model.FeedLiquidComposition = Constraint(rule = FeedLiquidComposition)
def feedVaporPhaseSummation(m):
    return sum([m.FeedVaporPhaseMolarFrac[c] for c in m.Component])==1
model.feedVaporPhaseSummation = Constraint(rule = feedVaporPhaseSummation)
def feedLiquidPhaseSummation(m):
    return sum([m.FeedLiquidPhaseMolarFrac[c] for c in m.Component])==1
model.feedLiquidPhaseSummation = Constraint(rule = feedLiquidPhaseSummation)
#-------------column-----------------
def materialBalances(m,tray, comp):
    if tray == model.NumberOfTrays.value:
        if tray == RefluxTray:
            return (m.vaporLeavingMolarFlowCompo[tray - 1, comp] \
                   - m.liquidLeavingMolarFlowCompo[tray, comp] - m.vaporLeavingMolarFlowCompo[tray, comp] \
                   + m.ircRefluxMolarFlow * m.vaporLeavingMolarFraction[model.NumberOfTrays.value, comp])*1e-3 == 0
        else:
            return (m.vaporLeavingMolarFlowCompo[tray - 1, comp] \
                   - m.liquidLeavingMolarFlowCompo[tray, comp] - m.vaporLeavingMolarFlowCompo[tray, comp])*1e-3 == 0
    elif tray == 1:
        if tray == AirFeedTray:
            return (m.liquidLeavingMolarFlowCompo[tray + 1, comp] \
                   - m.liquidLeavingMolarFlowCompo[tray, comp] - m.vaporLeavingMolarFlowCompo[tray, comp] \
                   + m.FeedMolarFlow * m.FeedMolarFraction[comp])*1e-3 == 0
        else:
            return (m.liquidLeavingMolarFlowCompo[tray + 1, comp] \
                   - m.liquidLeavingMolarFlowCompo[tray, comp] - m.vaporLeavingMolarFlowCompo[tray, comp])*1e-3 == 0
    else:
        if tray == RefluxTray:
            return (m.liquidLeavingMolarFlowCompo[tray + 1, comp] + m.vaporLeavingMolarFlowCompo[tray - 1, comp] \
                   - m.liquidLeavingMolarFlowCompo[tray, comp] - m.vaporLeavingMolarFlowCompo[tray, comp]  \
                    + m.ircRefluxMolarFlow * m.vaporLeavingMolarFraction[model.NumberOfTrays.value, comp])*1e-3 == 0
        elif tray == AirFeedTray:
            return (m.liquidLeavingMolarFlowCompo[tray + 1, comp] + m.vaporLeavingMolarFlowCompo[tray - 1, comp] \
                   - m.liquidLeavingMolarFlowCompo[tray, comp] - m.vaporLeavingMolarFlowCompo[tray, comp] \
                   + m.FeedMolarFlow * m.FeedMolarFraction[comp])*1e-3 == 0
        else:
            return (m.liquidLeavingMolarFlowCompo[tray+1, comp] + m.vaporLeavingMolarFlowCompo[tray-1, comp]  \
                   - m.liquidLeavingMolarFlowCompo[tray,comp] - m.vaporLeavingMolarFlowCompo[tray, comp])*1e-3==0
model.columnMaterialBalances = Constraint(model.AllTrays, model.Component, rule=materialBalances)

def energyBalances(m,tray):
    if tray == model.NumberOfTrays.value:
        if tray == RefluxTray:
            return (m.vaporLeavingMolarFlow[tray - 1] * m.vaporLeavingMolarEnthalpy[tray - 1] \
                   - m.liquidLeavingMolarFlow[tray] * m.liquidLeavingMolarEnthalpy[tray] \
                   - m.vaporLeavingMolarFlow[tray] * m.vaporLeavingMolarEnthalpy[tray] \
                   + m.ircRefluxMolarFlow * m.ircCondLiquidMolarEnthalpy)*1e-5 == 0
        else:
            return (m.vaporLeavingMolarFlow[tray - 1] * m.vaporLeavingMolarEnthalpy[tray - 1] \
                   - m.liquidLeavingMolarFlow[tray] * m.liquidLeavingMolarEnthalpy[tray] \
                   - m.vaporLeavingMolarFlow[tray] * m.vaporLeavingMolarEnthalpy[tray])*1e-5 == 0
    elif tray == 1:
        if tray == AirFeedTray:
            return (m.liquidLeavingMolarFlow[tray + 1] * m.liquidLeavingMolarEnthalpy[tray + 1] \
                   - m.liquidLeavingMolarFlow[tray] * m.liquidLeavingMolarEnthalpy[tray] \
                   - m.vaporLeavingMolarFlow[tray] * m.vaporLeavingMolarEnthalpy[tray] \
                   + m.FeedMolarFlow * m.feedEnthalpy)*1e-5 == 0
        else:
            return (m.liquidLeavingMolarFlow[tray + 1] * m.liquidLeavingMolarEnthalpy[tray + 1] \
                   - m.liquidLeavingMolarFlow[tray] * m.liquidLeavingMolarEnthalpy[tray] \
                   - m.vaporLeavingMolarFlow[tray] * m.vaporLeavingMolarEnthalpy[tray])*1e-5 == 0
    else:
        if tray == RefluxTray:
            return (m.liquidLeavingMolarFlow[tray + 1] * m.liquidLeavingMolarEnthalpy[tray + 1] \
                   + m.vaporLeavingMolarFlow[tray - 1] * m.vaporLeavingMolarEnthalpy[tray - 1] \
                   - m.liquidLeavingMolarFlow[tray] * m.liquidLeavingMolarEnthalpy[tray] \
                   - m.vaporLeavingMolarFlow[tray] * m.vaporLeavingMolarEnthalpy[tray] \
                   + m.ircRefluxMolarFlow * m.ircCondLiquidMolarEnthalpy)*1e-5 == 0
        elif tray == AirFeedTray:
            return (m.liquidLeavingMolarFlow[tray + 1] * m.liquidLeavingMolarEnthalpy[tray + 1] \
                   + m.vaporLeavingMolarFlow[tray - 1] * m.vaporLeavingMolarEnthalpy[tray - 1] \
                   - m.liquidLeavingMolarFlow[tray] * m.liquidLeavingMolarEnthalpy[tray] \
                   - m.vaporLeavingMolarFlow[tray] * m.vaporLeavingMolarEnthalpy[tray]\
                    + m.FeedMolarFlow * m.feedEnthalpy)*1e-5 == 0
        else:
            return (m.liquidLeavingMolarFlow[tray+1]*m.liquidLeavingMolarEnthalpy[tray+1]\
                   + m.vaporLeavingMolarFlow[tray-1]*m.vaporLeavingMolarEnthalpy[tray-1]  \
                   - m.liquidLeavingMolarFlow[tray]*m.liquidLeavingMolarEnthalpy[tray]\
                   - m.vaporLeavingMolarFlow[tray]*m.vaporLeavingMolarEnthalpy[tray])*1e-5==0
model.columnEnergyBalances = Constraint(model.AllTrays, rule=energyBalances)

def ColumnLiquidMoleFracNorm(m, tray):
    return sum([m.liquidLeavingMolarFraction[tray, c] for c in m.Component])==1
model.columnLiquidMoleFracNorm = Constraint(model.AllTrays, rule=ColumnLiquidMoleFracNorm)
def ColumnVaporMoleFracNorm(m, tray):
    return sum([m.vaporLeavingMolarFraction[tray, c] for c in m.Component])==1
model.columnVaporMoleFracNorm = Constraint(model.AllTrays, rule=ColumnVaporMoleFracNorm)
def ColumnVaporFraction(m,tray):
    return m.vaporLeavingMolarFraction[tray, 'Oxygen'] == vapor_oxygen_composition(m.trayPressure[tray],m.trayTemperature[tray])
model.ColumnVaporFraction = Constraint(model.AllTrays, rule = ColumnVaporFraction)
def ColumnLiquidFraction(m,tray):
    return m.liquidLeavingMolarFraction[tray, 'Oxygen'] == liquid_oxygen_composition(m.trayPressure[tray],m.trayTemperature[tray])
model.ColumnLiquidFraction = Constraint(model.AllTrays, rule = ColumnLiquidFraction)
def ColumnPressureProfile(m, tray):
    return m.trayPressure[tray] == (ColumnTopPressure-ColumnBottomPressure)/(model.NumberOfTrays.value-1)*(tray-1)+ColumnBottomPressure
model.columnPressureProfile = Constraint(model.AllTrays, rule = ColumnPressureProfile)
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
#-------------IRC Expand Valve-------------------
def ExpandValvePressure(m):
    return (m.trayPressure[1]-m.expandValveDeltaP-m.ircRebPressure)*1e-3 == 0
model.ExpandValvePressure = Constraint(rule=ExpandValvePressure)
def ExpandValveEnthalpy(m):
    return (LiquidPhaseEnthalpy(m.trayTemperature[1], m.trayPressure[1], m.liquidLeavingMolarFraction[1, 'Oxygen'],
                               m.liquidLeavingMolarFraction[1, 'Nitrogen'])- \
                                 model.ircOutExpandValveMolarEnthalpy)*1e-6 ==0
model.ExpandValveEnthalpy = Constraint(rule=ExpandValveEnthalpy)
def EVOutMaterialBalance(m):
    return m.EVOutVaporFraction * m.EVOutVPMolarFrac['Oxygen'] + (1 - m.EVOutVaporFraction) * \
           m.EVOutLPMolarFrac['Oxygen'] \
           - m.liquidLeavingMolarFraction[1, 'Oxygen'] == 0
model.EVOutMaterialBalance = Constraint(rule = EVOutMaterialBalance)
def EVOutVaporComposition(m):
    return m.EVOutVPMolarFrac['Oxygen'] == vapor_oxygen_composition(m.ircRebPressure,m.ircEVOutTemperature)
model.EVOutVaporComposition = Constraint(rule = EVOutVaporComposition)
def EVOutLiquidComposition(m):
    return m.EVOutLPMolarFrac['Oxygen'] == liquid_oxygen_composition(m.ircRebPressure, m.ircEVOutTemperature)
model.EVOutLiquidComposition = Constraint(rule = EVOutLiquidComposition)
def EVOutVaporPhaseSummation(m):
    return sum([m.EVOutVPMolarFrac[c] for c in m.Component])==1
model.EVOutVaporPhaseSummation = Constraint(rule = EVOutVaporPhaseSummation)
def EVOutLiquidPhaseSummation(m):
    return sum([m.EVOutLPMolarFrac[c] for c in m.Component])==1
model.EVOutLiquidPhaseSummation = Constraint(rule = EVOutLiquidPhaseSummation)