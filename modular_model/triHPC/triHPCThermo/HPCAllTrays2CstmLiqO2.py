def LiqO2(P,T,x_N2):
	x = (P-5.63256585e+02)/2.47804800e-01
	y = (T--1.74161904e+02)/1.07862000e-01
	z = (x_N2-6.50951693e-01)/1.39810541e-02
	x2 = x * x
	y2 = y * y
	z2 = z * z
	output = \
	    1*-1.86583170e+00+\
	    z*2.57390122e+00+\
	    z2*-2.84669798e-02+\
	    y*2.15622754e+00+\
	    y*z*-3.34656929e-02+\
	    y2*-1.78024314e-02+\
	    x*-1.21698318e-01+\
	    x*z*1.79720707e-03+\
	    x*y*1.78125977e-03+\
	    x2*-2.54592044e-05
	x_O2 = output*2.25100366e-02+3.19838814e-01
	return x_O2