def vap_oxygen_composition(pressure,temperature):
	x = (pressure-560.000000)/3.000000
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
	z = 0.031597+\
	    y*0.884764+\
	    y2*0.080528+\
	    y3*0.003111+\
	    x*-0.031766+\
	    xy*-0.005974+\
	    xy2*-0.000447+\
	    xy3*-0.000017+\
	    x2*0.000170+\
	    x2y*0.000032+\
	    x2y2*0.000001+\
	    x2y3*0.000001+\
	    x3*-0.000001+\
	    x3y*-0.000000+\
	    x3y2*0.000001+\
	    x3y3*-0.000001
	return z*0.106132+0.138657
def liq_oxygen_composition(pressure,temperature):
	x = (pressure-560.000000)/3.000000
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
	z = 0.038660+\
	    y*1.029545+\
	    y2*-0.072909+\
	    y3*0.004704+\
	    x*-0.038660+\
	    xy*0.004695+\
	    xy2*-0.000401+\
	    xy3*0.000025+\
	    x2*0.000000+\
	    x2y*-0.000000+\
	    x2y2*-0.000001+\
	    x2y3*0.000001+\
	    x3*-0.000000+\
	    x3y*0.000000+\
	    x3y2*0.000000+\
	    x3y3*-0.000001
	return z*0.159593+0.329449
