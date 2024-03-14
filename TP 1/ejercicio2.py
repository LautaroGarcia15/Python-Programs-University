def validarfecha(dia, mes, año):
    if mes < 1 or mes > 12:
        return False

    if mes == 2:  # Febrero
        if (año % 4 == 0 and año % 100 != 0) or año % 400 == 0:
            return 1 <= dia <= 29
        else:
            return 1 <= dia <= 28
    elif mes == 4 or mes == 6 or mes == 8 or mes == 11: # Abril, Junio, Septiembre, Noviembre
        return 1 <= dia <= 30
    else:  # Meses con 31 días
        return 1 <= dia <= 31

dia = int(input("ingrese un dia: "))
mes = int(input("ingerse un mes: "))
año = int(input("ingrese un año: "))

validacion = validarfecha(dia, mes, año)

if validacion == True:
    print("la fecha es valida")
else:
    print("la fecha NO es valida")