'''
41. Función que recibe una lista y elimina los valores negativos
'''

def eliminarNegativos(limite_lista):
    coleccion = []
    contador = 0
    while contador < limite_lista:
        numero = int(input("ingresa el numero: "))
        contador+=1
        
        if(numero >= 0):
            coleccion.append(numero)
            
    print(coleccion)
        

numero = int(input("ingrese el limite de numeros de la coleccion: "))
eliminarNegativos(numero)

