'''
1. Construir una función que reciba como parámetro un entero de hasta 5
dígitos y retorne su último dígito.
'''

def lastNumber(number):
    numero_convert = str(number)
    last_digit = int(numero_convert[-1])
    return last_digit

def main():
    pedir = int(input("ingresa un numero de por lo menos 5 digitos: "))
    
    if pedir <= 99999:
        print(lastNumber(pedir))
    else:
        print('numero invalido')
        

main()