def generar_matriz(N):
    matriz = [[0]*N for fila in range(N)]
    return matriz

def imprimir_matriz(matriz):
    for fila in matriz:
        for elemento in fila:
            print("%3d" %elemento, end="")
        print()

def rellenar_matriz(matriz):
    num = 0.5
    for f in range(len(matriz)):
        num *= 2
        for c in range(len(matriz[0])):
            matriz[len(matriz)-f-1][c] = num
            
    return matriz

N = int(input("Ingrese N: "))
matriz = generar_matriz(N)
matriz = rellenar_matriz(matriz)
imprimir_matriz(matriz)