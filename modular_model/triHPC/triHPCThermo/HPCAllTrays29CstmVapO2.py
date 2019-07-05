def VapO2(P,T,x_N2):
	x = (P-5.46529756e+02)/2.47804900e-01
	y = (T--1.77912681e+02)/8.55980000e-03
	z = (x_N2-9.91318725e-01)/1.30032045e-03
	output = \
	    1*-2.81634479e+01+\
	    z*3.18543620e+01+\
	    y*2.88668146e+01+\
	    x*-1.99671411e+01
	y_O2 = output*6.38422208e-05+2.54218593e-04
	return y_O2