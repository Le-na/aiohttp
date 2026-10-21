import aiohttp
import asyncio

async def main():
    async with aiohttp.ClientSession() as session:
        async with session.get("https://httpbingo.org/get") as resp:
            r = await resp.json()
            print(resp.status)
            print(r)

asyncio.run(main())
