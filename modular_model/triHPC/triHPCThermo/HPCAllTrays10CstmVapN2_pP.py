def VapN2_pP(P,T,x_N2):
	x = (P-5.58238537e+02)/3.71707300e-01
	y = (T--1.76514223e+02)/8.64501333e-02
	z = (x_N2-8.61446995e-01)/1.32629992e-02
	output = \
	    1*-1.37862242e-03+\
	    z*-1.53152808e-04+\
	    y*-1.04328525e-04+\
	    x*1.18841598e-05
	y_N2 = output*1.00000000e+00+0.00000000e+00
	return y_N2