from typing import Optional
from datetime import datetime

class Comment:
    def __init__(
        self,
        comment:str,
        author_id:int,
        article_id:int,
        id:Optional[int]=None,
        parent_comment_id:Optional[int]=None,
        created_at:Optional[datetime]=None,
        updated_at:Optional[datetime]=None
    ):
        self.id=id
        self.comment=comment
        self.author_id=author_id
        self.article_id=article_id
        self.parent_comment_id=parent_comment_id
        self.created_at=created_at
        self.updated_at=updated_at
        
    @classmethod
    def from_orm(cls, db):
        return cls(
            id=db.id,
            comment=db.comment,
            author_id=db.author_id,
            article_id=db.article_id,
            parent_comment_id=db.parent_comment_id,
            created_at=db.created_at,
            updated_at=db.updated_at
        )