def LiqO2(P,T,x_N2):
	x = (P-5.60097073e+02)/3.71707300e-01
	y = (T--1.75716179e+02)/1.16025133e-01
	z = (x_N2-7.84620737e-01)/1.65897362e-02
	x2 = x * x
	y2 = y * y
	z2 = z * z
	output = \
	    1*-1.92987758e+00+\
	    z*2.67855783e+00+\
	    z2*-2.10374445e-02+\
	    y*2.26451847e+00+\
	    y*z*-2.11368677e-02+\
	    y2*-1.30275686e-02+\
	    x*-1.75329795e-01+\
	    x*z*1.51989514e-03+\
	    x*y*1.63839282e-03+\
	    x2*-5.85880095e-06
	x_O2 = output*2.47741593e-02+1.80088236e-01
	return x_O2