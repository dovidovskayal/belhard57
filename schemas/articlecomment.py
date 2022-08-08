from pydantic import BaseModel, Field
from sqlalchemy import TIMESTAMP
from datetime import datetime


class ArticleCommentSchema(BaseModel):
    user_id: int
    article_id: str
    comment: str = Field(max_length=140)
    date_created: datetime = Field(default=datetime.utcnow())



class ArticleCommentInDBSchema(ArticleCommentSchema):
    id: int = Field(ge=1)