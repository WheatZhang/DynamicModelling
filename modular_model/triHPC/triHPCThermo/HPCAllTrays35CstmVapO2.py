def VapO2(P,T,x_N2):
	x = (P-5.42812683e+02)/2.47804900e-01
	y = (T--1.78032390e+02)/7.45390000e-03
	z = (x_N2-9.95543246e-01)/1.02042860e-03
	output = \
	    1*-9.27727520e+01+\
	    z*9.28009487e+01+\
	    y*9.36470183e+01+\
	    x*-7.47234494e+01
	y_O2 = output*1.69448096e-05+4.01955240e-05
	return y_O2