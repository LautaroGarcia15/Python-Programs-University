def primer_archivo():
    try:
        archivo1 = open("E:\\Programacion 1\\TP 6\\archej5a1.CSV", "rt")
        salida1 = open("E:\\Programacion 1\\TP 6\\archej5s1.CSV", "wt")

        for linea in archivo1:
            Nombre = linea[0:20]
            nro = linea[21:29]
            dirreccion = linea[30:70]
            salida1.write("Apellido y nombre: "+Nombre+" Nro: "+nro+" Dirreccion: "+dirreccion)

        print("Los archivos se grabaron correctamente.")

    except FileNotFoundError:
        print("No se encontro el archivo.")
    except OSError as mensaje:
        print("ERROR: ", mensaje)
    finally:
        try:
            archivo1.close()
            salida1.close()
        except NameError:
            pass

def segundo_archivo():
    try:
        archivo2 = open("E:\\Programacion 1\\TP 6\\archej5a2.CSV", "rt")
        salida2 = open("E:\\Programacion 1\\TP 6\\archej5s2.CSV", "wt")

        for linea in archivo2:
            datos = linea.split('#')
            nombre = datos[0]
            nro = datos[1]
            direccion = datos[2]
            salida2.write("Apellido y nombre: "+nombre+", Nro: "+nro+", Direccion: "+direccion)
        
        print("Los archvos se grabaron correctamente. ")



    except FileNotFoundError:
        print("No se encontro el archivo.")
    except OSError as mensaje:
        print("ERROR: ", mensaje)
    finally:
        try:
            archivo2.close()
            salida2.close()
        except NameError:
            pass

def tercer_archivo():
    try:
        archivo3 = open("E:\\Programacion 1\\TP 6\\archej5a3.CSV", "rt")
        salida3 = open("E:\\Programacion 1\\TP 6\\archej5s3.CSV", "wt")
    
        for linea in archivo3:

            campo1 = int(linea[0:2])
            campo2 = int(linea[campo1+2:campo1+4])
            campo3 = int(linea[campo1+campo2+4:campo1+campo2+6])

            nombre = linea[2:campo1+2]
            nro = linea[campo1+4:campo1+campo2+4]
            direccion = linea[campo1+campo2+6: campo3 + campo2 + campo1]

            salida3.write("Apellido y nombre: "+nombre+", Nro: "+nro+", Direccion: "+direccion+"\n")

        print("Los archivos se grabaron con exito.")


    except FileNotFoundError:
        print("No se encontro el archivo.")
    except OSError as mensaje:
        print("ERROR: ", mensaje)
    finally:
        try:
            archivo3.close()
            salida3.close()
        except NameError:
            pass

#primer_archivo()
#segundo_archivo()
tercer_archivo()
