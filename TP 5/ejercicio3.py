def obtener_nombre_mes():
    try:
        numero_mes = int(input("Ingrese un número de mes (1-12): "))
        
        meses = ["Enero", "Febrero", "Marzo", "Abril",
                "Mayo", "Junio", "Julio", "Agosto",
                "Septiembre", "Octubre", "Noviembre", "Diciembre"]
        
        mes = meses[numero_mes - 1]
        print("El nombre del mes es: ",(mes))
        
    except ValueError:
        print("Solo se permite el ingreso de numeros")
    except IndexError:
        print("Solo se permite el ingreso de numeros entre el 1 y el 12")
        
    print("   ")
    

obtener_nombre_mes()

