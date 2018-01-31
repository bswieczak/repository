#!/usr/bin/env python

import subprocess
import os

def utworzFoldery(struktura):
	podfolder = 0
	nazwaPodfolderu = ""
	for i in range(len(struktura)):
		wystapienia = struktura[i].count("\t")
		if wystapienia == 0:
			while podfolder != 0:
				podfolder -= 1
				os.chdir("../")
			subprocess.call(["mkdir " + struktura[i]], shell=True)
			nazwaPodfolderu = struktura[i]
		else:
			if podfolder == wystapienia:
				subprocess.call(["mkdir " + struktura[i]], shell=True)
				podfolder = wystapienia
			elif wystapienia > podfolder:
				podfolder = wystapienia
				os.chdir(os.getcwd() + "/" +  nazwaPodfolderu)
				subprocess.call(["mkdir " + struktura[i]], shell=True)
			else:
				while podfolder > wystapienia:
					podfolder -= 1
					os.chdir("../")
				subprocess.call(["mkdir " + struktura[i]], shell=True)
			nazwaPodfolderu = struktura[i].replace("\t", "")
struktura = '''K1
	K2
	K3
		K4
	K8
K5
	K6'''



utworzFoldery(struktura.split("\n"))
