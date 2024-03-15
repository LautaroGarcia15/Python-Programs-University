def generar_matriz(N):
    matriz = [[0]*N for fila in range(N)]
    return matriz

def imprimir_matriz(matriz):
    for fila in matriz:
        for elemento in fila:
            print("%3d" %elemento, end="")
        print()

def rellenar_matriz(matriz):
    
    return matriz

N = int(input("Ingrese N: "))
matriz = generar_matriz(N)
matriz = rellenar_matriz(matriz)
imprimir_matriz(matriz)