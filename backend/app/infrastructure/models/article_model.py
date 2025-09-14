from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from ..database import Base as BaseModel
from .article_tag_model import article_tag
from datetime import datetime

class ArticleModel(BaseModel):
    
    __tablename__ = "articles"
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(255), nullable=False)
    content = Column(Text, nullable=False)
    image = Column(String, nullable=True)
    author_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    
    time = datetime.now
    
    created_at = Column(DateTime, default=time)
    updated_at = Column(DateTime, default=time, onupdate=datetime.now)
    
    # Relações com as outras tabelas
    author = relationship("UserModel", back_populates="articles")
    tags = relationship("TagModel", secondary=article_tag, back_populates="article")
    
    comments = relationship("CommentModel", back_populates="article", cascade="all, delete-orphan")