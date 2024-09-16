import random

# Función para generar un asiento aleatorio que aún no ha sido asignado
def generar_asiento_aleatorio(asientos_ocupados, max_filas, asientos_por_fila):
    while True:
        fila = random.randint(1, max_filas)
        asiento = random.choice([chr(i) for i in range(ord('A'), ord(asientos_por_fila) + 1)])
        asiento_aleatorio = f"{fila}{asiento}"
        if asiento_aleatorio not in asientos_ocupados:
            return asiento_aleatorio

# Función principal que procesa el archivo de texto
def procesar_asignaciones_de_asientos(archivo):
    asignaciones = []
    asientos_ocupados = set()
    max_filas = 30
    asientos_por_fila = 'J'

    with open("E:\\Programacion 1\\Final\\archivo.CSV", "rt") as arch:
        for linea in arch:
            partes = linea.strip().split(';')
            if len(partes) == 1:  # Formato 2, necesitamos asignar un asiento
                nombre_pasajero = partes[0]
                asiento_aleatorio = generar_asiento_aleatorio(asientos_ocupados, max_filas, asientos_por_fila)
                asientos_ocupados.add(asiento_aleatorio)
                asignaciones.append((nombre_pasajero, asiento_aleatorio))
            elif len(partes) == 3:  # Formato 1, el asiento ya está asignado
                nombre_pasajero, fila, asiento = partes
                asiento_designado = f"{fila.strip()}{asiento.strip()}"
                if asiento_designado in asientos_ocupados:
                    print(f"Colisión detectada: El asiento {asiento_designado} ya está ocupado.")
                    
                else:
                    asientos_ocupados.add(asiento_designado)
                asignaciones.append((nombre_pasajero, asiento_designado))

    # Ordenar las asignaciones por fila y asiento
    asignaciones.sort(key=lambda x: (int(x[1][:-1]), x[1][-1]))

    # Imprimir las asignaciones
    print("Asignaciones de asiento:")
    for asignacion in asignaciones:
        print(f"Pasajero: {asignacion[0]}, Asiento: {asignacion[1]}")


archivo = open("E:\\Programacion 1\\Final\\archivo.CSV", "rt")
procesar_asignaciones_de_asientos(archivo)