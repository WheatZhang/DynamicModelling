def VapO2_pT(P,T,x_N2):
	x = (P-5.58238537e+02)/3.71707300e-01
	y = (T--1.76514223e+02)/8.64501333e-02
	z = (x_N2-8.61135306e-01)/1.32683185e-02
	output = \
	    1*2.21605154e-01+\
	    z*-2.33536773e-04+\
	    y*2.82883014e-04+\
	    x*-2.96528422e-05
	y_O2 = output*1.00000000e+00+0.00000000e+00
	return y_O2