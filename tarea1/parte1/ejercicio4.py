'''
4. Leer un número entero de dos dígitos y determinar a cuánto es
igual la suma de sus dígitos.
'''

numero = int(input("ingrese un numero de 2 digitos: "))
if numero >= 10 and numero <= 99:
    convert = str(numero)
    numero1 = int(convert[0])
    numero2 = int(convert[1])
    
    suma = numero1 + numero2
    print(suma)
    
else:
    print("numero invalido, debe ser de 2 digitos")