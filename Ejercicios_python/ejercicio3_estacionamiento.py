# =============================================================
# Archivo     : ejercicio3_estacionamiento.py
# Curso       : SOFT-01 Principios de Programación 1
# Autor       : Gabriel mendez cantillano
# Fecha       : 22/11/2026
# Versión     : 1.0
# Descripción : Sistema de consola para administrar un
#               estacionamiento de 20 espacios mediante un menú
#               repetitivo (while True) y condicional múltiple.
# =============================================================

# Constantes
CAPACIDAD_TOTAL = 20
TARIFA_HORA = 800

# Inicialización 
vehiculos_dentro = 0
salidas_registradas = 0
recaudacion_total = 0

#Menú repetitivo
while True:
    print("==== ESTACIONAMIENTO ====")
    print("1. Registrar ingreso")
    print("2. Registrar salida")
    print("3. Consultar ocupación")
    print("4. Consultar recaudación")
    print("5. Salir")
    opcion = input("Seleccione una opción: ")

    # --- Decisión múltiple ---
    if opcion == "1":
        if vehiculos_dentro < CAPACIDAD_TOTAL:
            vehiculos_dentro = vehiculos_dentro + 1
            print("Ingreso registrado.")
        else:
            print("No hay espacios disponibles.")

    elif opcion == "2":
        if vehiculos_dentro == 0:
            print("No hay vehículos en el estacionamiento.")
        else:
            # Validación de horas (entero > 0)
            horas = int(input("Horas a cobrar: "))
            while horas <= 0:
                print("Valor inválido: las horas deben ser mayores que cero.")
                horas = int(input("Horas a cobrar: "))

            pago = horas * TARIFA_HORA
            vehiculos_dentro = vehiculos_dentro - 1
            salidas_registradas = salidas_registradas + 1
            recaudacion_total = recaudacion_total + pago
            print(f"Salida registrada. Monto a pagar: ₡{pago}")

    elif opcion == "3":
        espacios_libres = CAPACIDAD_TOTAL - vehiculos_dentro
        print(f"Espacios ocupados: {vehiculos_dentro}")
        print(f"Espacios libres: {espacios_libres}")

    elif opcion == "4":
        print(f"Recaudación total: ₡{recaudacion_total}")
        print(f"Vehículos que han salido: {salidas_registradas}")

    elif opcion == "5":
        espacios_libres = CAPACIDAD_TOTAL - vehiculos_dentro
        print("Resumen final")
        print(f"Espacios ocupados: {vehiculos_dentro}")
        print(f"Espacios libres: {espacios_libres}")
        print(f"Salidas procesadas: {salidas_registradas}")
        print(f"Recaudación total: ₡{recaudacion_total}")
        break

    else:
        print("Opción inexistente. Intente nuevamente.")
