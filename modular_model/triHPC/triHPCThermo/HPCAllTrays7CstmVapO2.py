def VapO2(P,T,x_N2):
	x = (P-5.60097073e+02)/3.71707300e-01
	y = (T--1.75716179e+02)/1.16025133e-01
	z = (x_N2-7.84030782e-01)/1.71796904e-02
	x2 = x * x
	y2 = y * y
	z2 = z * z
	output = \
	    1*-1.97001053e+00+\
	    z*2.68140304e+00+\
	    z2*-2.42252912e-02+\
	    y*2.22299304e+00+\
	    y*z*-8.53218110e-03+\
	    y2*-3.20568884e-04+\
	    x*-1.71229262e-01+\
	    x*z*9.74550446e-04+\
	    x*y*3.45185993e-05+\
	    x2*3.81183236e-05
	y_O2 = output*1.17780826e-02+8.32771990e-02
	return y_O2