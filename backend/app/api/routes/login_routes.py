from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from app.application.user_service import UserService
from app.schemas.user_schema import UserLogin
from app.infrastructure.database import open_session
from app.utils.api_response import response_success, response_error
from app.api.dependency import CommonDeps, get_common_deps

router = APIRouter(prefix="/login", tags=["login"])

@router.post("/")
def user_login(user_credentials: UserLogin, db:Session = Depends(open_session)):
    
    print('User credentials: ', user_credentials)
    try:
        user_service = UserService(db)
        token = user_service.login(user_credentials)
        print('Token: ', token)
        if token:
        
            return response_success(
                data = {
                    "access_token": token,
                    "token_type": "bearer",
                },
                message= "Usuário logado com sucesso!"
            )
            
    except ValueError as error:
        return response_error(
            message = str(error),
            status_code = status.HTTP_401_UNAUTHORIZED  
        )
        
    # return response_error(
    #     status_code=401,
    #     details = "E-mail ou senha inválidos"
    # )
    