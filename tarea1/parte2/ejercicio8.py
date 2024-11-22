'''
Ejercicio 8:

Crea un programa que pida dos números enteros x y y. El programa debe:

Imprimir el mayor de los dos números.
Si el mayor es divisible por el menor, mostrar el cociente de la división.
Si no es divisible, mostrar el residuo de la división.

'''

x = int(input("introduce el valor de numero x: "))
y = int(input("introduce el valor de número y: "))

if x > y:
    mayor = x
    menor = y
else:
    mayor = y
    menor = x

print(f"El mayor de los dos números es: {mayor}")

if mayor % menor == 0:
    cociente = mayor // menor
    print(f"el mayor es divisible por el menor, el cociente es: {cociente}")
else:
    residuo = mayor % menor
    print(f"El mayor no es divisible por el menor, el residuo es: {residuo}")






