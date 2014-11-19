#!/usr/bin/env python

import scipy as S
import scipy.io as SIO
import pylab

from errorfill import errorfill

def plot_curves(name, curve_matrix):
	pylab.figure()
	pylab.title("All "+name+" Curves")
	for row in curve_matrix:
		pylab.plot(row)
	
	pylab.figure()
	pylab.title("Mean "+name+" curve")
	errorfill(range(curve_matrix.shape[1]), curve_matrix.mean(0), curve_matrix.std(0))

def load_and_plot(aname):
	matlab_dict = SIO.loadmat("./data/" + aname + ".mat")
	data = matlab_dict.get(aname,None)
	if data is None:
		data = matlab_dict.get(aname.upper(),None)
	if data is None:
		print "Could not load_plot " + aname
		return
	plot_curves(aname.upper(), data)

toplot=['dl','erk', 'sna', 'twi', 'vnd', 'ind']
for one_name in toplot:
	load_and_plot(one_name)

pylab.show()
