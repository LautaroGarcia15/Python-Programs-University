def verificacion_de_listas(lista):
    lista_aux = []
    
    for i in range(len(lista)):
        lista_aux.append(lista[i])
    ordenada = sorted(lista_aux)

    if lista == ordenada:
        return True
    else:
        return False

#lista = [1, 2, 3]
lista = ["b", "a"]

verificacion = verificacion_de_listas(lista)

if verificacion == True:
    print("La lista esta ordenada.")
else:
    print("La lista no esta ordenada.")