def VapO2_px_N2(P,T,x_N2):
	x = (P-5.63256585e+02)/2.47804800e-01
	y = (T--1.74161904e+02)/1.07862000e-01
	z = (x_N2-6.50594679e-01)/1.43380675e-02
	output = \
	    1*2.05851967e+00+\
	    z*-4.44424650e-02+\
	    y*-1.31071892e-02+\
	    x*8.91623214e-04
	y_O2 = output*1.00000000e+00+0.00000000e+00
	return y_O2