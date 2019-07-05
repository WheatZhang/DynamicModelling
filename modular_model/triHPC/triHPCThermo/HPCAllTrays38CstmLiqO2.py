def LiqO2(P,T,x_N2):
	x = (P-5.41016098e+02)/1.23902400e-01
	y = (T--1.78085558e+02)/3.57790000e-03
	z = (x_N2-9.97437801e-01)/4.90805060e-04
	output = \
	    1*-1.19734068e+02+\
	    z*1.19734294e+02+\
	    y*1.20734895e+02+\
	    x*-1.00586148e+02
	x_O2 = output*1.55385915e-05+3.58575089e-05
	return x_O2