#Enunciado. 
# Una plataforma de videos muestra la duración total en minutos. 
# Escriba un programa que lea una cantidad entera de minutos y muestre a cuántas horas y minutos equivale. 
# Ejemplo: 135 minutos equivalen a 2 horas y 15 minutos.
# Problema 5: Convertir minutos a horas y minutos

# ----- Entrada -----
minutos_totales = int(input("Ingrese los minutos totales: "))

# ----- Proceso -----
minutos_por_hora = 60
horas = minutos_totales // minutos_por_hora
minutos_restantes = minutos_totales % minutos_por_hora

# ----- Salida -----
print("Equivale a", horas, "horas y", minutos_restantes, "minutos")