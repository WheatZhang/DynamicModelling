def VapEtlp(P,T,x_N2):
	x = (P-5.58858049e+02)/3.71707300e-01
	y = (T--1.76272221e+02)/9.79506000e-02
	z = (x_N2-8.37725053e-01)/1.44673586e-02
	output = \
	    1*2.60060890e+00+\
	    z*-2.76201009e+00+\
	    y*-1.70751346e+00+\
	    x*1.59033578e-01
	vap_etlp = output*2.28032251e+01+-6.03275577e+03
	return vap_etlp