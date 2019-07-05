def VapEtlp(P,T,x_N2):
	x = (P-5.51361951e+02)/4.95609800e-01
	y = (T--1.77699350e+02)/2.96411000e-02
	z = (x_N2-9.76663628e-01)/3.93187149e-03
	output = \
	    1*3.85845378e+00+\
	    z*-3.85235442e+00+\
	    y*-2.85886670e+00+\
	    x*1.15921470e+00
	vap_etlp = output*4.04720869e+00+-6.07760319e+03
	return vap_etlp