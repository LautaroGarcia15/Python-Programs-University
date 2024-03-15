import random

def listar_num ():
    numeros = []
    cant_numeros = random.randint(10, 99)

    for i in range(0, cant_numeros):
        numeros.append(random.randint(1000,9999))
    
    return numeros

def sumatoria(listado):

    return sum(listado)

def eliminar_valor(listado, eliminar):
    while eliminar in listado:
        listado.remove(eliminar)

    return listado

def capicua(listado):                 #falta hacer este metodo 
    capicua = False
    al_reves = listado.reverse()
    if listado == al_reves:
        capicua = True
    
    return capicua

listado = listar_num()
print("La lista cargada es: ", listado)

suma = sumatoria(listado)
print("La suma de los elementos de la lista es: ", suma)

eliminar = int(input("ingrese el valor que desea eliminar: "))
eliminar_valor(listado,eliminar)
print("La nueva lista sin el valor ingresado es: ", listado)

capicua(listado)
if capicua == True:
    print("La lista es capicua. ")
else:
    print("La lista no es capicua. ")