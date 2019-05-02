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

"""

# variables
ciclo = 1200
seguroUno = 100
seguroDos = 150
costoCarrera = 0

# ingreso de datos
modalidad = input("Seleccione su modalidad: \n1.Presencial \n2.Distancia: ")
modalidad = int (modalidad)

edad = input("Ingrese su edad:")
edad = int (edad)


# cálculos
if (modalidad == 1) and (edad <= 20 ):
	costoCarrera = (seguroUno * 8) + (ciclo * 8)
	print ("El costo de su carrera es: %d" % (costoCarrera))
else:
	if (modalidad == 1) and (edad > 20 ):
		costoCarrera = (seguroDos * 8) + (ciclo * 8)
		print ("El costo de su carrera es: %d" % (costoCarrera))
	else:
		if (modalidad == 2) and (edad <= 20 ):
			costoCarrera = (seguroUno * 10) + (ciclo * 10)
			print ("El costo de su carrera es: %d" % (costoCarrera))
		else:
			if (modalidad == 2) and (edad > 20):
				costoCarrera = (seguroDos * 10) + (ciclo * 10)
				print ("El costo de su carrera es: %d" % (costoCarrera))




	











	






