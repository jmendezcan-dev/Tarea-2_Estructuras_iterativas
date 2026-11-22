# =============================================================
# Archivo     : ejercicio4_expedicion.py
# Curso       : SOFT-01 Principios de Programación 1
# Autor       : Gabriel mendez cantillano
# Fecha       : 22/11/2026
# Versión     : 1.0
# Descripción : Simula el abastecimiento de agua y alimento de
#               una expedición con ciclos for y while, validando
#               consumos e interrumpiendo con break si un
#               recurso se agota antes de terminar.
# =============================================================

# Constantes 
AGUA_INICIAL = 150
ALIMENTO_INICIAL = 100
MIN_JORNADAS = 1
MAX_JORNADAS = 30

# --- Entrada: jornadas planeadas (validación) ---
print("=== Control de abastecimiento de la expedición ===")
jornadas_planeadas = int(input(f"Cantidad de jornadas ({MIN_JORNADAS}-{MAX_JORNADAS}): "))
while jornadas_planeadas < MIN_JORNADAS or jornadas_planeadas > MAX_JORNADAS:
    print("Valor inválido: ingrese un entero entre 1 y 30.")
    jornadas_planeadas = int(input(f"Cantidad de jornadas ({MIN_JORNADAS}-{MAX_JORNADAS}): "))

#  Inicialización
agua_restante = AGUA_INICIAL
alimento_restante = ALIMENTO_INICIAL
agua_total_consumida = 0
alimento_total_consumido = 0
dias_completados = 0

# --- Iteración sobre las jornadas ---
for dia in range(1, jornadas_planeadas + 1):
    # Verificar existencias antes de iniciar la jornada
    if agua_restante == 0 or alimento_restante == 0:
        print("Recursos agotados: no se puede iniciar otra jornada.")
        break

    print(f" Jornada {dia} (agua: {agua_restante} L, alimento: {alimento_restante} u) ")

    # Validación del consumo de agua
    agua_consumida = int(input("Agua consumida (litros): "))
    while agua_consumida <= 0 or agua_consumida > agua_restante:
        print(f"Valor inválido: debe ser positivo y no mayor que {agua_restante} L.")
        agua_consumida = int(input("Agua consumida (litros): "))

    # Validación del consumo de alimento
    alimento_consumido = int(input("Alimento consumido (unidades): "))
    while alimento_consumido <= 0 or alimento_consumido > alimento_restante:
        print(f"Valor inválido: debe ser positivo y no mayor que {alimento_restante} u.")
        alimento_consumido = int(input("Alimento consumido (unidades): "))

    # Proceso: descontar y acumular
    agua_restante = agua_restante - agua_consumida
    alimento_restante = alimento_restante - alimento_consumido
    agua_total_consumida = agua_total_consumida + agua_consumida
    alimento_total_consumido = alimento_total_consumido + alimento_consumido
    dias_completados = dias_completados + 1

    print(f"Saldo: {agua_restante} litros de agua y {alimento_restante} unidades de alimento.")

    # Interrupción anticipada si hay jornadas pendientes
    if (agua_restante == 0 or alimento_restante == 0) and dia < jornadas_planeadas:
        print("Un recurso llegó a cero: la expedición se interrumpe.")
        break

# --- Cálculos finales ---
promedio_agua = agua_total_consumida / dias_completados
promedio_alimento = alimento_total_consumido / dias_completados

if dias_completados == jornadas_planeadas:
    estado = "Expedición completada"
else:
    estado = "Expedición interrumpida por agotamiento de recursos"

# --- Salida ---
print(" INFORME FINAL ")
print(f"Días completados: {dias_completados} de {jornadas_planeadas}")
print(f"Agua consumida: {agua_total_consumida} litros")
print(f"Alimento consumido: {alimento_total_consumido} unidades")
print(f"Agua restante: {agua_restante} litros")
print(f"Alimento restante: {alimento_restante} unidades")
print(f"Promedio diario de agua: {promedio_agua:.2f} litros")
print(f"Promedio diario de alimento: {promedio_alimento:.2f} unidades")
print(f"Estado: {estado}")
