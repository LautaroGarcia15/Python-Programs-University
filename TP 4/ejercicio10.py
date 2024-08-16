def cambiar_palabra(cadena, reemplazo, nueva):     # hay q limpiar las palabras con coma.
    palabras = cadena.strip(",").split()
    cantidad = 0
    for palabra in range(len(palabras)):
        if palabras[palabra] == reemplazo:
            palabras[palabra] = nueva
            cantidad += 1

    cadena_nueva = " ".join(palabras)

    return cadena_nueva, cantidad

cadena = input("Ingrese una cadena: ")
reemplazo = input("Ingrese la palabra que desea reemplazar: ")
nueva = input("Ingrese la palabra por la que desea cambiar: ")
nueva_cadena, cantidad = cambiar_palabra(cadena, reemplazo, nueva)
print(f"La nueva cadena es: {nueva_cadena}, se reemplazo {cantidad} veces ")    