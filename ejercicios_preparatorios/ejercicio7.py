'''
PROGRAMA QUE LEA UN NUMERO DE TRES DÍGITOS (DEBE VALIDAR ESA ENTRADA) 
Y CALCULE LA SUMATORIA DE SUS DÍGITOS
'''

numero = int(input("ingresa un numero de 3 digitos: "))

if numero < 100 or numero > 999:
    print("introduzca un valor valido de 3 digitos")
else:
    numero = str(numero)
    
    digit1 = int(numero[0])
    digit2 = int(numero[1])
    digit3 = int(numero[2])
    
    print(f"la suma de los 3 digitos de {numero} es {digit1 + digit2 + digit3}")
    
