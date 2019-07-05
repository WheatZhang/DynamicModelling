def LiqEtlp(P,T,x_N2):
	x = (P-5.46529756e+02)/2.47804900e-01
	y = (T--1.77912681e+02)/8.55980000e-03
	z = (x_N2-9.91318725e-01)/1.30032045e-03
	output = \
	    1*9.40178088e+00+\
	    z*-1.05652235e+01+\
	    y*-8.40208752e+00+\
	    x*6.18179558e+00
	liq_etlp = output*9.96554547e-01+-1.08965666e+04
	return liq_etlp