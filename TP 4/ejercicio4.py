def numero_romano(numero):
    valores = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    simbolos = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
    resultado = ""

    if numero > 3999:
        miles = numero // 1000
        resultado += "M" * miles
        numero %= 1000

    i  = 0
    while numero > 0:
        repeticion = numero // valores [i]
        resultado += simbolos[i] * repeticion
        numero -= valores[i] * repeticion

        i += 1

    return resultado 

numero = int(input("Ingrese un numero: "))

numero_rom = numero_romano(numero)
print(numero_rom)