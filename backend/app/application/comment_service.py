from sqlalchemy.orm import Session
from app.domain.comment import Comment
from app.domain.article import Article
from app.infrastructure.repositories.comment_repository import CommentRepository
from app.schemas.comment_schema import CommentCreate, CommentRead

class CommentService:
    
    def __init__(self, db:Session):
        self.repository = CommentRepository(db)
        self.db = db
        
    def create_comment(self, comment_data:CommentCreate, article_id_data:int, user_id:int) -> CommentRead:
        print(f'Article id que chegou aqui: {article_id_data}')
        comment = Comment(
            comment = comment_data.comment,
            author_id = user_id,
            article_id = article_id_data,
            parent_comment_id = comment_data.parent_comment_id
        )
        
        comment_saved = self.repository.save(comment)
        
        return CommentRead.model_validate(Comment.from_orm(comment_saved))

    def get_all_comments(self, article_data: Article) -> list[CommentRead]:
        list_comments = self.repository.get_all_comments(article_data)
        return [CommentRead.model_validate(comment) for comment in list_comments]
    
    def delete_comment(self, comment_id:int, user_id:int) -> bool:
        return self.repository.delete_comment(comment_id, user_id)