def VapO2_px_N2(P,T,x_N2):
	x = (P-5.49565366e+02)/3.71707300e-01
	y = (T--1.77793287e+02)/1.66706000e-02
	z = (x_N2-9.84357513e-01)/2.28757906e-03
	output = \
	    1*1.57243992e+00
	y_O2 = output*1.00000000e+00+0.00000000e+00
	return y_O2