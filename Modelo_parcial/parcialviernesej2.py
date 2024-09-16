def obtener_longitud(palabra):
    signos_de_puntuacion = [',', '.', '!', '?', ';', ':', '"', "'", '(', ')', '[', ']']
    for signo in signos_de_puntuacion:
        palabra = palabra.replace(signo, '')

    return len(palabra)

cadena = input("Ingrese una cadena: ")
lista = cadena.split()
lista.sort(key=lambda i: obtener_longitud(i))
lista = lista[::-1]
print(lista)