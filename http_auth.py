import aiohttp
import asyncio

async def main():
    async with aiohttp.ClientSession() as session:
        auth = aiohttp.BasicAuth("elena", "supersecret")
        async with session.get("https://httpbingo.org/basic-auth/elena/supersecret",
                               auth=auth) as resp:
            data = await resp.json()
            print(data)

asyncio.run(main())