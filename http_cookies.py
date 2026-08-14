import aiohttp
import asyncio

async def main():
    # auth = aiohttp.BaseAuth("A", )
    cookies = {"session_id": "abc123"}
    async with aiohttp.ClientSession(cookies=cookies) as session:
        async with session.get("https://httpbingo.org/cookies") as resp:
            data = await resp.json()
            print(data["cookies"])

asyncio.run(main())

