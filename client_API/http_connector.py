import aiohttp
import asyncio

async def main():
    connector = aiohttp.TCPConnector(limit=5)
    async with aiohttp.ClientSession(connector=connector) as session:
        async with session.get("https://httpbingo.org/get") as resp:
            print(resp.status)

asyncio.run(main())