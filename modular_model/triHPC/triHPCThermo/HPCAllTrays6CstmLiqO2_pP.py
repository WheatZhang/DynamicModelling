def LiqO2_pP(P,T,x_N2):
	x = (P-5.60778537e+02)/2.47804900e-01
	y = (T--1.75406333e+02)/8.02400667e-02
	z = (x_N2-7.60847837e-01)/1.14626069e-02
	output = \
	    1*-1.15485009e-02+\
	    z*8.23302254e-05+\
	    y*8.51793278e-05+\
	    x*-1.53373196e-06
	x_O2 = output*1.00000000e+00+0.00000000e+00
	return x_O2