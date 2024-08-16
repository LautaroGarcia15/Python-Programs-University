def ultimos_caracteres(cadena, N):
    subcadena = ''  
    for i in range(0, N):
        subcadena += cadena[-i-1]

    return subcadena[::-1]


cadena = input("ingrese una cadena de caracteres: ")
N = int(input("ingrese la cantidad de digitos que se desea ver: "))

ultimos_caracteres_cadena = ultimos_caracteres(cadena, N)
print("Los ultimos caracteres de la cadena son: ", ultimos_caracteres_cadena)