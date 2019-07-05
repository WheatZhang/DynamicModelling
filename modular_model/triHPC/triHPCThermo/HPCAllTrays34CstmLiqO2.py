def LiqO2(P,T,x_N2):
	x = (P-5.43432195e+02)/2.47804900e-01
	y = (T--1.78013507e+02)/7.57820000e-03
	z = (x_N2-9.94983140e-01)/1.03537262e-03
	output = \
	    1*-7.97322925e+01+\
	    z*7.97627735e+01+\
	    y*8.06019489e+01+\
	    x*-6.32103842e+01
	x_O2 = output*4.86629023e-05+1.33420247e-04
	return x_O2