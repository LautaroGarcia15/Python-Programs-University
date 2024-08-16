def cadena_ordenada(cadena):
    lista_cadena = cadena.split()
    lista_cadena.sort()

    return ' '.join(lista_cadena)

cadena = input("ingrese una cadena de caracteres: ")

cadena_ordenada_alfabeticamente = cadena_ordenada(cadena)
print ("La cadena ordenada alfabeticamente es: ", cadena_ordenada_alfabeticamente)