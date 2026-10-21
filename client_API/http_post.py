import aiohttp
import asyncio

async def main():
    async with aiohttp.ClientSession() as session:
        params={"name":"Elena", "skill":"aiohttp"}
        async with session.post("https://httpbingo.org/post", json=params) as resp:
            data = await resp.json()
            print(data["json"])

asyncio.run(main())