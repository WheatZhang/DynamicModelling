def VapN2_pT(P,T,x_N2):
	x = (P-5.59477561e+02)/3.71707300e-01
	y = (T--1.76004286e+02)/1.08199200e-01
	z = (x_N2-8.12044275e-01)/1.54324448e-02
	output = \
	    1*5.55522416e-02+\
	    z*7.37318183e-03+\
	    y*4.99766202e-03+\
	    x*-4.29783746e-04
	y_N2 = output*1.00000000e+00+0.00000000e+00
	return y_N2