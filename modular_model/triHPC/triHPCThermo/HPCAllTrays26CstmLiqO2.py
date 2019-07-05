def LiqO2(P,T,x_N2):
	x = (P-5.48326342e+02)/3.71707300e-01
	y = (T--1.77845947e+02)/1.46335000e-02
	z = (x_N2-9.87472328e-01)/2.08229564e-03
	output = \
	    1*-1.45472123e+01+\
	    z*1.56226330e+01+\
	    y*1.50765340e+01+\
	    x*-9.13153062e+00
	x_O2 = output*5.01043062e-04+1.44699652e-03
	return x_O2