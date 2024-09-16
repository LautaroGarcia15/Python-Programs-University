frase = input("Ingrese una frase: ")
lista = frase.split()
conjunto = set(lista)
print(conjunto)

lista_sin_duplicados = list(conjunto)
lista_ordenada = sorted(lista_sin_duplicados, key=len, reverse=True)

for palabra in lista_sin_duplicados:
    print(palabra)
