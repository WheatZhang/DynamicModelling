def VapN2_pP(P,T,x_N2):
	x = (P-5.62637073e+02)/2.47804800e-01
	y = (T--1.74564594e+02)/1.00692600e-01
	z = (x_N2-6.85778253e-01)/1.35418860e-02
	output = \
	    1*-1.40383784e-03+\
	    z*-1.52022962e-04+\
	    y*-9.99685351e-05+\
	    x*6.82609565e-06
	y_N2 = output*1.00000000e+00+0.00000000e+00
	return y_N2