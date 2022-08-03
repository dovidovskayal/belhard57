from typing import Optional

from sqlalchemy import select, update, delete
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from models import create_session, Category, Article
from schemas import CategorySchema, CategoryInDBSchema


class CRUDCategory:

    @staticmethod
    @create_session
    def add(category: CategorySchema, session: Session = None) -> Optional[CategoryInDBSchema]:
        category = Category(**category.dict())
        session.add(category)
        try:
            session.commit()
        except IntegrityError:
            pass
        else:
            session.refresh(category)
            return CategoryInDBSchema(**category.__dict__)

    @staticmethod
    @create_session
    def get(category_id: int, session: Session = None) -> Optional[CategoryInDBSchema]:
        category = session.execute(
            select(Category)
            .where(Category.id == category_id)
            # .where(or_(Category.id == category_id, Category.name == 'Food')) для объединения через и/или
        )
        category = category.first()
        if category:
            return CategoryInDBSchema(**category[0].__dict__)
        # return category[0] if (category := category.first()) else None

    @staticmethod
    @create_session
    def get_all(parent_id: int = None, session: Session = None) -> list[CategoryInDBSchema]:
        if parent_id:
            categories = session.execute(
                select(Category)
                .where(Category.parent_id == parent_id)
                .order_by(Category.id)
            )
        else:
            categories = session.execute(
                select(Category)
                .order_by(Category.id)
            )
        return [CategoryInDBSchema(**category[0].__dict__) for category in categories]

    @staticmethod
    @create_session
    def delete(category_id: int, session: Session = None) -> None:
        session.execute(
            delete(Category)
            .where(Category.id == category_id)
        )
        session.commit()

    @staticmethod
    @create_session
    def update(
            category: CategoryInDBSchema,
            session: Session = None
    ) -> bool:
        session.execute(
            update(Category)
            .where(Category.id == category.id)
            # .values(name=name if name else Category.name,
            #        parent_id=parent_id if parent_id else Category.parent_id)
            # )
            .values(**category.dict())
        )
        try:
            session.commit()
        except IntegrityError:
            return False
        else:
            return True

    @staticmethod
    @create_session
    def get_articles(category_id: int, session: Session = None) -> list[tuple[Category, Article]]:
        response = session.execute(
            select(Category, Article)
            .join(Article, Category.id == Article.category_id)
            .where(Category.id == category_id)
        )
        return response.all()
