from aiohttp import web




async def get_temperature(city):
    return 25

async def weather(request):
    return web.json_response({"city": "Moscow", "temp": await get_temperature("Moscow")})



def create_app():
    app = web.Application()
    app.router.add_get('/weather', weather)
    return app

if __name__ == "__main__":
    web.run_app(create_app())