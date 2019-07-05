from pyomo.environ import *
from pyomo.dae import *

def cond_model(ircHeatExchange): #Default: 1e7
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
    model.ircRefluxMolarFlow = Param(initialize=4315.151302996267 * 0.3)  #Reflux Ratio 0.6
    model.ircCondTemperature = Param(initialize=-177)
    model.ircCondPressure = Param(initialize=539.56)
    model.ircLNProductMolarFlow = Var(initialize=39.9979154,within=NonNegativeReals)
    model.GasDrawRatio = Var(initialize=0.3, bounds=(0, 1))

    #GasDrawRatio = 0.587744831
    MinimalTempDiff = 0.1
    model.expandValveDeltaP = Param(initialize=100)
    #model.ircLNProductMolarFlow = Param(initialize=39.9979154)
    model.heatTransferConstant = Param(initialize=238616) #Q=k*\deltaT
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
    model.ircHeatExchange=Param(initialize=ircHeatExchange)

    model.ircGNProductMolarFlow=Var(within=NonNegativeReals,initialize=2460.4011666837564)
    model.ircTopTrayVaporMolarFlow=Var(within=NonNegativeReals,initialize=4186.17236071245)
    #model.ircRefluxMolarFlow=Var(within=NonNegativeReals,initialize=1685.7732786301506)
    #model.ircCondTemperature=Var(bounds=(-230,-100),initialize=-170)
    #model.ircCondPressure=Var(bounds=(0,1000),initialize=450)
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
        return VaporPhaseEnthalpy(m.trayTemperature[NumberOfTrays], m.trayPressure[NumberOfTrays], m.vaporLeavingMolarFraction[NumberOfTrays,'Oxygen'],
                                  m.vaporLeavingMolarFraction[NumberOfTrays,'Nitrogen'])
    model.ircTopTrayVaporMolarEnthalpy = Expression(rule=_ircTopTrayVaporMolarEnthalpy)
    def _ircCondLiquidMolarEnthalpy(m):
        return LiquidPhaseEnthalpy(m.ircCondTemperature, m.ircCondPressure, m.vaporLeavingMolarFraction[NumberOfTrays,'Oxygen'],
                                   m.vaporLeavingMolarFraction[NumberOfTrays,'Nitrogen'])
    model.ircCondLiquidMolarEnthalpy = Expression(rule=_ircCondLiquidMolarEnthalpy)
    #-----------------------------------
    ###
    # Model constraints
    ###
    #-------------IRC Condenser Side-----------------
    def ITopTrayVaporMolarFlow(m):
        return (m.vaporLeavingMolarFlow[NumberOfTrays] - m.ircTopTrayVaporMolarFlow)*1e-3 ==0
    model.ITopTrayVaporMolarFlow =  Constraint(rule = ITopTrayVaporMolarFlow)
    # 这个是多余的
    # def ICondTemperature(m):
    #     return (m.trayTemperature[NumberOfTrays] - m.ircCondTemperature)*1e-2 == 0
    # model.ICondTemperature = Constraint(rule=ICondTemperature)
    # def ICondPressure(m):
    #     return (m.trayPressure[NumberOfTrays] - m.ircCondPressure)*1e-3 == 0
    # model.ICondPressure = Constraint(rule=ICondPressure)
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
    return model