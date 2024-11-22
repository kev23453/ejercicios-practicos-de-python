frutas = [] #creamos el arreglo. Vacio
 
#Con un for iteramos para pedir la cantidad de elementos previamente establecido
for i in range(3):
    frutas.append(input('Ingrese la fruta: '))
 
#Pedimos el valor a buscar
busqueda = input('Ingrese la fruta que desea comerse ahora: ')
 
encontrada = False
frutaSeleccionada = ''
 
for elemento in frutas:
    if(elemento == busqueda):
       encontrada = True
       frutaSeleccionada = elemento
 
if(encontrada):
    print(f'Usted se va a comer la {frutaSeleccionada}')
else:
    print(f'{busqueda} no encontrada')
   
 