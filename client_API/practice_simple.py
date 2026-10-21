import aiohttp
import asyncio

async def main():
    async with aiohttp.ClientSession() as session:
        async with session.get("https://httpbingo.org/get", params={'name':"Elena"}) as resp:
            data = await resp.json()
            print(resp.status)
            print(data["url"])
            print(data["args"])

asyncio.run(main())