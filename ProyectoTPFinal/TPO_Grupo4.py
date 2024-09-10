import random 
import os
import time
from colorama import init, Fore, Back

registro = []
cont = random.randint(0, 531)
comenzado = False

def mostrar_historial():
    try:
        historial =  open('historial.txt', 'r', encoding='utf-8')
        historial_data = [line.strip().split(';') for line in historial]
        historial_data.sort(key=lambda x: float(x[1]), reverse=True)
        for datos in historial_data:
            print(f"Nombre: {datos[0]}, Puntaje: {datos[1]}, Dificultad: {datos[2]}, Tiempo: {datos[3]}")
    except FileNotFoundError:
        print("El archivo de historial no se encontró.")

def guardar_historial(registros):
    # Guardamos el historial en base a nombre, puntaje, dificultad y tiempo.
    try:
        histo = open('historial.txt', 'a', encoding='utf-8')
        for registro in registros:
            nombre, puntaje, dificultad, tiempo = registro
            histo.write(f"{nombre};{puntaje};{dificultad};{tiempo}\n")
    except FileNotFoundError:
        print("El archivo de historial no se encontró.")

def imprimir(matriz):
    # Imprimimos la matriz con sus respectivas posiciones

    init()
    print('-'*109)
    print(f"{Fore.BLUE}|{'Posicion':^19}| |{Fore.BLUE}{'Jugadores':^19}| |{'Puntaje':^19}| |{'Dificultad':^19}| |{'Tiempo':^19}|{Fore.RESET}{Back.RESET}")
    print('-'*109)
    bronce = '\033[38;2;205;149;12m'
    colores = [Fore.LIGHTYELLOW_EX, Fore.LIGHTBLACK_EX, bronce]

    for indice, fila in enumerate(matriz):
        color = colores[indice] if indice < len(colores) else Fore.RED
        print(f"{color}|{(indice + 1):^19}| |{fila[0]:^19}| |{fila[1]:^19}| |{fila[2]:^19}| |{fila[3]:^19}|{Fore.RESET}")
        print('-'*109)
    time.sleep(7)



def rellenar_matriz(nombre, puntaje, dificultad, tiempo, registro):
    # Rellenamos la matriz
    registro.append([nombre, puntaje, dificultad, tiempo])
    return registro


def calcular_puntos(acertadas, cant_preguntas, tiempo):
    # Calculamos los puntos en base a respuestas correctas, dificultad y tiempo.
    puntos_respuestas = acertadas * 20
    puntos_tiempo = tiempo * 0.5
    puntos = round(((puntos_respuestas + cant_preguntas) - puntos_tiempo) / 3, 3)
    valor_real = (0 if puntos < 1 else puntos) 
    return valor_real


def chequeo_respuesta(opciones):
    # Chequear que la respuesta no se vaya de rango y sea un digito aceptado.
    cantidad_respuestas = len(opciones)
    respuesta_elegida = ''
    while True:
        respuesta_elegida = input("\nRespuesta elegida: ")

        if not respuesta_elegida.isdigit():
            print("Debes indexar un numero")
            continue

        if (int(respuesta_elegida) < 1) or (int(respuesta_elegida) > cantidad_respuestas):
            print(f"Debes indexar entre 1 y {cantidad_respuestas}")
            continue
        break
    return respuesta_elegida


def preguntados(preguntas):
    #Mostramos sus preguntas con sus respectivas opciones.
    acertadas = 0
    for pregunta, opciones, respuesta_correcta in preguntas:
        print(f"Pregunta: {pregunta}")
        for index, opcion in enumerate (opciones):
            print(f'{index + 1}. {opcion}')
        
        respuesta = chequeo_respuesta(opciones)

        if respuesta == respuesta_correcta:
            print("Respuesta correcta")
            acertadas += 1

        else:
            print(f"Respuesta incorrecta. La respuesta correcta era: {opciones[(int(respuesta_correcta)-1)]}")
        time.sleep(3)
        clear_screen()
    return acertadas


def matriz_preguntas(cant_preguntas, contador, archivo):
    # Seleccionar preguntas del archivo.
    cuestionario = []
    contador = contador if (contador + cant_preguntas) <= 530 else 0
    for indice, valor in enumerate(archivo):
        if (indice >= contador) and (indice < (contador + cant_preguntas)):
            datos_pregunta = valor.strip().split(';')
            pregunta = datos_pregunta[0]
            opciones = datos_pregunta[1:-1]
            respuesta_correcta = datos_pregunta[-1]
            cuestionario.append([pregunta, opciones, respuesta_correcta])

        elif (indice >= (contador + cant_preguntas)):
            contador += cant_preguntas
            archivo.seek(0)
            break
    
    return cuestionario, contador


def complejidad():
    # Realizamos recursividad para obtener el nivel del jugador.
    nivel = input("Seleccione dificultad (Facil/Medio/Dificil): ").lower()
    diccionario_niveles = {'facil':10, 'medio':15, 'dificil':20}

    if nivel in diccionario_niveles:
        return diccionario_niveles[nivel], nivel
    else:
        return complejidad()
    

def chequeo_nombre():
    # Se realiza un check para obtener un nombre pertinente.
    name = input("Ingrese su nombre de usuario: ")
    
    while not (name.isalpha()) or (len(name)<= 2):
        name = input("Ingrese su nombre de usuario: ")
        
    return name.capitalize() 


def clear_screen():
    # Comprobamos el sistema operativo para limpiar la consola
    if os.name == 'posix':  
        os.system('clear')
    elif os.name == 'nt': 
        os.system('cls')

try:
    archivo = open('ProyectoTPFinal/preguntas.txt', 'r', encoding='utf-8')
except FileNotFoundError:
    print("El archivo no se encontró. Verifica la ruta y el nombre del archivo.")

while True:
    clear_screen()
    if comenzado:
        print('Indexa "s" o "salir" si deseas finalizar el juego o culquier tecla para continuar jugando.')
        interrogatorio = input('Deseas salir?: ')
        if (interrogatorio.lower() == 'salir') or (interrogatorio.lower() == 's') :
            try:
                archivo.close()
            except FileNotFoundError:
                print("El archivo no se encontró. Verifica la ruta y el nombre del archivo.")
            break
    comenzado = True

    clear_screen()
    nombre = chequeo_nombre() 

    clear_screen()
    cantidad_preguntas, dificultad = complejidad()

    clear_screen()
    preguntas, cont = matriz_preguntas(cantidad_preguntas, cont, archivo)

    inicio_tiempo = time.time()
    correctas = preguntados(preguntas)
    fin_tiempo = time.time()
    tiempo_total = round(fin_tiempo - inicio_tiempo, 2)

    print(f"El jugador {nombre} a respondido correctamente: {correctas} pregunta/s en un tiempo total de {tiempo_total} ")

    total_puntos = calcular_puntos(correctas, cantidad_preguntas, tiempo_total)
    podio = rellenar_matriz(nombre, total_puntos, dificultad, tiempo_total, registro)
    podio.sort(key = lambda x: x[1], reverse = True)
    
try:
    imprimir(podio)
except NameError:
    print(f'{Fore.RED} -'*20)
    print(f'{Fore.RED}|No se encuentran jugadores en el podio.|{Fore.RED}')
    print(f' -'*20 )
    
    
if len(registro) > 0:
    guardar_historial(registro)

print(f"{Fore.RESET}EL HISTORIAL DE JUGADORES: ")
mostrar_historial()

