def imprimir_fecha(fecha):
    meses = [
    "Enero", "Febrero", "Marzo", "Abril",
    "Mayo", "Junio", "Julio", "Agosto",
    "Septiembre", "Octubre", "Noviembre", "Diciembre"]

    dia,mes,año = fecha
    fecha_extendido = (str(dia)+' de '+(meses[mes-1])+' de '+str(año))

    return fecha_extendido

dia = int(input("Ingerse un dia: "))
mes = int(input("Ingrese un mes: "))
año = int(input("Ingrese un año: "))
fecha = (dia,mes,año)

extencion = imprimir_fecha(fecha)
print(extencion)