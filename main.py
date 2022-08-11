from datetime import datetime

from CRUD import CRUDArticle
from schemas import ArticleSchema

CRUDArticle.add(article=ArticleSchema(category_id=1,
                                      title='lianatesting2',
                                      body='lianatestingefwefwef2',
                                      date_create=datetime.utcnow(),
                                      author_id=1))
# print(CRUDArticle.get_all())
# CRUDArticle.delete(article_id=13)
