'''
PROGRAMA QUE LEA TRES NÚMEROS Y LOS MUESTRE EN ORDEN ASCENDENTE
(DE MENOR A MAYOR)
'''

#forma corta

numero1 = int(input("introduzca el numero: "))
numero2 = int(input("introduzca el numero: "))
numero3 = int(input("introduzca el numero: "))

lista_numeros = [numero1, numero2, numero3]

lista_numeros.sort();

print(f"ordenamiento de menor a mayor {lista_numeros}")
