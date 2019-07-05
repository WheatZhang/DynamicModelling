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
#--------------进料指定----------------
model.FeedMolarFlow = Param(initialize=2000)
model.FeedMolarFraction = Param(model.Component, initialize={'Oxygen':0.21,'Nitrogen':0.79})
model.FeedTemperature = Param(initialize = -174.0013876)
model.FeedPressure = Param(initialize = 564)
#--------------VLE热力学指定----------------
model.feedEquilConstantRatio = Param(initialize=0.5/1.26)
#--------------进料变量定义--------------
model.FeedVaporFraction = Param(initialize=0.8)
model.FeedVaporPhaseMolarFrac = Var(model.Component, bounds=(0,1), initialize={'Oxigen':0.18,'Nitrogen':0.82})
model.FeedLiquidPhaseMolarFrac = Var(model.Component, bounds=(0,1), initialize={'Oxigen':0.35,'Nitrogen':0.65})
# model.FeedVaporPhaseMolarFrac = Var(model.Component, bounds=(0,1), initialize={'Oxigen':0.21,'Nitrogen':0.79})
# model.FeedLiquidPhaseMolarFrac = Var(model.Component, bounds=(0,1), initialize={'Oxigen':0.21,'Nitrogen':0.79})
# 之前少定义了这个变量
feed_ec = {}
for c in model.Component:
    if c == 'Oxygen':
        feed_ec[c] = 0.4
    elif c=='Nitrogen':
        feed_ec[c] = 1.334
model.feedEquilibriumConstant = Var(model.Component,initialize=feed_ec )

#----------------------------------------
#     焓的热力学
#----------------------------------------
def LiquidPhaseEnthalpy(temperature, pressure, oxygen, nitrogen):
    return (8917.884 + (temperature - (-173)) * 418.68 + (pressure - 250) *-18.31725) * oxygen \
           + (3893.724 + (temperature - (-173)) * 418.68 + (pressure - 770) *-18.31725) * nitrogen
def VaporPhaseEnthalpy(temperature, pressure, oxygen, nitrogen):
    return (15407.424 + (temperature - (-173)) * 558.24 + (pressure - 250) * -19.43871429) * oxygen \
           + (8457.336 + (temperature - (-173)) * 558.24 + (pressure - 770) * -19.43871429) * nitrogen
#----------------------------------------
###
# Enthalpy expression
###
#-----------------进料------------------
def _feedEnthalpy(m):
    return LiquidPhaseEnthalpy(m.FeedTemperature,m.FeedPressure,m.FeedLiquidPhaseMolarFrac['Oxygen'],m.FeedLiquidPhaseMolarFrac['Nitrogen'])\
        +VaporPhaseEnthalpy(m.FeedTemperature,m.FeedPressure,m.FeedVaporPhaseMolarFrac['Oxygen'],m.FeedVaporPhaseMolarFrac['Nitrogen'])
model.feedEnthalpy = Expression(rule = _feedEnthalpy)

###                             
# Model constraints
###
#--------------feed------------------
def feedMaterialBalance(m):
    return m.FeedVaporFraction*m.FeedVaporPhaseMolarFrac['Nitrogen'] +(1-m.FeedVaporFraction)*m.FeedLiquidPhaseMolarFrac['Nitrogen']\
           == m.FeedMolarFraction['Nitrogen']
model.feedMaterialBalance = Constraint(rule = feedMaterialBalance)
# 之前缺少了Equalibrium
def feedEquilibrium(m):
    return m.feedEquilibriumConstant['Oxygen'] == m.feedEquilibriumConstant['Nitrogen'] * m.feedEquilConstantRatio
model.feedEquilibrium = Constraint(rule = feedEquilibrium)
def feedVLE(m, comp):
    return m.FeedVaporPhaseMolarFrac[comp] == m.FeedLiquidPhaseMolarFrac[comp] *m.feedEquilibriumConstant[comp]
model.feedVLE = Constraint(model.Component, rule = feedVLE)
# 进料之前缺少summation
def feedVaporPhaseSummation(m):
    return sum([m.FeedVaporPhaseMolarFrac[c] for c in m.Component])==1
model.feedVaporPhaseSummation = Constraint(rule = feedVaporPhaseSummation)
def feedLiquidPhaseSummation(m):
    return sum([m.FeedLiquidPhaseMolarFrac[c] for c in m.Component])==1
model.feedLiquidPhaseSummation = Constraint(rule = feedLiquidPhaseSummation)
