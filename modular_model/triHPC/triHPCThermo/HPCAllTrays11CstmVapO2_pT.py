def VapO2_pT(P,T,x_N2):
	x = (P-5.57619024e+02)/3.71707300e-01
	y = (T--1.76727421e+02)/7.47418000e-02
	z = (x_N2-8.82675867e-01)/1.14249750e-02
	output = \
	    1*2.20104529e-01+\
	    z*3.15570395e-04+\
	    y*6.40623343e-04+\
	    x*-7.44515924e-05
	y_O2 = output*1.00000000e+00+0.00000000e+00
	return y_O2