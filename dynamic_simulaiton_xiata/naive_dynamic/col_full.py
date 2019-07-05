from pyomo.environ import *
from pyomo.dae import *
from binary_fitting_result import vapor_oxygen_composition,liquid_oxygen_composition,liquid_nitrogen_enthalpy,liquid_oxygen_enthalpy,vapor_nitrogen_enthalpy,vapor_oxygen_enthalpy
import tools

model = ConcreteModel()
#----------单位-----------
#  温度：℃，
#  温差：K
#  压力：kPa
#  物质的量：kmol
#  流量：kmol/h
#  摩尔焓：kJ/kmol
#---------------时间定义---------------
model.time = ContinuousSet(bounds=(0,10)) # Unscaled time
#-------------------------------------------
#       discretilization
#-------------------------------------------
discretizer = TransformationFactory('dae.collocation')
discretizer.apply_to(model, nfe=5, ncp = 3,scheme='LAGRANGE-RADAU')
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
FeedMolarFlow = 2000
FeedPressure = 564
FeedVaporFraction = 0.8
model.FeedMolarFlow = Param(model.time, initialize=FeedMolarFlow)

time_point = model.time.value
dict = {}
for i in time_point:
    dict[i,"Oxygen"] = 0.21
    dict[i,"Nitrogen"] = 0.79
model.FeedMolarFraction = Param(model.time, model.Component,initialize=dict)

model.FeedPressure = Param(model.time, initialize = FeedPressure)
model.FeedVaporFraction = Param(model.time, initialize=FeedVaporFraction)
#--------------IRC指定-----------------
GasDrawRatio = 0.587744831
MinimalTempDiff = 0.1
ircLNProductMolarFlow = 39.9979154
model.expandValveDeltaP = Param(initialize=400)
model.heatTransferConstant = Param(initialize=1736458) #Q=k*\deltaT
model.ircLNProductMolarFlow = Param(model.time,initialize=ircLNProductMolarFlow)

#--------------进料变量定义--------------
model.FeedTemperature = Var(model.time,initialize = -173.9443271855090)
model.FeedVaporPhaseMolarFrac = Var(model.time,model.Component, bounds=(0,1))
model.FeedLiquidPhaseMolarFrac = Var(model.time,model.Component, bounds=(0,1))
tools.set_initials_partial_index(model, "FeedVaporPhaseMolarFrac", [1], {'Oxygen':0.17446238761409605,'Nitrogen':0.825537612385904})
tools.set_initials_partial_index(model, "FeedLiquidPhaseMolarFrac", [1], {'Oxygen':0.3521504495436156,'Nitrogen':0.6478495504563845})

#--------------塔板变量定义--------------
trayTemperature = {1:-173.95468911864418,
          2 : -174.04289794868478,
          3 : -174.15714273889026,
          4 : -174.30720463757226,
          5 : -174.50650197332345,
          6 : -174.77256420660035,
          7 : -175.12661587133596,
          8 : -175.59126550801687,
          9 : -176.18515438692876,
         10 : -176.91425326265394}
