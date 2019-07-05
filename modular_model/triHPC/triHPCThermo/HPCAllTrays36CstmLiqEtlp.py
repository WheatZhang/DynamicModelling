def LiqEtlp(P,T,x_N2):
	x = (P-5.42193171e+02)/2.47804900e-01
	y = (T--1.78050970e+02)/7.34360000e-03
	z = (x_N2-9.96060985e-01)/1.00746068e-03
	output = \
	    1*8.59906471e+00+\
	    z*-8.59911185e+00+\
	    y*-7.59918360e+00+\
	    x*6.55044120e+00
	liq_etlp = output*9.47614725e-01+-1.09065180e+04
	return liq_etlp