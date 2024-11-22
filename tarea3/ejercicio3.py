'''
3. Construir una función que reciba dos números enteros y muestre en consola 
la tabla de multiplicar del primer número siendo el límite de la tabla el
Segundo número. Ejemplo: Si se pasa el 2 y el 7. Debera mostrar la tabla del 2,
con los multiplicadores hasta el 7
'''

def operacion(x, y):
    for n in range(1, y+1, 1):
        print(f"{x} x {n} = {x * n}")

def main():
    num1 = int(input("ingresa el primer numero: "))
    num2 = int(input("ingresa el segundo numero: "))

    operacion(num1, num2)
    
main()