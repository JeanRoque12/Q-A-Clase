import re

class UserManager:
    EMAIL_REGEX = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    PASSWORD_REGEX = r"^(?=.*[A-Za-z])(?=.*\d)(?=.*[A-Z])[A-Za-z\d@$!%*?&]{8,}$"
    
    def __init__(self):
        self.users = {}
    
    def add_user(self, username, email, password):
        if not re.match(self.EMAIL_REGEX, email):
            raise ValueError("Correo inválido")
        if not re.match(self.PASSWORD_REGEX, password):
            raise ValueError("Contraseña insegura: mínimo 8 caracteres, al menos una letra y un número")
        
        if username in self.users:
            raise ValueError("El usuario ya existe")
        
        self.users[username] = {"email": email, "password": password}
        return "Usuario creado exitosamente"
    
    def remove_user(self, username):
        if username not in self.users:
            raise ValueError("Usuario no encontrado")
        
        del self.users[username]
        return "Usuario eliminado"
    
    def get_users(self):
        return self.users
