'''
11. Leer un número entero de tres dígitos y determinar a cuánto es igual
la suma de sus dígitos.
'''


numero1 = int(input("ingrese un numero de 3 digitos: "))

if (numero1 >= 100 and numero1 <= 999):
    int_to_str1 = str(numero1) 
    resultado = int(int_to_str1[0]) + int(int_to_str1[1]) + int(int_to_str1[2])      
    print(f"la suma de los digitos de {numero1} es: {resultado}")
else:
    print("ambos numeros deben ser de 3 digitos")




