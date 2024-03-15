import random

def crear_matriz(filas, columnas):
    matriz = []
    for f in range(filas):
        matriz.append([])
        for c in range(columnas):
            matriz[f].append(random.randint(0, 150))

    return matriz

def mostrar_matriz(matriz):
    for fila in matriz:
        
        for elemento in fila: 
            print( "%5d" %elemento, end="")
            
        print()

def bicicletas_por_fabrica(matriz):
    for f in range(len(matriz)):
        print("La fabrica ", f+1, "fabrico", sum(matriz[f]), "bicicletas")

def mas_produjo(matriz):
    fabrica = 0
    dia = 0
    bicicletas = 0
    for fila in range(len(matriz)):
        for elemento in range(len(matriz[0])):
            if max(matriz [fila]) > bicicletas:
                fabrica = fila
                dia = elemento
                bicicletas = matriz[fila][elemento]

    return fabrica, dia, bicicletas

def dia_productivo(matriz):
    dia = 0
    max_produccion = 0
    
    for i in range(6):
        max_produccion_actual = 0
        for fila in range(len(matriz)):
            max_produccion_actual += matriz[fila][i]

        if max_produccion_actual > max_produccion:
            max_produccion = max_produccion_actual
            dia = i + 1  

    return max_produccion, dia


filas = int(input("Ingrese la cantidad de fabricas: "))
columnas = 6

matriz = crear_matriz(filas, columnas)
mostrar_matriz(matriz)
bicicletas_por_fabrica(matriz)

fabrica, dia, bici = mas_produjo(matriz)
print("La fabrica que mas produjo fue: ",fabrica, "el dia: ", dia, "produjo: ", bici," bicicletas.")

maxima_prod, dia_product = dia_productivo(matriz)
print ("El dia mas productivo fue el: ", dia_product,", se produjeron: ", maxima_prod," bicicletas")