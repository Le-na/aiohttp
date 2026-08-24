import aiohttp
import asyncio

async def main():
    j_body_of_post={"name":"Elena", "role":"backend developer"}
    async with aiohttp.ClientSession() as session:
        async with session.post("https://httpbingo.org/post", json=j_body_of_post) as resp:
            data = await resp.json()
            print(resp.status)
            print(data)

asyncio.run(main())
