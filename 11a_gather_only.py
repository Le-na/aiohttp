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
    ]
    async with aiohttp.ClientSession() as session:
        result = await asyncio.gather(fetch(session, url[0]),
                             fetch(session, url[1]),
                             fetch(session, url[2]),
                             )
        print(result)

asyncio.run(main())