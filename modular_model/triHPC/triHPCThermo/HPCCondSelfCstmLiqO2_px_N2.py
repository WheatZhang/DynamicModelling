def LiqO2_px_N2(P,T,x_N2):
	x = (P-5.38538049e+02)/4.13008000e-02
	y = (T--1.78156629e+02)/4.44600000e-04
	z = (x_N2-9.99452295e-01)/1.78184365e-04
	output = \
	    1*3.74609660e+00
	x_O2 = output*1.00000000e+00+0.00000000e+00
	return x_O2