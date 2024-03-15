import random
def crear_butacas(N,M):
    matriz = [[0 for c in range(M)]for f in range(N)]
    return matriz

def mostrar_butacas(matriz):
    for fila in matriz:
        for elemento in fila: 
            print("%3d" %elemento, end="")
        print()

def reservar(matriz, fila, butaca):
    if matriz[fila][butaca] == 0:
        matriz[fila][butaca] = 1
        return True
    else:
        return False
    
def cargar_sala(matriz):
    for f in range(len(matriz)):
        for c in range(len(matriz[0])):
            matriz[f][c] = random.randint(0,1)

    return matriz

def butacas_libres(matriz_aleatoria):
    libres = 0
    '''for f in range(len(matriz_aleatoria)):
        for c in range(len(matriz_aleatoria[0])):
            if matriz_aleatoria [f][c] == 0:
                libres += 1'''
    
    for f in matriz_aleatoria:
        libres += f.count(0)

    return libres

def butacas_contiguas(matriz_aleatoria):
    contiguas_max = 0
    contiguas_actuales = 0

    for f in range(len(matriz_aleatoria)):
        for c in range(len(matriz_aleatoria[0])):
            if matriz_aleatoria[f][c] == 0:
                contiguas_actuales += 1
            else:
                contiguas_max = max(contiguas_actuales, contiguas_max)
                contiguas_actuales = 0

    return contiguas_max

N = int(input("Ingrese cantidad de filas: "))
M = int(input("Ingrese catidad de butacas por filas: "))

matriz = crear_butacas(N,M)
mostrar_butacas(matriz)

fila = int(input("Ingrese la fila en la que desea reservar: "))
butaca = int(input("Ingrese la butaca que desea reservar de la fila: "))

print()
if reservar(matriz, fila, butaca):
    print("Reserva exitosa.")
else:
    print("La butaca seleccionada ya está ocupada o no existe.")
mostrar_butacas(matriz)

print()
print("Matriz rellenada: ")
matriz_aleatoria = cargar_sala(matriz)
mostrar_butacas(matriz_aleatoria)

butacas_libres = butacas_libres(matriz_aleatoria)
print("La cantidad de butacas disponibles son: ", butacas_libres)

butacas_contiguas = butacas_contiguas(matriz_aleatoria)
print("La mayor cantidad de butacas contiguas es: ", butacas_contiguas)
