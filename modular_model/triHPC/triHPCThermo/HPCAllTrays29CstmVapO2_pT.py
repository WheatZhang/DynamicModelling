def VapO2_pT(P,T,x_N2):
	x = (P-5.46529756e+02)/2.47804900e-01
	y = (T--1.77912681e+02)/8.55980000e-03
	z = (x_N2-9.91318725e-01)/1.30032045e-03
	output = \
	    1*2.15299604e-01
	y_O2 = output*1.00000000e+00+0.00000000e+00
	return y_O2