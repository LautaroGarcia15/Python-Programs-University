def diadelasemana(dia, mes, año):
    if mes < 3:
        mes += 10
        año -= 1
    else:
        mes -= 2
    
    siglo = año // 100
    año2 = año % 100
    diasem = (((26 * mes - 2) // 10) + dia + año2 + (año2 // 4) + (siglo // 4) - (2 * siglo)) % 7
    if diasem < 0:
        diasem += 7
    return diasem

def imprimir_calendario(mes, año):
    dias_en_mes = 31
    if mes == 4 or mes == 6 or mes == 9 or mes == 11:
        dias_en_mes = 30
    elif mes == 2:
        if (año % 4 == 0 and (año % 100 != 0 or año % 400 == 0)):
            dias_en_mes = 29
        else:
            dias_en_mes = 28

    print()
    print("Calendario de: ",mes,"/",año)
    print("Dom Lun Mar Mie Jue Vie Sab")
    
    primer_dia = diadelasemana(1, mes, año)
    
    for i in range(primer_dia):
        print("   ", end=" ")
    
    dia_actual = 1
    for i in range(dias_en_mes):
        print(dia_actual, end=" ")

        if (primer_dia + dia_actual) % 7 == 0:
            print()
        dia_actual += 1

    print()

mes = int(input("Ingrese el número del mes (1-12): "))
año = int(input("Ingrese el año: "))

imprimir_calendario(mes, año)
