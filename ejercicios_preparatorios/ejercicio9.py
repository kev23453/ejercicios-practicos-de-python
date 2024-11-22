'''
PROGRAMA QUE LEA UN NUMERO DE DOS DÍGITOS Y DETERMINE SI UN DÍGITO
ES MÚLTIPLO DE OTRO


ARREGLAR

'''

numero = int(input("introduzca un numero de 2 digitos: "))

if numero < 10 and numero > 99:
    print("introduzca un numero valido, debe ser de 2 digitos")
else:
    numero = str(numero)
    
    digito1 = int(numero[0])
    digito2 = int(numero[1])
    
    if digito1 % digito2 == 0 :
        print(f"{digito1} es multiplo de {digito2}") 
    else:
        print(f"{digito1} no es multiplo de {digito2}")
    
