import random

def generar_matriz(fila, columnas):
    matriz = [[0]*columnas for f in range(fila)]
    return matriz

def rellenar_matriz(matriz):
    numeros = ['1','2','3','4','5','6','7','10','11','12']
    palos = ["Espada", "Oro", "Basto", "Copa"]
    cartas_dispo = [numero + " de "+ palo for numero in numeros for palo in palos]

    for fila in range(len(matriz)):
        for columna in range(len(matriz[0])):
            carta = random.choice(cartas_dispo)
            matriz[fila][columna] = carta
            cartas_dispo.remove(carta)

    return matriz

fila = int(input("ingrese cantidad de jugadores: "))
columnas = 3
while fila < 2 or fila > 6:
    fila = int(input("ingrese cantidad de jugadores: "))
print()
           
matriz = generar_matriz(fila, columnas)
cartas = rellenar_matriz(matriz)

for i, jugador in enumerate(cartas):
    print("Jugador", i+1, end=":  ")
    for carta in jugador:
        print("%15s" %carta, end="")
    print()
