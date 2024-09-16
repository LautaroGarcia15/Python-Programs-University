def obtener_primer_digito(numero):
    if numero < 0:
        numero = -numero
    while numero >= 10:
        numero //= 10
    return numero

lista = []

num = int(input("Ingrese un número: "))

while num != -1:
    lista.append(num)
    num = int(input("Ingrese un número: "))
    
suma = 0
for numero in lista:
    primer_digito = obtener_primer_digito(numero)
    suma += primer_digito

print("Lista completa:", lista)
print("La suma de los primeros dígitos de los números es:", suma)