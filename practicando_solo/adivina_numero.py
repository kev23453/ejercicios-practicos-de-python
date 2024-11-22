'''
- Crea un juego en el que la computadora elija un número del 1 al 10, 
y el usuario tiene que adivinarlo. El juego continúa hasta que el usuario
acierte el número.

- con 5 intentos
            
- cada vez que pierda un intento que me diga cuantos me quedan

'''

import random

numero_aletorio = random.randint(1, 10)
contador = 1
intentos = 5

numero = int(input("ingresa un numero entre 1 a 10: "))

while numero != numero_aletorio:
    print("numero equivocado")
    numero = int(input("ingresa otro numero: "))
    contador += 1
    print(f"te quedan {intentos - contador} intentos")
    if contador == intentos:
        print("intentos agotados")
        break;
    
if numero == numero_aletorio:
    print("respuesta correcta")
    
    
    
    

'''almacenador.append(pedir_numero)
        contador += 1
    
    contador_lista = 0
    for n in almacenador:
        contador_lista += n
    
    print(contador_lista)'''    
