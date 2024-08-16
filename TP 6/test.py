# Función para grabar las alturas de los atletas en un archivo
def GrabarRangoAlturas():
    with open("alturas_atletas.txt", "w") as archivo:
        while True:
            deporte = input("Ingrese el nombre del deporte (o 'q' para salir): ")
            if deporte == 'q':
                break
            archivo.write(f"< {deporte} >\n")
            while True:
                altura = input("Ingrese la altura del atleta (o 'q' para terminar este deporte): ")
                if altura == 'q':
                    break
                archivo.write(f"{altura}\n")

# Función para calcular y grabar los promedios de las alturas en un archivo
def GrabarPromedio():
    with open("alturas_atletas.txt", "r") as archivo_entrada, open("promedios_alturas.txt", "w") as archivo_salida:
        deporte = ""
        alturas = []
        for linea in archivo_entrada:
            if linea.startswith("<"):
                if alturas:
                    promedio = sum(alturas) / len(alturas)
                    archivo_salida.write(f"< {deporte} >\n")
                    archivo_salida.write(f"Promedio de alturas deporte: {promedio}\n")
                deporte = linea.strip(" <>\n")
                alturas = []
            else:
                alturas.append(float(linea.strip()))

# Función para mostrar las disciplinas con atletas más altos que el promedio general
def MostrarMasAltos():
    with open("promedios_alturas.txt", "r") as archivo:
        promedios = {}
        deporte = ""
        for linea in archivo:
            if linea.startswith("<"):
                deporte = linea.strip(" <>\n")
            else:
                promedio = float(linea.split(":")[1])
                promedios[deporte] = promedio

        promedio_general = sum(promedios.values()) / len(promedios)

        print("Disciplinas con atletas más altos que el promedio general:")
        for deporte, promedio in promedios.items():
            if promedio > promedio_general:
                print(deporte)

# Main
if __name__ == "__main__":
    while True:
        print("1. Grabar alturas de atletas")
        print("2. Calcular y grabar promedios de alturas")
        print("3. Mostrar disciplinas con atletas más altos que el promedio general")
        print("4. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            GrabarRangoAlturas()
        elif opcion == "2":
            GrabarPromedio()
        elif opcion == "3":
            MostrarMasAltos()
        elif opcion == "4":
            break
        else:
            print("Opción no válida. Intente de nuevo.")
