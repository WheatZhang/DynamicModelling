def VapO2_pT(P,T,x_N2):
	x = (P-5.63876098e+02)/2.47804800e-01
	y = (T--1.73749259e+02)/1.10194100e-01
	z = (x_N2-6.16340540e-01)/1.37704460e-02
	output = \
	    1*2.31962739e-01
	y_O2 = output*1.00000000e+00+0.00000000e+00
	return y_O2