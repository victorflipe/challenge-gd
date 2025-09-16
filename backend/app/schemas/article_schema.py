from pydantic import BaseModel
from typing import Optional
from datetime import datetime
from .tag_schema import TagRead
from .user_schema import UserReadArticle

class BaseSchema(BaseModel):
    model_config = {
        "from_attributes": True
    }

class ArticleCreate(BaseSchema):
    title: str
    content: str
    image: Optional[str]
    author_id: Optional[int] = None
    tags: list[str] = []
    
class ArticleRead(BaseSchema):
    id: int
    title: str
    content: str
    image: Optional[str]
    author: UserReadArticle
    tags: list[TagRead] = []
    created_at: datetime
    updated_at: datetime
    
class ArticleUpdate(BaseSchema):
    id: int
    title: str
    content: str
    tags: list[TagRead] = []
    image: Optional[str]
    
