
nombre =  input("ingrese su nombre: ")
edad = int(input("ingrese su edad: "))
nacionalidad = input("ingrese su nacionalidad: ")

if edad >= 18 and nacionalidad == 'dominicana': 
    contador = 1
    salvador = 0
    while contador <= 5:
        pedir_numero = int(input("ingrese una cantidad: ")) 
        salvador += pedir_numero
        contador += 1
    
    print(salvador)
        
elif edad >= 18 and nacionalidad != 'dominicana':
    contador2 = 1
    while contador2 <= edad:
        print(f"{contador2} - Visita RD")
        contador2 += 1
 

elif edad < 18 and nacionalidad == 'dominicana':
     edad = edad * 3
     contador3 = 1
     while contador3 <= edad:
         print(f"{contador3} - espera a crecer")
         contador3 += 1
 
else:
    intentos = 0
    numero_correcto = 3
    
    adivinar = int(input("adivina el numero secreto (1- 10): "))
    
    while adivinar != numero_correcto:
        print("numero incorrecto")
        adivinar = int(input("intentalo otra vez: "))
        intentos += 1
    
    if adivinar == numero_correcto:
        print(f"{adivinar} es el numero correcto, felicidades. ")
        print(f"te ha tomado adivinar {intentos} intentos")
 
 
 
