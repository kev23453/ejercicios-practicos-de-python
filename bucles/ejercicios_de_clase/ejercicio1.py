'''
programa que le solicite al usuario un numero y muestre la secuencia
de numeros desde el 1 hasta el numero solicitado
'''

numero = int(input("ingrese el limite del ciclo: "))
contador = 1

while contador <= numero:
    print(contador)
    contador += 1
