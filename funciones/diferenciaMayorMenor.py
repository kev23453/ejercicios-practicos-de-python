'''
38. Función que recibe una lista de números y devuelve la diferencia
entre el mayor y el menor
'''

def mayorMenor(limite):
    lista = [];
    contador = 0;
    while contador < limite:
        numero = int(input("ingresa un numero: "))
        contador+=1
        
        lista.append(numero);
        
    print(lista)
    mx = max(lista)
    mn = min(lista)
    
    res = mx - mn
    
    print(f"la diferencia entre el mayor y el menor es: {res}")


numero = int(input("ingresa cuantos numeros tendra tu lista: "))

mayorMenor(numero)
