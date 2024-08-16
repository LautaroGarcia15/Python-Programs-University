def GrabarRangoAlturas():
    try:
        alturas = open("Alturas.txt", "wt")

        while True:
            deporte = input("Ingrese Nombre del deporte (Ingrese 'salir' para terminar): ")
            if deporte.lower() == 'salir':
                break
            alturas.write(deporte+'\n')

            while True:
                altura = input("Ingrese la altura del atleta (Ingrese 'salir' para terminar): ")
                if altura.lower() == 'salir':
                    break
                alturas.write(altura+'\n')

        alturas.write(" ")
        print("El archivo se guardo correctamente.")

    except OSError as mensaje:
        print("Hubo un error: ", mensaje)
    finally:
        try:
            alturas.close()
        except NameError:
            pass

def GrabarPromedio():
    todas_alturas = open("E:\\Programacion 1\\TP 6\\Alturas.txt", "rt")
    promedios = open("E:\\Programacion 1\\TP 6\\PromediosAlturas.txt", "wt")

    suma_alturas = 0
    cantidad_alturas = 0

    for line in todas_alturas:
        line = line.strip('\n')

        if (line.isalpha() or line == " "):
            if (cantidad_alturas > 0):
                promedios.write(str(suma_alturas / cantidad_alturas)+'\n')
                promedios.write(line+'\n')

                suma_alturas = 0
                cantidad_alturas = 0
            else:
                promedios.write(line+'\n')

        else:

            cantidad_alturas += 1
            suma_alturas += float(line)
        

    
    todas_alturas.close()
    promedios.close()

    print("El archivo de los promedios se creo correctamente.")

def MostrarMasAltos():
    promedio = open("E:\\Programacion 1\\TP 6\\PromediosAlturas.txt", "rt")

    promedio_general = 0
    cantidad = 0

    for linea in promedio:
        linea = linea.strip('\n')

        try:
            valor = float(linea)
            promedio_general += valor
            cantidad += 1
        except ValueError:
            # Si la conversión a float falla, no es un número y continuamos con la siguiente línea
            continue
    
    promedio_total = promedio_general / cantidad

    print("Promedio total:", promedio_total)
    
    # Vuelve al principio del archivo para volver a leer

    for linea in promedio:
        linea = linea.strip('\n')

        try:
            valor = float(linea)
            if valor > promedio_total:
                print("Disciplina que supera el promedio:", valor)
        except ValueError:
            # Si la conversión a float falla, no es un número y continuamos con la siguiente línea
            continue 





#GrabarRangoAlturas()
GrabarPromedio()
MostrarMasAltos()