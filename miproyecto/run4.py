"""
file: misvariables.py
autor: @naludena1

Deseamos obtener el costo de una carrera universitaria. El valor
promedio de cada ciclo es de $1200, el valor promedio del
seguro educativo por ciclo es de $100 si la edad del estudiante es
<= 20 caso contrario sera de $150. Si el estudiante tiene una modalidad
a distancia el numero de ciclos a seguir es de 10 caso contrario
debera seguir 8 ciclos. Obtener la proyeccion del costo
de la carrera de un estudiante



casos: distancia-18 
       presencial-22

"""


edad = input("Ingrese su edad: ")
edad = int (edad)
modalidad = input("Seleccione su modalidad: \n1.Presencial \n2.Distancia: ")
modalidad = int (modalidad)

if edad <= 20:
	valor = 100
else:
	valor = 150
	if modalidad = 1:
		ciclos = 8
	






