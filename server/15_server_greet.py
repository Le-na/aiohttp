from aiohttp import web

async def greet(request):
    name = request.query.get("name", "незнакомец")
    return web.Response(text=f"Привет {name}")


app = web.Application()
app.router.add_get("/greet", greet)
web.run_app(app)
