def generar_cuadrado(N):
    matriz = [[0]*N for i in range(N)]
    for f in range(len(matriz)):
        for c in range(len(matriz[0])):
            n = int(input("ingrese un numero: "))
            matriz[f][c] = n
        
    return matriz

def imprimir_matriz(matriz):
    for fila in matriz:
        for elemento in fila:
            print("%3d" %elemento, end="")
        print()

def es_magico(matriz):
    #filas
    suma_fila = []
    for f in range(len(matriz)):
        suma_fila.append(sum(matriz[f]))
    
    if max(suma_fila) != min(suma_fila):
        return False
    

    #columnas
    columnas = []
    for c in range(len(matriz)):
        suma_columnas = 0
        for f in range(len(matriz[0])):
            suma_columnas += matriz[f][c]
        columnas.append(suma_columnas)
    if max(columnas) != min(columnas):
        return False

    #diagonales
    principal = 0
    secundaria = 0
    for f in range(len(matriz)):
        principal += matriz[f][f]
        secundaria += matriz[f][len(matriz)- f -1]
    
    if principal != secundaria:
        return False
    
    return True

N = int(input("Ingrese la cantidad de filas y columnas: "))
matriz = generar_cuadrado(N)
imprimir_matriz(matriz)

if es_magico(matriz):
    print("Es un cuadrado magico. ")
else:
    print("NO es un cuadrado magico. ")