def VapO2(P,T,x_N2):
	x = (P-5.56999512e+02)/3.71707300e-01
	y = (T--1.76911493e+02)/6.36114000e-02
	z = (x_N2-9.01482074e-01)/1.00892736e-02
	x2 = x * x
	y2 = y * y
	z2 = z * z
	output = \
	    1*-2.13100757e+00+\
	    z*2.86334959e+00+\
	    z2*-7.86099648e-03+\
	    y*2.36780313e+00+\
	    y*z*3.74448053e-03+\
	    y2*3.18453928e-03+\
	    x*-3.29503184e-01+\
	    x*z*-1.85420540e-04+\
	    x*y*-8.95443413e-04+\
	    x2*1.53419996e-04
	y_O2 = output*5.88871166e-03+2.90149724e-02
	return y_O2