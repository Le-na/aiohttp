# import asyncio
# async def demo():
#     print("Start")
#     await asyncio.sleep(1)
#     print("Finish")
#
#
# asyncio.run(demo())
#
# async def name_hi(name):
#     print("Start")
#     await asyncio.sleep(1)
#     print("Hi!", name)
#     await asyncio.sleep(1)
#     print("Finish")
#
# asyncio.run(name_hi("Lena"))

#
# import asyncio
#
# async def task(name, seconds):
#     print(f"{name}: старт")
#     await asyncio.sleep(seconds)
#     print(f"{name}: финиш")
#
# async def main():
#     await asyncio.gather(
#         task("A", 1),
#         task("B", 1),
#     )
#
# asyncio.run(main())

import asyncio

async def task(name, seconds):
    print(f"{name}: старт")
    await asyncio.sleep(seconds)
    print(f"{name}: финиш")

async def main():
    await asyncio.gather(
        task("A", 1),
        task("B", 1),
    )

asyncio.run(main())




