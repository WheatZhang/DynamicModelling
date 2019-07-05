def LiqO2(P,T,x_N2):
	x = (P-5.38538049e+02)/4.13008000e-02
	y = (T--1.78156629e+02)/4.44600000e-04
	z = (x_N2-9.99452295e-01)/1.78184365e-04
	output = \
	    1*-3.85446781e+01+\
	    z*1.71532731e+02+\
	    y*5.93178442e+01+\
	    x*-1.32987506e+02
	x_O2 = output*3.89136138e-06+2.39200076e-06
	return x_O2