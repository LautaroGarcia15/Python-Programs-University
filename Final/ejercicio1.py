import random

def generar_asientos(N):
    asientos = [[0]*6 for i in range(N)]

    return asientos

def imprimir_asientos(matriz):
    letras_columnas = ['A', 'B', 'C', 'D', 'E', 'F']

    print("", end="")
    for letra in letras_columnas:
        print(f"  {letra}", end="")
    print()


    for fila in matriz:
        for elemento in fila:
            print("%3d" %elemento, end="")
        print()

def asignar_asientos(matriz,N):
    try:
        letras_a_indices = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5}
        letras = ['A', 'B', 'C', 'D', 'E', 'F']
        pasajeros = open("E:\\Programacion 1\\Final\\archivo.CSV", "rt")
        
        for linea in pasajeros:
            datos = linea.strip().split(';')

            if len(datos) == 3:
                letra = datos[2]
                asiento = letras_a_indices.get(letra)

                if matriz[int(datos[1])-1][asiento] == 0:

                    matriz[int(datos[1])-1][asiento] = 1
                    print("Pasajero: ", datos[0],", Asiento: ", datos[1] + datos[2])
                    print()
                
                else:
                    print("coalicion en la posicion: ", letra, datos[1])
        
        for linea in pasajeros:
            datos = linea.strip().split(';')

            if len(datos) == 1:

                fila = random.randint(0,N)
                lugar = random.randint(0,5)

                while matriz[fila][lugar] == 1:
                    fila = random.randint(0, N - 1)
                    lugar = random.randint(0, 5)

                matriz[fila][lugar] = 1
                print("Pasajero: ", datos[0], ", Asiento: ", str(fila) + letras[lugar])
                

        print()
        print("Se asignaron todos los asientos: ")

        return matriz
    
    except FileNotFoundError:
        print("No se encontro el archivo: ")

    except OSError as mensaje:
        print("Error: ", mensaje)
    
    finally:
        try:
            pasajeros.close()
        except NameError:
            pass

def mostrar_asientos_libre(asignados):
    letras = ['A', 'B', 'C', 'D', 'E', 'F']
    print("Los asientos libres son: ")

    for fila in range(len(asignados)):
        for columna in range(len(asignados[0])):
            if asignados[fila][columna] == 0:
                print(fila,letras[columna])



N = int(input("Ingrese cantidad de filas: "))
print()
matriz = generar_asientos(N)
#imprimir_asientos(matriz)
asignados = asignar_asientos(matriz,N)
print()
imprimir_asientos(asignados)
print()
mostrar_asientos_libre(asignados)