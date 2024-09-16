import random
def generar_matriz(jugadores):
    matriz = [[0]*3 for fila in range(jugadores)]

    palos = ["Oro","Espada","Copa","Basto"]
    numeros = ["1","2","3","4","5","6","7","10","11","12"]

    baraja = [numero + " de " + palo for numero in numeros for palo in palos]
    
    for f in range(len(matriz)):
        for c in range(len(matriz[0])):
            carta = random.choice(baraja)
            matriz[f][c] = carta
            baraja.remove(carta)

    return matriz

def mostrar_cartas(matriz):
    for i, fila in enumerate(matriz):
        print("Jugador ", i+1, end=":   ")
        for elemento in fila:
            print("%17s" %elemento, end="")
        print()


jugadores = int(input("Ingrese la cantidad de jugadores:"))
while jugadores < 2 or jugadores > 6:
    jugadores = int(input("Ingrese la cantidad de jugadores:"))

matriz = generar_matriz(jugadores)
matriz =  mostrar_cartas(matriz)
print(matriz)
