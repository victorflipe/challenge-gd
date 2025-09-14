class InfrastructureError(Exception):
    pass

class UserAlreadyExistsError(InfrastructureError):
    def __init__(self, email:str):
        self.email = email
        super().__init__(f"O e-mail '{email}' já está em uso.")
        
class DataBaseError(InfrastructureError):
    def __init(self, message:str = "Erro no banco de dados"):
        super().__init__(message)