import random

def procesar_naranjas(cosechadas):
    cajones = 0
    jugo = 0

    for _ in range(cosechadas):
        peso = random.randint(150, 350)
        if peso < 200 or peso > 300:
            jugo += 1
        else:
            cajones += peso // 300
            cajones += (peso % 300) // 300

    return cajones, jugo

def calcular_camiones(cajones):
    camiones = cajones // 10
    if cajones % 10 > 0:
        camiones += 1
    return camiones

cosechadas = int(input("Ingrese la cantidad total de naranjas cosechadas: "))
cajones, jugo = procesar_naranjas(cosechadas)

print("Se pueden llenar", cajones, "cajones.")
print("Hay", jugo, "naranjas para jugo.")

camiones = calcular_camiones(cajones)

print("Se necesitan", camiones, "camiones para transportar la cosecha.")

if cajones % camiones >= 8:
    print("Se puede despachar el camión.")
else:
    print("El camión no será despachado debido a la ocupación insuficiente.")
