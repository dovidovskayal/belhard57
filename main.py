from datetime import datetime
from CRUD import CRUDArticleComment



# category = CRUDCategory.get(category_id=1)
# print(category)
# category.name = 'Eда'
# category.parent_id = None
# CRUDCategory.update(category=category)
# print(CRUDCategory.get(category_id=1))
from schemas import ArticleCommentSchema, ArticleCommentInDBSchema

# CRUDArticle.add(article=ArticleSchema(category_id=1, title='обед', body='eкуацпlmlfemnfelmnf',date_create,
# author_id=1)) CRUDArticle.add(article=ArticleSchema(category_id=1, title='ужин',
# body='erlfme4п23п3пelmlfemnfelmnf',date_create, author_id=2))


#CRUDArticleComment.add(articlecomment=ArticleCommentSchema(user_id=1, article_id=1, comment='gkvnaelrgvnaelgagqe',
                                                           #date_created=datetime.utcnow()))


print(CRUDArticleComment.get_all())