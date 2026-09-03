from aiohttp import web




async def weather(request):
    return web.json_response({"temp":25})




def create_app():
    app = web.Application()
    app.router.add_get("/weather", weather)
    return app



if __name__ == "__main__":
    web.run_app(create_app())