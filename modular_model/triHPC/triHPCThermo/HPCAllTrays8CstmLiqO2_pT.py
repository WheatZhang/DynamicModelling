def LiqO2_pT(P,T,x_N2):
	x = (P-5.59477561e+02)/3.71707300e-01
	y = (T--1.76004286e+02)/1.08199200e-01
	z = (x_N2-8.11442958e-01)/1.60337615e-02
	output = \
	    1*4.88842537e-01+\
	    z*-3.71320571e-03+\
	    y*-4.70887746e-03+\
	    x*3.08224752e-04
	x_O2 = output*1.00000000e+00+0.00000000e+00
	return x_O2