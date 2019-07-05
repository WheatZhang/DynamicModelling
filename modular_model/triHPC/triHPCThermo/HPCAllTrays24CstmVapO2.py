def VapO2(P,T,x_N2):
	x = (P-5.49565366e+02)/3.71707300e-01
	y = (T--1.77793287e+02)/1.66706000e-02
	z = (x_N2-9.84357513e-01)/2.28757906e-03
	output = \
	    1*-1.17856873e+01+\
	    z*1.23667440e+01+\
	    y*1.23545286e+01+\
	    x*-6.55941061e+00
	y_O2 = output*2.90867235e-04+1.07722297e-03
	return y_O2