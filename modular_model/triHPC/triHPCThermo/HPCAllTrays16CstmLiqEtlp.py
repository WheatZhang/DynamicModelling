def LiqEtlp(P,T,x_N2):
	x = (P-5.54521463e+02)/3.71707300e-01
	y = (T--1.77417593e+02)/4.69959000e-02
	z = (x_N2-9.51559553e-01)/5.66992393e-03
	output = \
	    1*5.32459856e+00+\
	    z*-4.68511345e+00+\
	    y*-4.58816880e+00+\
	    x*9.17886051e-01
	liq_etlp = output*9.86042926e+00+-1.09007201e+04
	return liq_etlp