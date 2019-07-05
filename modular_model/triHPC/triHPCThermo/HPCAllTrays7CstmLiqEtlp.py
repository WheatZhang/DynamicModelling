def LiqEtlp(P,T,x_N2):
	x = (P-5.60097073e+02)/3.71707300e-01
	y = (T--1.75716179e+02)/1.16025133e-01
	z = (x_N2-7.84620737e-01)/1.65897362e-02
	output = \
	    1*3.00441988e+00+\
	    z*-2.96288769e+00+\
	    y*-2.20797792e+00+\
	    x*1.82735144e-01
	liq_etlp = output*4.72736909e+01+-1.10602577e+04
	return liq_etlp