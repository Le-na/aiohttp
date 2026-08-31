from aiohttp import web

async def status(request):
    return web.json_response({"db": request.app["db"]})



async def init_db(app):
    print("Подключаемся к базе...")
    app["db"] = {"connected": True}
    print("База готова")

async def close_db(app):
    print("Закрываем базу...")
    app["db"] = {"connected": False}
    print("База закрыта")

app = web.Application()
app.on_startup.append(init_db)
app.on_cleanup.append(close_db)
app.router.add_get("/status", status)
web.run_app(app)