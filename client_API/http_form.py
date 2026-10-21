import aiohttp
import  asyncio
async def main():
    async with aiohttp.ClientSession() as session:
        data = {"name":"Elena", "skill":"aiohttp"}
        async with session.post("https://httpbingo.org/post", data=data) as resp:
            joy = await resp.json()
            print(joy["form"])

asyncio.run(main())