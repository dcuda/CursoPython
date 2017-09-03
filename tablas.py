# -*- coding:utf-8 -*-

# dado un nro natural imprimir su tabla de multiplicar desarrollada con sumas sucesivas
# si se ingresa "0" no genera las sumas sucesivas
nro = int(raw_input("Ingrese el numero: "))
if nro:
	for j in range(1,11):
		for i in range(1,j):
				print str(nro),"+",
		print str(nro),"=", nro*j
	
