def generar_matriz(N):
    matriz = [[0]*N for i in range(N)]

    return matriz

def rellenarmatriz(matriz_vacia):

    filas = len(matriz_vacia)
    columnas = len(matriz_vacia[0])

    for f in range(filas):
        for c in range(columnas):
            n = int(input("Ingrese una valor: "))
            matriz_vacia[f][c] = n

    return matriz_vacia

def imprimir_matriz(matriz_rellenada):
    for fila in matriz_rellenada:
        for elemento in fila:
            print("%3d" %elemento, end="")
        print()

def ordenar_filas(matriz_rellenada):
    for f in range(len(matriz_rellenada)):
        matriz_rellenada[f].sort()
    
    return matriz_rellenada

N = int(input("ingrese N: "))
matriz_vacia = generar_matriz(N)

matriz_rellenada = rellenarmatriz(matriz_vacia)
imprimir_matriz(matriz_rellenada)

print()
print("Matiz ordenada")
print()

ordenar_filas(matriz_rellenada)
imprimir_matriz(matriz_rellenada)