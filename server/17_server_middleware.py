from aiohttp import web




async def handler_secret(request):
    return web.json_response({"message":"Секретные данные"})

@web.middleware
async def auth_mw(request, handler):
    if "Authorization" not in request.headers:
        return web.json_response({"error":"Нет доступа"}, status=401)
    return await handler(request)

app = web.Application()
app.middlewares.append(auth_mw)
app.router.add_get("/secret", handler_secret)
web.run_app(app)