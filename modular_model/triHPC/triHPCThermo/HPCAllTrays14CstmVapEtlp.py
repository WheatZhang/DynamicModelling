def VapEtlp(P,T,x_N2):
	x = (P-5.55760488e+02)/3.71707300e-01
	y = (T--1.77199707e+02)/4.48098000e-02
	z = (x_N2-9.31022717e-01)/7.67438050e-03
	output = \
	    1*2.72324902e+00+\
	    z*-3.07164849e+00+\
	    y*-1.72389421e+00+\
	    x*3.47256757e-01
	vap_etlp = output*1.01938238e+01+-6.05953573e+03
	return vap_etlp