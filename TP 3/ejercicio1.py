def generar_matriz():
    filas = int(input("Ingrese la cantidad de filas de la matriz: "))
    columnas = int(input("Ingrese la cantidad de columnas de la matriz: "))

    matriz = [[0]*columnas for i in range(filas)]
    return matriz


def imprimir_matriz(matriz_rellenada):
    for fila in matriz_rellenada:
        for elemento in fila: 
            print("%3d" %elemento, end="")
        print()


def rellenar_matriz(matriz):
    filas = len(matriz)
    columnas = len(matriz[0])

    for f in range(filas):
        for c in range(columnas):
            n = int(input("ingrese un numero: "))
            matriz[f][c] = n

    return matriz


def intercambiar_filas(matriz_rellenada):
    fila1 = int(input("Ingrese la fila que desea intercambiar: "))
    fila2 = int(input("Ingrese la fila por la de la desea intercambiar: "))

    matriz_rellenada[fila1], matriz_rellenada[fila2] = matriz_rellenada[fila2], matriz_rellenada[fila1]

    return matriz_rellenada


def intercambiar_columnas(matriz_rellenada):
    columna1 = int(input("Ingrese la columna que desea intercambiar: "))
    columna2 = int(input("Ingrese la columna por la de la desea intercambiar: "))

    for fila in matriz_rellenada:
        fila[columna1], fila[columna2] = fila[columna2], fila[columna1]

    return matriz_rellenada


def trasponer_matriz(matriz_rellenada):
    filas = len(matriz_rellenada)
    columnas = len(matriz_rellenada[0])

    #matriz_transpuesta = [[0 for _ in range(filas)] for _ in range(columnas)]

    for fila in range(filas):
        for columna in range(fila, columnas):
            
            matriz_rellenada[columna][fila],matriz_rellenada[fila][columna] = matriz_rellenada[fila][columna], matriz_rellenada[columna][fila]

    return matriz_rellenada


def promedio_fila(matriz_rellenada, promedio_de_fila):
    for fila in range(len(matriz_rellenada)):
        if fila == promedio_de_fila:
            return sum(matriz_rellenada[fila]) / len(matriz_rellenada[fila])


def columna_impar(matriz_rellenada, por_columna):
    impares = 0
    for fila in range(len(matriz_rellenada)):
        elemento = matriz_rellenada[fila][por_columna]  
        if elemento % 2 != 0:
            impares += 1
      
    return (impares/len(matriz_rellenada))*100
            

def matriz_simetrica_d1(matriz_rellenada, matriz_transpuesta):
    if matriz_rellenada == matriz_transpuesta:
        return True
    return False


def matriz_simetrica_d2(matriz_rellenada): 
    filas = len(matriz_rellenada)
    columnas = len(matriz_rellenada[0])

    matriz_d2 = [[0 for _ in range(filas)] for _ in range(columnas)]

    for fila in range(filas):
        for columna in range(columnas):
            matriz_d2[fila][columna] = matriz_rellenada[columna][fila]

    return matriz_d2



matriz = generar_matriz()
matriz_rellenada = rellenar_matriz(matriz)
print()
imprimir_matriz(matriz_rellenada)


print()
intercambiar_filas(matriz_rellenada)
print("Filas intercambiadas: ")
imprimir_matriz(matriz_rellenada)

print()
intercambiar_columnas(matriz_rellenada)
print("Columnas intercambiadas: ")
imprimir_matriz(matriz_rellenada)


print()
matriz_transpuesta = trasponer_matriz(matriz_rellenada)
print("Matriz transpuesta:")
imprimir_matriz(matriz_transpuesta)

print()
matriz_sim_d2 = matriz_simetrica_d2(matriz_rellenada)
print("Matriz D2 :")
imprimir_matriz(matriz_sim_d2)

promedio_de_fila = int(input("Ingrese el número de fila de la que desea saber el promedio: "))
promedio = promedio_fila(matriz_rellenada, promedio_de_fila)
print("El promedio de la fila ", promedio_de_fila, "es: ", promedio)

por_columna = int(input("Ingrese el valor de la columna de la cual quiere saber el porcentaje: "))
impa = columna_impar(matriz_rellenada, por_columna)
print(impa)

if matriz_simetrica_d1(matriz_rellenada, matriz_transpuesta):
    print("la matriz es simetricra con respecto a su diagonal principal. ")
else:
    print("la matriz NO es simetricra con respecto a su diagonal principal. ")

