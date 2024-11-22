'''Desarrolla el clásico juego del ahorcado, donde la computadora elige una 
palabra aleatoria y el jugador debe adivinarla letra por letra.
El jugador tiene un número limitado de intentos antes de perder.
Muestra al jugador las letras adivinadas correctamente y las que aún faltan.'''

nombre_juego = r'''==============================================================================
        _                                    _             
       | |                                  | |            
  __ _ | |__    ___   _ __   ___   __ _   __| |  ___   ___ 
 / _` || '_ \  / _ \ | '__| / __| / _` | / _` | / _ \ / __|
| (_| || | | || (_) || |   | (__ | (_| || (_| || (_) |\__ 
 \__,_||_| |_| \___/ |_|    \___| \__,_| \__,_| \___/ |___/
                                                           
=============================================================================='''


import random

palabras = [
    {'palabra': 'estrella', 'pista': 'Cuerpo celeste que brilla con luz propia.'},
    {'palabra': 'viento', 'pista': 'Corriente de aire en movimiento.'},
    {'palabra': 'fuego', 'pista': 'Fenómeno de combustión con calor y luz.'},
    {'palabra': 'río', 'pista': 'Corriente de agua que fluye hacia el mar.'},
    {'palabra': 'bosque', 'pista': 'Gran extensión de terreno con árboles.'},
    {'palabra': 'mar', 'pista': 'Gran extensión de agua salada.'},
    {'palabra': 'nube', 'pista': 'Masa visible de vapor de agua en el cielo.'},
    {'palabra': 'roca', 'pista': 'Piedra grande y sólida.'},
    {'palabra': 'isla', 'pista': 'Porción de tierra rodeada de agua por todas partes.'},
    {'palabra': 'delfin', 'pista': 'Mamífero marino inteligente.'},
    {'palabra': 'desierto', 'pista': 'Lugar seco con escasa vegetación.'},
    {'palabra': 'volcan', 'pista': 'Montaña que expulsa lava cuando entra en erupción.'},
    {'palabra': 'nieve', 'pista': 'Cristales de agua helada que caen del cielo.'},
    {'palabra': 'cactus', 'pista': 'Planta del desierto con espinas.'},
    {'palabra': 'abeja', 'pista': 'Insecto que produce miel.'},
    {'palabra': 'huracan', 'pista': 'Tormenta tropical muy fuerte.'},
    {'palabra': 'ciudad', 'pista': 'Lugar donde viven muchas personas con edificios y calles.'},
    {'palabra': 'puente', 'pista': 'Construcción que une dos lugares separados.'},
    {'palabra': 'tren', 'pista': 'Medio de transporte sobre rieles.'},
    {'palabra': 'avión', 'pista': 'Medio de transporte que vuela.'},
]

#titulo  
print(nombre_juego)
print("escribe 'salir' para quitar el programa \n")

#definir intentos y palabras
intentos = 8
palabra_descompuesta = []
 
#almacenando una palabra aleatoria de la lista
palabra_aleatoria = random.choice(palabras)
palabra_seleccionada = palabra_aleatoria['palabra']

#agregar la palabra a la lista
for n in palabra_seleccionada:
    palabra_descompuesta.append(n)
    
#numero de caracteres de la palabra "agua" (4)
caracteres = len(palabra_descompuesta);

rango_valores = []
for x in range(caracteres):
    rango_valores.append(f"_")
    
    
#colocar dentro del bucle
palabra = ''
for x in rango_valores:
    palabra += x


print(f"tu palabra es: {palabra}")
posicion = 0
pista_proporcionada = False

while True:
    preguntar = input("ingresa una letra: ")
    
    if preguntar == 'salir':
        break
    
    if len(preguntar) > 1:
        print("solo puedes colocar una letra ⚠️")
    
    elif preguntar != palabra_descompuesta[0]:
        print(f"incorrecto ✖️, te quedan {intentos-1}")
        intentos -= 1
    else:
        print("correcto ✅")
        palabra_descompuesta.pop(0)
        
        rango_valores[posicion] = preguntar
        posicion+=1
        
        palabra_cortada = ''
        for n in rango_valores:
            palabra_cortada += n
        
        print(f"tu palabra es: {palabra_cortada}\n") 
    
    
    if palabra_descompuesta == []:
        print("Winner 🥳")
        break
    
    
    if intentos == 2 and pista_proporcionada == False:
        pista = input("Bueno mio, ute lo que va a perder. Quiere la pista? (si/no) ")
        if pista == 'si':
            print(palabra_aleatoria['pista'])
            pista_proporcionada = True
        elif pista == 'no':
            print(palabra_aleatoria['pista'])
            pista_proporcionada = True
        else:
            print("vayase de ahi entonces")
            pista_proporcionada = True
        
    elif intentos == 0:
        print("Game Over 🥀")
        break

'''
rango_valores: [" _ , _ , _ , _ "]

al adivinar una palabra a este arreglo eliminara la primera posicion
y añadira la palabra al input

rango_valores: [" P, _ , _ , _ "]

asi sucesivamente con las siguientes posiciones

'''