from sqlalchemy import select, update, delete
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from models import create_session, User
from schemas import UserSchema, UserInDBSchema


class CRUDUser:


    @staticmethod
    @create_session
    def add(user: UserSchema, session: Session = None) -> UserInDBSchema | None:
        user = User(**user.dict())
        session.add(user)
        try:
            session.commit()
        except IntegrityError:
            pass
        else:
            session.refresh(user)
            return UserInDBSchema(**user.__dict__)


    @staticmethod
    @create_session
    def get(user_id: int, session: Session = None) -> UserInDBSchema | None:
        user = session.execute(
            select(User)
            .where(User.id == user_id)
        )
        user = user.first()
        if user:
            return UserInDBSchema(**user.__dict__)


    @staticmethod
    @create_session
    def get_all(is_blocked_id: int, session: Session = None) -> list[UserInDBSchema]:
        if is_blocked_id:
            users = session.execute(
                select(User)
                .where(User.is_blocked_id == is_blocked_id)
                .order_by(User.id)

            )
        else:
            users = session.execute(
                select(User)
                .order_by(User.id)
            )
        return [UserInDBSchema(**user[0].__dict__) for user in users]


    @staticmethod
    @create_session
    def delete(user_id: int, session: Session = None) -> None:
        session.execute(
            delete(User)
            .where(User.id == user_id)
        )
        session.commit()


    @staticmethod
    @create_session
    def update(user: UserSchema, session: Session = None) -> bool:
        session.execute(
            update(User)
            .where(User.id == user.id)
            .values(**user.dict())
        )
        try:
            session.commit()
        except IntegrityError:
            return False
        else:
            return True

