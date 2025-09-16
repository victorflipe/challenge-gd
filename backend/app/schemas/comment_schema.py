from typing import Optional
from pydantic import BaseModel
from datetime import datetime
from .user_schema import UserRead

class CommentCreate(BaseModel):
    comment: str
    parent_comment_id: Optional[int] = None
    
    
class CommentRead(BaseModel):
    
    comment: str
    parent_comment_id: Optional[int] = None
    replies: Optional[list["CommentRead"]] = []
    author: UserRead
    created_at: datetime
    updated_at: datetime
    
    model_config = {
        "from_attributes": True
    }

CommentRead.update_forward_refs()