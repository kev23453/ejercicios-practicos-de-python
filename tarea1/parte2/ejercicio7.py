'''
Ejercicio 7:

Escribe un programa que pida tres números a, b, y c. El programa debe determinar
si la suma de a y b es mayor que el producto de b y c. Muestra un mensaje indicando
cuál de las dos operaciones es mayor, o si son iguales.

'''
a = int(input("ingresa el valor de a: "))
b = int(input("ingresa el valor de b: "))
c = int(input("ingresa el valor de c: "))

suma = (a+b)
producto = (b*c)

if suma > producto:
    print("la suma es mayor que el producto")
elif producto > suma:
    print("el producto es mayor que la suma")
else:
    print("el producto y la suma son iguales")