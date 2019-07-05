#!/usr/bin/env python
#-*- coding:utf-8 -*-
from pyomo.environ import *

def argon_PR_model(temp, pressure, liquid_argon): #temp in ℃，pressure in KPa
    model = ConcreteModel()
    model.Component = Set(initialize=['Oxygen','Argon', 'Nitrogen'])

    model.pressure = Param(initialize=pressure*1000)
    model.temperature = Param(initialize=temp+273.15)
    dict = {
    'Oxygen':7.94000000000000e-07,
    'Argon':0.988273950000000,
    'Nitrogen':0.0117
    }
    model.x = Var(model.Component, initialize=dict, bounds=(0,1))
    dict = {
    'Oxygen':7.02000000000000e-07,
    'Argon':0.961808760000000,
    'Nitrogen':0.0381905300000000
    }
    model.y = Var(model.Component, initialize=dict, bounds=(0,1))

    model.CriticalTemp = Param(model.Component, initialize={'Oxygen':154.77,'Argon':150.71, 'Nitrogen':126.15}) #单位K
    model.CriticalPressure = Param(model.Component, initialize={'Oxygen':5080000,'Argon':4864000, 'Nitrogen':3394000})# Critical pressure, pa
    model.ComponentOmega = Param(model.Component, initialize={'Oxygen':0.019,'Argon':0,'Nitrogen':0.045})
    model.SatPresCorC = Param(model.Component, initialize={'Oxygen':-5.667,'Nitrogen':-6.344})
    dict = {
        ('Oxygen','Oxygen'):0,
        ('Oxygen', 'Argon'): 0.0265,
        ('Oxygen', 'Nitrogen'): -0.01238,
        ('Argon', 'Oxygen'): 0.0265,
        ('Argon', 'Argon'): 0,
        ('Argon', 'Nitrogen'): -0.004071,
        ('Nitrogen', 'Oxygen'): -0.01238,
        ('Nitrogen', 'Argon'): -0.004071,
        ('Nitrogen', 'Nitrogen'): 0
    }
    model.Kij = Param(model.Component,model.Component,initialize=dict)
    model.ReferenceTemp = Param(model.Component, initialize={'Oxygen':298.15,'Argon':298.15, 'Nitrogen':298.15}) #单位K
    # Reference state enthalpy for ideal gas at reference temperature, cal/mol
    model.DHFORM = Param(model.Component, initialize={'Oxygen':0,'Argon':0, 'Nitrogen':0})
    # Parameters to calculate the equation for the DIPPR ideal gas heat capacity model by Aly and Lee 1981,unit: cal/(mol*k)
    model.CPIGDP1= Param(model.Component, initialize={'Oxygen':1/4180*29103,'Argon':1/4180*20786, 'Nitrogen':1/4180*29105})
    model.CPIGDP2= Param(model.Component, initialize={'Oxygen':1/4180*10040,'Argon':1/4180*0, 'Nitrogen':1/4180*8614.9})
    model.CPIGDP3= Param(model.Component, initialize={'Oxygen':2526.5,'Argon':0, 'Nitrogen':1701.6})
    model.CPIGDP4= Param(model.Component, initialize={'Oxygen':1/4180*9356,'Argon':1/4180*0, 'Nitrogen':1/4180*103.47})
    model.CPIGDP5= Param(model.Component, initialize={'Oxygen':1153.8,'Argon':0, 'Nitrogen':909.79})
    model.CPIGDP6= Param(model.Component, initialize={'Oxygen':50,'Argon':-173.15, 'Nitrogen':50})
    model.CPIGDP7= Param(model.Component, initialize={'Oxygen':1500,'Argon':1226.85, 'Nitrogen':1500})
    model.RGas = Param(initialize=8.314) #J/(mol*K)

    model.ZL = Var(initialize=0.0043)
    model.ZV = Var(initialize=0.9632)
    model.K = Var(model.Component, initialize={'Oxygen':1.0792,'Argon':1.0214,'Nitrogen':3.0749})

    def Tr_Calculate(m,comp):
        return m.temperature / m.CriticalTemp[comp]
    model.Tr = Expression(model.Component, rule = Tr_Calculate)
    def Pr_Calculate(m,comp):
        return m.pressure / m.CriticalPressure[comp]
    model.Pr = Expression(model.Component, rule = Pr_Calculate)
    def m_Calculate(m,comp):
        return 0.37464+1.54226*m.ComponentOmega[comp]-0.26992*m.ComponentOmega[comp]*m.ComponentOmega[comp]
    model.m = Expression(model.Component, rule = m_Calculate)
    def alpha_Calculate(m,comp):
        return (1+m.m[comp]*(1-sqrt(m.Tr[comp])))**2
    model.alpha = Expression(model.Component, rule = alpha_Calculate)
    def ai_Calculate(m,comp):
        return 0.45724*m.alpha[comp]*(m.RGas**2)*(m.CriticalTemp[comp]**2)/m.CriticalPressure[comp]
    model.ai = Expression(model.Component, rule = ai_Calculate)
    def bi_Calculate(m,comp):
        return 0.07780*m.RGas*m.CriticalTemp[comp]/m.CriticalPressure[comp]
    model.bi = Expression(model.Component, rule = bi_Calculate)
    def aij_Calculate(m,comp1, comp2):
        return sqrt(m.ai[comp1]*m.ai[comp2])*(1-m.Kij[comp1,comp2])
    model.aij = Expression(model.Component,model.Component, rule = aij_Calculate)
    def aL_Calculate(m):
        return sum([sum([m.aij[c1,c2]*m.x[c1]*m.x[c2] for c1 in m.Component]) for c2 in m.Component])
    model.aL = Expression(rule = aL_Calculate)
    def bL_Calculate(m):
        return sum([m.bi[c] * m.x[c] for c in m.Component])
    model.bL = Expression(rule = bL_Calculate)
    def aV_Calculate(m):
        return sum([sum([m.aij[c1,c2]*m.y[c1]*m.y[c2] for c1 in m.Component]) for c2 in m.Component])
    model.aV = Expression(rule = aV_Calculate)
    def bV_Calculate(m):
        return sum([m.bi[c] * m.y[c] for c in m.Component])
    model.bV = Expression(rule = bV_Calculate)
    def AL_Calculate(m):
        return m.aL*m.pressure/((m.RGas*m.temperature)**2)
    model.AL = Expression(rule = AL_Calculate)
    def BL_Calculate(m):
        return m.bL*m.pressure/(m.RGas*m.temperature)
    model.BL = Expression(rule = BL_Calculate)
    def AV_Calculate(m):
        return m.aV*m.pressure/((m.RGas*m.temperature)**2)
    model.AV = Expression(rule = AV_Calculate)
    def BV_Calculate(m):
        return m.bV*m.pressure/(m.RGas*m.temperature)
    model.BV = Expression(rule = BV_Calculate)
    def SL_Calculate(m, comp):
        return sum([m.aij[c,comp] * m.x[c] for c in m.Component])
    model.SL = Expression(model.Component, rule = SL_Calculate)
    def SV_Calculate(m, comp):
        return sum([m.aij[c,comp] * m.y[c] for c in m.Component])
    model.SV = Expression(model.Component, rule = SV_Calculate)


    def ZL_Calculate(m):
        return m.ZL**3+m.ZL**2*(m.BL-1)+m.ZL*(m.AL-m.BL**2*3-2*m.BL)+(m.BL**2+m.BL**3-m.AL*m.BL)==0
    model.ZL_Calculate = Constraint(rule = ZL_Calculate)
    def ZV_Calculate(m):
        return m.ZV**3+m.ZV**2*(m.BV-1)+m.ZV*(m.AV-m.BV**2*3-2*m.BV)+(m.BV**2+m.BV**3-m.AV*m.BV)==0
    model.ZV_Calculate = Constraint(rule = ZV_Calculate)

    def PHIL_Calculate(m, comp):
        return exp(m.bi[comp]/m.bL*(m.ZL-1)-log(m.ZL-m.BL)-m.AL/m.BL/2/sqrt(2)*(2*m.SL[comp]/m.aL-m.bi[comp]/m.bL)*log((m.ZL+2.414*m.BL)/(m.ZL-0.414*m.BL)))
    model.PHIL = Expression(model.Component, rule = PHIL_Calculate)
    def PHIV_Calculate(m, comp):
        return exp(m.bi[comp]/m.bV*(m.ZV-1)-log(m.ZV-m.BV)-m.AV/m.BV/2/sqrt(2)*(2*m.SV[comp]/m.aV-m.bi[comp]/m.bV)*log((m.ZV+2.414*m.BV)/(m.ZV-0.414*m.BV)))
    model.PHIV = Expression(model.Component, rule = PHIV_Calculate)

    def K_Calculate(m, comp):
        return m.PHIL[comp]/m.PHIV[comp] -m.K[comp] == 0
    model.K_Calculate = Constraint(model.Component, rule = K_Calculate)

    def DIPPR_temp_constraint1(m, comp):
        return m.temperature>=m.CPIGDP6[comp]
    model.DIPPR_temp_constraint1 = Constraint(model.Component, rule=DIPPR_temp_constraint1)
    def DIPPR_temp_constraint2(m, comp):
        return m.temperature<=m.CPIGDP7[comp]
    model.DIPPR_temp_constraint2 = Constraint(model.Component, rule=DIPPR_temp_constraint2)
    def H0_Calculate(m, comp): #unit: J/mol
        if comp == 'Argon':
            return 20786*(m.temperature-298.15)/1000
        else:
            return 4.18*(m.DHFORM[comp]+m.CPIGDP1[comp]*(m.temperature-m.ReferenceTemp[comp])+2*m.CPIGDP2[comp]*m.CPIGDP3[comp]*(-exp(2/m.temperature*m.CPIGDP3[comp])+\
        exp(2/m.ReferenceTemp[comp]*m.CPIGDP3[comp]))/(exp(2/m.temperature*m.CPIGDP3[comp])-1)/(exp(2/m.ReferenceTemp[comp]*m.CPIGDP3[comp])-1)-\
        2*m.CPIGDP4[comp]*m.CPIGDP5[comp]*(exp(2/m.temperature*m.CPIGDP5[comp])-exp(2/m.ReferenceTemp[comp]*m.CPIGDP5[comp]))/\
                         (exp(2/m.temperature*m.CPIGDP5[comp])+1)/(exp(2/m.ReferenceTemp[comp]*m.CPIGDP5[comp])+1))
    model.H0 = Expression(model.Component, rule= H0_Calculate)

    def M_Calculate(m, comp1, comp2):
        return m.m[comp1]*sqrt(m.Tr[comp1])/(2*sqrt(m.alpha[comp1]))
    model.M = Expression(model.Component, model.Component, rule = M_Calculate)

    # Calculate the enthalpy of liquid phase mixture %unit: J/mol
    def HL_Calculate(m):
        return sum([m.x[c]*m.H0[c] for c in m.Component])+\
               m.RGas*m.temperature*((m.ZL-1)-1/(2**1.5)*(1/m.BL)*log((1+m.BL/m.ZL*2.414)/(1-m.BL/m.ZL*0.414))* \
               sum([sum([m.x[c1]*m.x[c2] * m.AL * (1+m.M[c1,c2]+m.M[c2,c1]) for c1 in m.Component]) for c2 in m.Component]))
    model.HL = Expression(rule = HL_Calculate)
    # Calculate the enthalpy of vapor phase mixture %unit: J/mol
    def HV_Calculate(m):
        return sum([m.y[c] * m.H0[c] for c in m.Component]) + \
               m.RGas*m.temperature*((m.ZV-1)-1/(2**1.5)*(1/m.BV)*log((1+m.BV/m.ZV*2.414)/(1-m.BV/m.ZV*0.414))*\
               sum([sum([m.y[c1] * m.y[c2] * m.AV * (1 + m.M[c1, c2] + m.M[c2, c1]) for c1 in m.Component]) for c2 in m.Component]))
    model.HV = Expression(rule = HV_Calculate)
    # def liquidArgonSpec(m):
    #     return m.x['Argon']== liquid_argon
    # model.liquidArgonSpec = Constraint(rule = liquidArgonSpec)
    def VapSummation(m):
        return sum([m.y[c] for c in m.Component]) == 1
    model.VapSummation = Constraint(rule=VapSummation)
    def LiqSummation(m):
        return sum([m.x[c] for c in m.Component]) == 1
    model.LiqSummation = Constraint(rule=LiqSummation)
    def PhEquilibruim(m, comp):
        return m.x[comp] * m.K[comp] - m.y[comp] == 0
    model.PhEquilibruim = Constraint(model.Component, rule=PhEquilibruim)

    solver=SolverFactory('ipopt')
    results = solver.solve(model,tee=True)
    with open('PR_display.txt', 'w') as file:
        model.display(ostream=file)
    return value(model.x['Nitrogen']),value(model.y['Argon']),value(model.y['Nitrogen']),value(model.HV),value(model.HL)

liquid_argon = 0.98827395
pressure = 124.4
temp = -182.704
x_n,y_ar,y_n,hv,hl = argon_PR_model(temp, pressure, liquid_argon)
print(x_n)
print(y_ar)
print(y_n)
print(hv)
print(hl)

