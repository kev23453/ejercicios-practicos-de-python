''' Ejercicio 4:

Solicite al usuario 3 números que representen los lados de un triángulo,
escribe un programa que verifique si los números pueden formar un triángulo.
Para que sea un triángulo válido, debe cumplirse que la suma de cualquier par 
de lados sea mayor que el tercer lado.

El programa debe pedir tres números enteros y determinar si pueden formar un
triángulo válido.

Usar una sola condicional

a+b debe ser mayor que c
c+b debe ser mayor que a
a+c debe ser mayor que b

'''

a = int(input("ingrese el lado A de un triangulo: "))
b = int(input("ingrese el lado B de un triangulo: "))
c = int(input("ingrese el lado C de un triangulo: "))

if( (a+b > c) and (c+b > a) and (a+c > b) ):
    print("el triangulo puede formarse con estos lados")
else:
    print("el triangulo no puede formarse con esos lados")


