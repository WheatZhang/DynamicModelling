def LiqEtlp(P,T,x_N2):
	x = (P-5.38538049e+02)/8.26016000e-02
	y = (T--1.78154406e+02)/4.44600000e-04
	z = (x_N2-9.99124757e-01)/2.75160732e-04
	output = \
	    1*4.08397617e+00+\
	    z*-1.57034958e+01+\
	    y*-3.08402052e+00+\
	    x*1.47036440e+01
	liq_etlp = output*1.41755738e-01+-1.09140636e+04
	return liq_etlp