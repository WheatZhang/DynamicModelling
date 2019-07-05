def LiqEtlp(P,T,x_N2):
	x = (P-5.56999512e+02)/3.71707300e-01
	y = (T--1.76911493e+02)/6.36114000e-02
	z = (x_N2-9.01482074e-01)/9.77338450e-03
	output = \
	    1*3.39556583e+00+\
	    z*-3.32344552e+00+\
	    y*-2.48537692e+00+\
	    x*3.68976349e-01
	liq_etlp = output*2.42178564e+01+-1.09435204e+04
	return liq_etlp