model.trayTemperature = Var(model.time,model.AllTrays,bounds=(-230,-100))
tools.set_initials_partial_index(model, "trayTemperature", [1], trayTemperature)
trayPressure = {
        1:  564.0    ,
    2:561.2844444444445,
    3:558.5688888888889,
    4:555.8533333333334,
    5:553.1377777777777,
    6:550.4222222222222,
    7:547.7066666666666,
    8:544.9911111111111,
    9:542.2755555555555,
    10:          539.56
}
model.trayPressure = Var(model.time,model.AllTrays,bounds=(0,1000))
tools.set_initials_partial_index(model, "trayPressure", [1], trayPressure)
vaporLeavingMolarFlow = {
    1: 1599.3390569005921,
2:1598.1857186567934,
3:1596.4669080753486,
4:1593.9721432437116,
5:1590.4338561743114,
6:1585.5422644025891,
7:1578.9940091995832,
8:1570.5888358227262,
9:1560.3677273173848,
10:1519.8375493891103
}
model.vaporLeavingMolarFlow = Var(model.time,model.AllTrays, within=NonNegativeReals)
tools.set_initials_partial_index(model, "vaporLeavingMolarFlow", [1], vaporLeavingMolarFlow)
liquidLeavingMolarFlow=   {1 :1066.7254209868436,
  2 : 666.0644778874357,
  3 :  664.911139643637,
  4 : 663.1923290621919,
  5 : 660.6975642305553,
  6 : 657.1592771611548,
  7 : 652.2676853894326,
  8 : 645.7194301864266,
  9 : 637.3142568095694,
 10 :  627.093148304228
}
model.liquidLeavingMolarFlow = Var(model.time,model.AllTrays, within=NonNegativeReals)
tools.set_initials_partial_index(model, "liquidLeavingMolarFlow", [1], liquidLeavingMolarFlow)
vaporLeavingMolarFraction = {
(1, 'Nitrogen') :  0.8261041411615242,
  (1, 'Oxygen') :  0.1738958588384758,
(2, 'Nitrogen') :    0.82787963124624,
  (2, 'Oxygen') : 0.17212036875376016,
(3, 'Nitrogen') :  0.8310104179728867,
  (3, 'Oxygen') : 0.16898958202711337,
(4, 'Nitrogen') :  0.8360237061799887,
  (4, 'Oxygen') : 0.16397629382001136,
(5, 'Nitrogen') :  0.8436263429508646,
  (5, 'Oxygen') : 0.15637365704913544,
(6, 'Nitrogen') :  0.8547101991352113,
  (6, 'Oxygen') : 0.14528980086478877,
(7, 'Nitrogen') :  0.8702949089656328,
  (7, 'Oxygen') : 0.12970509103436725,
(8, 'Nitrogen') :  0.8913547111786565,
  (8, 'Oxygen') : 0.10864528882134354,
(9, 'Nitrogen') :  0.9184872706799356,
  (9, 'Oxygen') : 0.08151272932006437,
(10, 'Nitrogen') :  0.9514604305969547,
 (10, 'Oxygen') : 0.04853956940304518
}
model.vaporLeavingMolarFraction = Var(model.time,model.AllTrays, model.Component, bounds=(0,1))
tools.set_initials_partial_index(model, "vaporLeavingMolarFraction", [1,2], vaporLeavingMolarFraction)
liquidLeavingMolarFraction = {
 (1, 'Nitrogen') : 0.6487387977936688,
   (1, 'Oxygen') : 0.3512612022063311,
 (2, 'Nitrogen') : 0.6504577253361858,
   (2, 'Oxygen') : 0.3495422746638142,
 (3, 'Nitrogen') : 0.6544206355826032,
   (3, 'Oxygen') : 0.3455793644173969,
 (4, 'Nitrogen') : 0.6615076509809633,
   (4, 'Oxygen') :0.33849234901903674,
 (5, 'Nitrogen') : 0.6729624717884669,
   (5, 'Oxygen') : 0.3270375282115332,
 (6, 'Nitrogen') : 0.6904841501084793,
   (6, 'Oxygen') : 0.3095158498915207,
 (7, 'Nitrogen') : 0.7162784884136001,
   (7, 'Oxygen') :0.28372151158639985,
 (8, 'Nitrogen') : 0.7529843333662811,
   (8, 'Oxygen') : 0.2470156666337188,
 (9, 'Nitrogen') : 0.8033366896342916,
   (9, 'Oxygen') :0.19666331036570847,
(10, 'Nitrogen') : 0.8694147971191808,
  (10, 'Oxygen') :0.13058520288081915
}
model.liquidLeavingMolarFraction = Var(model.time,model.AllTrays, model.Component, bounds=(0,1))
tools.set_initials_partial_index(model, "liquidLeavingMolarFraction", [1,2], liquidLeavingMolarFraction)

def vaporLeavingMolarFlowCompo(m,t,tray, comp):
    return m.vaporLeavingMolarFraction[t,tray,comp]*m.vaporLeavingMolarFlow[t,tray]
model.vaporLeavingMolarFlowCompo = Expression(model.time,model.AllTrays, model.Component,rule=vaporLeavingMolarFlowCompo)
def liquidLeavingMolarFlowCompo(m,t,tray, comp):
    return m.liquidLeavingMolarFraction[t,tray,comp]*m.liquidLeavingMolarFlow[t,tray]
