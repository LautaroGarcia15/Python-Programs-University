def generar_matriz(N):
    matriz = []
    for f in range(N):
        matriz.append([0]*N)
    return matriz

def rellenar_matriz(matriz):
    num = 1
    for f in range(len(matriz)):
        matriz[len(matriz)-f-1][f] = num
        num *= 3
    return matriz

def mostrar_matriz(matriz):
    for fila in matriz:
        for elemento in fila: 
            print("%3d" %elemento, end="")
        print()


N = int(input("Ingrese las cantidad de filas y columnas de la matriz: "))


matriz = generar_matriz(N)
matriz = rellenar_matriz(matriz)
mostrar_matriz(matriz)

