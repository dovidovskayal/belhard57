from pydantic import BaseModel, Field


class UserSchema(BaseModel):
    username: str = Field(max_length=24, unique=True, default=None)
    hashed_password: str = Field(default=None)
    email: str = Field(unique=True)
    is_blocked: bool = Field(default=False)


class UserInDBSchema(UserSchema):
    id: int = Field(ge=1)
