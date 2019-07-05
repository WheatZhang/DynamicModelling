def LiqO2(P,T,x_N2):
	x = (P-5.55140976e+02)/3.71707300e-01
	y = (T--1.77309886e+02)/3.74264667e-02
	z = (x_N2-9.42447433e-01)/6.32140659e-03
	output = \
	    1*-2.44635462e+00+\
	    z*3.62126231e+00+\
	    y*2.86847041e+00+\
	    x*-6.77439792e-01
	x_O2 = output*6.63647082e-03+3.17139521e-02
	return x_O2