'''
3.Leer 2 números enteros y determinar cuál de los dos tiene mayor cantidad
de dígitos.
'''

a = int(input("ingresa el primer numero entero: "))
b = int(input("ingresa el segundo numero entero: "))

aCantidad = len(str(a))
bCantidad = len(str(b))

if aCantidad > bCantidad:
    print(f"{a} tiene mas caracteres que {b}")
else:
    print(f"{b} tiene mas caracteres que {a}")
    
