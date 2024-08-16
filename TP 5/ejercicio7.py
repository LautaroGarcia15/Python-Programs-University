import random

def juego():

    intentos = 0
    numero = random.randint(1,500)
    print(numero)

    while True:
        try:
            num_usuario = int(input("Ingrese un numero: "))
            intentos += 1

            while numero != num_usuario:
                assert 1 <= num_usuario <= 500

                if num_usuario < numero:
                    print("El numero que tenes que adivinar es mayor: ")
                    num_usuario = int(input("Ingrese un numero: "))  

                elif num_usuario > numero:
                    print("El numero que tenes que adivinar es menor: ")
                    num_usuario = int(input("Ingrese un numero: "))


                intentos += 1
                 
            print("Si, el numero es: ",numero)
            print("La cantidad de intentos fue: ", intentos)


        except ValueError:
            print("Se permiten solo valores numericos")
            print("Intentalo nuevamente.")
            intentos += 1
            
        except AssertionError:
            print("Solo se permiten numeros entre 1 y 500.")
            print("Intentalo nuevamente.")

juego()