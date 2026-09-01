from aiohttp import web



async def health(request):
    return web.json_response({"status":"okey"})


def create_app():
    app = web.Application()
    app.router.add_get("/health", health)
    return app

if __name__ == '__main__':
    web.run_app(create_app())