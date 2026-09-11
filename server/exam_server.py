import aiohttp
from aiohttp import web


async def add(request):
    request.app["visits"] += 1  #увеличиваем на 1
    return web.json_response({"result": int(request.query["a"]) + int(request.query["b"])})

async def greet(request):
    name = request.query.get("name", "гость")
    return web.json_response({"hello": f"Привет, {name}"})

async def echo(request):
    data = await request.json()
    if "text" in data:
        return web.json_response({"echo": data["text"]})    #внутри не нужно писать status=200, он вызывается автоматически
    else:
        return web.json_response({"error": "нет ключа text"}, status=400)


async def startup_counter(app):
    # Создаем один раз на старте, поэтому значение начинается с 0.
    # чтото вроде "Полки" внутри "хранилища" app
    app["visits"] = 0

async def stats(request):   #Читаем "полку" request.app и возвращаем результат
    return web.json_response({'visits': request.app['visits']})



@web.middleware
async def auth_middleware(request, handler):
    if request.method != 'POST':
        return await handler(request)
    elif request.headers.get("X-API-Key") == "secret123":
        return await handler(request)
    else:
        return web.json_response({"error": "unauthorized"}, status=401)


async def ws_websocket_handler(request):
    ws = web.WebSocketResponse()
    await ws.prepare(request)
    async for msg in ws:
        if msg.type == aiohttp.WSMsgType.TEXT:
            await ws.send_str(msg.data.upper())

def create_app():
    app = web.Application()
    app.router.add_get("/add", add)
    app.router.add_get("/greet", greet)
    app.router.add_post("/echo", echo)
    app.router.add_get("/stats", stats) #регистрируем, чтобы сервер знал о hendler stats
    app.router.add_get("/ws", ws_websocket_handler)
    app.middlewares.append(auth_middleware)
    app.on_startup.append(startup_counter)
    return app


if __name__ == '__main__':
    web.run_app(create_app())
