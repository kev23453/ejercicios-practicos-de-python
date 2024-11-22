'''
2.Leer un número entero y determinar a cuánto es igual al suma de sus dígitos 
pares.
'''

numero = int(input("ingrese un numero entero: "))
numero = str(numero)
suma = 0

for n in numero: 
    if int(n) % 2 == 0:
        suma += int(n)
    
print(suma)

