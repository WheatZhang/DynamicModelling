def VapN2(P,T,x_N2):
	x = (P-5.48945854e+02)/3.71707300e-01
	y = (T--1.77820504e+02)/1.55368000e-02
	z = (x_N2-9.86029272e-01)/2.18797134e-03
	output = \
	    1*-8.34406939e-01+\
	    z*1.87401350e+00+\
	    y*8.34531042e-01+\
	    x*-4.76442417e-01
	y_N2 = output*1.16618025e-03+9.92723849e-01
	return y_N2