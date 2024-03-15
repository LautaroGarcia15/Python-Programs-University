def generar_matriz(N):
    matriz = [[0] * N for fila in range(N)]
    return matriz

def imprimir_matriz(matriz):
    for fila in matriz:
        for elemento in fila:
            print("%3d" % elemento, end="")
        print()

def rellenar_matriz(matriz):
    num = 1
    for suma_abajo in range(N - 1, -N, -1):
        for fila in range(N):
            columna = suma_abajo + fila
            if 0 <= columna < N:
                matriz[fila][columna] = num
                num += 1
    return matriz

N = int(input("Ingrese N: "))
matriz = generar_matriz(N)
matriz = rellenar_matriz(matriz)
imprimir_matriz(matriz)
