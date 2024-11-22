'''
PROGRAMA QUE LEA UN NUMERO ENTERO DE DOS DÍGITOS Y DETERMINE
SI SUS DOS DÍGITOS SON IGUALES.
'''


numero = input("ingresa un numero de 2 digitos: ")

primer_digito = int(numero[0])
segundo_digito = int(numero[1])
    
if primer_digito == segundo_digito:
    print(f"ambos digitos del numero {numero} son iguales")
else:
    print(f"los digitos del numero {numero} son diferentes")