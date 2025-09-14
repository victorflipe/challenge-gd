from sqlalchemy import Table, Column, Integer, ForeignKey
from ..database import Base as BaseModel

article_tag = Table(
    "articles_tags",
    BaseModel.metadata,
    Column("article_id", Integer, ForeignKey("articles.id"), primary_key=True),
    Column("tag_id", Integer, ForeignKey("tags.id"), primary_key=True)
)