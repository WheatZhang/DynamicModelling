def VapO2(P,T,x_N2):
	x = (P-5.63876098e+02)/2.47804800e-01
	y = (T--1.73749259e+02)/1.10194100e-01
	z = (x_N2-6.16340540e-01)/1.37704460e-02
	output = \
	    1*-1.84990465e+00+\
	    z*2.38246985e+00+\
	    y*2.11216960e+00+\
	    x*-1.15620104e-01
	y_O2 = output*1.21017390e-02+1.82075979e-01
	return y_O2