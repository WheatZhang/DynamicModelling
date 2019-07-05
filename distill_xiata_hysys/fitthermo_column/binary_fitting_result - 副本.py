#!/usr/bin/env python
#-*- coding:utf-8 -*-
def vapor_nitrogen_composition(pressure,temperature):
	x = (pressure-100.000000)/500.000000
	y = (temperature--195.914523)/34.081421
	x2 = x*x
	x3 = x*x2
	x4 = x*x3
	y2 = y*y
	y3 = y*y2
	y4 = y*y3
	xy = x*y
	x2y = x2*y
	xy2 = x*y2
	x3y = x3*y
	x2y2 = x2*y2
	xy3 = x*y3
	z = 0.001903+\
	    x*-1.624830+\
	    y*1.314065+\
	    x2*5.190200+\
	    xy*-6.236612+\
	    y2*3.111479+\
	    x3*-8.037417+\
	    x2y*10.640503+\
	    xy2*-4.370953+\
	    y3*0.463780+\
	    x4*4.109210+\
	    x3y*-6.167151+\
	    x2y2*3.989928+\
	    xy3*-2.368203+\
	    y4*0.981991
	return z
	
def liquid_nitrogen_composition(pressure,temperature):
	x = (pressure-100.000000)/500.000000
	y = (temperature--195.914523)/34.081421
	x2 = x*x
	x3 = x*x2
	y2 = y*y
	y3 = y*y2
	xy = x*y
	x2y = x2*y
	xy2 = x*y2
	x3y = x3*y
	x2y2 = x2*y2
	xy3 = x*y3
	x3y2 = x3*y2
	x2y3 = x2*y3
	x3y3 = x3*y3
	z = 0.004688+\
	    y*5.102425+\
	    y2*-8.582956+\
	    y3*5.623218+\
	    x*-6.353776+\
	    xy*18.091677+\
	    xy2*-14.713666+\
	    xy3*0.254038+\
	    x2*1.645231+\
	    x2y*-15.156516+\
	    x2y2*23.946051+\
	    x2y3*-8.012103+\
	    x3*1.373898+\
	    x3y*0.570620+\
	    x3y2*-6.053944+\
	    x3y3*3.258808
	return z

def liquid_nitrogen_enthalpy(pressure,temperature):
	x = (pressure-100.000000)/500.000000
	y = (temperature--200.000000)/37.000000
	x2 = x*x
	x3 = x*x2
	y2 = y*y
	y3 = y*y2
	xy = x*y
	x2y = x2*y
	xy2 = x*y2
	x3y = x3*y
	x2y2 = x2*y2
	xy3 = x*y3
	x3y2 = x3*y2
	x2y3 = x2*y3
	x3y3 = x3*y3
	z = 0.000562+\
	    y*0.932428+\
	    y2*-0.079852+\
	    y3*0.197291+\
	    x*-0.001991+\
	    xy*0.194579+\
	    xy2*-0.214213+\
	    xy3*-0.179700+\
	    x2*0.010680+\
	    x2y*-0.389695+\
	    x2y2*0.792000+\
	    x2y3*-0.169544+\
	    x3*-0.005175+\
	    x3y*0.215382+\
	    x3y2*-0.521881+\
	    x3y3*0.218421
	return z*1864.455570+-13457.519087
	
def liquid_oxygen_enthalpy(pressure,temperature):
	x = (pressure-100.000000)/500.000000
	y = (temperature--200.000000)/37.000000
	x2 = x*x
	x3 = x*x2
	y2 = y*y
	y3 = y*y2
	xy = x*y
	x2y = x2*y
	xy2 = x*y2
	x3y = x3*y
	x2y2 = x2*y2
	xy3 = x*y3
	x3y2 = x3*y2
	x2y3 = x2*y3
	x3y3 = x3*y3
	z = -0.001162+\
	    y*0.850871+\
	    y2*0.449245+\
	    y3*-0.346104+\
	    x*0.022997+\
	    xy*-0.406914+\
	    xy2*-0.322334+\
	    xy3*1.049611+\
	    x2*-0.037320+\
	    x2y*0.981229+\
	    x2y2*-0.910912+\
	    x2y3*-0.565309+\
	    x3*0.020327+\
	    x3y*-0.587405+\
	    x3y2*0.879245+\
	    x3y3*-0.074628
	return z*2246.517325+-12132.703363

def vapor_nitrogen_enthalpy(pressure,temperature):
	x = (pressure-100.000000)/500.000000
	y = (temperature--195.000000)/35.000000
	x2 = x*x
	x3 = x*x2
	y2 = y*y
	y3 = y*y2
	xy = x*y
	x2y = x2*y
	xy2 = x*y2
	x3y = x3*y
	x2y2 = x2*y2
	xy3 = x*y3
	x3y2 = x3*y2
	x2y3 = x2*y3
	x3y3 = x3*y3
	z = -0.000051+\
	    y*1.011616+\
	    y2*-0.020553+\
	    y3*0.009069+\
	    x*-0.366990+\
	    xy*0.282324+\
	    xy2*-0.171983+\
	    xy3*0.046324+\
	    x2*-0.076505+\
	    x2y*0.006112+\
	    x2y2*0.183867+\
	    x2y3*-0.124395+\
	    x3*0.000594+\
	    x3y*0.002199+\
	    x3y2*-0.062719+\
	    x3y3*0.054660
	return z*972.952444+-6229.873107
	
def vapor_oxygen_enthalpy(pressure,temperature):
	x = (pressure-100.000000)/500.000000
	y = (temperature--195.000000)/35.000000
	x2 = x*x
	x3 = x*x2
	y2 = y*y
	y3 = y*y2
	xy = x*y
	x2y = x2*y
	xy2 = x*y2
	x3y = x3*y
	x2y2 = x2*y2
	xy3 = x*y3
	x3y2 = x3*y2
	x2y3 = x2*y3
	x3y3 = x3*y3
	z = 0.000048+\
	    y*1.008708+\
	    y2*-0.012656+\
	    y3*0.003913+\
	    x*-0.319371+\
	    xy*0.189582+\
	    xy2*-0.083460+\
	    xy3*0.023737+\
	    x2*-0.066301+\
	    x2y*0.181841+\
	    x2y2*-0.212997+\
	    x2y3*0.085251+\
	    x3*-0.028705+\
	    x3y*0.023442+\
	    x3y2*0.038556+\
	    x3y3*-0.034177
	return z*1006.693525+-6343.520276


