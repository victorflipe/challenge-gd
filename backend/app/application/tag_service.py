from sqlalchemy.orm import Session
from app.infrastructure.repositories.tag_repository import TagRepository
from app.domain.tag import Tag
from app.infrastructure.models.tag_model import TagModel
from app.schemas.tag_schema import TagCreate, TagRead
from typing import Optional

class TagService:
    
    def __init__(self, db:Session):
        self.repository = TagRepository(db)
        self.db = db
        
    def create_tag(self, tag_data:str) -> TagModel:
        
        """ Cria uma nova tag, caso já exista retorna o objeto da Tag """
        
        try:
            tag_obj = self.get_by_name(tag=tag_data)
            
            if not tag_obj:
            
                new_tag = Tag(
                    tag = tag_data
                )
            
                return self.repository.save(tag_data=new_tag)
            
            return tag_obj
            
        except Exception as error:
            raise ValueError(error)
        
    
    def get_by_name(self, tag:str) -> Optional[Tag]:
        
        """Retorna a Tag caso exista"""
        
        tag = self.repository.get_by_name(tag)
        
        if not tag:
            return None
        
        return tag
    
    def get_all_tags(self) -> list[TagRead]:
        
        """Retorna todas as Tags cadastradas"""
        
        list_tags = self.repository.get_all_tags()
        return [TagRead.from_orm(tag) for tag in list_tags]
    