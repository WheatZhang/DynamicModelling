def VapN2_px_N2(P,T,x_N2):
	x = (P-5.59477561e+02)/3.71707300e-01
	y = (T--1.76004286e+02)/1.08199200e-01
	z = (x_N2-8.12044275e-01)/1.54324448e-02
	output = \
	    1*1.07295022e+00+\
	    z*6.13342007e-02+\
	    y*5.16944908e-02+\
	    x*-4.28348120e-03
	y_N2 = output*1.00000000e+00+0.00000000e+00
	return y_N2