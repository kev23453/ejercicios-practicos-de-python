paises = []

for n in range(6):
    registrar = input("ingresa un pais preferido: ")
    paises.append(registrar)
    

new_pais = input("ingresa un nuevo pais: ")
posicion = int(input("ingresa la posicion en que desea insertar pais: "))
posicion = posicion - 1
paises.insert(posicion, new_pais);

for x in paises:
    print(x)
    
    
print('******************************************')


encontrada = False
pais_seleccionado = '';

buscar = input("busca el nombre de un pais: ")
for elemento in paises:
    if(elemento == buscar):
        encontrada = True
        pais_seleccionado = elemento

if(encontrada):
    print(f"has buscado el pais {pais_seleccionado}")
else:
    print(f"{buscar} no ha sido encontrada")    
