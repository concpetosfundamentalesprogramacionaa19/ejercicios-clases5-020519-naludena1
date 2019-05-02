"""
file: run.py
autor: @naludena1
"""

from misvariables import *

# uso de condicional simple

nota = input("Ingrese la primera nota")
nota2 = input("Ingrese la primera nota")

nota = int(nota)
nota2 = int(nota2)

if nota >=18:
	print ("%s - %d" % (mensaje, nota))
else:
	print ("%s - %d" % (mensaje2, nota))


if nota2 >=18:
	print ("%s - %d" % (mensaje, nota2))
else:
	print ("%s - %d" % (mensaje2, nota2))

