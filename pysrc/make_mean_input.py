#!/usr/bin/env python

import scipy as S
import scipy.io as SIO

import sys

import os.path

from factor import *

def load_data(aname,adir=None,mean=False,normalize=True):
	filename = aname.lower()
	if adir != None:
		filename = os.path.join(adir, filename)

	matlab_dict = SIO.loadmat(filename + ".mat")
	data = matlab_dict.get(aname,None)
	if data is None:
		data = matlab_dict.get(aname.upper(),None)
	if data is None:#still none
		raise Exception("could not load data for " + aname)
	if mean:
		data = data.mean(0)
		if normalize:
			data /= data.max()
		data = data.reshape(1,-1)

	
	return data



#all=['dl','erk', 'sna', 'twi', 'vnd', 'ind']
output='ind'

inputs1=['dl']
special1=['vfl','cic']
inputs2=['sna', 'Vnd']

foo = [(n, load_data(n,"full_data",mean=True)) for n in inputs1]
len=foo[0][1].shape[1]

foo.extend([(n,S.ones((1,len))) for n in special1])

foo.extend([(n, load_data(n,"full_data",mean=True)) for n in inputs2])


F = FactorExpr()

for name, samples in foo:
	F.add(name.lower(), samples)

F.write(sys.argv[1])

E = FactorExpr()
E.add('dperk',load_data("erk","full_data",mean=True))
E.write(sys.argv[2])

EXP = FactorExpr()
EXP.add('ind', load_data('ind','full_data',mean=True))
EXP.write(sys.argv[3])
