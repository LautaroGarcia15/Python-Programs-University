def eliminarclaves(diccionario, lista):
    try:
        for elemento in lista:
            diccionario.pop(elemento)
        return True, diccionario
    

    except KeyError:
        print("El elemento no se encuentra en el conjunto")


diccionario = {1:'Pelota',2:'Palo', 3:'Mano',4:'Raqueta'}
lista = [1,3]
valor, dic = eliminarclaves(diccionario, lista)
print(valor)
print(diccionario)
