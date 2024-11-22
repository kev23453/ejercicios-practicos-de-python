'''
2. Construir una función que reciba como parámetro un entero y retorne 
true si dicho entero es par o false si es impar
'''

def par(numero):
    return numero % 2 == 0

def main():
    numero = int(input("ingresa un numero: "))
    print(par(numero))

main()