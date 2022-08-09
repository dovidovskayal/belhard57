from sqlalchemy import select, update, delete
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession

from models import create_async_session, ArticleComment
from schemas import ArticleCommentSchema, ArticleCommentInDBSchema


class CRUDArticleComment:

    @staticmethod
    @create_async_session
    async def add(article_comment: ArticleCommentSchema,
                  session: AsyncSession = None) -> ArticleCommentInDBSchema | None:
        article_comment = ArticleComment(**article_comment.dict())
        session.add(article_comment)
        try:
            await session.commit()
        except IntegrityError:
            pass
        else:
            await session.refresh(article_comment)
            return ArticleCommentInDBSchema(**article_comment.__dict__)

    @staticmethod
    @create_async_session
    async def get(article_comment_id: int, session: AsyncSession = None) -> ArticleCommentInDBSchema:
        article_comment = await session.execute(
            select(ArticleComment)
            .where(ArticleComment.id == article_comment_id)
        )
        article_comment = article_comment.first()
        if article_comment:
            return ArticleCommentInDBSchema(**article_comment[0].__dict__)

    @staticmethod
    @create_async_session
    async def get_all(session: AsyncSession = None) -> list[ArticleCommentInDBSchema]:
        article_comments = await session.execute(
            select(ArticleComment)
        )
        return [ArticleCommentInDBSchema(**article_comment[0].__dict__) for article_comment in article_comments]

    @staticmethod
    @create_async_session
    async def delete(article_comment_id: int, session: AsyncSession = None) -> None:
        await session.execute(
            delete(ArticleComment)
            .where(ArticleComment.id == article_comment_id)
        )
        await session.commit()

    @staticmethod
    @create_async_session
    async def update(article_comment: ArticleCommentSchema, session: AsyncSession = None) -> bool:
        await session.execute(
            update(ArticleComment)
            .where(ArticleComment.id == article_comment.id)
            .values(**article_comment.dict())
        )
        try:
            await session.commit()
        except IntegrityError:
            return False
        else:
            return True
