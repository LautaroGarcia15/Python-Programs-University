def suma(cadena1,cadena2):
    try:
        num1 = ''
        num2=  ''
        for i in cadena1:
            if '0' <=  i <= '9':
                num1 += i
        for j in cadena2:
            if '0' <=  j <= '9':
                num2 += j

        num1 = int(num1)
        num2 = int(num2)
        suma = num1 + num2
        print("La suma es: ",suma)
        
    except ValueError:
        print(-1)


cadena1 = input("ingrese una cadena: ")
cadena2 = input("ingrese otra cadena: ")
suma(cadena1,cadena2)