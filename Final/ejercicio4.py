import random

def generar_asientos(N):
    if N<= 30:
        matriz= [[0]*6 for i in range(N)]
    else:
        matriz= [[0]*10 for i in range(N)]
        
    return matriz

def tipo_vuelo(N):
    if N<= 30:
        columnas_dicc={"A":0,"B":1,"C":2,"D":3,"E":4,"F":5}
    else:
        columnas_dicc={"A":0,"B":1,"C":2,"D":3,"E":4,"F":5,"G":6,"H":7,"I":8,"J":9}
    
    return columnas_dicc

def asignar_asientos(matriz,dicc):
    try:
        pasajeros = open("E:\\Programacion 1\\Final\\Vuelos.txt", "rt", encoding="UTF8")

        coaliciones = []
        columnas_letra=["A","B","C","D","E","F","G","H","I","J"]
        print("PASAJEROS ASIGNADOS: ")

        for linea in pasajeros:
            datos = linea.strip().split(';')

            if len(datos) == 3:
                nombre = datos[0]
                fila = int(datos[1])
                columna = dicc[datos[2]]

                print("Pasajero: ", nombre,"Ubicacion: ", str(fila)+str(datos[2]))
                
                if 0 <= fila < len(matriz) and 0 <= columna < len(matriz[0]):
                    if matriz[fila][columna] == 0:
                        matriz[fila][columna] = 1
                    else:
                        coaliciones.append([fila, datos[2]])
            
            elif len(datos) == 1:
                nombre = datos[0]
                fila = random.randint(0,len(matriz)-1)
                columna = random.randint(0,len(dicc)-1)
                
                print("Pasajero: ", nombre,"Ubicacion: ", str(fila)+str(columnas_letra[columna]))

                if 0 <= fila < len(matriz) and 0 <= columna < len(matriz[0]):
                    if matriz[fila][columna] == 0:
                        matriz[fila][columna] = 1
                    else:
                        coaliciones.append([fila, columnas_letra[columna]])
            
        print("El archivo se grabo correctamente.")
        
        return matriz, coaliciones

    except FileNotFoundError:
        print("El archivo no se encontro.")
    except OSError as mensaje:
        print("Error: ", mensaje)
    finally:
        try:
            pasajeros.close()
        except NameError:
            pass

def mostrar_coaliciones(coaliciones):
    for elemento in coaliciones:
        print("Hay coalicion en la posicion: ", str(elemento[0])+str(elemento[1]))

def mostrar_asientos_vacios(matri_final):
    columnas_letras=["A","B","C","D","E","F","G","H","I","J"]
    print("UBICACIONES LIBRES: ")
    for fila in range(len(matri_final)):
        for columna in range(len(matriz[0])):
            if matri_final[fila][columna] == 0:
                print(str(fila)+str(columnas_letras[columna]))


def imprimir_matriz(matriz):
    if len(matriz[0])==6:
            columnas_letra=["A","B","C","D","E","F"]
    elif len(matriz[0])==10:
            columnas_letra=["A","B","C","D","E","F","G","H","I","J"]

    print(end="   " )    
    for i in columnas_letra:
        print(f"  {i}", end="")
    print()

    for i,fila in enumerate(matriz):
        print(i,"|", end="")
        for elemento in fila:
            print("%3d" %elemento, end="")
        print()

N = int(input("Ingese cantidad de filas de la aeronave: "))
matriz = generar_asientos(N)
dicc = tipo_vuelo(N)
matri_final, coaliciones = asignar_asientos(matriz,dicc)
mostrar_coaliciones(coaliciones)
imprimir_matriz(matri_final)
mostrar_asientos_vacios(matri_final)