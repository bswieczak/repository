#!/usr/bin/env python

import subprocess

kompilacja = subprocess.call(["g++ -o hello hello.cpp"], shell=True)

uruchomienie = subprocess.call(["./hello"], shell=True)

if kompilacja == 0:
	if uruchomienie == 0:
		print "skompilowano i uruchomiono"
	else:
		print "skompilowano, blad uruchomienia"
else:
	print "blad kompilacji"
