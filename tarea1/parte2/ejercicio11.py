'''
Ejercicio 11

Escribe un programa que calcule el descuento en una compra. El programa debe
solicitar el total de la compra y aplicar el siguiente descuento:

Si el total es mayor que 500, aplica un 20% de descuento.
Si el total está entre 200 y 500, aplica un 10% de descuento.
Si el total es menor que 200, no hay descuento.

'''

total = int(input("ingrese el total de la compra: "))

if total > 500:
    descuento = (total * 20) / 100
    print(f"se ha aplicado un 20% de descuento, su total es {total - descuento}")
elif total >= 200 and total <= 500:
    descuento = (total * 10) / 100
    print(f"se ha aplicado un 10% de descuento, su total es {total - descuento}")
else:
    print("no hay descuento")