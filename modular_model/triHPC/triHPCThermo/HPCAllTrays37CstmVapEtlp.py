def VapEtlp(P,T,x_N2):
	x = (P-5.41573658e+02)/2.47804900e-01
	y = (T--1.78069279e+02)/7.24480000e-03
	z = (x_N2-9.96540601e-01)/9.95332218e-04
	output = \
	    1*3.61781464e+00+\
	    z*-3.61796545e+00+\
	    y*-2.61787205e+00+\
	    x*2.19644167e+00
	vap_etlp = output*1.06929380e+00+-6.09306840e+03
	return vap_etlp