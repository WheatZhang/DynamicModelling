def VapO2_pT(P,T,x_N2):
	x = (P-5.38538049e+02)/8.26016000e-02
	y = (T--1.78154406e+02)/4.44600000e-04
	z = (x_N2-9.99124757e-01)/2.75160732e-04
	output = \
	    1*2.14316620e-01
	y_O2 = output*1.00000000e+00+0.00000000e+00
	return y_O2