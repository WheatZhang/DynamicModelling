def VapO2_pT(P,T,x_N2):
	x = (P-5.41573658e+02)/2.47804900e-01
	y = (T--1.78069279e+02)/7.24480000e-03
	z = (x_N2-9.96540601e-01)/9.95332218e-04
	output = \
	    1*2.12373706e-01
	y_O2 = output*1.00000000e+00+0.00000000e+00
	return y_O2