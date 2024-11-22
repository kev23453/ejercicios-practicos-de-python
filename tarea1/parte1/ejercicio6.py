'''
6.Leer un número entero de dos dígitos y determinar si los dos dígitos
son iguales.
'''

numero = int(input("ingrese un numero de 2 digitos: "))
if numero >= 10 and numero <= 99:
    int_to_str = str(numero)
    if int_to_str[0] == int_to_str[1]:
        print("los digitos son iguales")
    else:
        print("los digitos son diferentes")
else:
    print("te dije 1 numero de 2 digitos >:( )")