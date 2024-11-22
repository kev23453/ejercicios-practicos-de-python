'''  Ejercicio 3:

Escribe un programa que solicite tres números: a, b y c. El programa debe
verificar si c está dentro del rango definido por a y b. Imprime un mensaje
que indique si c está dentro del intervalo o no.

Usar una sola condicional '''

a = int(input("ingresa un numero a: "))
b = int(input("ingresa un numero b: ")) 
c = int(input("ingresa un numero c: "))


if (c >= a and c <= b):
    print(f"{c} esta en el intervalo entre {a} y {b}")
else:
    print(f"{c} no esta en el intervalo entre {a} y {b}")

