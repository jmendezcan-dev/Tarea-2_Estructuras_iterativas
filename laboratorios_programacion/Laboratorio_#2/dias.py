# Dias

dia = int(input("Ingresa un número de día (1-7): ")) #input() siempre devuelve texto (str). Como vamos a comparar contra números, lo convertimos con int().
match dia:                                           # match dia: toma el número ingresado como valor a evaluar.
    case 1: #case 1: … case 5: comparan contra un valor exacto (patrón literal). Si dia vale 3, se imprime “Miércoles” y no se revisa ningún otro caso.
        print("Lunes")
    case 2:
        print("Martes")
    case 3:
        print("Miércoles")
    case 4:
        print("Jueves")
    case 5:
        print("Viernes")
    case 6 | 7:                                    #case 6 | 7: agrupa dos valores con |. Tanto 6 como 7 imprimen “Fin de semana”.                                       
        print("Fin de semana")
    case _:                                      #•	case _: atrapa cualquier otro número (0, 8, -2, 100…) e imprime un mensaje de error
        print("Número de día no válido")
