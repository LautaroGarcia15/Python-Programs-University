def generar_matriz(N):
    matriz = [[0]*N for i in range(0,N)]
    return matriz

def imprimir_matriz(matriz):
    for fila in matriz:
        for elemento in fila:
            print("%3d" %elemento, end="")
        print()

def rellenar_matriz(matriz):
    numero = 1
    for f in range(len(matriz)):
        for c in range(len(matriz[0])):
            if f % 2 == 0:
                matriz[f][c] = numero
                numero += 1
            else:
                matriz[f][len(matriz)-c-1] = numero
                numero += 1
                
    return matriz

N = int(input("ingrese N: "))
matriz = generar_matriz(N)
matriz = rellenar_matriz(matriz)
imprimir_matriz(matriz)