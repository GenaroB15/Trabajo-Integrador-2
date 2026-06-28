def mostrar_tablero(tablero):
    print()
    print(" ", tablero[0], "|", tablero[1], "|", tablero[2])
    print("---+---+---")
    print(" ", tablero[3], "|", tablero[4], "|", tablero[5])
    print("---+---+---")
    print(" ", tablero[6], "|", tablero[7], "|", tablero[8])
    print()


def verificar_ganador(tablero, jugador):
    combinaciones = [
        [0,1,2], [3,4,5], [6,7,8],
        [0,3,6], [1,4,7], [2,5,8],
        [0,4,8], [2,4,6]
    ]

    for c in combinaciones:
        if tablero[c[0]] == tablero[c[1]] == tablero[c[2]] == jugador:
            return True
    return False


def jugar_tateti():
    tablero = ["1","2","3",
               "4","5","6",
               "7","8","9"]

    jugador = "X"
    jugadas = 0

    while True:
        print("\n========== TA-TE-TI ==========")
        mostrar_tablero(tablero)

        try:
            pos = int(input(f"Jugador {jugador}, elija una posición (1-9): ")) - 1
        except:
            print("Ingrese un número.")
            continue

        if pos < 0 or pos > 8:
            print("Posición inválida.")
            continue

        if tablero[pos] == "X" or tablero[pos] == "O":
            print("Esa casilla ya está ocupada.")
            continue

        tablero[pos] = jugador
        jugadas += 1

        if verificar_ganador(tablero, jugador):
            mostrar_tablero(tablero)
            print(f"\n¡¡Ganó el jugador {jugador}!!")
            break

        if jugadas == 9:
            mostrar_tablero(tablero)
            print("\nEmpate.")
            break

        if jugador == "X":
            jugador = "O"
        else:
            jugador = "X"

    input("\nPresione ENTER para volver al menú...")

from random import randint

def ahorcado():

    palabras = ["panadero", "dinosaurio", "helipuerto", "tiburon"]

    palabra = palabras[randint(0, len(palabras) - 1)]

    vidas = 6
    letras_correctas = []
    letras_incorrectas = []

    while vidas > 0:

        print("\nPalabra:")

        gano = True

        for letra in palabra:
            if letra in letras_correctas:
                print(letra, end=" ")
            else:
                print("_", end=" ")
                gano = False

        print("\n")
        print("Vidas:", vidas)
        print("Incorrectas:", letras_incorrectas)

        if gano:
            print("\n¡¡GANASTE!!")
            return

        letra = input("Ingrese una letra: ").lower()

        if len(letra) != 1:
            print("Ingrese solo una letra.")
            continue

        if letra in letras_correctas or letra in letras_incorrectas:
            print("Ya ingresaste esa letra.")
            continue

        if letra in palabra:
            letras_correctas.append(letra)
            print("¡Correcto!")
        else:
            letras_incorrectas.append(letra)
            vidas -= 1
            print("Incorrecto.")

    print("\nPerdiste.")
    print("La palabra era:", palabra)

ahorcado()
def menu():
    opcion = -1

    while opcion != 0:
        print("\n==============================")
        print("      Bienvenido   ")
        print("==============================")
        print("1 - Ta-Te-Ti")
        print("2 - Juego 2")
        print("3 - ahorcado")
        print("4 - Juego 4")
        print("0 - Salir")

        try:
            opcion = int(input("Seleccione una opción: "))
        except:
            print("Ingrese un número válido.")
            continue

        if opcion == 1:
            jugar_tateti()

        elif opcion == 2:
            print("\nJuego en desarrollo...")
            input("Presione ENTER para volver al menú.")

        elif opcion == 3:
          ahorcado()

        elif opcion == 4:
            print("\nJuego en desarrollo...")
            input("Presione ENTER para volver al menú.")

        elif opcion == 0:
            print("\nGracias por jugar.")

        else:
            print("Opción incorrecta.")


menu()
