'''
34. Función que calcula el cuadrado de todos los números en una lista
'''

def cuadradoList(parametroLista):
    lista = []
    contador = 0
    while contador < parametroLista:
        preguntar = int(input("ingresa el numero: "))
        contador+=1
        lista.append(preguntar)
        print(lista)
        
    for i in lista:
        print(f"{i} elevado al cuadrado es = {i**2}")
        
        
cuadradoList(4)

