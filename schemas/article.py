from pydantic import BaseModel, Field
from sqlalchemy import TIMESTAMP
from datetime import datetime


class ArticleSchema(BaseModel):
    title: str = Field(max_length=50)
    body: str = Field(max_length=1024)
    category_id: int = Field(ge=1)
    # date_create = Field(default=datetime.utcnow())
    user_id: int = Field(ge=1)


class ArticleInDBSchema(ArticleSchema):
    id: int = Field(ge=1)