'''
PROGRAMA QUE LEA DOS NÚMEROS Y DETERMINE SI LA SUMATORIA DE AMBOS 
NÚMEROS ES PAR O IMPAR
'''

numero1 = int(input("introduzca el primer numero: "))
numero2 = int(input("introduzca el segundo digito: "))

par_impar = (numero1 + numero2) % 2

if par_impar == 0:
    print(f"la suma de los 2 valores es par")
else:
    print(f"la suma de los 2 valores es impar")