import random 
import os
import time
from colorama import init, Fore, Back

registro = []
contador = 0
correctas = 0

def clear_screen():
    # Comprobamos el sistema operativo
    if os.name == 'posix':  
        os.system('clear')
    elif os.name == 'nt': 
        os.system('cls')

def imprimir(matriz):
    init()

    print('-'*87)
    print(f"{Back.BLACK}|{Fore.BLUE}{'Jugadores':^19}| |{'Puntaje':^19}| |{'Dificultad':^19}| |{'Tiempo':^19}|{Fore.RESET}{Back.RESET}")
    print('-'*87)
    bronce = '\033[38;2;205;149;12m'
    colores = [Fore.LIGHTYELLOW_EX, Fore.LIGHTBLACK_EX, bronce]

    for indice, fila in enumerate(matriz):
        color = colores[indice] if indice < len(colores) else Fore.RED
        print(f"{color}|{fila[0]:^19}| |{fila[1]:^19}| |{fila[2]:^19}| |{fila[3]:^19}|{Fore.RESET}")
        print('-'*87)

def chequeo_nombre():
    name = input("Ingrese su nombre de usuario (o escriba 'salir' para terminar): ")
    
    while not (name.isalpha()) or (len(name)<= 2):
        name = input("Ingrese su nombre de usuario (o escriba 'salir' para terminar): ")
        
    return name.capitalize()


def complejidad():
    nivel = input("Seleccione dificultad (Facil/Medio/Dificil): ").lower()
    diccionario_niveles = {'facil':10, 'medio':15, 'dificil':20}

    if nivel in diccionario_niveles:
        return diccionario_niveles[nivel], nivel
    
    else:
        return complejidad()
    

def chequeo_respuesta(opciones):
    cantidad_respuestas = len(opciones)
    respuesta_elegida = ''
    while True: 
        respuesta_elegida = input("Respuesta elegida:")

        if not respuesta_elegida.isdigit():
            print("Debes indexar un numero")
            continue

        if (int(respuesta_elegida) < 1 or int(respuesta_elegida) > cantidad_respuestas):
            print(f"Debes indexar entre 1 y {cantidad_respuestas}")
            continue
        break

    return respuesta_elegida


def calcular_puntos(correctas, cant_preguntas, tiempo):
    puntos_respuestas = correctas * 10
    puntos_tiempo = tiempo * 0.5
    puntos = round(((puntos_respuestas + cant_preguntas) - puntos_tiempo) / 3, 3)
    valor_real = (0 if puntos < 1 else puntos) 
    return valor_real


def rellenar_matriz(nombre, puntaje, dificultad, tiempo, registro):
    registro.append([nombre, puntaje, dificultad, tiempo])
    return registro

def guardar_datos(registro):
    try:
        with open('registro_jugadores.txt', 'a', encoding='utf-8') as archivo:
            archivo.write("Nombre | Puntaje | Dificultad | Tiempo\n")
            archivo.write("-" * 45 + "\n")
            for jugador in registro:
                archivo.write(f"{jugador[0]} | {jugador[1]} | {jugador[2]} | {jugador[3]}\n")
    except Exception as e:
        print(f"Error al guardar los datos en el archivo: {e}")




while True:
    nombre = chequeo_nombre()
    if nombre.lower() == 'salir':
        break

    cantidad_preguntas, dificultad = complejidad()
    preguntas = []
    try:
        archivo = open('preguntas.txt', 'r', encoding='utf-8')
        contador = contador if (contador + cantidad_preguntas) < 531 else 0
        for indice, valor in enumerate(archivo):
            if (indice >= contador) and (indice < (contador + cantidad_preguntas)):
                datos_pregunta = valor.strip().split(';')
                pregunta = datos_pregunta[0]
                opciones = datos_pregunta[1:-1]
                respuesta_correcta = datos_pregunta[-1]
                preguntas.append([pregunta, opciones, respuesta_correcta])

            elif (indice >= (contador + cantidad_preguntas)):
                contador += cantidad_preguntas
                break

    except FileNotFoundError:
        print("El archivo no se encontró. Verifica la ruta y el nombre del archivo.")
    finally:
        archivo.close()

    inicio_tiempo = time.time()

    for pregunta, opciones, respuesta_correcta in preguntas:
        print(f"Pregunta: {pregunta}")
        for index, opcion in enumerate (opciones):
            print(f'{index + 1}. {opcion}')
        
        respuesta = chequeo_respuesta(opciones)

        if respuesta == respuesta_correcta:
            print("Respuesta correcta")
            correctas += 1

        else:
            print(f"Respuesta incorrecta. La respuesta correcta era: {opciones[(int(respuesta_correcta)-1)]}")
        #time.sleep(3)
        clear_screen()

    fin_tiempo = time.time()
    tiempo_total = round(fin_tiempo - inicio_tiempo, 2)

    print(f"El jugador {nombre} a respondido correctamente: {correctas} pregunta/s en un tiempo total de {tiempo_total} ")

    total_puntos = calcular_puntos(correctas, cantidad_preguntas, tiempo_total)
    podio = rellenar_matriz(nombre, total_puntos, dificultad, tiempo_total, registro)
    podio.sort(key = lambda x: x[1], reverse = True)
    
try:
    imprimir(podio)
    guardar_datos(podio)
except NameError:
    print(f'{Fore.RED} -'*20)
    print(f'{Fore.RED}|No se encuentran jugadores en el podio.|{Fore.RED}')
    print(' -'*20)
