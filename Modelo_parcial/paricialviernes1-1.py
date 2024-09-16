def generar_matriz(N):
    matriz = [[0]*N for fila in range(N)]
    return matriz

def rellenar_matriz(matriz):
    num = 1
    for c in range(len(matriz)):
        for f in range(len(matriz[0])):
            if c % 2 == 0:
                matriz[f][c] = num
                num += 1
            elif c % 2 != 0:
                matriz[len(matriz)-f-1][c] = num
                num += 1
            

def imprimir_matriz(matriz):
    for fila in matriz:
        for elemento in fila:
            print("%3d" %elemento, end="")
        print()

N = int(input("Ingrese N:"))
matriz = generar_matriz(N)
rellenar_matriz(matriz)
imprimir_matriz(matriz)