import json
from pathlib import Path
from app.infrastructure.database import localSession
from app.infrastructure.models.user_model import UserModel
from app.infrastructure.models.comment_model import CommentModel
from app.infrastructure.models.article_model import ArticleModel
from app.infrastructure.models.tag_model import TagModel

# Classe fake para simular o current_user
class FakeCommon:
    def __init__(self, db, current_user):
        self.db = db
        self.current_user = current_user

def migrate_articles():
    json_path = Path(__file__).parent.parent / "data" / "articles.json"
    
    with open(json_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    db = localSession()

    try:
        for item in data:
            
            user = db.query(UserModel).filter_by(name=item["author"]).first()
            
            if not user:
                print(f"Criando usuário: {item['author']}")
                user = UserModel(
                    name=item["author"],
                    email=f'{item["author"]}@email.com',
                    password="teste"  # lembre-se de hashear em produção
                )
                db.add(user)
                db.commit()
                db.refresh(user)

            article = ArticleModel(
                title=item["title"],
                content=item["content"],
                image=item.get("image", None),
                author_id=user.id
            )
            db.add(article)
            db.commit()
            db.refresh(article)

            for key in ["tag1", "tag2", "tag3"]:
                tag_name = item.get(key)
                if tag_name:
                    tag = db.query(TagModel).filter_by(tag=tag_name).first()
                    if not tag:
                        tag = TagModel(tag=tag_name)
                        db.add(tag)
                        db.commit()
                        db.refresh(tag)

                    if tag not in article.tags:
                        article.tags.append(tag)
                        db.commit()

        print("Migração concluída com sucesso!")

    except Exception as e:
        db.rollback()
        print("Erro na migração:", e)
    finally:
        db.close()

if __name__ == "__main__":
    migrate_articles()
