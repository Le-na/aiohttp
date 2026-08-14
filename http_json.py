import aiohttp
import asyncio

async def main():
    async with aiohttp.ClientSession() as session:
        async with session.get("https://httpbingo.org/get") as resp:
            data = await resp.json()
            print(data["method"])
            print(data["url"])

asyncio.run(main())