from functions.mostrar_texto import texto
from functions.character import caracther

texto("hola como estas", "yellow")
#texto(f"{Fore.RED} que personaje vas a elegir [1] flower boy - [2] sir baudelarie")

#characters 
flower_boy = caracther()
sir_bauledaire = caracther()

#asign character
personaje = None

texto("Bienvenido a tyler's world, con que personaje te gustaria iniciar? \n", "white")

print("[1]- flower boy\n")
print("[2]- sir bauledaire\n")

elegir = int(input("digita el numero del personaje: "))
if elegir == 1:
    print("haz elegido a flower boy")
elif elegir == 2:
    print("haz elegido a sir bauledaire")


