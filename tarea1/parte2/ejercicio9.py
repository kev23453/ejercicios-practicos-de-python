'''Ejercicio 9:

Escribe un programa que solicite dos números enteros. El programa mostrara un
mensaje con su matricula si ambos números son pares y ambos números son divisibles
entre 3. O si al menos uno de los números es negativo.

En caso contrario mostrar un mensaje con su nombre.

Usar una sola condicional
'''

num1 = int(input("ingrese un numero: "))
num2 = int(input("ingrese un numero: "))

if((num1 % 2 == 0 and num1 % 3 == 0) or (num2 % 2 == 0 and num2 % 3 == 0) or (num1 < 0 or num2 < 0)):
    print("2024-1611")
else:
    print("kevin francisco")