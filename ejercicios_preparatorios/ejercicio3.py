'''
PROGRAMA QUE LEA UN NUMERO DE DOS DÍGITOS QUE DETERMINE LA SUMA DE LOS 
DOS DÍGITOS.
'''

numero = int(input("ingresa el numero: "))

if numero < 10 or numero > 99:
    print("introduzca un numero valido (2 digitos)")
else:
    numero = str(numero)
    
    digito1 = int(numero[0])
    digito2 = int(numero[1])
    
    print(f"la suma de los 2 digitos del numero {numero} es {digito1 + digito2}")
    