model.liquidLeavingMolarFlowCompo = Expression(model.time,model.AllTrays, model.Component, rule=liquidLeavingMolarFlowCompo)
#-------------IRC变量定义---------------
model.ircWasteMolarFlow=Var(model.time,initialize=762.8130470360793)
model.ircGNProductMolarFlow=Var(model.time,within=NonNegativeReals,initialize=960)
model.ircTopTrayVaporMolarFlow=Var(model.time,within=NonNegativeReals,initialize=1633)
model.ircDrainMolarFlow=Var(model.time,within=NonNegativeReals,initialize=274)
model.ircBottomLiquidMolarFlow=Var(model.time,within=NonNegativeReals,initialize=1000)
model.ircRefluxMolarFlow=Var(model.time,within=NonNegativeReals,initialize=633)
model.ircCondTemperature=Var(model.time,bounds=(-230,-100),initialize=-186.348)
model.ircCondPressure=Var(model.time,bounds=(0,1000),initialize=164)
model.ircRebTemperature=Var(model.time,bounds=(-230,-100),initialize=-188.314)
model.ircRebPressure=Var(model.time,bounds=(0,1000),initialize=564-model.expandValveDeltaP.value)
model.ircHeatExchange=Var(model.time,within=NonNegativeReals,initialize=3.413876e6)
model.ircDrainMolarFraction=Var(model.time,model.Component,bounds=(0,1))
model.ircWNMolarFraction=Var(model.time,model.Component,bounds=(0,1))
tools.set_initials_partial_index(model, "ircDrainMolarFraction", [1], {"Nitrogen":0.4397329326864435,"Oxygen":0.5602670673135565})
tools.set_initials_partial_index(model, "ircWNMolarFraction", [1], {"Nitrogen":0.7320088321502859,"Oxygen":0.26799116784971416})

#--------------膨胀阀变量定义---------------
model.EVOutVPMolarFrac = Var(model.time,model.Component, bounds=(0,1))
model.EVOutLPMolarFrac = Var(model.time,model.Component, bounds=(0,1))
model.EVOutVaporFraction = Var(model.time,initialize=0.14, bounds=(0,0.3))
model.ircEVOutTemperature = Var(model.time,initialize=-188.314, bounds = (-200,-170))
tools.set_initials_partial_index(model, "EVOutVPMolarFrac", [1], {'Oxygen':0.11858191339664961,'Nitrogen':0.8814180866033504})
tools.set_initials_partial_index(model, "EVOutLPMolarFrac", [1], {'Oxygen':0.32213092774934615,'Nitrogen':0.6778690722506538})
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
def _feedEnthalpy(m,t):
    return (1-m.FeedVaporFraction[t])*LiquidPhaseEnthalpy(m.FeedTemperature[t],m.FeedPressure[t],m.FeedLiquidPhaseMolarFrac[t,'Oxygen'],m.FeedLiquidPhaseMolarFrac[t,'Nitrogen'])\
        +m.FeedVaporFraction[t]*VaporPhaseEnthalpy(m.FeedTemperature[t],m.FeedPressure[t],m.FeedVaporPhaseMolarFrac[t,'Oxygen'],m.FeedVaporPhaseMolarFrac[t,'Nitrogen'])
model.feedEnthalpy = Expression(model.time,rule= _feedEnthalpy)
#-----------------下塔------------------
def _liquidLeavingMolarEnthalpy(m, t,tray):
    return LiquidPhaseEnthalpy(m.trayTemperature[t,tray], m.trayPressure[t,tray], m.liquidLeavingMolarFraction[t,tray,'Oxygen'],\
                               m.liquidLeavingMolarFraction[t,tray,'Nitrogen'])
model.liquidLeavingMolarEnthalpy = Expression(model.time, model.AllTrays, rule=_liquidLeavingMolarEnthalpy)
def _vaporLeavingMolarEnthalpy(m, t,tray):
    return VaporPhaseEnthalpy(m.trayTemperature[t,tray], m.trayPressure[t,tray],\
                               m.vaporLeavingMolarFraction[t,tray, 'Oxygen'],\
                               m.vaporLeavingMolarFraction[t,tray, 'Nitrogen'])
