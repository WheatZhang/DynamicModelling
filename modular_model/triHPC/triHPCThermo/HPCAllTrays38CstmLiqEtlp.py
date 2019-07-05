def LiqEtlp(P,T,x_N2):
	x = (P-5.41016098e+02)/1.23902400e-01
	y = (T--1.78085558e+02)/3.57790000e-03
	z = (x_N2-9.97437801e-01)/4.90805060e-04
	output = \
	    1*8.70963602e+00+\
	    z*-8.70966035e+00+\
	    y*-7.70970851e+00+\
	    x*6.82808381e+00
	liq_etlp = output*4.58074241e-01+-1.09090652e+04
	return liq_etlp