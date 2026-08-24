# import aiohttp
# import asyncio
#
# async def main():
#     async with aiohttp.ClientSession() as session:
#         async with session.get("https://httpbingo.org/delay/10") as resp:
#             timeout = aiohttp.ClientTimeout(total=3)
#             try:
#                 asincio

import aiohttp
import asyncio

async def main():
    async with aiohttp.ClientSession() as session:
        try:
            async with session.get("https://httpbingo.org/delay/10",
                                   timeout=aiohttp.ClientTimeout(total=3)) as resp:
                # выполнится, если timeout не сработает. Будет ошибка, если оставить без какого либо действия
                print(resp.status)
                print("Ответ получен!  ")
        except asyncio.TimeoutError:
            print("Превышен таймаут!")

asyncio.run(main())




