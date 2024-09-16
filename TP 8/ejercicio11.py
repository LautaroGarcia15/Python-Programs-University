def contar_vocales(palabra, dic):
    vocales = ['a','e','i','o','u']
    for letra in palabra:
        if letra in vocales:
            dic[letra] = dic[letra] + 1
    return dic

frase = input("Ingrese una frase: ")
lista_palabras = frase.split()
vocaless = 'aeiou'
dic = dict.fromkeys(vocaless, 0)

for palabra in lista_palabras:
    dic = contar_vocales(palabra, dic)

print(lista_palabras)
print (dic)