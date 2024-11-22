#conversor de unidades
metros = int(input("ingrese la cantidad de metros a convertir: "))

cm = metros * 100
mm = cm * 10
print(f"{metros} metros equivalen a {cm} centimetros y {mm} milimetros")




#area de un circulo
radio = int(input("ingrese el radio del circulo para calcular su area: "))
PI = 3.1416
area = 0

area = round(PI * radio ** 2, 2)
print(f"el area del circulo es {area}")




#operaciones basicas

numero1 = int(input("ingrese el primer numero: "))
numero2 = int(input("ingrese el segundo numero: "))

suma = numero1 + numero2
resta = numero1 - numero2
multiplicacion = numero1 * numero2
division = numero1 / numero2

print(f"{numero1} + {numero2} = {suma}")
print(f"{numero1} - {numero2} = {resta}")
print(f"{numero1} * {numero2} = {multiplicacion}")
print(f"{numero1} / {numero2} = {division}")





#calculo de edad

fecha_nacimiento = int(input("ingrese la fecha en la cual usted nacio: "))
año_actual = int(input("ingrese el año actual: "))

edad = año_actual - fecha_nacimiento
print(f"usted tiene en este momento {edad} años")






#intercambio de valores
valor1 = int(input("ingrese el primer valor: "))
valor2 = int(input("ingrese el segundo valor: "))

valor1, valor2 = valor2, valor1

print
(f"el primer valor ingresado ahora es: {valor1} y su segundo valor ahora es: {valor2}")