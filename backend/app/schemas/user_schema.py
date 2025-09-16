from pydantic import BaseModel, EmailStr
from datetime import datetime

class BaseSchema(BaseModel):
    model_config = {
        "from_attributes": True
    }

class UserCreate(BaseSchema):
    name: str
    email: EmailStr
    password: str
    
class UserRead(BaseSchema):
    id: int
    name: str
    email: EmailStr
    created_at: datetime

class UserReadArticle(BaseSchema):
    id: int
    name: str
    
class UserLogin(BaseSchema):
    email: EmailStr
    password: str