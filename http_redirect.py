import aiohttp
import asyncio

async def main():
    async with aiohttp.ClientSession() as session:
        # async with session.get("https://httpbingo.org/redirect/2", allow_redirects=False) as resp:
        async with session.get("https://httpbingo.org/redirect/2", allow_redirects=True) as resp:
            print(resp.status)

asyncio.run(main())