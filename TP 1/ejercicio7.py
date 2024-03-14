def diasiguiente(dia, mes, año):
    if mes == 12 and dia == 31:
        dia = 1
        año += 1
        mes = 1
    elif (mes == 4 or mes == 6 or mes == 9 or mes == 11) and dia == 30:
        dia = 1
        mes += 1
    elif mes == 2 and dia == 29:
        dia = 1
        mes += 1
    elif (mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 10 or mes == 8) and dia == 31:
        dia = 1
        mes += 1
    else:
        dia += 1

    return dia, mes, año

def dias_a_sumar(dia, mes, año, dia_suma):
    
    while dia_suma > 0:
        dia, mes, año = diasiguiente(dia, mes, año)
        dia_suma -= 1

    return dia, mes, año

def distancia_fechas(dia1, mes1, año1, dia2, mes2, año2):
    dias_del_medio = 0
    
    while dia1 != dia2 or mes1 != mes2 or año1 != año2:
        dia1, mes1, año1 = diasiguiente(dia1, mes1, año1)
        dias_del_medio += 1

    return dias_del_medio

dia = int(input("Ingrese un día: "))
mes = int(input("Ingrese un mes: "))
año = int(input("Ingrese un año: "))
print("")


sigdia, sigmes, sigaño = diasiguiente(dia, mes, año)
print(f"El día siguiente es: {sigdia}/{sigmes}/{sigaño}")
print("")


print("a)")
dia_suma = int(input("ingrese los dias que desea sumar: "))
print("")
diasum, messum, añosum = dias_a_sumar(dia, mes, año, dia_suma)
print(f"El día sumado es : {diasum}/{messum}/{añosum}")
print("")


print("b)")
dia1 = int(input("Ingrese el día de la primera fecha: "))
mes1 = int(input("Ingrese el mes de la primera fecha: "))
año1 = int(input("Ingrese el año de la primera fecha: "))
dia2 = int(input("Ingrese el día de la segunda fecha: "))
mes2 = int(input("Ingrese el mes de la segunda fecha: "))
año2 = int(input("Ingrese el año de la segunda fecha: "))
print("")
dias_de_diferencia = distancia_fechas(dia1, mes1, año1, dia2, mes2, año2)
print("Los dias de diferencia son : ", dias_de_diferencia)