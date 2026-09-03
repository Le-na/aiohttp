from aiohttp import web



async def server_error(request):
    return web.json_response({"error": "server error"}, status=500)


def error_create_app():
    app = web.Application()
    app.router.add_get("/error", server_error)
    return app

if __name__ == "__main__":
    web.run_app(create_app())