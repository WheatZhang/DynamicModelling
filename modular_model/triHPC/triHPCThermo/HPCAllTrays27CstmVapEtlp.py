def VapEtlp(P,T,x_N2):
	x = (P-5.47706829e+02)/3.71707300e-01
	y = (T--1.77869974e+02)/1.39084000e-02
	z = (x_N2-9.88731400e-01)/1.89154531e-03
	output = \
	    1*3.69236265e+00+\
	    z*-3.69262805e+00+\
	    y*-2.69249656e+00+\
	    x*1.75122763e+00
	vap_etlp = output*2.01998046e+00+-6.08523550e+03
	return vap_etlp