def VapO2_pP(P,T,x_N2):
	x = (P-5.63256585e+02)/2.47804800e-01
	y = (T--1.74161904e+02)/1.07862000e-01
	z = (x_N2-6.50594679e-01)/1.43380675e-02
	output = \
	    1*-5.63864956e-03+\
	    z*5.15896133e-05+\
	    y*1.99839240e-05+\
	    x*9.37969765e-07
	y_O2 = output*1.00000000e+00+0.00000000e+00
	return y_O2