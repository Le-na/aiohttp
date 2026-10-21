# import aiohttp
# import asyncio
# async def main():
#     async with aiohttp.ClientSession() as session:
#         async with session.get("https://httpbingo.org/get") as resp:
#             print(resp.status)
#             print(await resp.text())
#
# asyncio.run(main())

import aiohttp
import asyncio

async def main():
    async with aiohttp.ClientSession() as session:
        async with session.get("https://httpbingo.org/get") as resp:
            print(resp.status)
            print(await resp.text())
asyncio.run(main())