import aiohttp
import asyncio

async def main():
    connector = aiohttp.TCPConnector(limit=2)
    async with aiohttp.ClientSession(connector=connector) as session:
        async with session.get("https://httpbingo.org/get?page=1") as resp:
            print(resp.status)
        async with session.get("https://httpbingo.org/get?page=2") as resp:
            print(resp.status)
        async with session.get("https://httpbingo.org/get?page=3") as resp:
            print(resp.status)

asyncio.run(main())