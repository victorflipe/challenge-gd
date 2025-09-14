from typing import Optional
from pydantic import BaseModel
from datetime import datetime

class CommentCreate(BaseModel):
    comment: str
    parent_comment_id: Optional[int] = None
    
    
class CommentRead(BaseModel):
    
    comment: str
    parent_comment_id: Optional[int] = None
    author_id: int
    created_at: datetime
    updated_at: datetime
    
    model_config = {
        "from_attributes": True
    }
