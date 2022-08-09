from sqlalchemy import select, update, delete
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession

from models import create_async_session, Article
from schemas import ArticleSchema, ArticleInDBSchema


class CRUDArticle:

    @staticmethod
    @create_async_session
    async def add(article: ArticleSchema, session: AsyncSession = None) -> ArticleInDBSchema | None:
        article = Article(**article.dict())
        session.add(article)
        try:
            await session.commit()
        except IntegrityError:
            pass
        else:
            await session.refresh(article)
            return ArticleInDBSchema(**article.__dict__)

    @staticmethod
    @create_async_session
    async def get(article_id: int, session: AsyncSession = None) -> ArticleInDBSchema:
        article = await session.execute(
            select(Article)
            .where(Article.id == article_id)
        )
        article = article.first()
        if article:
            return ArticleInDBSchema(**article[0].__dict__)

    @staticmethod
    @create_async_session
    async def get_all(session: AsyncSession = None) -> list[ArticleInDBSchema]:
        articles = await session.execute(
            select(Article)
        )
        return [ArticleInDBSchema(**artical[0].__dict__) for artical in articles]

    @staticmethod
    @create_async_session
    async def delete(article_id: int, session: AsyncSession = None) -> None:
        await session.execute(
            delete(Article)
            .where(Article.id == article_id)
        )
        await session.commit()

    @staticmethod
    @create_async_session
    async def update(article: ArticleSchema, session: AsyncSession = None) -> bool:
        await session.execute(
            update(Article)
            .where(Article.id == article.id)
            .values(**article.dict())
        )
        try:
            await session.commit()
        except IntegrityError:
            return False
        else:
            return True
