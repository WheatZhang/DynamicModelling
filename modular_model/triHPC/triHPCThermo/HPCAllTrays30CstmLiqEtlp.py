def LiqEtlp(P,T,x_N2):
	x = (P-5.45910244e+02)/2.47804900e-01
	y = (T--1.77933948e+02)/8.29410000e-03
	z = (x_N2-9.92196920e-01)/1.28159015e-03
	output = \
	    1*9.03167682e+00+\
	    z*-1.02668039e+01+\
	    y*-8.03191044e+00+\
	    x*6.10300657e+00
	liq_etlp = output*1.01078849e+00+-1.08980395e+04
	return liq_etlp