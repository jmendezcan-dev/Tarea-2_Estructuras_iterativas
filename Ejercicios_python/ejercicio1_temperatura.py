# =============================================================
# Archivo     : ejercicio1_temperatura.py
# Curso       : SOFT-01 Principios de Programación 1
# Autor       : Gabriel mendez cantillano
# Fecha       : 22/11/2026
# Versión     : 1.0
# Descripción : Simula el calentamiento de una cámara
#               experimental con un ciclo while, mostrando la
#               temperatura de cada ciclo y el total de ciclos.
# =============================================================

# --- Entrada ---
print(" Control de temperatura de la cámara experimental ")
temperatura_inicial = float(input("Temperatura inicial (°C): "))
temperatura_objetivo = float(input("Temperatura objetivo (°C): "))
incremento = float(input("Incremento por ciclo (°C): "))

# --- Validación de la configuración ---
if temperatura_objetivo <= temperatura_inicial:
    print("Configuración inválida: el objetivo debe ser mayor que la temperatura inicial.")
elif incremento <= 0:
    print("Configuración inválida: el incremento debe ser mayor que cero.")
else:
    # --- Inicialización del ciclo ---
    temperatura_actual = temperatura_inicial
    ciclos = 0

    print("Iniciando calentamiento...")
    # --- Iteración: continúa mientras no se alcance el objetivo ---
    while temperatura_actual < temperatura_objetivo:
        temperatura_actual = temperatura_actual + incremento  # actualización
        ciclos = ciclos + 1
        print(f"Ciclo {ciclos}: {temperatura_actual} °C")

    # --- Salida ---
    print(" Resultado final ")
    print(f"Temperatura alcanzada: {temperatura_actual} °C")
    print(f"Total de ciclos: {ciclos}")
