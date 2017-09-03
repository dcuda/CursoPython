# -*- coding:utf-8 -*-

# dado un nro natural imprimir su factorial

nro = int(raw_input("Ingrese el numero: "))
nroaux = nro

if nro:
	for j in range(1,nro):
			nroaux = nroaux * j
	print str(nro),"! =", str(nroaux)#= 1"
		
else:
	print "0 ! = 1"
			

