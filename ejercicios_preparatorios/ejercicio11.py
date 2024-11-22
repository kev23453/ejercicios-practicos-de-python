'''
PROGRAMA QUE LEA UN NUMERO ENTERO DE TRES DIGITOS 
Y DETERMINE SI EL PRIMERO ES IGUAL AL ULTIMO.
'''

numero = int(input("ingresa un numero de 3 digitos: "))

if numero < 100 and numero > 999:
    print("debes ingresar un numero valido que contenga 3 digitos")
else:
    numero = str(numero)
    
    digito1 = numero[0]
    digito2 = numero[1] 
    digito3 = numero[2] 
    
    if digito1 == digito3: 
        print(f"el primer y ultimo digito de este numero: {numero} son iguales")
    else:
        print(f"el primer y ultimo digito de este numero: {numero} son diferentes")



