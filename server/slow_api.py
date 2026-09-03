import asyncio

from aiohttp import web


async def slow_api(request):
    await asyncio.sleep(10)
    return web.json_response({"data":"finnaly"})


def create_app():
    app = web.Application()
    app.router.add_get("/slow", slow_api)
    return app


if __name__ == "__main__":
    web.run_app(create_app())
