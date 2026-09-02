from aiohttp import web


async def handler_secret(request):
    return web.json_response({"data":"secret"})

@web.middleware
async def auth_mw(request, handler):
    if "Authorization" not in request.headers:
        return web.json_response({"error":"Нет доступа"}, status=401)
    return await handler(request)


def create_app():
    app = web.Application()
    app.middlewares.append(auth_mw)
    app.router.add_get("/secret", handler_secret)
    return app

if __name__ == "__main__":
    web.run_app(create_app())



