'''
Escribe un programa que utilice un bucle while para pedir al usuario
números enteros. El programa debe seguir pidiendo números hasta que el 
usuario introduzca un número negativo. Al final, debe imprimir la suma de
todos los números ingresados (excluyendo el negativo).

'''


#while True:
 #   input()

'''
Crea un programa que utilice un bucle for para imprimir una tabla de
multiplicar del 1 al 12 de un número que el usuario ingrese.
si numero es mayor a 12, repetir el programa
'''

numero = int(input("que tabla de multiplicar quieres ver? "))
limite = 12

while numero <= limite:
    print(f"{numero} x {limite}: {numero * limite}")
    numero += 1
    







'''numero = int(input("que tabla de multiplicar quieres ver? "))

if numero > 12 or numero < 1:
    print("ingrese otro valor")
else:
    rango = 12
    for num in range(rango):
        print(f"{numero} x {num} = {numero * num}")
    '''
