from fastapi import APIRouter, HTTPException, Depends, Header
from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session
from app.application.user_service import UserService
from app.schemas.user_schema import UserCreate, UserRead, UserLogin
from app.infrastructure.database import open_session
from app.utils.api_response import response_success, response_error
from app.api.auth import get_current_user
from app.api.dependency import CommonDeps, get_common_deps
from app.infrastructure.exceptions import UserAlreadyExistsError

router = APIRouter(prefix="/users", tags=["users"])

@router.post("/")
def create_user(user:UserCreate, db:Session = Depends(open_session)):
    
    service_user = UserService(db)
    
    try:
        user_created = service_user.create_user(
             user_data = user
        )
        
        return response_success(
            data = user_created.model_dump(include={"id", "name", "email"}),
            message = "Usuário criado com sucesso!"
        )
        
    except UserAlreadyExistsError as error:
        return response_error(
            details = error,
            status_code = 400      
        )
        
    # except HTTPException as error:
    #     return response_error(
    #         detail = str(e)
    #         message = error.detail,
    #         status_code = error.status_code
    #     )


@router.get("/getuser")
def get_user(user:UserRead = Depends(get_current_user)):
   
    print("Common user: ", user)
    
    return response_success(
        data = jsonable_encoder(user),
    )
    # user_service = UserService(db)