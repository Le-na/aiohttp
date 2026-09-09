from aiohttp import web


async def add(request):
    return web.json_response({"result": int(request.query["a"]) + int(request.query["b"])})


async def greet(request):
    name = request.query.get("name", "гость")
    return web.json_response({"hello": f"Привет, {name}"})

async def echo(request):
    data = await request.json()
    if "text" in data:
        return web.json_response({"echo": data["text"]}, status=200)
    else:
        return web.json_response({"error": "нет ключа text"}, status=400)



@web.middleware
async def auth_middleware(request, handler):
    if request.method != 'POST':
        return await handler(request)
    elif request.headers.get("X-API-Key") == "secret123":
        return await handler(request)
    else:
        return web.json_response({"error": "unauthorized"}, status=401)


def create_app():
    app = web.Application()
    app.router.add_get("/add", add)
    app.router.add_get("/greet", greet)
    app.router.add_post("/echo", echo)
    app.middlewares.append(auth_middleware)
    return app


if __name__ == '__main__':
    web.run_app(create_app())
