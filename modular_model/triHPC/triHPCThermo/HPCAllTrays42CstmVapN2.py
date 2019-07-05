def VapN2(P,T,x_N2):
	x = (P-5.38538049e+02)/8.26016000e-02
	y = (T--1.78154406e+02)/4.44600000e-04
	z = (x_N2-9.99124757e-01)/2.75160732e-04
	output = \
	    1*-1.94035498e-01+\
	    z*1.87018235e+00+\
	    y*1.94043655e-01+\
	    x*-8.70192438e-01
	y_N2 = output*1.47206573e-04+9.99531462e-01
	return y_N2