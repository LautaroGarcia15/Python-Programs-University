def calcular_articulos():
    try:
        archivo = open("E:\\Programacion 1\\Final\\articulos.CSV", "rt")
        diccionario_mayor = {}
        diccionario_menor = {}
        diccionario_promedio = {}

        for linea in archivo:
            datos = linea.strip().split(';')

            codigo = datos[0]
            descripcion = datos[1]
            localidad = datos[2]
            provincia = datos[3]
            precio = datos[4]

            if codigo not in diccionario_mayor or int(diccionario_mayor[codigo][0]) < int(precio): #verificacion mayor
                diccionario_mayor[codigo] = [precio,localidad,provincia,descripcion]
                
            if codigo not in diccionario_menor or int(diccionario_menor[codigo][0]) > int(precio): #verificacion menor
                diccionario_menor[codigo] = [precio,localidad,provincia,descripcion]
            
            if codigo not in diccionario_promedio:
                diccionario_promedio[codigo] = [int(precio), 1, descripcion]
            
            else:
                diccionario_promedio[codigo][0] += int(precio)
                diccionario_promedio[codigo][1] += 1
        
        diccionario_mayor_ordenado = dict(sorted(diccionario_mayor.items(), key = lambda x: x[1][3]))
        diccionario_menor_ordenado = dict(sorted(diccionario_menor.items(), key= lambda x : x[1][3]))
        diccionario_promedio_ordenado = dict(sorted(diccionario_promedio.items(), key= lambda x: x[1][2]))

        print()
        print("PRECIOS MAXIMOS POR PRODUCTO: ")
        for producto in diccionario_mayor_ordenado:
            print("Producto: ", producto, ", Precio: ",diccionario_mayor_ordenado[producto][0], ", Localidad: ", diccionario_mayor_ordenado[producto][1], ", Provincia: ", diccionario_mayor_ordenado[producto][2])
        
        print()
        print("PRECIOS MINIMOS POR PRODUCTO: ")
        for producto in diccionario_menor_ordenado:
            print("Producto: ", producto, ", Precio: ",diccionario_menor_ordenado[producto][0], ", Localidad: ", diccionario_menor_ordenado[producto][1], ", Provincia: ", diccionario_menor_ordenado[producto][2])
        
        print()
        print("PRECIO PROMEDIO POR PRODUCTO")
        for producto in diccionario_promedio_ordenado:
            print("Poducto: ",producto, ", Precio promedio: ", (diccionario_promedio_ordenado[producto][0])/(diccionario_promedio_ordenado[producto][1] ))

            
    except FileNotFoundError:
        print("No se encontro el archivo.")
    except OSError as mensaje:
        print("Error: ", mensaje)
    finally:
        try:
            archivo.close()
        except NameError:
            pass

calcular_articulos()