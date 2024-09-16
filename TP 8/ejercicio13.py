def buscarclave(diccionario, valor):
    claves = []
    for elemento in diccionario:
        if valor == diccionario[elemento]:
            claves.append(elemento)
    
    return claves


diccionario = {1:'Pelota',2:'Palo', 3:'Mano',4:'Raqueta', 5:'Pelota'}
valor = 'Pelota'
calves1 = buscarclave(diccionario,valor)
print("Las claves son: ", calves1)
