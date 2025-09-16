from fastapi import HTTPException
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError, SQLAlchemyError
from app.domain.user import User
from app.schemas.user_schema import UserRead
from app.infrastructure.models.user_model import UserModel
from app.infrastructure.exceptions import UserAlreadyExistsError, DataBaseError

class UserRepository:
    
    def __init__(self, db:Session):
        self.db = db
    
    def save(self, user:User) -> UserModel:
        try:
            
            user_obj = UserModel(
                name = user.name,
                email = user.email,
                password = user.password
            )
            
            self.db.add(user_obj)
            self.db.commit()
            self.db.refresh(user_obj)
            return UserRead.model_validate(user_obj)
        
        except IntegrityError as error:
            self.db.rollback()
            raise UserAlreadyExistsError(user_obj.email)
            
        except SQLAlchemyError as error:
            self.db.rollback()
            raise DataBaseError(user_obj.email)
            
    def get_by_email(self, user_email:str) -> User:
        return self.db.query(UserModel).filter_by(email=user_email).first()
    
    def get_by_id(self, user_id:int) -> User:
        return self.db.query(UserModel).filter_by(id=user_id).first()
   
    def check_user(self, user_id:int) -> UserModel:
        return self.db.query(UserModel).filter_by(id=user_id).first()

    def get_by_name(self, user_name:str) -> UserModel:
        return self.db.query(UserModel).filter_by(name=user_name).first()