# from aiohttp import web
#
# async def hello(request):
#     return web.Response(text="Привет!")
#
# app = web.Application()
# app.router.add_get("/", hello)
# web.run_app(app)


from aiohttp import web

async def hello(request):
    return web.Response(text="Привет!")

async def bye(request):
    return web.Response(text="Пока!")


def create_app():
    app = web.Application()
    app.router.add_get("/", hello)
    app.router.add_get("/bye", bye)
    return app

if __name__ == '__main__':
    app = create_app()
    web.run_app(app)

    app = web.Application()
    app.router.add_get("/", hello)
    app.router.add_get("/bye", bye)
    web.run_app(app)