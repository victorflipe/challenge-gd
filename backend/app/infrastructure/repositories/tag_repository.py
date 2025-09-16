from fastapi import HTTPException
from sqlalchemy.exc import IntegrityError, SQLAlchemyError
from sqlalchemy.orm import Session
from app.domain.tag import Tag
from app.schemas.tag_schema import TagCreate, TagRead
from app.infrastructure.models.tag_model import TagModel

class TagRepository:
    
    def __init__(self, db:Session):
        self.db = db
    
    def save(self, tag_data:Tag) -> TagCreate:
        
        """Cria uma nova tag e a retorna"""
        
        try:
            tag_obj = TagModel(
                tag = tag_data.tag,
            )
            self.db.add(tag_obj)
            self.db.flush()
            self.db.refresh(tag_obj)
            
            return tag_obj
        
        except IntegrityError as error:
            self.db.rollback()
            raise ValueError(error)
            
        except SQLAlchemyError as error:
            self.db.rollback()
            raise ValueError(error)
        
    def get_by_name(self, tag_name:str)->Tag | None:
        
        """Verifica se a tag já existe no banco, caso contrário retorna None"""
        
        try:
            tag_found = self.db.query(TagModel).filter(TagModel.tag.ilike(tag_name)).first()
            return tag_found
        
        except SQLAlchemyError as error:
            self.db.rollback()
            raise ValueError(error)
        
    def get_all_tags(self) -> list[Tag]:
        
        """Retorna todas as Tags cadastradas"""
        
        return self.db.query(TagModel).all()