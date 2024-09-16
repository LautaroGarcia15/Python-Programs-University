def cantidad_digitos(numero, cont):
    if numero > 0:
        cont += 1
        return cantidad_digitos(numero // 10, cont)
    else:
        return cont

numero = int(input("Ingrese un número: "))
cont = 0
digitos = cantidad_digitos(numero, cont)
print("La cantidad de dígitos de", numero, "es:", digitos)