model.vaporLeavingMolarEnthalpy = Expression(model.time, model.AllTrays, rule=_vaporLeavingMolarEnthalpy)
#----------------------------------------
###
# Enthalpy expression
###
#------------------IRC------------------
def _ircTopTrayVaporMolarEnthalpy(m,t):
    return VaporPhaseEnthalpy(m.trayTemperature[t,m.NumberOfTrays.value], m.trayPressure[t,m.NumberOfTrays.value], m.vaporLeavingMolarFraction[t,m.NumberOfTrays.value,'Oxygen'],
                              m.vaporLeavingMolarFraction[t,m.NumberOfTrays.value,'Nitrogen'])
model.ircTopTrayVaporMolarEnthalpy = Expression(model.time, rule=_ircTopTrayVaporMolarEnthalpy)
def _ircCondLiquidMolarEnthalpy(m,t):
    return LiquidPhaseEnthalpy(m.ircCondTemperature[t], m.ircCondPressure[t], m.vaporLeavingMolarFraction[t,m.NumberOfTrays.value,'Oxygen'],
                               m.vaporLeavingMolarFraction[t,m.NumberOfTrays.value,'Nitrogen'])
model.ircCondLiquidMolarEnthalpy = Expression(model.time, rule=_ircCondLiquidMolarEnthalpy)
def _ircDrainMolarEnthalpy(m,t):
    return LiquidPhaseEnthalpy(m.ircRebTemperature[t], m.ircRebPressure[t], m.ircDrainMolarFraction[t,'Oxygen'],
                               m.ircDrainMolarFraction[t,'Nitrogen'])
model.ircDrainMolarEnthalpy = Expression(model.time, rule=_ircDrainMolarEnthalpy)
def _ircWNMolarEnthalpy(m,t):
    return VaporPhaseEnthalpy(m.ircRebTemperature[t], m.ircRebPressure[t], m.ircWNMolarFraction[t,'Oxygen'],
                              m.ircWNMolarFraction[t,'Nitrogen'])
model.ircWNMolarEnthalpy = Expression(model.time, rule=_ircWNMolarEnthalpy)
#--------------IRC Expand Valve-----------------------
def _ircOutExpandValveMolarEnthalpy(m,t):
    return LiquidPhaseEnthalpy(m.ircEVOutTemperature[t], m.ircRebPressure[t], m.EVOutLPMolarFrac[t,'Oxygen'],
                               m.EVOutLPMolarFrac[t,'Nitrogen'])*(1-m.EVOutVaporFraction[t])+\
VaporPhaseEnthalpy(m.ircEVOutTemperature[t], m.ircRebPressure[t], m.EVOutVPMolarFrac[t,'Oxygen'],
                               m.EVOutVPMolarFrac[t,'Nitrogen'])*m.EVOutVaporFraction[t]
model.ircOutExpandValveMolarEnthalpy = Expression(model.time, rule=_ircOutExpandValveMolarEnthalpy)
#-----------------------------------
###
# Model constraints
###
#--------------feed------------------
def feedMaterialBalance(m,t):
    return m.FeedVaporFraction[t] * m.FeedVaporPhaseMolarFrac[t,'Nitrogen'] + (1 - m.FeedVaporFraction[t]) * \
           m.FeedLiquidPhaseMolarFrac[t,'Nitrogen'] \
           - m.FeedMolarFraction[t,'Nitrogen'] == 0
model.feedMaterialBalance = Constraint(model.time, rule = feedMaterialBalance)
def FeedVaporComposition(m,t):
    return m.FeedVaporPhaseMolarFrac[t,'Oxygen'] == vapor_oxygen_composition(m.FeedPressure[t],m.FeedTemperature[t])
model.FeedVaporComposition = Constraint(model.time, rule = FeedVaporComposition)
def FeedLiquidComposition(m,t):
    return m.FeedLiquidPhaseMolarFrac[t,'Oxygen'] == liquid_oxygen_composition(m.FeedPressure[t],m.FeedTemperature[t])
