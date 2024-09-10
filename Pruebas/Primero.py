import random
import time

def agregar_puntaje(nombre, correctas, dificultad, registros, tiempo):
    registros.append([nombre, correctas, dificultad, tiempo])

registros = []  

while True:
    nombre = input("Ingrese su nombre de usuario (o escriba 'salir' para terminar): ").capitalize()
    if nombre.lower() == 'salir':
        break

    while True:
        dificultad = input("Seleccione dificultad (Facil/Medio/Dificil): ").lower()
        
        if dificultad == 'facil':
            cantidad_preguntas = 10
            break
        elif dificultad == 'medio':
            cantidad_preguntas = 15
            break
        elif dificultad == 'dificil':
            cantidad_preguntas = 20 
            break
        else:
            print("La dificultad seleccionada no es válida. Por favor, elija 'facil', 'medio' o 'dificil'.")

    archivo = open('preguntas.txt', 'r', encoding='utf-8')

    preguntas = []

    for i in archivo:
        datos_pregunta = i.strip().split(';')
        pregunta = datos_pregunta[0]
        opciones = datos_pregunta[1:-1] 
        respuesta_correcta = datos_pregunta[-1]
        preguntas.append((pregunta, opciones, respuesta_correcta))

    archivo.close()

    random.shuffle(preguntas)
    preguntas = preguntas[:cantidad_preguntas]

    correctas = 0
    inicio_tiempo = time.time()

    for pregunta, opciones, respuesta_correcta in preguntas:
        print(f"Pregunta: {pregunta}")
        for opcion in opciones:
            print(opcion)

        respuesta = input("Seleccione la opción correcta mediante un número entero: ")

        if respuesta == respuesta_correcta:
            print("Respuesta correcta")
            correctas += 1
        else:
            print(f"Respuesta incorrecta. La respuesta correcta era: {opciones[int(respuesta_correcta)-1]}")

    fin_tiempo = time.time()
    tiempo_total = fin_tiempo - inicio_tiempo

    print(f"Respuestas correctas: {correctas}")
    print(f"Tiempo total: {tiempo_total:.2f} segundos")

    agregar_puntaje(nombre, correctas, dificultad, registros, tiempo_total)

print("Registros de los jugadores:")
for registro in registros:
    nombre, correctas, dificultad, tiempo = registro
    print(f"Jugador: {nombre}, Respuestas correctas: {correctas}, Dificultad: {dificultad}, Tiempo: {tiempo:.2f} segundos")
