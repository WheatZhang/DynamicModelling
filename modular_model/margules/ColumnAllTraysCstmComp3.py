def vap_oxygen_composition(pressure,temperature):
	x = (pressure-557.000000)/2.000000
	y = (temperature--174.000000)/2.000000
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
	z = 0.021410+\
	    y*0.894164+\
	    y2*0.081286+\
	    y3*0.003140+\
	    x*-0.021488+\
	    xy*-0.004041+\
	    xy2*-0.000303+\
	    xy3*-0.000011+\
	    x2*0.000077+\
	    x2y*0.000014+\
	    x2y2*0.000001+\
	    x2y3*0.000000+\
	    x3*-0.000000+\
	    x3y*-0.000000+\
	    x3y2*0.000000+\
	    x3y3*-0.000000
	return z*0.105729+0.143137
def liq_oxygen_composition(pressure,temperature):
	x = (pressure-557.000000)/2.000000
	y = (temperature--174.000000)/2.000000
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
	z = 0.026225+\
	    y*1.042792+\
	    y2*-0.073777+\
	    y3*0.004760+\
	    x*-0.026224+\
	    xy*0.003185+\
	    xy2*-0.000274+\
	    xy3*0.000018+\
	    x2*-0.000000+\
	    x2y*-0.000001+\
	    x2y2*0.000003+\
	    x2y3*-0.000002+\
	    x3*-0.000000+\
	    x3y*0.000001+\
	    x3y2*-0.000002+\
	    x3y3*0.000001
	return z*0.156847+0.337676
