def VapO2(P,T,x_N2):
	x = (P-5.43432195e+02)/2.47804900e-01
	y = (T--1.78013507e+02)/7.57820000e-03
	z = (x_N2-9.94983140e-01)/1.03537262e-03
	output = \
	    1*-7.95028694e+01+\
	    z*7.95339808e+01+\
	    y*8.03721136e+01+\
	    x*-6.30304494e+01
	y_O2 = output*2.02146164e-05+5.53545029e-05
	return y_O2