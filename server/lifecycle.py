from aiohttp import web


async def init_db(app):
    print("Подключаемся к базе ...")
    app["db"] = {"connected": True}
    print("База готова")


async def close_db(app):
    print("Отключение от базы ...")
    app['db'] = {"connected": False}
    print("База закрыта")


async def status(request):
    return web.json_response({"db": request.app["db"]})



def create_app():
    app = web.Application()
    app.on_startup.append(init_db)
    app.on_cleanup.append(close_db)
    app.router.add_get("/status", status)
    return app

if __name__ == "__main__":
    web.run_app(create_app())