model.FeedLiquidComposition = Constraint(model.time, rule = FeedLiquidComposition)
def feedVaporPhaseSummation(m,t):
    return sum([m.FeedVaporPhaseMolarFrac[t,c] for c in m.Component])==1
model.feedVaporPhaseSummation = Constraint(model.time, rule = feedVaporPhaseSummation)
def feedLiquidPhaseSummation(m,t):
    return sum([m.FeedLiquidPhaseMolarFrac[t,c] for c in m.Component])==1
model.feedLiquidPhaseSummation = Constraint(model.time, rule = feedLiquidPhaseSummation)
#-------------column-----------------
def materialBalances(m,t,tray, comp):
    if tray == model.NumberOfTrays.value:
        if tray == RefluxTray:
            return (m.vaporLeavingMolarFlowCompo[t,tray - 1, comp] \
                   - m.liquidLeavingMolarFlowCompo[t,tray, comp] - m.vaporLeavingMolarFlowCompo[t,tray, comp] \
                   + m.ircRefluxMolarFlow[t] * m.vaporLeavingMolarFraction[t,model.NumberOfTrays.value, comp])*1e-3 == 0
        else:
            return (m.vaporLeavingMolarFlowCompo[t,tray - 1, comp] \
                   - m.liquidLeavingMolarFlowCompo[t,tray, comp] - m.vaporLeavingMolarFlowCompo[t,tray, comp])*1e-3 == 0
    elif tray == 1:
        if tray == AirFeedTray:
            return (m.liquidLeavingMolarFlowCompo[t,tray + 1, comp] \
                   - m.liquidLeavingMolarFlowCompo[t,tray, comp] - m.vaporLeavingMolarFlowCompo[t,tray, comp] \
                   + m.FeedMolarFlow[t] * m.FeedMolarFraction[t,comp])*1e-3 == 0
        else:
            return (m.liquidLeavingMolarFlowCompo[t,tray + 1, comp] \
                   - m.liquidLeavingMolarFlowCompo[t,tray, comp] - m.vaporLeavingMolarFlowCompo[t,tray, comp])*1e-3 == 0
    else:
        if tray == RefluxTray:
            return (m.liquidLeavingMolarFlowCompo[t,tray + 1, comp] + m.vaporLeavingMolarFlowCompo[t,tray - 1, comp] \
                   - m.liquidLeavingMolarFlowCompo[t,tray, comp] - m.vaporLeavingMolarFlowCompo[t,tray, comp]  \
                    + m.ircRefluxMolarFlow[t] * m.vaporLeavingMolarFraction[t,model.NumberOfTrays.value, comp])*1e-3 == 0
        elif tray == AirFeedTray:
            return (m.liquidLeavingMolarFlowCompo[t,tray + 1, comp] + m.vaporLeavingMolarFlowCompo[t,tray - 1, comp] \
                   - m.liquidLeavingMolarFlowCompo[t,tray, comp] - m.vaporLeavingMolarFlowCompo[t,tray, comp] \
                   + m.FeedMolarFlow[t] * m.FeedMolarFraction[t,comp])*1e-3 == 0
        else:
            return (m.liquidLeavingMolarFlowCompo[t,tray+1, comp] + m.vaporLeavingMolarFlowCompo[t,tray-1, comp]  \
                   - m.liquidLeavingMolarFlowCompo[t,tray,comp] - m.vaporLeavingMolarFlowCompo[t,tray, comp])*1e-3==0
model.columnMaterialBalances = Constraint(model.time,model.AllTrays, model.Component, rule=materialBalances)

