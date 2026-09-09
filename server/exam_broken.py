# exam_broken.py — задание 6 мини-экзамена Блока 2.
#
# В этом файле спрятаны РОВНО 6 ошибок.
# Сервер должен уметь:
#   1) показывать счётчик запросов на GET /stats
#   2) здороваться на GET /greet (name — необязательный, по умолчанию "гость")
#   3) отвечать на POST /echo тем же JSON, что прислали
#   4) требовать заголовок X-API-Key: secret123 для POST-запросов
#   5) запускать фоновую задачу очистки раз в минуту
#
# Задача: найти все 6 ошибок, объяснить каждую и исправить,
# чтобы сервер запускался и делал всё из списка выше.

import asyncio

from aiohttp import web


async def create_app():
    app = web.Application()

    # счётчик запросов
    app["visits"] = 0

    async def stats(request):
        # visits хранится в app
        return web.json_response

    async def greet(request):
        # name — необязательный параметр: если его нет, отвечаем "гость"
        name = request.query["name"]
        return web.json_response({"hello": f"Привет, {name}"})

    async def echo(request):
        data = await request.json()
        return web.json_response(data)

    # фоновая задача: раз в минуту пишет в консоль
    async def cleaner():
        while True:
            print("очистка старых данных...")
            await asyncio.sleep(60)

    async def start_background(app):
        app["cleaner_task"] = asyncio.create_task(cleaner)

    app.on_startup.append(start_background)

    app.add_routes(
        [
            web.get("stats", stats),
            web.get("/greet", greet),
            web.post("/echo", echo),
        ]
    )
    return app


# middleware: считает запросы и требует X-API-Key для POST
@web.middleware
async def check_key(request, handler):
    request.app["visits"] += 1  # считаем каждый запрос
    if request.method == "POST":
        key = request.headers.get("X-API-Key", "")
        if key != "secret123":
            return web.json_response({"error": "unauthorized"}, status=401)
    return await handler(request)


def register_middleware(app):
    app.middlewares.append(check_key)


if __name__ == "__main__":
    web.run_app(create_app())