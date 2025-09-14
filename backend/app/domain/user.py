from typing import Optional
from datetime import datetime

class User:
    def __init__(
        self,
        name:str,
        email:str,
        password:str,
        id:Optional[int]=None,
        created_at:Optional[datetime]=None,
        updated_at:Optional[datetime]=None
    ):
        self.id=id
        self.name = name
        self.email = email
        self.password = password
        self.created_at = created_at
        self.updated_at = updated_at
        
    @classmethod
    def from_orm(cls, db):
        return cls(
            id=db.id,
            name=db.name,
            email=db.email,
            created_at=db.created_at
        )
        
    @classmethod
    def encrypt_password(cls):
        #Criar aqui a regra para encriptação de senha
        pass         
    