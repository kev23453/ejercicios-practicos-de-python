class User:
    def __init__(self, username, password, edad) -> None: #constructor
        self.username:str = username 
        self.password:str = password
        self.edad:int  = edad
        
    def registrarUser(self):
        print(f"{self.username},{self.password}, {self.edad}")

        
        
new_usuario = User('pedro','0349432','24')

new_usuario.registrarUser()
