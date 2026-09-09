from aiohttp import web


async def add(request):
    return web.json_response({"result": int(request.query["a"]) + int(request.query["b"])})

async def greet(request):
    name = request.query.get("name", "гость")
    return web.json_response({"hello:": f"Привет, {name}"})



def create_app():
    app = web.Application()
    app.router.add_get("/greet", greet)
    app.router.add_get("/add", add)
    return app


if __name__ == "__main__":
    web.run_app(create_app())