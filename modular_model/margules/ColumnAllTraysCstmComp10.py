def vap_oxygen_composition(pressure,temperature):
	x = (pressure-535.000000)/9.000000
	y = (temperature--177.000000)/1.000000
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
	z = 0.171871+\
	    y*0.787594+\
	    y2*0.039722+\
	    y3*0.000812+\
	    x*-0.174763+\
	    xy*-0.017414+\
	    xy2*-0.000713+\
	    xy3*-0.000005+\
	    x2*0.002940+\
	    x2y*0.000268+\
	    x2y2*0.000059+\
	    x2y3*-0.000023+\
	    x3*-0.000048+\
	    x3y*0.000012+\
	    x3y2*-0.000033+\
	    x3y3*0.000016
	return z*0.047425+0.033206
def liq_oxygen_composition(pressure,temperature):
	x = (pressure-535.000000)/9.000000
	y = (temperature--177.000000)/1.000000
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
	z = 0.190367+\
	    y*0.841543+\
	    y2*-0.033089+\
	    y3*0.001180+\
	    x*-0.190367+\
	    xy*0.012482+\
	    xy2*-0.000585+\
	    xy3*0.000029+\
	    x2*0.000001+\
	    x2y*-0.000025+\
	    x2y2*0.000047+\
	    x2y3*-0.000023+\
	    x3*-0.000001+\
	    x3y*0.000017+\
	    x3y2*-0.000032+\
	    x3y3*0.000015
	return z*0.117487+0.099461
