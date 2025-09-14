from .database import Base, engine
from .models.user_model import UserModel
from .models.article_model import ArticleModel
from .models.comment_model import CommentModel
from .models.tag_model import TagModel

def init_db():
    Base.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
    print("Tabelas criadas com sucesso.")
    
if __name__ == "__main__":
    init_db()