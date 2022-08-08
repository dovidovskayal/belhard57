from sqlalchemy import select, update, delete
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from models import create_session, ArticleComment
from schemas import ArticleCommentSchema, ArticleCommentInDBSchema


class CRUDArticleComment:

    @staticmethod
    @create_session
    def add(article_comment: ArticleCommentSchema, session: Session = None) -> ArticleCommentInDBSchema | None:
        article_comment = ArticleComment(**article_comment.dict())
        session.add(article_comment)
        try:
            session.commit()
        except IntegrityError:
            pass
        else:
            session.refresh(article_comment)
            return ArticleCommentInDBSchema(**article_comment.__dict__)

    @staticmethod
    @create_session
    def get(article_comment_id: int, session: Session = None) -> ArticleCommentInDBSchema:
        article_comment = session.execute(
            select(ArticleComment)
            .where(ArticleComment.id == article_comment_id)
        )
        article_comment = article_comment.first()
        if article_comment:
            return ArticleCommentInDBSchema(**article_comment[0].__dict__)

    @staticmethod
    @create_session
    def get_all(session: Session = None) -> list[ArticleCommentInDBSchema]:
        article_comments = session.execute(
            select(ArticleComment)
        )
        return [ArticleCommentInDBSchema(**article_comment[0].__dict__) for article_comment in article_comments]

    @staticmethod
    @create_session
    def delete(article_comment_id: int, session: Session = None) -> None:
        session.execute(
            delete(ArticleComment)
            .where(ArticleComment.id == article_comment_id)
        )
        session.commit()

    @staticmethod
    @create_session
    def update(article_comment: ArticleCommentSchema, session: Session = None) -> bool:
        session.execute(
            update(ArticleComment)
            .where(ArticleComment.id == article_comment.id)
            .values(**article_comment.dict())
        )
        try:
            session.commit()
        except IntegrityError:
            return False
        else:
            return True
