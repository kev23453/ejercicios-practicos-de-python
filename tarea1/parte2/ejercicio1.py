'''
Ejercicio 1:

Escribe un programa que pida al usuario un número entero y determine si:

El número es positivo.
El número es par.
El número es múltiplo de 5.

Si cumple con estas condiciones, mostrar un mensaje de felicitaciones en 
caso contrario mostrar un mensaje de que lo intente después.

'''

numero = int(input("ingresa un numero: "))

if(numero > 0 and numero % 2 == 0 and numero % 5 == 0):
    print("felicitaciones")
else:
    print("intentalo mas tarde")



