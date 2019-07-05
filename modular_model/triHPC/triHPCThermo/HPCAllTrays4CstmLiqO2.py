def LiqO2(P,T,x_N2):
	x = (P-5.62017561e+02)/2.47804900e-01
	y = (T--1.74950614e+02)/6.71933000e-02
	z = (x_N2-7.23608844e-01)/7.27108322e-03
	output = \
	    1*-2.81762890e+00+\
	    z*2.91264185e+00+\
	    y*3.09923034e+00+\
	    x*-2.78582590e-01
	x_O2 = output*1.00172953e-02+2.56438479e-01
	return x_O2