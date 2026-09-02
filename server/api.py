from aiohttp import web



async def health(request):
    return web.json_response({"status":"ok"})


async def echo(request):
    data = await request.json()
    return web.json_response(data)



def create_app():
    app = web.Application()
    app.router.add_get("/health", health)
    app.router.add_post("/echo", echo)
    return app

if __name__ == '__main__':
    web.run_app(create_app())