def energyBalances(m,t, tray):
    if tray == model.NumberOfTrays.value:
        if tray == RefluxTray:
            return (m.vaporLeavingMolarFlow[t,tray - 1] * m.vaporLeavingMolarEnthalpy[t,tray - 1] \
                   - m.liquidLeavingMolarFlow[t,tray] * m.liquidLeavingMolarEnthalpy[t,tray] \
                   - m.vaporLeavingMolarFlow[t,tray] * m.vaporLeavingMolarEnthalpy[t,tray] \
                   + m.ircRefluxMolarFlow[t] * m.ircCondLiquidMolarEnthalpy[t])*1e-5 == 0
        else:
            return (m.vaporLeavingMolarFlow[t,tray - 1] * m.vaporLeavingMolarEnthalpy[t,tray - 1] \
                   - m.liquidLeavingMolarFlow[t,tray] * m.liquidLeavingMolarEnthalpy[t,tray] \
                   - m.vaporLeavingMolarFlow[t,tray] * m.vaporLeavingMolarEnthalpy[t,tray])*1e-5 == 0
    elif tray == 1:
        if tray == AirFeedTray:
            return (m.liquidLeavingMolarFlow[t,tray + 1] * m.liquidLeavingMolarEnthalpy[t,tray + 1] \
                   - m.liquidLeavingMolarFlow[t,tray] * m.liquidLeavingMolarEnthalpy[t,tray] \
                   - m.vaporLeavingMolarFlow[t,tray] * m.vaporLeavingMolarEnthalpy[t,tray] \
                   + m.FeedMolarFlow[t] * m.feedEnthalpy[t])*1e-5 == 0
        else:
            return (m.liquidLeavingMolarFlow[t,tray + 1] * m.liquidLeavingMolarEnthalpy[t,tray + 1] \
                   - m.liquidLeavingMolarFlow[t,tray] * m.liquidLeavingMolarEnthalpy[t,tray] \
                   - m.vaporLeavingMolarFlow[t,tray] * m.vaporLeavingMolarEnthalpy[t,tray])*1e-5 == 0
    else:
        if tray == RefluxTray:
            return (m.liquidLeavingMolarFlow[t,tray + 1] * m.liquidLeavingMolarEnthalpy[t,tray + 1] \
                   + m.vaporLeavingMolarFlow[t,tray - 1] * m.vaporLeavingMolarEnthalpy[t,tray - 1] \
                   - m.liquidLeavingMolarFlow[t,tray] * m.liquidLeavingMolarEnthalpy[t,tray] \
                   - m.vaporLeavingMolarFlow[t,tray] * m.vaporLeavingMolarEnthalpy[t,tray] \
                   + m.ircRefluxMolarFlow[t] * m.ircCondLiquidMolarEnthalpy[t])*1e-5 == 0
        elif tray == AirFeedTray:
            return (m.liquidLeavingMolarFlow[t,tray + 1] * m.liquidLeavingMolarEnthalpy[t,tray + 1] \
                   + m.vaporLeavingMolarFlow[t,tray - 1] * m.vaporLeavingMolarEnthalpy[t,tray - 1] \
                   - m.liquidLeavingMolarFlow[t,tray] * m.liquidLeavingMolarEnthalpy[t,tray] \
                   - m.vaporLeavingMolarFlow[t,tray] * m.vaporLeavingMolarEnthalpy[t,tray]\
                    + m.FeedMolarFlow[t] * m.feedEnthalpy[t])*1e-5 == 0
        else:
            return (m.liquidLeavingMolarFlow[t,tray+1]*m.liquidLeavingMolarEnthalpy[t,tray+1]\
                   + m.vaporLeavingMolarFlow[t,tray-1]*m.vaporLeavingMolarEnthalpy[t,tray-1]  \
                   - m.liquidLeavingMolarFlow[t,tray]*m.liquidLeavingMolarEnthalpy[t,tray]\
                   - m.vaporLeavingMolarFlow[t,tray]*m.vaporLeavingMolarEnthalpy[t,tray])*1e-5==0
model.columnEnergyBalances = Constraint(model.time, model.AllTrays, rule=energyBalances)

def ColumnLiquidMoleFracNorm(m, t, tray):
    return sum([m.liquidLeavingMolarFraction[t,tray, c] for c in m.Component])==1
model.columnLiquidMoleFracNorm = Constraint(model.time, model.AllTrays, rule=ColumnLiquidMoleFracNorm)
def ColumnVaporMoleFracNorm(m, t, tray):
    return sum([m.vaporLeavingMolarFraction[t,tray, c] for c in m.Component])==1
