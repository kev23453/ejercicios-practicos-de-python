'''
35. Función que recibe una lista de números y devuelve los positivos
'''

numero = int(input("ingresa el limite del arreglo: "))

def back_positives(parametroLista):
    lista = []
    contador = 0
    while contador < parametroLista:
        preguntar = int(input("ingresa el numero: "))
        contador+=1
        lista.append(preguntar)
        print(lista)
        
    for i in lista:
        if(i > 0):
            print(f"{i}")
    

back_positives(numero)
