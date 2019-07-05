def VapO2_pP(P,T,x_N2):
	x = (P-5.59477561e+02)/3.71707300e-01
	y = (T--1.76004286e+02)/1.08199200e-01
	z = (x_N2-8.11142284e-01)/1.63344354e-02
	output = \
	    1*-5.35797048e-03+\
	    z*-1.14191194e-06+\
	    y*-2.03747834e-05+\
	    x*5.86059996e-06
	y_O2 = output*1.00000000e+00+0.00000000e+00
	return y_O2