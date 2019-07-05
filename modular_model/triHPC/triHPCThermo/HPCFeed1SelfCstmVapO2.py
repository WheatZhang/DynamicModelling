def VapO2(P,T,x_N2):
	x = (P-5.38538049e+02)/8.26016000e-02
	y = (T--1.78154406e+02)/4.44600000e-04
	z = (x_N2-9.99124757e-01)/2.75160732e-04
	output = \
	    1*-5.35328135e+01+\
	    z*2.43557769e+02+\
	    y*5.45339899e+01+\
	    x*-2.44527713e+02
	y_O2 = output*1.74726202e-06+2.49477518e-06
	return y_O2