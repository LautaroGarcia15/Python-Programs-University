def buscar_subcadena(cadena, subcadena):
    cadena = cadena.lower()
    subcadena = subcadena.lower()
    count = 0
    i = 0

    while i < len(cadena):
        j = 0
        while i < len(cadena) and j < len(subcadena):
            if cadena[i] == subcadena[j]:
                j += 1
            i += 1
        if j == len(subcadena):
            count += 1

    return count

cadena = "Platero es pequeño, peludo, suave; tan blando por fuera, que se diría todo de algodón,que no lleva huesos. Sólo los espejos de azabache de sus ojos son duros cual dos escarabajos de cristal negro."
subcadena = input("Ingrese la subcadena: ")

cantidad = buscar_subcadena(cadena, subcadena)
print(f"La subcadena {subcadena} se encuentra {cantidad} veces en la cadena {cadena}.")

