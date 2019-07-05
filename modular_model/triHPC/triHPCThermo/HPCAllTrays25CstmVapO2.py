def VapO2(P,T,x_N2):
	x = (P-5.48945854e+02)/3.71707300e-01
	y = (T--1.77820504e+02)/1.55368000e-02
	z = (x_N2-9.86029272e-01)/2.18797134e-03
	output = \
	    1*-1.21754261e+01+\
	    z*1.30217079e+01+\
	    y*1.26887055e+01+\
	    x*-7.23312175e+00
	y_O2 = output*2.63730150e-04+8.06965194e-04
	return y_O2