def VapN2(P,T,x_N2):
	x = (P-5.40396585e+02)/1.23902400e-01
	y = (T--1.78102248e+02)/2.35833333e-03
	z = (x_N2-9.97848887e-01)/4.61257558e-04
	output = \
	    1*2.52896361e-01+\
	    z*6.40435928e-01+\
	    y*-2.52992319e-01+\
	    x*3.19847998e-01
	y_N2 = output*2.46645277e-04+9.98848893e-01
	return y_N2