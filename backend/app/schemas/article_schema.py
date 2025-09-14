from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

class BaseSchema(BaseModel):
    model_config = {
        "from_attributes": True
    }

class ArticleCreate(BaseSchema):
    title: str
    content: str
    image: str | None
    tags: List[str] = []
    
class ArticleRead(BaseSchema):
    id: int
    title: str
    content: str
    image: str | None
    tags: List[str] = []
    created_at: datetime
    updated_at: datetime
    
class ArticleUpdate(BaseSchema):
    id: int
    title: str
    content: str
    tags: List[str] = []
    image: Optional[str]
    
