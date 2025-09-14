from datetime import datetime, timedelta
from passlib.context import CryptContext
from jose import jwt, JWTError
from app.schemas.user_schema import UserRead
from app.infrastructure.repositories.user_repository import UserRepository
from app.domain.user import User
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session

from app.infrastructure.database import open_session
import os

pwd_context = CryptContext(schemes = ["bcrypt"], deprecated = "auto")

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/login")

SECRET_KEY = os.getenv("SECRET_KEY")

ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60

def get_password_hash(password: str):
    return pwd_context.hash(password)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)

def get_token_expiration() -> timedelta:
    return timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)

def create_access_token(data: dict) -> str:
        to_encode = data.copy()
        expire_time = datetime.now() + get_token_expiration()
        to_encode.update({"exp": expire_time})
        return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

def get_user_token(token: str = Depends(oauth2_scheme)):
    payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    user_id = int(payload.get("sub"))
    return user_id

def get_current_user(
    token: str = Depends(oauth2_scheme),
    db: Session = Depends(open_session)
):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        user_id = int (payload.get("sub"))
        
        if user_id is None:
            raise HTTPException(status_code=401, detail = "Token inválido")
        
    except JWTError as error:
        raise HTTPException(status_code=401, detail = "Token inválido")

    user = UserRepository(db).get_by_id(user_id)
    print(f'Usuário pego agora: {user.id}')

    if not user:
        raise HTTPException(status_code=401, detail = "Usuário não encontrado")

    print("Usuário final: ", user)
    return UserRead.from_orm(user)
