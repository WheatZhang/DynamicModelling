def VapN2_pP(P,T,x_N2):
	x = (P-5.58858049e+02)/3.71707300e-01
	y = (T--1.76272221e+02)/9.79506000e-02
	z = (x_N2-8.37418800e-01)/1.47736117e-02
	output = \
	    1*-1.37099076e-03+\
	    z*-1.71784483e-04+\
	    y*-1.16789314e-04+\
	    x*1.18705444e-05
	y_N2 = output*1.00000000e+00+0.00000000e+00
	return y_N2