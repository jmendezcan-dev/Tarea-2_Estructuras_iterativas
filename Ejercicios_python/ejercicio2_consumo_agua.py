# =============================================================
# Archivo     : ejercicio2_consumo_agua.py
# Curso       : SOFT-01 Principios de Programación 1
# Autor       : Gabriel mendez cantillano
# Fecha       : 22/11/2026
# Versión     : 1.0
# Descripción : Registra el consumo de agua de siete días con un
#               ciclo for y calcula total, promedio, máximo y
#               días que superan el umbral de referencia.
# =============================================================

#Constantes 
DIAS_SEMANA = 7
UMBRAL_LITROS = 150

#Inicialización de acumuladores y contadores 
consumo_total = 0
consumo_maximo = 0
dias_sobre_umbral = 0

print(" Registro semanal de consumo de agua ")

# --- Iteración: cantidad de días conocida ---
for dia in range(1, DIAS_SEMANA + 1):
    # Entrada con validación (valores >= 0)
    consumo_dia = float(input(f"Día {dia} - consumo (litros): "))
    while consumo_dia < 0:
        print("Valor inválido: el consumo no puede ser negativo.")
        consumo_dia = float(input(f"Día {dia} - consumo (litros): "))

    # Proceso
    consumo_total = consumo_total + consumo_dia
    if consumo_dia > consumo_maximo:
        consumo_maximo = consumo_dia
    if consumo_dia > UMBRAL_LITROS:
        dias_sobre_umbral = dias_sobre_umbral + 1

# --- Cálculo del promedio ---
promedio_diario = consumo_total / DIAS_SEMANA

# --- Salida ---
print(" Resumen semanal ")
print(f"Consumo total: {consumo_total:.2f} litros")
print(f"Promedio diario: {promedio_diario:.2f} litros")
print(f"Mayor consumo: {consumo_maximo:.2f} litros")
print(f"Días que superaron {UMBRAL_LITROS} litros: {dias_sobre_umbral}")
