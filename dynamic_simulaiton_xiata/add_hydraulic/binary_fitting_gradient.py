#!/usr/bin/env python
#-*- coding:utf-8 -*-
def liquid_nitrogen_enthalpy_DT(pressure,temperature):
	x = (pressure-100.000000)/500.000000
	y = (temperature--200.000000)/37.000000
	y2 = y*y
	x2 = x*x
	x3 = x*x2
	y2dy = 2*y
	y3dy = 3*y2
	yxdy = x
	y2xdy = 2*y*x
	yx2dy = x2
	y3xdy = 3*y2*x
	y2x2dy = 2*y*x2
	yx3dy = x3
	y3x2dy = 3*y2*x2
	y2x3dy = 2*y*x3
	y3x3dy = 3*y2*x3
	zdy = 0.932428+\
	    yxdy*0.194579+\
	    yx2dy*-0.389695+\
	    yx3dy*0.215382+\
	    y2dy*-0.079852+\
	    y2xdy*-0.214213+\
	    y2x2dy*0.792000+\
	    y2x3dy*-0.521881+\
	    y3dy*0.197291+\
	    y3xdy*-0.179700+\
	    y3x2dy*-0.169544+\
	    y3x3dy*0.218421
	return zdy*50.390691
def liquid_oxygen_enthalpy_DT(pressure,temperature):
	x = (pressure-100.000000)/500.000000
	y = (temperature--200.000000)/37.000000
	y2 = y*y
	x2 = x*x
	x3 = x*x2
	y2dy = 2*y
	y3dy = 3*y2
	yxdy = x
	y2xdy = 2*y*x
	yx2dy = x2
	y3xdy = 3*y2*x
	y2x2dy = 2*y*x2
	yx3dy = x3
	y3x2dy = 3*y2*x2
	y2x3dy = 2*y*x3
	y3x3dy = 3*y2*x3
	zdy = 0.850871+\
	    yxdy*-0.406914+\
	    yx2dy*0.981229+\
	    yx3dy*-0.587405+\
	    y2dy*0.449245+\
	    y2xdy*-0.322334+\
	    y2x2dy*-0.910912+\
	    y2x3dy*0.879245+\
	    y3dy*-0.346104+\
	    y3xdy*1.049611+\
	    y3x2dy*-0.565309+\
	    y3x3dy*-0.074628
	return zdy*60.716684
def liquid_oxygen_composition_DP(pressure,temperature):
	x = (pressure-100.000000)/500.000000
	y = (temperature--195.914523)/34.081421
	x2 = x*x
	y2 = y*y
	y3 = y*y2
	x2dx = 2*x
	x3dx = 3*x2
	xydx = y
	x2ydx = 2*x*y
	xy2dx = y2
	x3ydx = 3*x2*y
	x2y2dx = 2*x*y2
	xy3dx = y3
	x3y2dx = 3*x2*y2
	x2y3dx = 2*x*y3
	x3y3dx = 3*x2*y3
	zdx = -6.353776+\
	    xydx*18.091677+\
	    xy2dx*-14.713666+\
	    xy3dx*0.254038+\
	    x2dx*1.645231+\
	    x2ydx*-15.156516+\
	    x2y2dx*23.946051+\
	    x2y3dx*-8.012103+\
	    x3dx*1.373898+\
	    x3ydx*0.570620+\
	    x3y2dx*-6.053944+\
	    x3y3dx*3.258808
	return zdx*0.002000
def liquid_oxygen_composition_DT(pressure,temperature):
	x = (pressure-100.000000)/500.000000
	y = (temperature--195.914523)/34.081421
	y2 = y*y
	x2 = x*x
	x3 = x*x2
	y2dy = 2*y
	y3dy = 3*y2
	yxdy = x
	y2xdy = 2*y*x
	yx2dy = x2
	y3xdy = 3*y2*x
	y2x2dy = 2*y*x2
	yx3dy = x3
	y3x2dy = 3*y2*x2
	y2x3dy = 2*y*x3
	y3x3dy = 3*y2*x3
	zdy = 5.102425+\
	    yxdy*18.091677+\
	    yx2dy*-15.156516+\
	    yx3dy*0.570620+\
	    y2dy*-8.582956+\
	    y2xdy*-14.713666+\
	    y2x2dy*23.946051+\
	    y2x3dy*-6.053944+\
	    y3dy*5.623218+\
	    y3xdy*0.254038+\
	    y3x2dy*-8.012103+\
	    y3x3dy*3.258808
	return zdy*0.029341
