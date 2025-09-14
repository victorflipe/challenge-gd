from typing import Optional
from datetime import datetime

class Tag:
    def __init__(
        self,
        tag:str,
        id:Optional[int]=None,
        created_at:Optional[datetime]=None,
        updated_at:Optional[datetime]=None
    ):
        self.id=id
        self.tag=tag
        self.created_at=created_at
        self.updated_at=updated_at
        
    @classmethod
    def from_orm(cls, db):
        return cls(
            id=db.id,
            tag=db.tag,
            created_at=db.created_at,
            updated_at=db.updated_at
        )
    