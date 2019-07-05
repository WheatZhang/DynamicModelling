def VapN2(P,T,x_N2):
	x = (P-5.52600976e+02)/4.95609800e-01
	y = (T--1.77613684e+02)/3.85316000e-02
	z = (x_N2-9.69189779e-01)/4.78707116e-03
	output = \
	    1*-9.56432741e-01+\
	    z*1.92663095e+00+\
	    y*9.56688294e-01+\
	    x*-2.93431120e-01
	y_N2 = output*2.49780329e-03+9.84717576e-01
	return y_N2