import math 
def raiz():
    while True:
        try:
            num =  int(input("ingrese un numero: "))
            assert num >= 0
            raiz = math.sqrt(num)
            print("La raiz es: ", raiz)
            break

        except ValueError:
            print("Solo se permite el ingreso de numeros positivos.") 
        except AssertionError:
            print('El numero debe ser positivos.')
        print("Intentelo de nuevo.")

raiz()


