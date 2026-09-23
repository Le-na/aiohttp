from aiohttp import web


async def list_print(request):
    data = web.json_response(int(request.match_info["id"]))
    return data







def create_app():
    app = web.Application()
    app.router.add_get("/list/{id}", list_print)
    return app



if __name__ == "__main__":
    web.run_app(create_app())