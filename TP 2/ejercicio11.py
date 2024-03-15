def listados_de_pacientes():
    lista_urgencia = []
    lista_turno = []
    n = int(input("ingrese el numero de afiliado: "))
    while n != -1:
        condicion = int(input("ingrese 0 si viene por urgencia o ingrese 1 si viene por turno: "))

        if condicion == 0:
            lista_urgencia.append(n)
        elif condicion == 1:
            lista_turno.append(n)

        n = int(input("ingrese el numero de afiliado: "))
    
    return lista_turno, lista_urgencia

def busqueda(buscar, turno, urgencia):

    if buscar in turno:
        por_turnos = turno.count(buscar)

    if buscar in urgencia:
        por_urgencia = urgencia.count(buscar)

    return por_turnos,por_urgencia


turno,urgencia = listados_de_pacientes()

print("Los pacientes que ingresaron por turno son : ",turno)
print("Los pacientes ingresados por ugencia son: ", urgencia)

buscar = int(input("ingrese el numero de afiliado que desea buscar: "))

por_turno, por_urgencia = busqueda(buscar, turno, urgencia)

print("El paciente: ", buscar, "fue atendido por turno: ", por_turno)
print("El paciente: ", buscar, "fue atendido por urgencia: ", por_urgencia)
