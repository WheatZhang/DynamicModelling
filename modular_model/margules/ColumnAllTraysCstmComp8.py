def vap_oxygen_composition(pressure,temperature):
	x = (pressure-538.000000)/11.000000
	y = (temperature--177.000000)/2.000000
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
	z = 0.106967+\
	    y*0.808075+\
	    y2*0.081541+\
	    y3*0.003416+\
	    x*-0.109155+\
	    xy*-0.021800+\
	    xy2*-0.001606+\
	    xy3*-0.000162+\
	    x2*0.002230+\
	    x2y*0.000604+\
	    x2y2*-0.000522+\
	    x2y3*0.000394+\
	    x3*-0.000042+\
	    x3y*-0.000156+\
	    x3y2*0.000505+\
	    x3y3*-0.000355
	return z*0.091772+0.028793
def liq_oxygen_composition(pressure,temperature):
	x = (pressure-538.000000)/11.000000
	y = (temperature--177.000000)/2.000000
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
	z = 0.129242+\
	    y*0.939467+\
	    y2*-0.073674+\
	    y3*0.004965+\
	    x*-0.129242+\
	    xy*0.016909+\
	    xy2*-0.001440+\
	    xy3*0.000032+\
	    x2*0.000001+\
	    x2y*0.000118+\
	    x2y2*-0.000423+\
	    x2y3*0.000300+\
	    x3*0.000001+\
	    x3y*-0.000110+\
	    x3y2*0.000383+\
	    x3y3*-0.000270
	return z*0.211509+0.087035
