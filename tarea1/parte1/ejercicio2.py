'''
2.Leer un número entero y determinar si tiene 3 dígitos.

'''
numero = int(input("ingrese un numero: "))

if numero >= 100 and numero <= 999:
    print(f"{numero} tiene 3 digitos")
else:
    print("numero no valido") 