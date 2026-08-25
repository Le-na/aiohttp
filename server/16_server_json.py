# from aiohttp import web
#
# async def info(request):
#     data = {"name":"Elena", "skill":"aiohttp"}
#     return web.json_response(data)
#
# app = web.Application()
# app.router.add_get("/info", info)
# web.run_app(app)

from aiohttp import web

async def info(request):
    data = {"name":"Elena", "skill":"aiohttp"}
    return web.json_response(data)

async def create_user(request):
    data = await request.json()
    return web.json_response({"status":"Created", "user":data})
app = web.Application()
app.router.add_get("/info", info)
app.router.add_post("/user", create_user)
web.run_app(app)
