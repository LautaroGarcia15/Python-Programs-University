5
def generar_matriz(N):
    matriz = [[0]*N for fila in range(N)]
    return matriz

def imprimir_matriz(matriz):
    for fila in matriz:
        for elemento in fila:
            print("%3d" %elemento, end="")
        print()

def rellenar_matriz(matriz):
    num = 1

    for digonal in range(2*len(matriz)-1):
        if digonal < len(matriz):
            fila = 0
            columna = digonal
        else:
            fila = digonal - len(matriz) + 1
            columna = len(matriz) - 1
        
        while fila < len(matriz) and columna >= 0:
            matriz[fila][columna] = num
            num += 1
            fila += 1
            columna -= 1

    return matriz

N = int(input("Ingrese N: "))
matriz = generar_matriz(N)
matriz = rellenar_matriz(matriz)
imprimir_matriz(matriz)