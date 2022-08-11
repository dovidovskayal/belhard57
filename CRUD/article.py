from sqlalchemy import select, update, delete
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from models import create_session, Article
from schemas import ArticleSchema, ArticleInDBSchema


class CRUDArticle:

    @staticmethod
    @create_session
    def add(article: ArticleSchema, session: Session = None) -> ArticleInDBSchema | None:
        article = Article(**article.dict())
        session.add(article)
        try:
            session.commit()
        except IntegrityError:
            pass
        else:
            session.refresh(article)
            return ArticleInDBSchema(**article.__dict__)

    @staticmethod
    @create_session
    def get(article_id: int, session: Session = None) -> ArticleInDBSchema:
        article = session.execute(
            select(Article)
            .where(Article.id == article_id)
        )
        article = article.first()
        if article:
            return ArticleInDBSchema(**article[0].__dict__)

    @staticmethod
    @create_session
    def get_all(session: Session = None) -> list[ArticleInDBSchema]:
        articles = session.execute(
            select(Article)
        )
        return [ArticleInDBSchema(**artical[0].__dict__) for artical in articles]

    @staticmethod
    @create_session
    def delete(article_id: int, session: Session = None) -> None:
        session.execute(
            delete(Article)
            .where(Article.id == article_id)
        )
        session.commit()

    @staticmethod
    @create_session
    def update(article: ArticleSchema, session: Session = None) -> bool:
        session.execute(
            update(Article)
            .where(Article.id == article.id)
            .values(**article.dict())
        )
        try:
            session.commit()
        except IntegrityError:
            return False
        else:
            return True