model.columnVaporMoleFracNorm = Constraint(model.time, model.AllTrays, rule=ColumnVaporMoleFracNorm)
def ColumnVaporFraction(m,t, tray):
    return m.vaporLeavingMolarFraction[t,tray, 'Oxygen'] == vapor_oxygen_composition(m.trayPressure[t,tray],m.trayTemperature[t,tray])
model.ColumnVaporFraction = Constraint(model.time, model.AllTrays, rule = ColumnVaporFraction)
def ColumnLiquidFraction(m,t, tray):
    return m.liquidLeavingMolarFraction[t,tray, 'Oxygen'] == liquid_oxygen_composition(m.trayPressure[t,tray],m.trayTemperature[t,tray])
model.ColumnLiquidFraction = Constraint(model.time, model.AllTrays, rule = ColumnLiquidFraction)
def ColumnPressureProfile(m, t, tray):
    return m.trayPressure[t,tray] == (ColumnTopPressure-ColumnBottomPressure)/(model.NumberOfTrays.value-1)*(tray-1)+ColumnBottomPressure
model.columnPressureProfile = Constraint(model.time, model.AllTrays, rule = ColumnPressureProfile)
#-----------------------------------
###
# Model constraints
###
#-------------IRC Condenser Side-----------------
def ITopTrayVaporMolarFlow(m,t):
    return (m.vaporLeavingMolarFlow[t, m.NumberOfTrays.value] - m.ircTopTrayVaporMolarFlow[t])*1e-3 ==0
model.ITopTrayVaporMolarFlow =  Constraint(model.time, rule = ITopTrayVaporMolarFlow)
def ICondPressure(m,t):
    return (m.trayPressure[t,m.NumberOfTrays.value] - m.ircCondPressure[t])*1e-3 == 0
model.ICondPressure = Constraint(model.time, rule=ICondPressure)
def deriveGNProductMolarFlow(m,t):
    return (m.ircGNProductMolarFlow[t] - GasDrawRatio * m.ircTopTrayVaporMolarFlow[t])*1e-3 == 0
model.deriveGNProductMolarFlow = Constraint(model.time, rule = deriveGNProductMolarFlow)
def IRCCondMaterialBalance(m,t):
    return (m.ircTopTrayVaporMolarFlow[t]*(1-GasDrawRatio)-m.ircLNProductMolarFlow[t]-m.ircRefluxMolarFlow[t])*1e-3==0
model.ircCondMaterialBalance = Constraint(model.time, rule = IRCCondMaterialBalance)
def IRCCondEnergyBalance(m,t):
    return (m.ircTopTrayVaporMolarFlow[t]*(1-GasDrawRatio)*m.ircTopTrayVaporMolarEnthalpy[t] \
           -(m.ircLNProductMolarFlow[t]+m.ircRefluxMolarFlow[t])*m.ircCondLiquidMolarEnthalpy[t] - m.ircHeatExchange[t])*1e-5==0
model.ircCondEnergyBalance = Constraint(model.time, rule = IRCCondEnergyBalance)
#-------------IRC Reboiler Side-----------------
def IBottomLiquidMolarFlow(m,t):
    return (m.liquidLeavingMolarFlow[t,1] - m.ircBottomLiquidMolarFlow[t])*1e-3 ==0
model.IBottomLiquidMolarFlow =  Constraint(model.time,rule = IBottomLiquidMolarFlow)
def IRCRebMaterialBalance(m,t, comp):
    return (m.ircBottomLiquidMolarFlow[t]*m.liquidLeavingMolarFraction[t,1,comp]\
        - m.ircWasteMolarFlow[t]*m.ircWNMolarFraction[t,comp]\
        - m.ircDrainMolarFlow[t]*m.ircDrainMolarFraction[t,comp])*1e-3 == 0
model.ircRebMaterialBalance = Constraint(model.time,model.Component, rule = IRCRebMaterialBalance)
def IRCRebEnergyBalance(m,t):
    return (m.ircBottomLiquidMolarFlow[t]*m.ircOutExpandValveMolarEnthalpy[t]+m.ircHeatExchange[t]\
        -m.ircWasteMolarFlow[t] *m.ircWNMolarEnthalpy[t]-m.ircDrainMolarFlow[t]*m.ircDrainMolarEnthalpy[t])*1e-5==0
