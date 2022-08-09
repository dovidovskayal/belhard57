# from requests import Session
# from time import sleep
# def get_responce():
#     with Session() as session:
#         responce = session.get(
#             url="https://developerhub.alfabank.by:8273/partner/1.0.1/public/rates"
#
#         )
#         print(responce.status_code)
#
#
# for i in range(10):
#     get_responce()
#
from aiohttp import ClientSession
import asyncio


async def get_responce():
    async with ClientSession() as session:
        responce = await session.get(
            url="https://developerhub.alfabank.by:8273/partner/1.0.1/public/rates"

        )
        await asyncio.sleep(3)
        print(responce.status)

async def main():
    loop = asyncio.get_running_loop()
    tasks = [loop.create_task(get_responce()) for i in range(10)]
    for task in tasks:
        await task
asyncio.run(main())
