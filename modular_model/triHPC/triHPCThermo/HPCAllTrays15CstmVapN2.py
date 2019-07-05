def VapN2(P,T,x_N2):
	x = (P-5.55140976e+02)/3.71707300e-01
	y = (T--1.77309886e+02)/3.74264667e-02
	z = (x_N2-9.42378729e-01)/6.05942822e-03
	output = \
	    1*-6.56210395e-01+\
	    z*1.76071430e+00+\
	    y*6.56522537e-01+\
	    x*-1.56112782e-01
	y_N2 = output*3.51553288e-03+9.72463756e-01
	return y_N2