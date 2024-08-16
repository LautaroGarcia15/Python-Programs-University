def filtrar_palabras_ciclos(frase,numero):
    palabras = frase.split()
    frase_filtrada = ""

    for palabra in palabras:
        if len(palabra) >= numero:
            frase_filtrada = frase_filtrada + palabra + " "
    
    return frase_filtrada

def filtrar_palbabras_lista(frase, numero):
    palabras = frase.split()
    resultado = [palabra for palabra in palabras if len(palabra) >= numero]

    return ' '.join(resultado)

def filtrar_palabras_filter(frase, numero):
    palabras = frase.split()
    palabras_filtradas = list(filter(lambda palabra: len(palabra) >= numero,palabras))
    
    return ' '.join(palabras_filtradas)

frase = input("Ingrese una frase y un numero entero: ")

numero = ''
for i in frase:
    if i >='0' and i <= '9':
        numero += i

numero = int(numero)

por_ciclos = filtrar_palabras_ciclos(frase,numero)
print("La cadena filtrada por ciclos es: ", por_ciclos)

por_comprension = filtrar_palbabras_lista(frase, numero)
print("La cadena filtrada por comprension es: ", por_comprension)

por_filter = filtrar_palabras_filter(frase, numero)
print("La cadena filtrada por filter: ", por_filter)