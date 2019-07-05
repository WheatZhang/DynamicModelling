def VapO2(P,T,x_N2):
	x = (P-5.60778537e+02)/2.47804900e-01
	y = (T--1.75406333e+02)/8.02400667e-02
	z = (x_N2-7.60655126e-01)/1.16553170e-02
	x2 = x * x
	y2 = y * y
	z2 = z * z
	output = \
	    1*-1.92223281e+00+\
	    z*2.61328457e+00+\
	    z2*-1.72046612e-02+\
	    y*2.18000754e+00+\
	    y*z*-6.90002862e-03+\
	    y2*-6.83152281e-04+\
	    x*-1.62178508e-01+\
	    x*z*7.21461823e-04+\
	    x*y*9.35744898e-05+\
	    x2*2.23444813e-05
	y_O2 = output*8.34663640e-03+9.91356796e-02
	return y_O2