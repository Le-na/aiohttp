# import aiohttp
# import asyncio
#
#
# async def main():
#     async with aiohttp.ClientSession() as session:
#         async with session.ws_connect("wss://echo.websocket.org") as ws:
#             await ws.send_str("раз")
#             await ws.send_str("два")
#             await ws.send_str("три")
#
#                 print(msg.type, msg.data)
#                 if msg.data == "close cmd":
#                     await ws.close()
#                     break
#
#
# asyncio.run(main())


import aiohttp
import asyncio


async def main():
    async with aiohttp.ClientSession() as session:
        # async with session.ws_connect("ws://echo.websocket.org") as ws:
        async with session.ws_connect("ws://localhost:8080/ws") as ws:
            await ws.send_str("раз")
            print("отправила сообщение: раз")
            await ws.send_str("два")
            print("отправила сообщение: два")
            await ws.send_str("три")
            print("отправила сообщение: три")

            count = 4
            async for msg in ws:
                if count == 0:
                    await ws.close()
                    break
                else:
                    print("получила сообщение", msg.data)
                    count -= 1


asyncio.run(main())