''' 7.Leer un número y calcularle su factorial.
    5*4*3*2*1 = 120
'''
print ("Programa que calcula el factorial")
numero = int(input("Introduzca el número: "))

factorial = 1

i = 1
while (i <= numero):
    factorial = factorial * i
    i = i + 1

print ("El factorial de " + str(numero) + " es " + str(factorial))