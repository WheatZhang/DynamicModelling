def VapN2(P,T,x_N2):
	x = (P-5.53220488e+02)/4.95609800e-01
	y = (T--1.77545850e+02)/2.98882000e-02
	z = (x_N2-9.64150648e-01)/5.13875682e-03
	output = \
	    1*-6.86176925e-01+\
	    z*1.92217179e+00+\
	    y*6.86496882e-01+\
	    x*-2.71639486e-01
	y_N2 = output*2.69386817e-03+9.82388634e-01
	return y_N2