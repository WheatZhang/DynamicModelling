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
#--------------塔设备指定--------------
NumberOfTrays = 5
AirFeedTray = 1
RefluxTray = NumberOfTrays
ColumnTopPressure = 539.56
ColumnBottomPressure = 564
model.AllTrays = RangeSet(1, NumberOfTrays) # 10块塔板，下面为1
model.feedEnthalpy = Var(initialize=0)
#--------------进料指定----------------
model.FeedMolarFlow = Param(initialize=2000)
model.FeedMolarFraction = Param(model.Component, initialize={'Oxygen':0.21,'Nitrogen':0.79})
model.FeedTemperature = Var(initialize = -174.0013876)
model.FeedPressure = Param(initialize = 564)
model.FeedVaporFraction = Param(initialize=0.8)
#--------------进料变量定义--------------
model.FeedVaporPhaseMolarFrac = Var(model.Component, bounds=(0,1), initialize={'Oxygen':0.17529771144636974,'Nitrogen':0.8247022885536303})
model.FeedLiquidPhaseMolarFrac = Var(model.Component, bounds=(0,1), initialize={'Oxygen':0.34880915421452136,'Nitrogen':0.6511908457854787})
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
def _feedEnthalpy(m):
    return m.feedEnthalpy == (1-m.FeedVaporFraction)*LiquidPhaseEnthalpy(m.FeedTemperature,m.FeedPressure,m.FeedLiquidPhaseMolarFrac['Oxygen'],m.FeedLiquidPhaseMolarFrac['Nitrogen'])\
        +m.FeedVaporFraction*VaporPhaseEnthalpy(m.FeedTemperature,m.FeedPressure,m.FeedVaporPhaseMolarFrac['Oxygen'],m.FeedVaporPhaseMolarFrac['Nitrogen'])
model.DfeedEnthalpy = Constraint(rule= _feedEnthalpy)

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

