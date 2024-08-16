try :
    archivo_entrada = open("E:/Programacion 1/TP 6/NombreApellidos.txt", "rt")

    archivo_armenia =  open("ARMENIA.TXT", "wt")
    archivo_italia = open("ITALIA.TXT", "wt")
    archivo_espana = open("ESPAÑA.TXT", "wt")

    for linea in archivo_entrada:
        apellido, nombre = linea.strip().split(", ")

        if apellido[-3:] == "ian":
            archivo_armenia.write(f"{apellido.title()}, {nombre}\n")

        elif apellido[-3:] == "ini":
            archivo_italia.write(f"{apellido.title()}, {nombre}\n")

        elif apellido[-2:] == "ez":
            archivo_espana.write(f"{apellido.title()}, {nombre}\n")

    print("Todo se guardo correctamente.")


except FileNotFoundError:
    print("No se encontro el archivo.")
except OSError as mensaje:
    print("Se produjo el error: ", mensaje)
finally:
    try:
        archivo_armenia.close()
        archivo_italia.close()
        archivo_espana.close()
    except NameError:
        pass

