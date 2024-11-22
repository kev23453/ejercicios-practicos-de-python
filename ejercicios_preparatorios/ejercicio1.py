#PROGRAMA QUE LEA UN NUMERO Y DETERMINE SI ES POSITIVO O NEGATIVO,
# MOSTRANDO UN MENSAJE PARA CADA CASO.

numero = int(input("ingrese el numero: "))

if numero > 0:
    print(f"{numero} es positivo")
elif numero == 0:
    print(f"{numero} es cero")
else:
    print(f"{numero} es negativo")
