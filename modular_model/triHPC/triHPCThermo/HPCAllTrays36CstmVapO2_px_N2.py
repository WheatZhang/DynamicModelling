def VapO2_px_N2(P,T,x_N2):
	x = (P-5.42193171e+02)/2.47804900e-01
	y = (T--1.78050970e+02)/7.34360000e-03
	z = (x_N2-9.96060985e-01)/1.00746068e-03
	output = \
	    1*1.54541222e+00
	y_O2 = output*1.00000000e+00+0.00000000e+00
	return y_O2