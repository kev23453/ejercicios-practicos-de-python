'''
5. Construir una función que reciba como parámetros dos números enteros y muestre
en consola cuál es el mayor

'''


def evaluarMayor(x, y):
    if x > y:
        print(f"{x} es mayor que {y}")
    else:
        print(f"{y} es mayor que {x}")


def main():
    n1 = int(input("ingresa el primer numero: "))
    n2 = int(input("ingresa el segundo numero: "))
    
    evaluarMayor(n1, n2)
    
main()