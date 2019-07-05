def VapO2(P,T,x_N2):
	x = (P-5.57619024e+02)/3.71707300e-01
	y = (T--1.76727421e+02)/7.47418000e-02
	z = (x_N2-8.82675867e-01)/1.14249750e-02
	x2 = x * x
	y2 = y * y
	z2 = z * z
	output = \
	    1*-2.07127223e+00+\
	    z*2.72976001e+00+\
	    z2*-9.34142124e-03+\
	    y*2.31877772e+00+\
	    y*z*3.32450044e-03+\
	    y2*3.37444928e-03+\
	    x*-2.75071561e-01+\
	    x*z*-1.32637273e-05+\
	    x*y*-7.84339581e-04+\
	    x2*1.43922051e-04
	y_O2 = output*7.09468980e-03+3.66996241e-02
	return y_O2