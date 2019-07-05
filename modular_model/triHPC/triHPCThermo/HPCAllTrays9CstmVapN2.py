def VapN2(P,T,x_N2):
	x = (P-5.58858049e+02)/3.71707300e-01
	y = (T--1.76272221e+02)/9.79506000e-02
	z = (x_N2-8.37418800e-01)/1.47736117e-02
	x2 = x * x
	y2 = y * y
	z2 = z * z
	output = \
	    1*-5.56790742e-01+\
	    z*1.57094716e+00+\
	    z2*4.35683716e-02+\
	    y*5.52390613e-01+\
	    y*z*7.02356600e-02+\
	    y2*2.29992685e-02+\
	    x*-5.14932963e-02+\
	    x*z*-6.45208527e-03+\
	    x*y*-4.38651151e-03+\
	    x2*2.22923988e-04
	y_N2 = output*9.89657512e-03+9.22569536e-01
	return y_N2