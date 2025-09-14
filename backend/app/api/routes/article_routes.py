from fastapi import APIRouter, HTTPException, Depends, status
from fastapi.encoders import jsonable_encoder
from app.domain.article import Article
from app.application.article_service import ArticleService
from app.schemas.article_schema import ArticleCreate, ArticleRead, ArticleUpdate
from app.schemas.comment_schema import CommentCreate, CommentRead
from app.application.comment_service import CommentService
# from app.infrastructure.database import open_session
from app.utils.api_response import response_error, response_success
# from sqlalchemy.orm import Session
# from app.schemas.user_schema import UserRead
# from app.api.auth import get_current_user
from app.api.dependency import CommonDeps, get_common_deps

router = APIRouter(prefix="/articles", tags=["articles"])

@router.post("/", response_model = ArticleRead)
def create_article(article:ArticleCreate, common: CommonDeps = Depends(get_common_deps)) -> ArticleRead:
    
    """Cria um novo artigo e o retorna"""
    
    db = common.db
    current_user = common.current_user
    
    try:
        service = ArticleService(db=db)
        
        list_tags = []
        
        for tag in article.tags:
            list_tags.append(service.create_tag(tag))
        
        print(f'Lista de tags ==>: {list_tags}')
        
        article_obj = Article(
            title = article.title,
            content = article.content,
            image = article.image,
            author_id = current_user.id,
        )
        
        new_article = service.create_article(
            article_data = article_obj
        )
        
        service.add_tags_to_article(new_article.id, list_tags)
        
        article_created = service.save_data(article = new_article)
        
        return response_success(
            data = jsonable_encoder(article_created),
            status_code = status.HTTP_201_CREATED,
            message = "Article created success!"
        )
        
    except HTTPException as error:
        return response_error(
            message = error.detail,
            status_code = error.status_code
        )

@router.post("/{article_id}/comments")
def create_comment(article_id:int, comment:CommentCreate, common: CommonDeps = Depends(get_common_deps)) -> CommentRead:
    
    """Criar um novo comentário"""
    
    db = common.db
    current_user = common.current_user
    
    try:
        print(f'O que chegou: {article_id}')
        serviceComment = CommentService(db)
        
        comment_created = serviceComment.create_comment(
            comment_data = comment,
            article_id_data = article_id,
            user_id = current_user.id
        )   
        
        return response_success( 
            data = jsonable_encoder(comment_created),
            message = "Comment created sucess!"
        )
    
    except HTTPException as error:
        return response_error(
            message = error.detail,
            status_code = error.status_code
        )
    
@router.get("/{article_id}/comments")
def get_comments(article_id:int, common: CommonDeps = Depends(get_common_deps)):
    
    """Pega todos os comentários vinculados ao artigo"""
    
    db = common.db
    
    print("Apenas mostra os comentários...")
    print("Article: ", article_id)
    article_service = ArticleService(db=db)
    article = article_service.check_article(article_id=article_id)
    
    print(f'Article selecionado: {article}')
    
    if not article:
        return response_error(
            message="Artigo não encontrado", 
            status_code=status.HTTP_400_BAD_REQUEST
        )
   
    list_comments = article_service.get_all_comments(article.id) 
    print('Lista de comentários ============', list_comments)
    # service = CommentService(db=db)
    # list_comments = service.get_all_comments(article)
    
    return response_success(
        data = [jsonable_encoder(comment) for comment in list_comments]
    )
    
@router.get("/")
def get_all_articles(common: CommonDeps = Depends(get_common_deps)):
    
    """Função que retorna todos os Articles cadastrados"""
    
    db = common.db
    
    service = ArticleService(db=db)
    result = service.get_all_articles()
    
    return response_success(
        data = [jsonable_encoder(article) for article in result]
    )
    
@router.put("/{article_id}", response_model = ArticleRead)
def edit_article(article_id:int, article:ArticleCreate, common: CommonDeps = Depends(get_common_deps)) -> ArticleRead:
    
    """Função para atualizar o Article"""
    
    db = common.db
    current_user = common.current_user
    print("Current user ", current_user)
    
    try:
        
        article_obj = Article(
            id = article_id,
            title = article.title,
            content = article.content,
            image = article.image,
            author_id = current_user.id,
            tags = article.tags
        )
        
        print(f'Objeto article: {article_obj}')
        article_service = ArticleService(db=db)
        article_updated = article_service.update_article(article_data = article_obj)
        
        return response_success(
            message = "Article atualizado com sucesso!",
            data=jsonable_encoder(article_updated)
        )
        
    except ValueError as error:
        print(f'É aqui...............................')
        return response_error(
            message=error.detail,
            status_code= error.status_code
        )
    except HTTPException as error:
        return response_error(
            message=error.detail,
            status_code= error.status_code
        )