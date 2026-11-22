#Enunciado.
#  Escriba un programa que lea el nombre de un estudiante y sus tres notas parciales 
# (pueden tener decimales), calcule el promedio y lo muestre con dos decimales.
# ----- Entrada -----
nombre_estudiante = input("Ingrese el nombre del estudiante: ")
nota_1 = float(input("Ingrese la nota 1: "))
nota_2 = float(input("Ingrese la nota 2: "))
nota_3 = float(input("Ingrese la nota 3: "))

# ----- Proceso -----
cantidad_notas = 3
suma_notas = nota_1 + nota_2 + nota_3
promedio = suma_notas / cantidad_notas

# ----- Salida -----
print("Estudiante:", nombre_estudiante)
print("Promedio sin formato:", promedio)
print("Promedio con round:", round(promedio, 2))
print("Promedio con format:", format(promedio, ".2f"))