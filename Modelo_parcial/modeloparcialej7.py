import random
def generar_matriz(N,M):
    matriz = [[0]*M for fila in range(N)]

    for f in range(len(matriz)):
        for c in range(len(matriz[0])):
            vecinos = []
            for i in range(f-1, f+2):
                for j in range(c-1,c+2):
                    if 0 <= i < N and 0 <= j < M and (i!= f or c!= j):
                        vecinos.append(matriz[i][j])
            
            num = random.randint(0,25)
            while num in vecinos:
               num = random.randint(0,25) 
            matriz[f][c] = num

    return matriz

def imprimir_matriz(matriz):
    for fila in matriz:
        for elemento in fila:
            print("%3d" %elemento, end="")
        print()

N = int(input("Ingrese N: "))
M =int(input("Ingrese M: "))
matriz = generar_matriz(N,M)
imprimir_matriz(matriz)