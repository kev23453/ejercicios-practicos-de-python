'''
9. Leer dos números enteros de dos dígitos y determinar si la suma de
los dos números da como resultado un número par.
'''

numero1 = int(input("ingrese el primer numero: "))
numero2 = int(input("ingrese el segundo numero: "))

if (numero1 >= 10 and numero1 <= 99) and (numero2 >= 10 and numero2 <= 99):
    resultado = numero1 + numero2
    if resultado % 2 == 0:
        mensaje = "es par"
        print(f"la suma de {numero1} + {numero2} = {resultado} y este es {mensaje}")
    else:
        mensaje = "es impar"
        print(f"la suma de {numero1} + {numero2} = {resultado} y este es {mensaje}")
else:
    print("ambos numeros deben ser de 2 digitos")


