from pyomo.environ import *
from pyomo.dae import *

from col_feed import model as model_feed
def obj_rule(m):
    return 1
model_feed.OBJ = Objective(rule=obj_rule)
solver=SolverFactory('ipopt')
results = solver.solve(model_feed)
FeedLiquidPhaseMolarFrac = {'Oxygen':model_feed.FeedLiquidPhaseMolarFrac._data['Oxygen'].value,\
                            'Nitrogen':model_feed.FeedLiquidPhaseMolarFrac._data['Nitrogen'].value}
FeedVaporPhaseMolarFrac = {'Oxygen':model_feed.FeedVaporPhaseMolarFrac._data['Oxygen'].value,\
                            'Nitrogen':model_feed.FeedVaporPhaseMolarFrac._data['Nitrogen'].value}
FeedMolarFlow = model_feed.FeedMolarFlow.value
FeedMolarFraction = {'Oxygen':model_feed.FeedMolarFraction._data['Oxygen'],\
                            'Nitrogen':model_feed.FeedMolarFraction._data['Nitrogen']}
feedEnthalpy = model_feed.feedEnthalpy.value

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
#--------------进料各变量--------------
model.FeedLiquidPhaseMolarFrac = Param(model.Component,initialize = FeedLiquidPhaseMolarFrac)
model.FeedVaporPhaseMolarFrac =  Param(model.Component,initialize = FeedVaporPhaseMolarFrac)
model.FeedMolarFlow =  Param(initialize = FeedMolarFlow)
model.FeedMolarFraction =  Param(model.Component,initialize = FeedMolarFraction)
model.feedEnthalpy =  Param(initialize = feedEnthalpy)
#--------------塔设备指定--------------
NumberOfTrays = 5
AirFeedTray = 1
RefluxTray = NumberOfTrays
ColumnTopPressure = 539.56
ColumnBottomPressure = 564
#--------------塔板变量定义--------------
model.AllTrays = RangeSet(1, NumberOfTrays) # 10块塔板，下面为1
#model.trayTemperature = Param(model.AllTrays,initialize=-170)
model.trayTemperature = Var(model.AllTrays,bounds=(-230,-100),initialize=-175)
model.trayPressure = Var(model.AllTrays,bounds=(0,1000), initialize = (ColumnTopPressure+ColumnBottomPressure)/2)
#在这个模型中，压力并没有用到，因为热力学为一个常数，只会影响到焓
#-------------回流指定----------------------
# 如果回流比<0.6则不能收敛出一个可行解
model.RefluxRatio = Param(initialize=0.6)
model.RefluxTemperature = Param(initialize=-177)
model.RefluxPressure = Param(initialize=539.56)
#后面将ircCondLiquidMolarEnthalpy指定为Expression了
#model.ircCondLiquidMolarEnthalpy = Var(initialize=0)
#--------------VLE热力学指定----------------
# 注意这里不能分别指定两个k，否则就没有自由度了
# 这里初始化需要注意
ec = {}
for t in model.AllTrays:
    for c in model.Component:
        if c == 'Oxygen':
            ec[t,c] = 0.4
        elif c=='Nitrogen':
            ec[t,c] = 1.334
model.EquilibriumConstant = Var(model.AllTrays, model.Component, initialize=ec)  # y=K*x
# 加入bound是必要的，否则不能收敛到一个合理的结果
# -----------加载其他变量--------------------------
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
# 这两个定义并没有被用到
#model.vaporLeavingMolarEnthalpyCompo = Var(model.AllTrays, model.Component, initialize=0)
#model.liquidLeavingMolarEnthalpyCompo = Var(model.AllTrays, model.Component, initialize=0)
#----------------------------------------
#     焓的热力学
#----------------------------------------
def LiquidPhaseEnthalpy(temperature, pressure, oxygen, nitrogen):
    return (8917.884 + (temperature - (-173)) * 418.68 + (pressure - 250) * 18.31725) * oxygen \
           + (3893.724 + (temperature - (-173)) * 418.68 + (pressure - 770) * 18.31725) * nitrogen
def VaporPhaseEnthalpy(temperature, pressure, oxygen, nitrogen):
    return (15407.424 + (temperature - (-173)) * 558.24 + (pressure - 250) * 19.43871429) * oxygen \
           + (8457.336 + (temperature - (-173)) * 558.24 + (pressure - 770) * 19.43871429) * nitrogen
