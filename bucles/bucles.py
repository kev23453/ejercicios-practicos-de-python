'''

los bucles en python

--while



'''


'''bucles para definir contadores de numeros'''

x = 0
while x < 10:
    print(f"numero{x}")
    x += 1



'''bucles para recorrer arrays'''

array = ["perro", "gato", "caballo", "halcon", "leopardo"]

for arreglo in array:
    print(arreglo)
    
    
    
    
autos = ["Mazda", "Toyota", "Kia", "Ford", "Tesla", "Audi", "Mercedez Benz"]
contador = 0

while contador < len(autos):
    print(autos[contador])
    contador += 1
