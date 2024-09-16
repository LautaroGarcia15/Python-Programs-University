n = int(input("ingrese numero: "))
funcion = lambda n : (((8*n+1)**0.5)-1) % 2 == 0 
print(funcion(n))
#-----------------------------------------------------------------------
def dec2hex(dec):
    hex = ""  # Inicializa una cadena vacía para almacenar el número hexadecimal resultante
    while dec != 0:
        digito = dec % 16  # Calcula el residuo al dividir el número decimal por 16
        dec = dec // 16  # Actualiza el número decimal dividiéndolo por 16
        hex = hex + (str(digito) if digito <= 9 else chr(55 + digito))  # Concatena el dígito convertido a hexadecimal a la cadena 'hex'
    hex = hex[::-1]  # Invierte la cadena 'hex' para obtener el resultado final en el orden correcto
    return hex  # Devuelve el número hexadecimal resultante

def comienzacon1(cadena, prefijo):
    """ Versión 1: Usando listas por comprensión """
    lista = [palabra for palabra in cadena.split() if palabra[:len(prefijo)] == prefijo]
    return lista
