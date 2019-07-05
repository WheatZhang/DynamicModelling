def LiqEtlp(P,T,x_N2):
	x = (P-5.59477561e+02)/3.71707300e-01
	y = (T--1.76004286e+02)/1.08199200e-01
	z = (x_N2-8.11743622e-01)/1.57330980e-02
	output = \
	    1*3.07752943e+00+\
	    z*-3.05966561e+00+\
	    y*-2.28443085e+00+\
	    x*2.02035919e-01
	liq_etlp = output*4.31942949e+01+-1.10326759e+04
	return liq_etlp