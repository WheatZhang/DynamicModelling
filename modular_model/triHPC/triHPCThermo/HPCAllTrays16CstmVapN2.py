def VapN2(P,T,x_N2):
	x = (P-5.54521463e+02)/3.71707300e-01
	y = (T--1.77417593e+02)/4.69959000e-02
	z = (x_N2-9.51353461e-01)/5.87601547e-03
	output = \
	    1*-9.30382516e-01+\
	    z*1.91398076e+00+\
	    y*9.30502758e-01+\
	    x*-1.75816840e-01
	y_N2 = output*3.11823528e-03+9.76483305e-01
	return y_N2