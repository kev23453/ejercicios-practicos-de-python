'''
PROGRAMA QUE LEA UN NUMERO Y DETERMINE SI ES MÚLTIPLO DE 6.

para saber si un numero es multiplo de otro se debe decir si el primer 
digito es divisible del segundo, si el

'''

numero = int(input("introduce el numero: "))
multiplo = 6

if numero % multiplo == 0:
    print(f"{numero} es multiplo de {multiplo}")
else:
    print(f"{numero} no es multiplo de {multiplo}")
