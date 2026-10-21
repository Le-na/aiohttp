import aiohttp
import asyncio


async def fetch(session, urls):
    async with session.get(urls)as resp:
        return resp.status



async def main():
    urls = [
        "https://httpbingo.org/get?page=1",
        "https://httpbingo.org/get?page=2",
        "https://httpbingo.org/get?page=3",
        "https://httpbingo.org/get?page=4",
        "https://httpbingo.org/get?page=5"
    ]
    connector = aiohttp.TCPConnector(limit=2)
    async with aiohttp.ClientSession(connector=connector) as session:
        result = await asyncio.gather(
            fetch(session, urls[0]),
            fetch(session, urls[1]),
            fetch(session, urls[2]),
            fetch(session, urls[3]),
            fetch(session, urls[4]),
        )
        print(result)


asyncio.run(main())


