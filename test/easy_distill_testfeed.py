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
#--------------塔设备指定--------------
NumberOfTrays = 5
AirFeedTray = 1
RefluxTray = NumberOfTrays
#--------------塔板变量定义--------------
model.AllTrays = RangeSet(1, NumberOfTrays) # 10块塔板，下面为1
#--------------进料指定----------------
model.FeedMolarFlow = Param(initialize=2000)
model.FeedMolarFraction = Param(model.Component, initialize={'Oxygen':0.21,'Nitrogen':0.79})
model.FeedVaporFraction = Param(initialize=0.8)
# 加入bound是必要的，否则不能收敛到一个合理的结果
#--------------进料变量定义--------------
# model.FeedVaporFraction = Var(bounds=(0,1),initialize=0.8)
model.FeedVaporPhaseMolarFrac = Var(model.Component, bounds=(0,1), initialize={'Oxigen':0.18,'Nitrogen':0.82})
model.FeedLiquidPhaseMolarFrac = Var(model.Component, bounds=(0,1), initialize={'Oxigen':0.35,'Nitrogen':0.65})
model.feedEquilConstantRatio = Param(initialize=0.5/1.266)
# 之前少定义了这个变量
feed_ec = {}
for c in model.Component:
    if c == 'Oxygen':
        feed_ec[c] = 0.502560524364477
    elif c=='Nitrogen':
        feed_ec[c] = 1.266452521398482
model.feedEquilibriumConstant = Var(model.Component,initialize=feed_ec )
#-----------------------------------
###                             
# Model constraints
###
#--------------feed------------------
#注意这里的质量守恒只能有一个
def feedMaterialBalance(m):
    return m.FeedVaporFraction*m.FeedVaporPhaseMolarFrac['Nitrogen'] +(1-m.FeedVaporFraction)*m.FeedLiquidPhaseMolarFrac['Nitrogen']\
           - m.FeedMolarFraction['Nitrogen'] == 0
model.feedMaterialBalance = Constraint(rule = feedMaterialBalance)
def feedVaporPhaseSummation(m):
    return sum([m.FeedVaporPhaseMolarFrac[c] for c in m.Component])==1
model.feedVaporPhaseSummation = Constraint(rule = feedVaporPhaseSummation)
def feedLiquidPhaseSummation(m):
    return sum([m.FeedLiquidPhaseMolarFrac[c] for c in m.Component])==1
model.feedLiquidPhaseSummation = Constraint(rule = feedLiquidPhaseSummation)
def feedEquilibrium(m):
    return m.feedEquilibriumConstant['Oxygen'] == m.feedEquilibriumConstant['Nitrogen'] * m.feedEquilConstantRatio
model.feedEquilibrium = Constraint(rule = feedEquilibrium)
def feedVLE(m, comp):
    return m.FeedVaporPhaseMolarFrac[comp] == m.FeedLiquidPhaseMolarFrac[comp] *m.feedEquilibriumConstant[comp]
model.feedVLE = Constraint(model.Component, rule = feedVLE)

def obj_rule(m):
    return 1
model.OBJ = Objective(rule=obj_rule)
solver=SolverFactory('ipopt')
results = solver.solve(model,tee=True)
with open('easy_distill_testfeed.txt', 'w') as file:
    model.display(ostream=file)