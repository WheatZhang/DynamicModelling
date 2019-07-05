def vap_oxygen_composition(pressure,temperature):
	x = (pressure-563.000000)/2.000000
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
	z = 0.021241+\
	    y*0.894132+\
	    y2*0.081478+\
	    y3*0.003148+\
	    x*-0.021317+\
	    xy*-0.004009+\
	    xy2*-0.000300+\
	    xy3*-0.000011+\
	    x2*0.000076+\
	    x2y*0.000014+\
	    x2y2*0.000001+\
	    x2y3*0.000000+\
	    x3*-0.000000+\
	    x3y*0.000000+\
	    x3y2*0.000000+\
	    x3y3*-0.000000
	return z*0.104315+0.136441
def liq_oxygen_composition(pressure,temperature):
	x = (pressure-563.000000)/2.000000
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
	z = 0.025997+\
	    y*1.043178+\
	    y2*-0.073944+\
	    y3*0.004770+\
	    x*-0.025996+\
	    xy*0.003157+\
	    xy2*-0.000270+\
	    xy3*0.000017+\
	    x2*0.000000+\
	    x2y*0.000000+\
	    x2y2*-0.000001+\
	    x2y3*0.000001+\
	    x3*-0.000000+\
	    x3y*-0.000000+\
	    x3y2*0.000001+\
	    x3y3*-0.000001
	return z*0.158226+0.325336
