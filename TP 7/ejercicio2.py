def binario_a_decimal(binario):
    if len(binario) == 0:
        return 0

    ultimo_digito = int(binario[-1])
    binario = binario[:-1]
    valor_decimal = binario_a_decimal(binario)
    valor_decimal = valor_decimal * 2 + ultimo_digito

    return valor_decimal

numero_binario = input("Ingrese un número binario: ")

try:
    decimal = binario_a_decimal(numero_binario)
    print(f"El número decimal equivalente es: {decimal}")
except ValueError:
    print("Entrada no válida. Asegúrate de ingresar un número binario válido (0s y 1s).")
