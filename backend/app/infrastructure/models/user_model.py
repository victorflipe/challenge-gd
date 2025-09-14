from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import relationship
from ..database import Base as BaseModel
from datetime import datetime

class UserModel(BaseModel):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
    
    time = datetime.now
    
    created_at = Column(DateTime, default=time)
    updated_at = Column(DateTime, default=time, onupdate=datetime.now)
    
    articles = relationship("ArticleModel", back_populates="author")
    comments = relationship("CommentModel", back_populates="author")