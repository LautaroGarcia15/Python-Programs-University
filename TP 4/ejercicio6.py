def extraer_rebanadas(frase, pos, caracteres):
    subcadena = frase[pos: (pos+caracteres)]

    return subcadena

def extraer_sin_rebanadas(frase, pos, caracteres):
    subcadena = ''

    for i in range(caracteres):
        if pos + i < len(frase):
            subcadena += frase[pos + i]

    return subcadena
    

frase = "El numero de telefono es 4356-7890"
pos = 25
caracteres = 9

subcadena_con_rebanadas = extraer_rebanadas(frase, pos, caracteres)
print("La subcadena con rebanadas es: ", subcadena_con_rebanadas)

subcadena_sin_rebanadas = extraer_sin_rebanadas(frase, pos, caracteres)
print("La subcadena sin rebanadas es: ", subcadena_sin_rebanadas)