def VapO2_pT(P,T,x_N2):
	x = (P-5.47706829e+02)/3.71707300e-01
	y = (T--1.77869974e+02)/1.39084000e-02
	z = (x_N2-9.88731400e-01)/2.05993546e-03
	output = \
	    1*2.15216715e-01
	y_O2 = output*1.00000000e+00+0.00000000e+00
	return y_O2