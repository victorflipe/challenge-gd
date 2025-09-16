import json
from pathlib import Path
from app.infrastructure.database import localSession
from app.infrastructure.models.user_model import UserModel
from app.infrastructure.models.article_model import ArticleModel
from app.infrastructure.models.tag_model import TagModel

def migrate_articles():
    json_path = Path(__file__).parent.parent / "data" / "articles.json"

    with open(json_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    db = localSession()

    try:
        for item in data:
            user = db.query(UserModel).filter_by(name=item["author"]).first()
            if not user:
                user = UserModel(name=item["author"])
                db.add(user)
                db.flush()

            article = ArticleModel(
                title=item["title"],
                content=item["content"],
                author_id=user.id
            )
            db.add(article)
            db.flush() 

            tags_list = []
            for key in ["tag1", "tag2", "tag3"]:
                if key in item and item[key]:

                    tag = db.query(TagModel).filter_by(tag=item[key]).first()
                    if not tag:
                        tag = TagModel(tag=item[key])
                        db.add(tag)
                        db.flush()
                    tags_list.append(tag)

            for tag in tags_list:
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
