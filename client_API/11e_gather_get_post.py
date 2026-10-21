import aiohttp
import asyncio

async def fetch_get(session, url):
    async with session.get(url) as resp:
        return resp.status

async def fetch_post(session, url, params):
    async with session.post(url,  json=params) as resp:
        return resp.status


async def main():
    params = [{"name": "Elena", "skill": "aiohttp"},
              {"name": "Elena", "skill": "gather"},
    ]
    url_post = ["https://httpbingo.org/post",
                "https://httpbingo.org/post",]


    #вариант 2
    #params1={"name": "Elena", "skill": "aiohttp"}
    #params2={"name": "Elena", "skill": "gather"}
    #     url_post = ["https://httpbingo.org/post", params1,
    #                 "https://httpbingo.org/post", params2, ]

    url_get = [
        "https://httpbingo.org/get?page=1",
        "https://httpbingo.org/get?page=2",
        "https://httpbingo.org/get?page=3",
        "https://httpbingo.org/get?page=4",
        "https://httpbingo.org/get?page=5",
    ]

    connector = aiohttp.TCPConnector(limit=3)
    async with aiohttp.ClientSession(connector=connector) as session:
        results = await asyncio.gather(fetch_get(session, url_get[0]),
                                       fetch_get(session, url_get[1]),
                                       fetch_get(session, url_get[2]),
                                       fetch_get(session, url_get[3]),
                                       fetch_get(session, url_get[4]),
                                       fetch_post(session, url_post[0], params[0]),
                                       fetch_post(session, url_post[1], params[1]),
                                       )
        print(results)

asyncio.run(main())

