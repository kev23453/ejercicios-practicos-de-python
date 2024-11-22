'''
48. Función que filtra los números impares de una lista
'''

def filtrarImpares(limite_arreglo):
    arreglo = []
    limite = 0
    while limite < limite_arreglo:
        numero = int(input("ingrese un numero: "))
        limite+=1
        
        if(numero % 2 == 1):
            arreglo.append(numero)
    
    print(arreglo)

numero = int(input("ingrese la cantidad que tendra el array: "))
filtrarImpares(numero)
