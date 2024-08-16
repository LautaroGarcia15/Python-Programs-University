def centrar_cadena(frase):
    espacio = (80//2)-(len(frase)//2)
    print(" "*espacio + frase)

frase = input("Ingrese una cadena de caracteres: ")
centrar_cadena(frase)