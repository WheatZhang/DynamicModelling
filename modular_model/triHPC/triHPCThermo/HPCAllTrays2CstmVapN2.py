def VapN2(P,T,x_N2):
	x = (P-5.63256585e+02)/2.47804800e-01
	y = (T--1.74161904e+02)/1.07862000e-01
	z = (x_N2-6.50594679e-01)/1.43380675e-02
	x2 = x * x
	y2 = y * y
	z2 = z * z
	output = \
	    1*-5.09998617e-01+\
	    z*1.50747759e+00+\
	    z2*3.50193090e-02+\
	    y*4.92036312e-01+\
	    y*z*5.84611025e-02+\
	    y2*1.79631107e-02+\
	    x*-2.92344631e-02+\
	    x*z*-3.33222949e-03+\
	    x*y*-2.12643040e-03+\
	    x2*7.01882306e-05
	y_N2 = output*1.17708759e-02+8.19933526e-01
	return y_N2