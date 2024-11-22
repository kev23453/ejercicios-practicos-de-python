usuario = "mr.garcia"
contraseña = "yosemite"

def validarUsuario(user, password): 
    us = usuario
    ps = contraseña
    if(user == us and password == ps):
        print(f"Bienvenido {user}")
    else:
        print("Acceso denegado")
        

pusuario = input("ingresa tu nombre usuario: ")
pcontraseña = input("ingresa la contraseña: ")

validarUsuario(pusuario, pcontraseña)