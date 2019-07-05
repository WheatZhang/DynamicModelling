def VapN2(P,T,x_N2):
	x = (P-5.59477561e+02)/3.71707300e-01
	y = (T--1.76004286e+02)/1.08199200e-01
	z = (x_N2-8.12044275e-01)/1.54324448e-02
	x2 = x * x
	y2 = y * y
	z2 = z * z
	output = \
	    1*-5.33576567e-01+\
	    z*1.54306798e+00+\
	    z2*4.41040223e-02+\
	    y*5.60139747e-01+\
	    y*z*7.43446544e-02+\
	    y2*2.51960052e-02+\
	    x*-4.76294125e-02+\
	    x*z*-6.16030692e-03+\
	    x*y*-4.33355976e-03+\
	    x2*1.98177032e-04
	y_N2 = output*1.07307295e-02+9.09890185e-01
	return y_N2