def eliminar_subcadena_rebanadas(frase,pos,caracteres):
    comienzo = frase [ : pos]
    final = frase[(pos+caracteres): ]

    return comienzo + final

def eliminar_subcadena_sin(frase, pos, caracteres):
    subcadena = ''
    for i in range(len(frase)):
        if i < pos or i >= pos + caracteres:
            subcadena += frase[i]
        
    return subcadena

frase = "El numero de telefono es 4356-7890"
pos = 25
caracteres = 9

con_rebanadas = eliminar_subcadena_rebanadas(frase,pos,caracteres)
print("La eliminacion de la sub cadena con rebanadas es: ", con_rebanadas)

sin_rebanadas = eliminar_subcadena_sin(frase, pos, caracteres)
print(sin_rebanadas)