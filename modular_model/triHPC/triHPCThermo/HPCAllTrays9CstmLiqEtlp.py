def LiqEtlp(P,T,x_N2):
	x = (P-5.58858049e+02)/3.71707300e-01
	y = (T--1.76272221e+02)/9.79506000e-02
	z = (x_N2-8.37112536e-01)/1.44767359e-02
	x2 = x * x
	y2 = y * y
	z2 = z * z
	output = \
	    1*3.18943151e+00+\
	    z*-3.05774501e+00+\
	    z2*2.07914298e-03+\
	    y*-2.28734063e+00+\
	    y*z*-3.45513127e-03+\
	    y2*3.73120376e-03+\
	    x*2.21887748e-01+\
	    x*z*8.24884157e-04+\
	    x*y*-3.21182484e-06+\
	    x2*-7.35489025e-05
	liq_etlp = output*3.95463614e+01+-1.10069583e+04
	return liq_etlp