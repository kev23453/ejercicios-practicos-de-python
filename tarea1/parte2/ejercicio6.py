'''
Ejercicio 6:

Haz un programa que pida dos números: x y y. El programa debe calcular la raíz
cuadrada de ambos números, siempre y cuando ambos números sean no negativos.
Si alguno de los números es negativo, el programa debe mostrar un mensaje
indicando que no se pueden calcular las raíces cuadradas.

'''
x = int(input("ingrese el valor de x: "))
y = int(input("ingrese el valor de y: "))

if(x > 0 and y > 0):
    raiz1 = x**0.5
    raiz2 = y**0.5
    print(f"la raiz cuadrada de {x} es {raiz1} y la raiz cuadrada de {y} es {raiz2}")
else:
    print("no se puede calcular la raiz cuadrada, uno o ambos numeros son negativos")
    