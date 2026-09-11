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


def create_app():   #ошибка 1 - create_app не ассинронная функция
    app = web.Application()

    # счётчик запросов
    app["visits"] = 0

    async def stats(request):
        # visits хранится в app
        return web.json_response({'visits': request.app["visits"]})    # ошибка 3  - значит мы должны возвращать "visits"

    async def greet(request):
        # name — необязательный параметр: если его нет, отвечаем "гость"
        name = request.query.get('name', "гость")
        # name = request.query["name"]    #тут просто чтение значения по ключу 'name', а нам нужен дефолт = "гость"
        # ошибка 2 - должно быть request.query.get('name', "гость") ключи и дефолтное значение
        return web.json_response({"hello": f"Привет, {name}"})

    async def echo(request):    #тут все верно
        data = await request.json()
        return web.json_response(data)

    # фоновая задача: раз в минуту пишет в консоль
    async def cleaner():
        while True:
            print("очистка старых данных...")
            await asyncio.sleep(60)

    async def start_background(app):
        app["cleaner_task"] = asyncio.create_task(cleaner())    #ошибка 4 - asyncio.create_task - вызывает функцию cleanner круглыми скобками

    app.on_startup.append(start_background)
    app.middlewares.append(check_key) # ошибка 6 - перенесла middlewar в пути

    app.add_routes(
        [
            web.get("/stats", stats),   # ошибка был пропущен /
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
        key = request.headers.get("X-API-Key", "")  #а нам не нужно положить "secret123" в пустые ""
        if key != "secret123":
            return web.json_response({"error": "unauthorized"}, status=401)
    return await handler(request)

#
# def register_middleware(app):
#     app.middlewares.append(check_key)


if __name__ == "__main__":
    web.run_app(create_app())