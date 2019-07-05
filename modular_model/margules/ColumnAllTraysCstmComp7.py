def vap_oxygen_composition(pressure,temperature):
	x = (pressure-540.000000)/13.000000
	y = (temperature--176.000000)/2.000000
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
	z = 0.123700+\
	    y*0.795850+\
	    y2*0.077329+\
	    y3*0.003121+\
	    x*-0.126677+\
	    xy*-0.024769+\
	    xy2*-0.001926+\
	    xy3*-0.000079+\
	    x2*0.003048+\
	    x2y*0.000598+\
	    x2y2*0.000042+\
	    x2y3*0.000004+\
	    x3*-0.000070+\
	    x3y*-0.000015+\
	    x3y2*0.000001+\
	    x3y3*-0.000001
	return z*0.102389+0.062930
def liq_oxygen_composition(pressure,temperature):
	x = (pressure-540.000000)/13.000000
	y = (temperature--176.000000)/2.000000
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
	z = 0.150111+\
	    y*0.914533+\
	    y2*-0.069219+\
	    y3*0.004576+\
	    x*-0.150110+\
	    xy*0.019168+\
	    xy2*-0.001697+\
	    xy3*0.000107+\
	    x2*0.000000+\
	    x2y*0.000001+\
	    x2y2*-0.000003+\
	    x2y3*0.000002+\
	    x3*-0.000000+\
	    x3y*-0.000001+\
	    x3y2*0.000002+\
	    x3y3*-0.000001
	return z*0.201734+0.175018
