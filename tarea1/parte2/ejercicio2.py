'''
Ejercicio 2:

Crea un programa que determine si un año es bisiesto. Google
las condiciones para que un año sea bisiesto. El programa debe pedir al 
usuario un año y decir si es bisiesto o no.

Usar una sola condicional
'''

año = int(input("Introduce un año: "))

if (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0):
    print(f"el año {año} es bisiesto")
else:
    print(f"El año {año} no es bisiesto.")
