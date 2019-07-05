def LiqO2_pT(P,T,x_N2):
	x = (P-5.61398049e+02)/2.47804900e-01
	y = (T--1.75105086e+02)/8.03391333e-02
	z = (x_N2-7.34764172e-01)/1.09413289e-02
	output = \
	    1*4.69607202e-01+\
	    z*-3.94716618e-03+\
	    y*-4.57424580e-03+\
	    x*2.91662576e-04
	x_O2 = output*1.00000000e+00+0.00000000e+00
	return x_O2