new_planet = ''#variable que almacenara nuestros datos del input
planets = []#array vacio

while new_planet.lower() != 'done':#mientras pongamos un valor que sea diferente de "done" hara una accion
    if new_planet:#si la variable es true entonces hara algo
        planets.append(new_planet)#al array se le agregan con el metodo append el valor que le pasemos a new_planet
    new_planet = input('Enter a new planet or done if done: ')#aqui declaramos el input
    

for planet in planets: #aqui hacemos un for para recorrer el array y le pasamos un param a cada valor
    print(planet)#aqui imprimimos todas los parametros
    
    
'''
explicacion:

la aplicacion se basa en indicarnos que insertemos un nuevo planeta y que salgamos,
si insertamos un dato diferente a salir el bucle se va a repetir, en cambio si colocamos
salir entonces se saldra de la estructura repetitiva, mientras insertemos datos estos iran 
llenando una coleccion (array), luego con un for se recorre ese array para traer de vuelta 
todos los parametros que se han estado almacenando en los arrays.

'''