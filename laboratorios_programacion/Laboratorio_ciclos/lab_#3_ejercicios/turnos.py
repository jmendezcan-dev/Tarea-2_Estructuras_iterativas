# turnos.
print("=== AGENDA DE TURNOS DEL DÍA ===")
apertura = int(input("Hora de apertura (0 a 23): "))
cierre = int(input("Hora de cierre (0 a 23): "))
while cierre <= apertura:
    print("El cierre debe ser posterior a la apertura.")
    cierre = int(input("Hora de cierre (0 a 23): "))
duracion = int(input("Minutos por turno: "))
 
inicio = apertura * 60                  # minutos desde la medianoche
ultimo_inicio = cierre * 60 - duracion  # el último turno debe terminar a tiempo
 
total_turnos = 0
for minuto in range(inicio, ultimo_inicio + 1, duracion):
    total_turnos += 1
    hora = minuto // 60
    minutos = minuto % 60
    fin = minuto + duracion
    hora_fin = fin // 60
    minutos_fin = fin % 60
    texto_inicio = f"{hora:02d}:{minutos:02d}"
    texto_fin = f"{hora_fin:02d}:{minutos_fin:02d}"
    print(f"Turno {total_turnos:>2}: {texto_inicio} a {texto_fin}")
 
print(f"Turnos disponibles: {total_turnos}")
