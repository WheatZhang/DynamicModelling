#!/usr/bin/env python
#-*- coding:utf-8 -*-
def liquid_density(pressure,temperature):
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
	z = 0.324408+\
	    y*3.434279+\
	    y2*-5.429304+\
	    y3*3.036496+\
	    x*-4.899861+\
	    xy*10.911479+\
	    xy2*-6.091897+\
	    xy3*-1.340842+\
	    x2*2.851829+\
	    x2y*-13.884229+\
	    x2y2*16.869963+\
	    x2y3*-4.666398+\
	    x3*0.000024+\
	    x3y*3.318750+\
	    x3y2*-6.436631+\
	    x3y3*2.657722
	return z*10.502094+25.345600

def vapor_density(pressure,temperature):
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
	z = 0.032589+\
	    y*-0.105374+\
	    y2*0.056759+\
	    y3*-0.027706+\
	    x*1.135023+\
	    xy*-0.600893+\
	    xy2*0.336817+\
	    xy3*-0.095589+\
	    x2*0.244771+\
	    x2y*-0.382819+\
	    x2y2*0.231063+\
	    x2y3*-0.042398+\
	    x3*0.062912+\
	    x3y*-0.061267+\
	    x3y2*0.009955+\
	    x3y3*0.003011
	return z*0.745460+0.138039
