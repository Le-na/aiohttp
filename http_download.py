import aiohttp
import asyncio

async def main():
    async with aiohttp.ClientSession() as session:
        async with session.get("https://httpbingo.org/image/png") as resp:
            content = await resp.read()
            with open("download.png", "wb") as f:
                f.write(content)
            print(len(content))

asyncio.run(main())