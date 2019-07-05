def vap_oxygen_composition(pressure,temperature):
	x = (pressure-535.000000)/13.000000
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
	z = 0.124026+\
	    y*0.792755+\
	    y2*0.079875+\
	    y3*0.003343+\
	    x*-0.127041+\
	    xy*-0.025325+\
	    xy2*-0.002031+\
	    xy3*-0.000076+\
	    x2*0.003087+\
	    x2y*0.000606+\
	    x2y2*0.000055+\
	    x2y3*0.000003+\
	    x3*-0.000073+\
	    x3y*-0.000008+\
	    x3y2*-0.000005+\
	    x3y3*-0.000000
	return z*0.094236+0.029669
def liq_oxygen_composition(pressure,temperature):
	x = (pressure-535.000000)/13.000000
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
	z = 0.149852+\
	    y*0.917174+\
	    y2*-0.071868+\
	    y3*0.004843+\
	    x*-0.149853+\
	    xy*0.019640+\
	    xy2*-0.001792+\
	    xy3*0.000123+\
	    x2*0.000003+\
	    x2y*-0.000011+\
	    x2y2*0.000011+\
	    x2y3*-0.000002+\
	    x3*-0.000001+\
	    x3y*0.000007+\
	    x3y2*-0.000009+\
	    x3y3*0.000003
	return z*0.215585+0.089520
