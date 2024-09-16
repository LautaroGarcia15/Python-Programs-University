import random
def generar_matriz(N,f,c):
    matriz = []
    for fila in range(N):
        matriz.append([])
        for columna in range(N):
            matriz[fila].append(random.randint(0,9))

    vecinos = []
    direcciones = [[1, 0], [-1, 0], [0, 1], [0, -1], [1, 1], [-1, -1], [1, -1], [-1, 1]]
    suma = 0

    for i, j in direcciones:
        lado_f,lado_c = f + i, c + j
        if 0 <= lado_f < len(matriz) and 0 <= lado_c < len(matriz):
            vecino = matriz[lado_f][lado_c]
            vecinos.append(vecino)
            suma += vecino
        

    return matriz, suma

def imprimir_matriz(matriz):
    for fila in matriz:
        for elemento in fila:
            print("%3d" %elemento, end="")
        print()


N = int(input("ingrese N: "))

while N < 3:
    N = int(input("ingrese N: "))

f = int(input("ingrese la fila: "))
c = int(input("ingrese la columna: "))

matriz, suma = generar_matriz(N,f,c)

imprimir_matriz(matriz)
print(suma)