model.ircRebEnergyBalance = Constraint(model.time,rule=IRCRebEnergyBalance)
def IRCRebWNSummation(m,t):
    return sum([m.ircWNMolarFraction[t,c] for c in m.Component]) == 1
model.IRCRebWNSummation = Constraint(model.time,rule=IRCRebWNSummation)
def IRCRebDrainSummation(m,t):
    return sum([m.ircDrainMolarFraction[t,c] for c in m.Component]) == 1
model.IRCRebDrainSummation = Constraint(model.time,rule=IRCRebDrainSummation)
def rebVaporComposition(m,t):
    return m.ircWNMolarFraction[t,'Oxygen'] == vapor_oxygen_composition(m.ircRebPressure[t],m.ircRebTemperature[t])
model.rebVaporComposition = Constraint(model.time,rule = rebVaporComposition)
def rebLiquidComposition(m,t):
    return m.ircDrainMolarFraction[t,'Oxygen'] == liquid_oxygen_composition(m.ircRebPressure[t],m.ircRebTemperature[t])
model.rebLiquidComposition = Constraint(model.time,rule = rebLiquidComposition)
#-------------IRC Heat Transfer-----------------
def IRCTempDiff(m,t):
    return (m.ircCondTemperature[t]-m.ircRebTemperature[t]-MinimalTempDiff)*1e-2>=0
model.ircTempDiff = Constraint(model.time,rule=IRCTempDiff)
def IRCHeatTransfer(m,t):
    return ((m.ircCondTemperature[t]-m.ircRebTemperature[t])*m.heatTransferConstant-m.ircHeatExchange[t])*1e-6==0
model.IRCHeatTransfer = Constraint(model.time,rule=IRCHeatTransfer)
#-------------IRC Expand Valve-------------------
def ExpandValvePressure(m,t):
    return (m.trayPressure[t,1]-m.expandValveDeltaP-m.ircRebPressure[t])*1e-3 == 0
model.ExpandValvePressure = Constraint(model.time,rule=ExpandValvePressure)
def ExpandValveEnthalpy(m,t):
    return (LiquidPhaseEnthalpy(m.trayTemperature[t,1], m.trayPressure[t,1], m.liquidLeavingMolarFraction[t,1, 'Oxygen'],
                               m.liquidLeavingMolarFraction[t,1, 'Nitrogen'])- \
                                 model.ircOutExpandValveMolarEnthalpy[t])*1e-5 ==0
model.ExpandValveEnthalpy = Constraint(model.time,rule=ExpandValveEnthalpy)
def EVOutMaterialBalance(m,t):
    return m.EVOutVaporFraction[t] * m.EVOutVPMolarFrac[t,'Oxygen'] + (1 - m.EVOutVaporFraction[t]) * \
           m.EVOutLPMolarFrac[t,'Oxygen'] \
           - m.liquidLeavingMolarFraction[t,1, 'Oxygen'] == 0
model.EVOutMaterialBalance = Constraint(model.time,rule = EVOutMaterialBalance)
def EVOutVaporComposition(m,t):
    return m.EVOutVPMolarFrac[t,'Oxygen'] == vapor_oxygen_composition(m.ircRebPressure[t],m.ircEVOutTemperature[t])
model.EVOutVaporComposition = Constraint(model.time,rule = EVOutVaporComposition)
def EVOutLiquidComposition(m,t):
    return m.EVOutLPMolarFrac[t,'Oxygen'] == liquid_oxygen_composition(m.ircRebPressure[t], m.ircEVOutTemperature[t])
model.EVOutLiquidComposition = Constraint(model.time,rule = EVOutLiquidComposition)
def EVOutVaporPhaseSummation(m,t):
    return sum([m.EVOutVPMolarFrac[t,c] for c in m.Component])==1
model.EVOutVaporPhaseSummation = Constraint(model.time,rule = EVOutVaporPhaseSummation)
def EVOutLiquidPhaseSummation(m,t):
    return sum([m.EVOutLPMolarFrac[t,c] for c in m.Component])==1
model.EVOutLiquidPhaseSummation = Constraint(model.time,rule = EVOutLiquidPhaseSummation)