from datetime import datetime
from typing import Optional, List
from .tag import Tag

class Article:
    def __init__(
        self,
        title:str,
        content:str,
        image:str,
        author_id:int,
        id:Optional[int]=None,
        tags:Optional[List[Tag]]=None,
        created_at:Optional[datetime]=None,
        updated_at:Optional[datetime]=None
    ):
        self.id = id
        self.title = title
        self.content = content
        self.image = image
        self.author_id = author_id
        self.tags = tags or []
        self.created_at = created_at
        self.updated_at = updated_at
        
    @classmethod
    def from_orm(cls, db):
        return cls(
            id=db.id,
            title=db.title,
            content=db.content,
            image=db.image,
            author_id=db.author_id,
            tags=[item.tag for item in db.tags],
            created_at=db.created_at,
            updated_at=db.updated_at
        )