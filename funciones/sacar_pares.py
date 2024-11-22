'''
36. Función que recibe una lista de números y devuelve el
promedio de los números pares
'''

def promedioPares(limite_arreglo):
    arreglo = []
    contador = 0
    while contador < limite_arreglo:
        numero = int(input("ingresa el numero: "))
        contador += 1
        arreglo.append(numero);
        print(arreglo);
        
    for i in arreglo:
        almacenador = 0
        if(i % 2 == 0):
            print(f"{almacenador + i}")
        
        
        
preguntar = int(input("ingresa cuantos numeros tendra el array: "))

promedioPares(preguntar)