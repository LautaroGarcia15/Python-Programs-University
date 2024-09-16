def validar_fecha(fecha):
    dia,mes,año = fecha

    if mes < 1 or mes > 12:
        return False

    #Verificar si es biciesto
    if mes == 2:
        if (año % 4 == 0 and año % 100 != 0) or año % 400 == 0:
            return 1 <= dia <= 29
        
    #Meses con 30 dias   
    if mes in (4, 6, 8, 11):
        return 1 <= dia <= 30
    
    #Meses con 31 días
    else:
        return 1 <= dia <= 31


    
dia = int(input("Ingerse un dia: "))
mes = int(input("Ingrese un mes: "))
año = int(input("Ingrese un año: "))
fecha = (dia,mes,año)

if validar_fecha(fecha):
    print("La fecha:",(fecha),"es valida")
else:
    print("La fecha no es valida.")