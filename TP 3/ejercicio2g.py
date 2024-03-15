def generar_matriz(N):
    matriz = [[0]*N for fila in range(N)]
    return matriz

def imprimir_matriz(matriz):
    for fila in matriz:
        for elemento in fila:
            print("%3d" %elemento, end="")
        print()

def rellenar_matriz(matriz, N):
    num = 1
    fila_inicio = 0
    columna_inicio = 0
    fila_final = N - 1  
    columna_final = N - 1  

    while num <= N * N:
        for i in range(columna_inicio, columna_final + 1):
            matriz[fila_inicio][i] = num
            num += 1
        fila_inicio += 1 

        for i in range(fila_inicio, fila_final + 1):
            matriz[i][columna_final] = num
            num += 1
        columna_final -= 1

        for i in range(columna_final, columna_inicio -1,-1):
            matriz[fila_final][i] = num
            num += 1
        fila_final -= 1

        for i in range(fila_final, fila_inicio - 1, -1):
            matriz[i][columna_inicio] = num
            num += 1
        columna_inicio += 1

    return matriz


N = int(input("Ingrese N: "))
matriz = generar_matriz(N)
matriz = rellenar_matriz(matriz,N)
imprimir_matriz(matriz)