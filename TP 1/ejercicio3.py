def totalgastado(viajes):
    valor = 74
    if viajes >= 1 and viajes <= 20:
        return valor
    
    if viajes >= 21 and viajes <= 30:
        valor = valor - (valor * 0.20)
        return valor
    
    if viajes >= 31 and viajes <= 40:
        valor = valor - (valor * 0.30)
        return valor
    
    else:
        valor = valor - (valor * 0.40)
        return valor
    


viajes = int(input("ingrese la cantidad de viajes: "))

totalapagar = totalgastado(viajes)

print("el total a pagar es: ", totalapagar)