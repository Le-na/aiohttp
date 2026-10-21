import aiohttp
import asyncio

async def main():
    session = aiohttp.ClientSession()
    resp =  await session.get("https://httpbingo.org/")
    data = await resp.text() #await resp.json() если использовать json то будет ошибка,
    # идет утечка ресурсов и «Unclosed client session», «Unclosed connector»
    # корень сайта ("https://httpbingo.org/") -  возвращает HTML, а не json
    # aiohttp пытается распарсить HTML как JSON и падает

    print(resp.status)
    print(data)
    resp.close()
    await session.close()


# asyncio.run(main())


async def ruf():
    session = aiohttp.ClientSession()
    try:
        resp = await session.get("https://httpbingo.org/get")
        try:
            data = await resp.json()
            print(resp.status)
            print(data)
        finally:
            resp.close()
    finally:
        await session.close()


# asyncio.run(ruf())



async def ruf2():
    async with aiohttp.ClientSession() as session:
        async with session.get("https://httpbingo.org/get") as resp:
            data = await resp.json()
            print(resp.status)
            print(data)

asyncio.run(ruf2())
