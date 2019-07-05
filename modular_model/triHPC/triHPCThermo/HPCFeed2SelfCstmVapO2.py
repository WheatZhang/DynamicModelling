def VapO2(P,T,x_N2):
	x = (P-5.40396585e+02)/1.23902400e-01
	y = (T--1.78102248e+02)/2.35833333e-03
	z = (x_N2-9.97848887e-01)/4.61257558e-04
	output = \
	    1*-9.91567280e+01+\
	    z*1.41388512e+02+\
	    y*1.00156039e+02+\
	    x*-1.26691938e+02
	y_O2 = output*4.26068330e-06+1.13068765e-05
	return y_O2