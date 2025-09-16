from fastapi import status, HTTPException
from sqlalchemy.orm import Session
from app.infrastructure.repositories.user_repository import UserRepository
from app.domain.user import User
from app.schemas.user_schema import UserCreate, UserRead, UserLogin
from app.infrastructure.exceptions import UserAlreadyExistsError, DataBaseError
from app.api.auth import pwd_context, create_access_token, get_password_hash

class UserService:
    
    def __init__(self, db: Session):
        self.repository = UserRepository(db)
        self.db = db
        
    # def create_user(self, db:Session, name:str, email:str, password:str):
    def create_user(self, user_data:UserCreate) -> UserRead:
        
        """Cria o usuário"""
        
        hashed_password = get_password_hash(user_data.password)
        
        user = User(
            name = user_data.name,
            email = user_data.email,
            password = hashed_password
        )
        
        try:
            user_repo = self.repository.save(user)
            return UserRead.model_validate(user_repo)
        
        except UserAlreadyExistsError as error:
            raise UserAlreadyExistsError("Email já cadastrado")
        
    def login(self, user_credentials: UserLogin) -> str:
        
        """Função de login do usuário, retornando uma string de sub"""
        
        user = self.repository.get_by_email(user_credentials.email)
        
        if not user:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="E-mail ou senha inválidos")
        
        if not pwd_context.verify(user_credentials.password, user.password):
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Credenciais inválidas")
        
        return create_access_token(data={"sub": str(user.id)})

    def check_user(self, user_id:int) -> UserRead:
        return UserRead.model_validate(self.repository.check_user(user_id))
    
        