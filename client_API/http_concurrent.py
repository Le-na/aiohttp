import aiohttp
import asyncio

# urls = ["https://httpbingo.org/get",
#         "https://httpbingo.org/get?foo=bar",
#         "https://httpbingo.org/get?name=Elena"
# ]

async def fetch(session, url):
    async with session.get(url) as resp:
        return resp.status


async def main():
    urls = ["https://httpbingo.org/get",
            "https://httpbingo.org/get?foo=bar",
            "https://httpbingo.org/get?name=Elena"
            ]
    async with aiohttp.ClientSession() as session:
        # async with session.get(url=urls) as resp:
        #     pass
        results = await asyncio.gather(
            fetch(session, urls[0]),
            fetch(session, urls[1]),
            fetch(session, urls[2])
        )
        print(results)



asyncio.run(main())