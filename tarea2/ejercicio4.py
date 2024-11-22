'''
4.Leer números hasta que digiten 0 y determinar a cuánto es igual el promedio 
de los números terminados en 5.
'''

numero = int(input("ingrese un numero: "))
lista_numeros = []

while numero != 0:
    lista_numeros.append(numero)
    numero = int(input("ingrese un numero: "))
    
#print(lista_numeros)
almacenar = 0
cantidad = 0

for n in lista_numeros:
    if n % 10 == 5:
        almacenar += n
        cantidad += 1

promedio = almacenar / cantidad
print(f"el promedio de los numeros terminados en 5 es: {promedio}")
