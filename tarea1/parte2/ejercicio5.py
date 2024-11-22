'''
Ejercicio 5:

Escribe un programa que solicite dos números enteros. Si ambos números son
positivos, el programa debe mostrar su producto. Si ambos son negativos, debe
mostrar su suma. Si uno es positivo y el otro negativo, el programa debe mostrar
la resta del mayor menos el menor.

'''

num1 = int(input("ingrese un numero: "))
num2 = int(input("ingrese un numero: "))

if(num1 > 0 and num2 > 0):
    producto = num1 * num2
    print(producto)
elif(num1 < 0 and num2 < 0):
    suma = num1 + num2
    print(suma)
else:
    if(num1 > num2):
        resta = num1 - num2
        print(resta)
    else:
        resta = num2 - num1
        print(resta)



