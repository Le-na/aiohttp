# import aiohttp  #импортирование библиотеки
# import asyncio  #импортирование библиотеки
#
# async def fetch(session, url):
#     # здесь происходит отправка запросов get с параметрами url, которая возвращает status
#     async with session.get(url) as resp:
#         return resp.status
#
# async def main():
#     #главная функция, которая ходит в функцию fetch(она отправляет запросы get)
#     #connector - это очередь на обработку запросов. Запросы отправляются оддновременно через gather
#     # в url хранятся пути
#     url = [
#         "https://httpbingo.org/get?page=1",
#         "https://httpbingo.org/get?page=2",
#         "https://httpbingo.org/get?page=3",
#         "https://httpbingo.org/get?page=4",
#         "https://httpbingo.org/get?page=5",
#     ]
#     connector = aiohttp.TCPConnector(limit=2)
#     async with aiohttp.ClientSession(connector=connector) as session:
#         #открываем ссесию через aiohttp.ClientSession,
#         # которая автоматически будет закрыта, когда программа отработает
#         #в result мы сохраняем результат работы всех запросов fetch(session, url[0-...]
#         #результат сохраняется списком
#         #этот результат - это return resp.status прописанный в функции fetch
#         #печатаем этот результат
#         result = await asyncio.gather(fetch(session, url[0]),
#                                       fetch(session, url[1]),
#                                       fetch(session, url[2]),
#                                       fetch(session, url[3]),
#                                       fetch(session, url[4]),
#                                       )
#         print(result)
#
# asyncio.run(main()) #запускаем функцию main


import aiohttp
import asyncio


async def fetch(session, url):
    async with session.get(url) as resp:
        return resp.status


async def main():
    url = [
        "https://httpbingo.org/get?page=1",
        "https://httpbingo.org/get?page=2",
        "https://httpbingo.org/get?page=3",
        "https://httpbingo.org/get?page=4",
        "https://httpbingo.org/get?page=5",
    ]
    async with aiohttp.ClientSession() as session:
        result = [await fetch(session, url[0]),
                  await fetch(session, url[1]),
                  await fetch(session, url[2]),
                  await fetch(session, url[3]),
                  await fetch(session, url[4]),]
        print(result)

asyncio.run(main())



