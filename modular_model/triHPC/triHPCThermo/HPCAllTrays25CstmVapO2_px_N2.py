def VapO2_px_N2(P,T,x_N2):
	x = (P-5.48945854e+02)/3.71707300e-01
	y = (T--1.77820504e+02)/1.55368000e-02
	z = (x_N2-9.86029272e-01)/2.18797134e-03
	output = \
	    1*1.56958957e+00
	y_O2 = output*1.00000000e+00+0.00000000e+00
	return y_O2