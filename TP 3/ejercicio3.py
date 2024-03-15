import random

def generar_matriz(N):
    matriz = [[0]*N for i in range(N)]
    return matriz
    
def rellenar_matriz(matriz, N):
    numeros_usados = []  
    
    for fila in range(len(matriz)):
        for elemento in range(len(matriz[0])):
            num_azar = random.randint(1, N**2)
            
            while num_azar in numeros_usados:
                num_azar = random.randint(1, N**2)
                
            matriz[fila][elemento] = num_azar
            numeros_usados.append(num_azar)

    return matriz

def imprimir_matriz(matriz_rellenada):
    for fila in matriz_rellenada:
        for elemento in fila: 
            print("%3d" %elemento, end="")
        print()

N = int(input("ingrese N: "))

matriz = generar_matriz(N)
matriz_rellenada = rellenar_matriz(matriz, N)
imprimir_matriz(matriz_rellenada)