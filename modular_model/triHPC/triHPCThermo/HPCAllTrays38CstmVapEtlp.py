def VapEtlp(P,T,x_N2):
	x = (P-5.41016098e+02)/1.23902400e-01
	y = (T--1.78085558e+02)/3.57790000e-03
	z = (x_N2-9.97437801e-01)/4.90805060e-04
	output = \
	    1*3.69061491e+00+\
	    z*-3.69062834e+00+\
	    y*-2.69067194e+00+\
	    x*2.28642735e+00
	vap_etlp = output*5.24165359e-01+-6.09359097e+03
	return vap_etlp