def VapO2_px_N2(P,T,x_N2):
	x = (P-5.54521463e+02)/3.71707300e-01
	y = (T--1.77417593e+02)/4.69959000e-02
	z = (x_N2-9.51559553e-01)/5.66992393e-03
	output = \
	    1*1.61034495e+00
	y_O2 = output*1.00000000e+00+0.00000000e+00
	return y_O2