def VapO2(P,T,x_N2):
	x = (P-5.62637073e+02)/2.47804800e-01
	y = (T--1.74564594e+02)/1.00692600e-01
	z = (x_N2-6.85595270e-01)/1.37248686e-02
	x2 = x * x
	y2 = y * y
	z2 = z * z
	output = \
	    1*-1.91121123e+00+\
	    z*2.56222030e+00+\
	    z2*-2.41808299e-02+\
	    y*2.16917636e+00+\
	    y*z*-1.30150095e-02+\
	    y2*-2.68842307e-03+\
	    x*-1.29410653e-01+\
	    x*z*9.68017302e-04+\
	    x*y*3.14734213e-04+\
	    x2*1.31125799e-05
	y_O2 = output*1.06886904e-02+1.40576895e-01
	return y_O2