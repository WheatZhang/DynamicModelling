def VapN2_pT(P,T,x_N2):
	x = (P-5.58238537e+02)/3.71707300e-01
	y = (T--1.76514223e+02)/8.64501333e-02
	z = (x_N2-8.61446995e-01)/1.32629992e-02
	output = \
	    1*5.64215905e-02+\
	    z*6.40977969e-03+\
	    y*4.20993906e-03+\
	    x*-4.48578539e-04
	y_N2 = output*1.00000000e+00+0.00000000e+00
	return y_N2