def vap_oxygen_composition(pressure,temperature):
	x = (pressure-545.000000)/10.000000
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
	z = 0.097851+\
	    y*0.819145+\
	    y2*0.079783+\
	    y3*0.003220+\
	    x*-0.099646+\
	    xy*-0.019483+\
	    xy2*-0.001517+\
	    xy3*-0.000061+\
	    x2*0.001828+\
	    x2y*0.000357+\
	    x2y2*0.000027+\
	    x2y3*0.000002+\
	    x3*-0.000032+\
	    x3y*-0.000006+\
	    x3y2*0.000000+\
	    x3y3*-0.000000
	return z*0.098297+0.061034
def liq_oxygen_composition(pressure,temperature):
	x = (pressure-545.000000)/10.000000
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
	z = 0.118782+\
	    y*0.948345+\
	    y2*-0.071876+\
	    y3*0.004750+\
	    x*-0.118781+\
	    xy*0.015168+\
	    xy2*-0.001344+\
	    xy3*0.000085+\
	    x2*0.000000+\
	    x2y*-0.000000+\
	    x2y2*-0.000000+\
	    x2y3*0.000000+\
	    x3*-0.000000+\
	    x3y*-0.000000+\
	    x3y2*0.000001+\
	    x3y3*-0.000000
	return z*0.196109+0.170359
