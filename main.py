from CRUD import CRUDArticle
from schemas import ArticleSchema

# CRUDArticle.add(article=ArticleSchema(category_id=2, title='lianatest2', body='lianatest2', user_id=1))
# print(CRUDArticle.get_all())
CRUDArticle.delete(article_id=6)