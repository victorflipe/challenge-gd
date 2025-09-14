from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm  import relationship
from ..database import Base as BaseModel
from .article_tag_model import article_tag
from datetime import datetime

class TagModel(BaseModel):
    
    __tablename__ = "tags"
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    tag = Column(String(255), nullable=False)
    
    time = datetime.now
    
    created_at = Column(DateTime, default=time)
    updated_at = Column(DateTime, default=time, onupdate=datetime.now)
    
    article = relationship("ArticleModel", secondary=article_tag, back_populates="tags")
    