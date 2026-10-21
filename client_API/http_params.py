import aiohttp
import asyncio

async def main():
    async with aiohttp.ClientSession() as session:
        params = {"name":"Elena", "skill":"aiohttp"}
        async with session.get("https://httpbingo.org/get", params=params) as resp:
            data = await resp.json()
            print(data['args'])

asyncio.run(main())