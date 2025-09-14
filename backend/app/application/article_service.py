from sqlalchemy.orm import Session
from app.domain.article import Article
from app.domain.tag import Tag
from app.infrastructure.repositories.article_repository import ArticleRepository
from app.infrastructure.repositories.tag_repository import TagRepository
from app.schemas.article_schema import ArticleRead, ArticleCreate
from app.schemas.tag_schema import TagRead
from app.schemas.comment_schema import CommentRead
from .tag_service import TagService
from app.infrastructure.models.tag_model import TagModel

class ArticleService:
    
    def __init__(self, db:Session):
        self.repository = ArticleRepository(db=db)
        self.db = db

    def create_article(self, article_data: Article) -> Article:

        """Cria um novo artigo"""

        # list_tags_saved = []
        # print('======================================================')
        # print('Listar prelim????????', article_data.tags)
        # for tag_name in article_data.tags:
        #     print('Antes...')
        #     tag = TagRead.from_orm(self.create_tag(tag_name))
        #     print('Tag agora...     ', tag)
        #     list_tags_saved.append(tag)    
        
        # print("Lista de tags: ", list_tags_saved)
            
        article = Article(
            title = article_data.title,
            content = article_data.content,
            image = article_data.image,
            author_id = article_data.author_id
        )
        
        article_created = self.repository.save(article)
        
        # Fazer o article pegar as tags aqui
        # article_created.tags = self.add_tags_to_article(article_id=article_created.id, list_tags=list_tags_saved)
        
        return self.save_data(article_created)
    
    def create_tag(self, tag_name:str) -> Tag:
        tag_service = TagService(self.db)
        tag_obj = tag_service.create_tag(tag_name)
        print(f'Obj tag: {tag_obj}')
        return tag_obj
    
    def update_tags(self, article_id: int, new_tags:list[Tag], tags_saved=None) -> list[Tag]:
        """Separa as TAGs que serão removidas e adicionadas e as salva no banco"""
        
        tags = [str.lower(tag) for tag in new_tags]
        tags_saved_str = [tag.tag.lower() for tag in tags_saved]
        
        print('Tag====================================', tags)
        print('Saved====================================', tags_saved_str)
        print('New====================================', new_tags)
        
        tags_to_remove = []
        tags_to_add = []
        
        for tag in tags:
            if tag not in tags_saved_str:
                tags_to_add.append(tag)
                
        for tag_saved in tags_saved:
            if tag_saved.tag.lower() not in tags:
                tags_to_remove.append(tag_saved)
        
        tags_to_add_treated = []
        
        for tag in tags_to_add:
            tag = self.create_tag(tag)
            tags_to_add_treated.append(tag)
            
            
        # tags_to_remove_id = [tag.id for tag in tags_to_remove]
        
        tags_updated = self.repository.update_tags_to_article(article_id, tags_to_remove, tags_to_add_treated)
        print(f'Updated tags........{tags_updated}')
        return tags_updated

    
    def update_article(self, article_data: Article) -> ArticleRead:

        """Atualiza o artigo"""

        print(f'Id: {article_data}')
        
        tags_saved = self.get_all_tags_to_article(article_id = article_data.id)
        print(f'salvas:         {tags_saved}')
        tags_updated = self.update_tags(
            article_id = article_data.id,
            tags_saved = tags_saved,
            new_tags = article_data.tags
        )
        
        article_to_update = Article(
            id = article_data.id,
            title = article_data.title,
            content = article_data.content,
            image = article_data.image,
            author_id = article_data.author_id,
            tags= tags_updated
        )
        
        # print(f'Tags já cadastradas: {tagsSaved}')
        # print(f'Tags passadas: {article_data.tags}')
        article_updated = self.repository.update(article=article_to_update)
        return article_updated
    
        # tag_service = TagService(self.db)
        # tag_service
        
        # article_update = self.repository.update(article_update)

    def get_article(self, id:int) -> ArticleRead:
        
        """Retorna o artigo com base no id"""
        
        article = self.repository.find(id)
        
        if not article:
            raise ValueError("Article not found")
        return article
        
    def get_all_tags_to_article(self, article_id:int) -> list[Tag] | None:

        """Retorna todos as tags do Article com base no id"""        
        
        list_tags = self.repository.get_all_tags_to_article(article_id)
        return list_tags
        # return [TagRead.from_orm(tag) for tag in list_tags] 
    
    def save_data(self, article:Article) -> ArticleRead:
        
        """Persiste os dados invocando o db.commit no repository"""
        
        article_saved = self.repository.save_data(article=article)
        return ArticleRead.from_orm(article_saved)
    
    def add_tags_to_article(self, article_id:int, list_tags:list[Tag]) -> list[Tag]:
    
        """Função para fazer o vínculo entre a Tag e o Artigo"""
    
        return self.repository.add_tags_to_article(article_id, list_tags)
    
    def get_all_articles(self) -> list[ArticleRead]:
    
        """Retorna uma lista com todos os registros de Article"""
    
        all_articles = self.repository.get_all_articles()
        
        articles_treated = []
        for article in all_articles:
            
            articles_treated.append(
                ArticleRead.model_validate(Article.from_orm(article))
            )
        
        return articles_treated

    def check_article(self, article_id:int) -> Article:
        
        """Checa se o Article existe e retorna o objeto se existir"""
        
        article = self.repository.check_article(article_id)
        return article
    
    def get_all_comments(self, article_id:int) -> list[CommentRead]:
        
        comments = self.repository.get_all_comments(article_id)
        return comments