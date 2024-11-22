'''
5.Leer un número entero de dos dígitos y determinar si ambos dígitos son pares.
'''

numero = int(input("ingrese un numero: "))

if numero >= 10 and numero <= 99:
    convert_int_to_str = str(numero)
    numero1 = int(convert_int_to_str[0])
    numero2 = int(convert_int_to_str[1])
    
    if numero1 % 2 == 0 and numero2 % 2 == 0:
        print("ambos digitos son pares")
    else:
        print("los digitos no son pares entre si")
    
else:
    print("numero invalido, tienes que colocar un numero de 2 digitos")