#----------------------------------------
###
# Enthalpy expression
###
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
# 要想计算出塔板上的温度，必须使用与温度有关的EquilConstantRatio
def ColumnEquilConstantRatio(m, tray):
    return 0.30075#-0.0021*m.trayTemperature[tray]*m.trayTemperature[tray] - 0.7477*m.trayTemperature[tray] - 65.435
model.EquilConstantRatio = Expression(model.AllTrays, rule= ColumnEquilConstantRatio)
#------------------Reflux-----------
def RefluxRatio(m):
    return m.RefluxRatio * m.vaporLeavingMolarFlow[NumberOfTrays]
model.ircRefluxMolarFlow = Expression(rule = RefluxRatio)

def RefluxEnthalpy(m):
    return LiquidPhaseEnthalpy(m.RefluxTemperature, m.RefluxPressure,\
                               m.vaporLeavingMolarFraction[NumberOfTrays,'Oxygen'],m.vaporLeavingMolarFraction[NumberOfTrays,'Nitrogen'])
model.ircCondLiquidMolarEnthalpy = Expression(rule=RefluxEnthalpy)
#-----------------------------------
###                             
# Model constraints
###
#-------------column-----------------
def materialBalances(m,tray, comp):
    if tray == NumberOfTrays:
        if tray == RefluxTray:
            return (m.vaporLeavingMolarFlowCompo[tray - 1, comp] \
                   - m.liquidLeavingMolarFlowCompo[tray, comp] - m.vaporLeavingMolarFlowCompo[tray, comp] \
                   + m.ircRefluxMolarFlow * m.vaporLeavingMolarFraction[NumberOfTrays, comp])*1e-3 == 0
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
                    + m.ircRefluxMolarFlow * m.vaporLeavingMolarFraction[NumberOfTrays, comp])*1e-3 == 0
        elif tray == AirFeedTray:
            return (m.liquidLeavingMolarFlowCompo[tray + 1, comp] + m.vaporLeavingMolarFlowCompo[tray - 1, comp] \
                   - m.liquidLeavingMolarFlowCompo[tray, comp] - m.vaporLeavingMolarFlowCompo[tray, comp] \
                   + m.FeedMolarFlow * m.FeedMolarFraction[comp])*1e-3 == 0
        else:
            return (m.liquidLeavingMolarFlowCompo[tray+1, comp] + m.vaporLeavingMolarFlowCompo[tray-1, comp]  \
                   - m.liquidLeavingMolarFlowCompo[tray,comp] - m.vaporLeavingMolarFlowCompo[tray, comp])*1e-3==0
model.columnMaterialBalances = Constraint(model.AllTrays, model.Component, rule=materialBalances)

def energyBalances(m,tray):
    if tray == NumberOfTrays:
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

# 这里m.EquilConstantRatio多了一个[tray]
def ColumnEquilibriumConstant(m,tray):
    return m.EquilibriumConstant[tray,'Oxygen'] == m.EquilibriumConstant[tray,'Nitrogen'] * m.EquilConstantRatio[tray]
model.ColumnEquilConstant = Constraint(model.AllTrays, rule = ColumnEquilibriumConstant)

def ColumnVLE(m, tray, comp):
    return m.vaporLeavingMolarFraction[tray, comp] == m.liquidLeavingMolarFraction[tray, comp] *m.EquilibriumConstant[tray,comp]
model.columnVLE = Constraint(model.AllTrays, model.Component, rule = ColumnVLE)

def ColumnPressureProfile(m, tray):
    return m.trayPressure[tray] == (ColumnTopPressure-ColumnBottomPressure)/(NumberOfTrays-1)*(tray-1)+ColumnBottomPressure
model.columnPressureProfile = Constraint(model.AllTrays, rule = ColumnPressureProfile)
#温度应该由一个类似于状态方程来求出
def ColumnTempCorrelation(m, tray):
    return (m.trayTemperature[tray] -  0.072*m.trayPressure[tray] + 214.36)*0.01 ==0
model.ColumnTempCorrelation = Constraint(model.AllTrays, rule= ColumnTempCorrelation)