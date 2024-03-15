def generar_matriz(N):
    matriz = []
    for f in range(N):
        matriz.append([0]*N)

    return matriz

def rellenar_matriz(matriz, N):
    
    N = 1
    for f in range(len(matriz)):
        condicion = 1
        for c in range(len(matriz[0])):
            if (f + 1) >= condicion:
                matriz[f][-c-1] = N
                N += 1
                condicion += 1

    return matriz
            


def mostrar_matriz(matriz):
    for fila in matriz:
        for elemento in fila: 
            print("%3d" %elemento, end="")
        print()


N = int(input("Ingrese las cantidad de filas y columnas de la matriz: "))


matriz = generar_matriz(N)
rellenar_matriz(matriz,N)
mostrar_matriz(matriz)