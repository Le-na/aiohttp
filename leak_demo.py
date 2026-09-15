import asyncio
import aiohttp


#сессия никогда не будет закрыта
async def session_never_close():
    print("session_never_close")
    sessions = []
    for i in range(5):
        s = aiohttp.ClientSession()
        async with s.get("http://127.0.0.1:8080/slow") as resp:
            print(f"сессия {i}: запрос выполнен, статус {resp.status}")
        sessions.append(s)
    print(f"Незакрытых сессий: {len(sessions)}")


#сессия закрывается командой await s.close()
async def session_closed():
    print("session_closed")
    sessions = []
    for i in range(5):
        s = aiohttp.ClientSession()
        async with s.get("http://127.0.0.1:8080/slow") as resp:
            print(f"сессия {i}: запрос выполнен, статус {resp.status}")
        sessions.append(s)
        print(f"сессия закрыта? {s.closed}")
        await s.close()
    print(f"Закрытых сессий: {len(sessions)}")




#сессия не закроется командой await s.close()
# Открытие сессии -> отлавливание ошибки -> никогда не закроется
# В консоли отлавливаются ошибки RuntimeError, Unclosed client session и Unclosed connector
async def session_closed_with_raise():
    print("session_closed")
    sessions = []
    for i in range(5):
        s = aiohttp.ClientSession()
        async with s.get("http://127.0.0.1:8080/slow") as resp:
            print(f"сессия {i}: запрос выполнен, статус {resp.status}")
            raise RuntimeError("Ошибка, сервер сломался")
        sessions.append(s)
        print(f"сессия закрыта? {s.closed}")
        await s.close()
    print(f"Закрытых сессий: {len(sessions)}")


# одна сесия открылась и закрылась автоматически
async def common_session():
    print("common_session")
    sessions = []
    i = 0
    async with aiohttp.ClientSession() as s:
        async with s.get("http://127.0.0.1:8080/slow") as resp:
            print(f"сессия {i}: запрос выполнен, статус {resp.status}")
        sessions.append(s)
        i += 1
    print(f"Автоматически закрытых сессий: {len(sessions)}")

# одна сесия открылась, поймала ошибку RuntimeError и закрылась автоматически
# в консоли нет ошибки Unclosed client session и Unclosed connector
async def common_session_with_raise():
    print("common_session")
    sessions = []
    i = 0
    async with aiohttp.ClientSession() as s:
        async with s.get("http://127.0.0.1:8080/slow") as resp:
            print(f"сессия {i}: запрос выполнен, статус {resp.status}")
        raise RuntimeError("Ошибка, сервер сломался")


asyncio.run(session_never_close())
asyncio.run(session_closed())
asyncio.run(session_closed_with_raise())

asyncio.run(common_session())
asyncio.run(common_session_with_raise())


