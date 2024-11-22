'''
7. Construir una función que reciba como parámetros dos enteros, 
el primero actuará como base y el segundo como exponente y retorne el 
resultado de elevar dicha base a dicho exponente. 
'''

def potencia (x, y):
    return x**y

def main():
    n1 = int(input("ingresa el primer numero: "))
    n2 = int(input("ingresa el segundo numero: "))
    
    print(potencia(n1, n2))

main()