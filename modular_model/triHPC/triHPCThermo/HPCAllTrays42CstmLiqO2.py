def LiqO2(P,T,x_N2):
	x = (P-5.38538049e+02)/8.26016000e-02
	y = (T--1.78154406e+02)/4.44600000e-04
	z = (x_N2-9.99124757e-01)/2.75160732e-04
	output = \
	    1*-5.35435270e+01+\
	    z*2.43606148e+02+\
	    y*5.45440579e+01+\
	    x*-2.44575219e+02
	x_O2 = output*4.22715460e-06+6.03642497e-06
	return x_O2