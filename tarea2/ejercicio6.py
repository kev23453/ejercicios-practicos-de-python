'''
6.Leer un número entero y mostrar en pantalla su tabla de multiplicar (hasta el 12)
'''
numero = int(input("que tabla de multiplicar deseas ver?"))

for n in range(1, 13):
    print(f"{n} x {numero} = {n * numero}")