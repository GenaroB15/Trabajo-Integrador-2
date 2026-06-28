import random

# --------------------------------------------------
# Juego
# --------------------------------------------------

def cuantos_conoces_los_numeros():
    puntos = 0

    print("\n********************************")
    print("CUANTO CONOCES LOS NUMEROS?")
    print("********************************")

    nombre = input("\nIngresa tu nombre: ").strip()
    while not nombre:
        print("El nombre no puede estar vacio.")
        nombre = input("Ingresa tu nombre: ").strip()

    print("\nElegi dificultad:")
    print("1- Facil   (suma y resta, numeros hasta 10, 5 preguntas)")
    print("2- Medio   (suma, resta y multiplicacion, hasta 50, 7 preguntas)")
    print("3- Dificil (todas las operaciones, hasta 100, 10 preguntas)")

    while True:
        dificultad = input("Opcion: ").strip()
        if dificultad == "1":
            maximo      = 10
            operaciones = ["+", "-"]
            cantidad    = 5
            break
        elif dificultad == "2":
            maximo      = 50
            operaciones = ["+", "-", "*"]
            cantidad    = 7
            break
        elif dificultad == "3":
            maximo      = 100
            operaciones = ["+", "-", "*", "/"]
            cantidad    = 10
            break
        else:
            print("Opcion invalida. Ingresa 1, 2 o 3.")

    for i in range(cantidad):
        num1      = random.randint(1, maximo)
        num2      = random.randint(1, maximo)
        operacion = random.choice(operaciones)

        if operacion == "+":
            resultado = num1 + num2
        elif operacion == "-":
            resultado = num1 - num2
        elif operacion == "*":
            resultado = num1 * num2
        else:
            num1      = num1 * num2
            resultado = num1 // num2

        correcta = random.choice([True, False])

        if correcta:
            respuesta_mostrada = resultado
        else:
            desvio             = random.randint(1, 10) * random.choice([1, -1])
            respuesta_mostrada = resultado + desvio
            if respuesta_mostrada == resultado:
                respuesta_mostrada += 1

        print(f"\nPregunta {i+1} de {cantidad}")
        print(f"Cuanto es {num1} {operacion} {num2}?")
        print(f"Respuesta: {respuesta_mostrada}")
        print("1- Es correcto")
        print("2- Es incorrecto")
        print("3- Salir")

        while True:
            opcion = input("Elegi: ").strip()
            if opcion in ["1", "2", "3"]:
                break
            print("Opcion invalida. Ingresa 1, 2 o 3.")

        if opcion == "3":
            print("Saliste del juego.")
            break

        if (opcion == "1" and correcta) or (opcion == "2" and not correcta):
            print("Correcto! +10 puntos")
            puntos += 10
        else:
            if correcta:
                print(f"Incorrecto. La respuesta {respuesta_mostrada} era correcta.")
            else:
                print(f"Incorrecto. La respuesta {respuesta_mostrada} era falsa. El resultado real es {resultado}.")

    print("\nJuego terminado")
    print(f"Puntaje final: {puntos} pts")
    return nombre, puntos


cuantos_conoces_los_numeros()