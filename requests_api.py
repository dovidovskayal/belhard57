# import json
from datetime import datetime

from requests import Session
from CRUD import CRUDArticle

# from schemas import ArticleSchema
from schemas import ArticleSchema


def put_response():
    list_article = CRUDArticle.get_all()
    for i in range(0, len(list_article)):
        with Session() as session:
            response = session.put(
                url="https://d474-80-93-191-82.eu.ngrok.io/api/1/article/add",
                json={"title": dict(list_article[i])['title'],
                      "body": dict(list_article[i])['body'],
                      "category_id": dict(list_article[i])['category_id'],
                      "user_id": 1}

            )
    print(response.json())
    print(response.status_code)


def get_response():
    with Session() as session:
        response = session.get(
            url="https://d474-80-93-191-82.eu.ngrok.io/api/1/article/get",
            params={'article_id': 26}
        )
        print(response.status_code)
        print(response.json())


def get_all_response():
    with Session() as session:
        response = session.get(
            url="https://d474-80-93-191-82.eu.ngrok.io/api/1/article/all",
            # params={'category_id': 1}
        )
        new_data = response.json()
        for i in range(0, len(new_data)):
            CRUDArticle.add(article=ArticleSchema(category_id=new_data[i]['category_id'],
                                                  title=new_data[i]['title'],
                                                  body=new_data[i]['body'],
                                                  date_create=datetime.utcnow(),
                                                  author_id=1))

        print(response.status_code)
        print(response.json())


# put_response()
# get_response()
get_all_response()

# import asyncio
# from aiohttp import ClientSession
#
#
# async def put_response():
#     async with ClientSession() as session:
#         response = await session.put(
#             url="https://d474-80-93-191-82.eu.ngrok.io/api/1/article/put",
#             json={"title": "string",
#                    "body": "string",
#                    "category_id": 1,
#                    "user_id": 1
#                    }
#         )
#         print(response.status)
#         print(await response.json())
#
#
# async def get_response():
#     async with ClientSession() as session:
#         response = await session.get(
#             url="https://d474-80-93-191-82.eu.ngrok.io/api/1/article/get",
#             params={'article_id': '1'}
#         )
#         print(response.status)
#         print(await response.json())
#
#
#
# # asyncio.run(put_response())
# asyncio.run(get_response())
