import aiohttp
import asyncio
import time

from aiohttp import TCPConnector


async def slow_api_get(url):
    start = time.time()
    status = []
    async with aiohttp.ClientSession() as session:
        for u in url:
            async with session.get(u) as resp:
                status.append(resp.status)
    finish = time.time() - start
    print(f"slow_api_get = finish_time: {finish} секунд, статусы: {status}")


async def fetch(session, url):
    async with session.get(url) as resp:
        return resp.status



url = [
    "http://127.0.0.1:8080/slow",
    "http://127.0.0.1:8080/slow",
    "http://127.0.0.1:8080/slow",
    "http://127.0.0.1:8080/slow",
    "http://127.0.0.1:8080/slow"
]

async def slow_gather(url):
    start = time.time()
    async with aiohttp.ClientSession() as session:
        result = await asyncio.gather(fetch(session, url[0]),
                                      fetch(session, url[1]),
                                      fetch(session, url[2]),
                                      fetch(session, url[3]),
                                      fetch(session, url[4]))
    finish = time.time() - start
    print(f"slow_gather = finish_time: {finish} секунд, статусы: {result}")


async def slow_gather_limit(url):
    start = time.time()
    connector = TCPConnector(limit=2)
    async with aiohttp.ClientSession(connector=connector) as session:
        result = await asyncio.gather(fetch(session, url[0]),
                                      fetch(session, url[1]),
                                      fetch(session, url[2]),
                                      fetch(session, url[3]),
                                      fetch(session, url[4]))
    finish = time.time() - start
    print(f"slow_gather_limit = finish_time: {finish} секунд, статусы: {result}")



asyncio.run(slow_api_get(url))
asyncio.run(slow_gather(url))
asyncio.run(slow_gather_limit(url))