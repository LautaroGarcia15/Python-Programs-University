import random

def crear_matriz(N, M):
    matriz = [[random.randint(0, 99) for c in range(M)] for f in range(N)]
    return matriz

def sumar(matriz, fila, columna):
    if fila == len(matriz):
        return 0  
    
    if columna == len(matriz[fila]):
      
        return sumar(matriz, fila + 1, 0)
    
    
    suma_elemento_actual = matriz[fila][columna]
    suma_resto_fila = sumar(matriz, fila, columna + 1)
    
    return suma_elemento_actual + suma_resto_fila

def imprimir_matriz(matriz):
    for fila in matriz:
        for elemento in fila: 
            print("%3d" %elemento, end="")
        print()

M = int(input("Ingrese M: "))
N = int(input("Ingrese N: "))
matriz = crear_matriz(N, M)
imprimir_matriz(matriz)
resultado = sumar(matriz, 0, 0)  
print("La suma de los elementos de la matriz es:", resultado)
