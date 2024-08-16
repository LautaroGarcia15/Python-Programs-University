def unidad(numero):
    unidades = ["", "uno", "dos", "tres", "cuatro", "cinco", "seis", "siete", "ocho", "nueve"]
    return unidades[numero]

def decena(numero):
    decenas = ["", "", "veinte", "treinta", "cuarenta", "cincuenta", "sesenta", "setenta", "ochenta", "noventa"]
    return decenas[numero]

def decena_especial(numero):
    especiales = ["diez", "once", "doce", "trece", "catorce", "quince", "dieciséis", "diecisiete", "dieciocho", "diecinueve"]
    return especiales[numero - 10]

def centena(numero):
    cientos = ["", "ciento", "doscientos", "trescientos", "cuatrocientos", "quinientos", "seiscientos", "setecientos", "ochocientos", "novecientos"]
    return cientos[numero]

def numero_a_palabras(numero):
    if numero == 0:
        return "cero"

    # Dividir el número en grupos de tres dígitos
    millones = numero // 1000000
    miles = (numero // 1000) % 1000
    unidades = numero % 1000

    resultado = ""

    if millones > 0:
        if millones == 1:
            resultado += "un millón"
        else:
            resultado += f"{numero_a_palabras(millones)} millones"

    if miles > 0:
        if resultado:
            resultado += " "
        if miles == 1:
            resultado += "mil"
        else:
            resultado += f"{numero_a_palabras(miles)} mil"

    if unidades > 0:
        if resultado:
            resultado += " "
        if unidades >= 100:
            resultado += f"{centena(unidades // 100)}"
            unidades %= 100
            if unidades > 0:
                resultado += " "
        if unidades >= 20:
            resultado += f"{decena(unidades // 10)}"
            unidades %= 10
            if unidades > 0:
                resultado += " "
        if unidades >= 10:
            resultado += f"{decena_especial(unidades)}"
            unidades = 0
        if unidades > 0:
            resultado += f"{unidad(unidades)}"

    return resultado

numero = input("Ingrese un número entre 0 y 1000000000 (un billón): ")

if numero.isdigit() and 0 <= int(numero) <= 1000000000:
    resultado = numero_a_palabras(int(numero))
    print(f"En palabras, el número {numero} es: {resultado}")
else:
    print("Error: Por favor, ingrese un número válido entre 0 y 1000000000 (un billón).")
