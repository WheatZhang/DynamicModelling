def VapO2(P,T,x_N2):
	x = (P-5.45910244e+02)/2.47804900e-01
	y = (T--1.77933948e+02)/8.29410000e-03
	z = (x_N2-9.92196920e-01)/1.28159015e-03
	output = \
	    1*-3.00370947e+01+\
	    z*3.44254202e+01+\
	    y*3.06907008e+01+\
	    x*-2.19251214e+01
	y_O2 = output*5.81168123e-05+1.87605582e-04
	return y_O2