from sqlalchemy import select, update, delete
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession

from models import create_async_session, User
from schemas import UserSchema, UserInDBSchema


class CRUDUser:


    @staticmethod
    @create_async_session
    async def add(user: UserSchema, session: AsyncSession = None) -> UserInDBSchema | None:
        user = User(**user.dict())
        session.add(user)
        try:
            await session.commit()
        except IntegrityError:
            pass
        else:
            await session.refresh(user)
            return UserInDBSchema(**user.__dict__)


    @staticmethod
    @create_async_session
    async def get(user_id: int, session: AsyncSession = None) -> UserInDBSchema | None:
        user = await session.execute(
            select(User)
            .where(User.id == user_id)
        )
        user = user.first()
        if user:
            return UserInDBSchema(**user[0].__dict__)


    @staticmethod
    @create_async_session
    async def get_all(is_blocked: bool, session: AsyncSession = None) -> list[UserInDBSchema]:
        if is_blocked:
            users = await session.execute(
                select(User)
                .where(User.is_blocked == is_blocked)

            )
        else:
            users = await session.execute(
                select(User)
                .order_by(User.id)
            )
        return [UserInDBSchema(**user[0].__dict__) for user in users]


    @staticmethod
    @create_async_session
    async def delete(user_id: int, session: AsyncSession = None) -> None:
        await session.execute(
            delete(User)
            .where(User.id == user_id)
        )
        await session.commit()


    @staticmethod
    @create_async_session
    async def update(user: UserSchema, session: AsyncSession = None) -> bool:
        await session.execute(
            update(User)
            .where(User.id == user.id)
            .values(**user.dict())
        )
        try:
            await session.commit()
        except IntegrityError:
            return False
        else:
            return True
