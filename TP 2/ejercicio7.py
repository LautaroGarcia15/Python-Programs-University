def intercalar_elementos(lista1, lista2):
    for i in range(len(lista2)):
        lista1[2 * i + 1:2 * i + 1] = [lista2[i]]
    print (lista1)

lista1 = [8, 1, 3]
lista2 = [5, 9, 7]
intercalar_elementos(lista1, lista2)