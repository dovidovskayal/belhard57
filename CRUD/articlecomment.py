from sqlalchemy import select, update, delete
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from models import create_session, ArticleComment
from schemas import ArticleCommentSchema, ArticleCommentInDBSchema


class CRUDArticleComment:

    @staticmethod
    @create_session
    def add(articlecomment: ArticleCommentSchema, session: Session = None) -> ArticleCommentInDBSchema | None:
        articlecomment = ArticleComment(**articlecomment.dict())
        session.add(articlecomment)
        try:
            session.commit()
        except IntegrityError:
            pass
        else:
            session.refresh(articlecomment)
            return ArticleCommentInDBSchema(**articlecomment.__dict__)

    @staticmethod
    @create_session
    def get(articlecomment_id: int, session: Session = None) -> ArticleCommentInDBSchema:
        articlecomment = session.execute(
            select(ArticleComment)
            .where(ArticleComment.id == articlecomment_id)
        )
        articlecomment = articlecomment.first()
        if articlecomment:
            return ArticleCommentInDBSchema(**articlecomment[0].__dict__)

    @staticmethod
    @create_session
    def get_all(session: Session = None) -> list[ArticleCommentInDBSchema]:
        """

        :rtype: object
        """
        article_comments = session.execute(
            select(ArticleComment)
        )
        return [ArticleCommentInDBSchema(**articalcomment[0].__dict__) for articalcomment in article_comments]

    @staticmethod
    @create_session
    def delete(articlecomment_id: int, session: Session = None) -> None:
        session.execute(
            delete(ArticleComment)
            .where(ArticleComment.id == articlecomment_id)
        )
        session.commit()

    @staticmethod
    @create_session
    def update(articlecomment: ArticleCommentSchema, session: Session = None) -> bool:
        session.execute(
            update(ArticleComment)
            .where(ArticleComment.id == articlecomment.id)
            .values(**articlecomment.dict())
        )
        try:
            session.commit()
        except IntegrityError:
            return False
        else:
            return True
