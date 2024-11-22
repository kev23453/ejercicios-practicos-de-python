'''
PROGRAMA QUE LEA DOS NÚMEROS Y DETERMINE CUAL ES EL MAYOR

'''

numero1 = int(input("introduce el primer digito: "))
numero2 = int(input("introduce el segundo digito: "))

if numero1 > numero2: 
    print(f"{numero1} es mayor a {numero2}")
else:
    print(f"{numero2} es mayor a {numero1}")