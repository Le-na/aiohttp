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
        "https://httpbingo.org/get?page=6",
        "https://httpbingo.org/get?page=7",
        "https://httpbingo.org/get?page=8",
        "https://httpbingo.org/get?page=9",
        "https://httpbingo.org/get?page=10",
    ]


    connector = aiohttp.TCPConnector(limit=3)
    async with aiohttp.ClientSession(connector=connector) as session:
        results = await asyncio.gather(fetch(session, url[0]),
                                       fetch(session, url[1]),
                                       fetch(session, url[2]),
                                       fetch(session, url[3]),
                                       fetch(session, url[4]),
                                       fetch(session, url[5]),
                                       fetch(session, url[6]),
                                       fetch(session, url[7]),
                                       fetch(session, url[8]),
                                       fetch(session, url[9]),
        )
        print(results)

asyncio.run(main())