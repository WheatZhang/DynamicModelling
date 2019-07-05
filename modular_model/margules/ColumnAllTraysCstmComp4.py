def vap_oxygen_composition(pressure,temperature):
	x = (pressure-550.000000)/10.000000
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
	z = 0.098184+\
	    y*0.824213+\
	    y2*0.074718+\
	    y3*0.002885+\
	    x*-0.099970+\
	    xy*-0.018788+\
	    xy2*-0.001432+\
	    xy3*-0.000039+\
	    x2*0.001818+\
	    x2y*0.000309+\
	    x2y2*0.000093+\
	    x2y3*-0.000035+\
	    x3*-0.000033+\
	    x3y*0.000015+\
	    x3y2*-0.000044+\
	    x3y3*0.000023
	return z*0.116540+0.142011
def liq_oxygen_composition(pressure,temperature):
	x = (pressure-550.000000)/10.000000
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
	z = 0.119786+\
	    y*0.942448+\
	    y2*-0.066527+\
	    y3*0.004294+\
	    x*-0.119786+\
	    xy*0.014554+\
	    xy2*-0.001257+\
	    xy3*0.000086+\
	    x2*0.000001+\
	    x2y*-0.000018+\
	    x2y2*0.000038+\
	    x2y3*-0.000020+\
	    x3*-0.000000+\
	    x3y*0.000012+\
	    x3y2*-0.000025+\
	    x3y3*0.000013
	return z*0.171692+0.335619
