'''
6. Construir una función que reciba como parámetro dos enteros de dos dígitos 
cada uno y retorne true si son inversos. Ejemplo: 83 es inverso de 38. Deberá 
retornar false si no es así.
'''

def inverso(x:int, y:int):
    if (x < 10 or x > 99) or (y < 10 or y > 99):
        return "numero invalido"
    else:
        x = str(x)
        y = str(y)
        
        if x == (y[::-1]):
            return True
        else:
            return False
        
def main():
    n1 = int(input("ingrese el primer numero: "))
    n2 = int(input("ingrese el segundo numero: "))
    
    print(inverso(n1, n2))

main()