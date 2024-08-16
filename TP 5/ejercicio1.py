def ingresar_numero_natural():
    while True:
        try:
            valor = int(input("Ingrese un número natural: "))
            assert valor >= 0
            return valor
        except ValueError:
            print("Solo se permiten numeros.")
        except AssertionError:
            print("El numero debe ser mayor a 0.")
        print("Intenta nuevamente.")


numero_natural = ingresar_numero_natural()
print(f"Ha ingresado el número natural: {numero_natural}")