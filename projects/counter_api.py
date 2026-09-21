from aiohttp import web


#создаем полку
async def startup_counter(app):
    app["counter"] = 0

#обнуляем полку
async def reset(request):
    request.app["counter"] = 0
    return web.json_response({"counter": request.app["counter"]})

#увеличиваем счетчик на 1
async def inc(request):
    request.app["counter"] += 1
    return web.json_response({"counter": request.app["counter"]})

#чтение полки
async def stats(request):
    return web.json_response({"counter": request.app["counter"]})



def create_app():
    app = web.Application()
    app.router.add_post("/inc", inc)
    app.router.add_post("/reset", reset)
    app.router.add_get("/stats", stats )
    app.on_startup.append(startup_counter)
    return app



if __name__ == "__main__":
    web.run_app(create_app())
