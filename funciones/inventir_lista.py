'''39. Función que invierte una lista'''

def invertirLista(limite_lista):
    arreglo = []
    limite = 0
    while limite < limite_lista:
        numero = int(input("ingrese el numero: "))
        limite+=1
        
        arreglo.append(numero)
    print(arreglo)
    
    arreglo.reverse()
    print(arreglo);
    
    print("_______________________________________")
    
    #con el metodo slice
    r = arreglo[::-1]
    print(r)
        
numero = int(input("ingrese el limite del arreglo: "))
invertirLista(numero)