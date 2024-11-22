'''
1.  Leer un número entero y determinar a cuánto es igual al suma de sus dígitos.
'''

numero = int(input("ingrese el numero entero: "))

numero = str(numero)
suma = 0

for n in numero:
    suma += int(n)
    
print(suma)