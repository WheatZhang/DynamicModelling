def VapO2_pT(P,T,x_N2):
	x = (P-5.40396585e+02)/1.23902400e-01
	y = (T--1.78102248e+02)/2.35833333e-03
	z = (x_N2-9.97848887e-01)/4.61257558e-04
	output = \
	    1*1.80499647e-01
	y_O2 = output*1.00000000e+00+0.00000000e+00
	return y_O2