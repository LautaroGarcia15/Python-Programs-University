def listas_resultantes(lista1, lista2):
    lista3 = []

    for i in range(len(lista1)):
        if lista1[i] not in lista2:
            lista3.append(lista1[i])

    return lista3

lista1 = ["camioneta", "caballo", "auto", "barco", "avion"]
lista2 = ["camioneta", "auto", "avion"]
lista3 = listas_resultantes(lista1, lista2)

print("La lista original es: ", lista1)
print("La lista secundaria es: ", lista2)
print("La lista resultante es: ", lista3)