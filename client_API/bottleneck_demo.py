import asyncio
import time

import aiohttp

# программа работала приммерно 7.51 секунда
# time.sleep(0.5) - пауза для всего event loop. Ниичего не работает пока спит
# asyncio.sleep(1) - пауза, но дает право работать другим handler.
# и event loop обслуживает других
async def session_in_cycle():
    print(f"Начало работы программы 'Сессия внутри цикла' + остановка работы соединения time.sleep(0,5)")
    start = time.time()
    for i in range(5):
        async with aiohttp.ClientSession() as session:
            async with session.get("http://127.0.0.1:8080/slow") as resp:
                time.sleep(0.5)
                print(resp.status)
    finish = time.time() - start
    print(f"Время работы программы 'Сессия внутри цикла': {finish:.2f}")




async def fetch(session, urls):
    async with session.get(urls) as resp:
        return resp.status

# программа работала 1 секунду
async def main():
    print(f"Начаало работы программы 'Сессия снаружи и открывается один раз + gather'")
    start = time.time()
    urls = ["http://127.0.0.1:8080/slow",
            "http://127.0.0.1:8080/slow",
            "http://127.0.0.1:8080/slow",
            "http://127.0.0.1:8080/slow",
            "http://127.0.0.1:8080/slow"
            ]
    async with aiohttp.ClientSession() as session:
        result = await asyncio.gather(fetch(session, urls[0]),
                                        fetch(session, urls[1]),
                                        fetch(session, urls[2]),
                                        fetch(session, urls[3]),
                                        fetch(session, urls[4]))
    finish = time.time() - start
    print(f"Время работы программы 'Сессия снаружи и открывается один раз + gather': {finish:.2f}")


asyncio.run(session_in_cycle())
asyncio.run(main())


