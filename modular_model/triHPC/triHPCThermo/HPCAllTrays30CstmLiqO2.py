def LiqO2(P,T,x_N2):
	x = (P-5.45910244e+02)/2.47804900e-01
	y = (T--1.77933948e+02)/8.29410000e-03
	z = (x_N2-9.92196920e-01)/1.17520781e-03
	output = \
	    1*-3.08860172e+01+\
	    z*3.24334403e+01+\
	    y*3.15300290e+01+\
	    x*-2.25248005e+01
	x_O2 = output*1.36042941e-04+4.54619680e-04
	return x_O2