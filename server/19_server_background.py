from aiohttp import web
import asyncio


async def status(request):
    return web.json_response({"status": "ok"})


async def ticker(app):
    while True:
        print("тик")
        await asyncio.sleep(3)

async def start_ticker(app):
        app["ticker"] = asyncio.create_task(ticker(app))

async def stop_ticker(app):
    app["ticker"].cancel()


app = web.Application()
app.router.add_get("/status", status)
app.on_startup.append(start_ticker)
app.on_cleanup.append(stop_ticker)
web.run_app(app)