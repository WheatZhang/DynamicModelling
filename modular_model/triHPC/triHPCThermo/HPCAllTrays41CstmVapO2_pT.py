def VapO2_pT(P,T,x_N2):
	x = (P-5.39157561e+02)/1.23902400e-01
	y = (T--1.78137427e+02)/2.31133333e-03
	z = (x_N2-9.98587128e-01)/4.55935043e-04
	output = \
	    1*1.93364079e-01
	y_O2 = output*1.00000000e+00+0.00000000e+00
	return y_O2