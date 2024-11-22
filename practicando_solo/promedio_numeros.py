contador = 0
numeros = []
   
while contador < 5:
    contador+=1
    numero = int(input("ingresa un numero: "))
 
    numeros.append(numero)
    print(numeros)
    
    if contador == 5:
        resultado = 0
        for i in numeros:
            resultado += i
            
        print(resultado / 5)
        

print("____________________________________________")






#sin array
contador = 0
almacenador = 0

while contador < 5:
    contador +=1 
    numero = int(input("ingresa un numero: "))
    almacenador += numero
    
print(almacenador/5)
        
