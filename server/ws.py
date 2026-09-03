from aiohttp import web



async def websocket_handler(request):
    ws = web.WebSocketResponse()
    await ws.prepare(request)
    async for msg in ws:
        await ws.send_str(msg.data)
    return ws



def create_app():
    app = web.Application()
    app.router.add_get("/websocket_handler", websocket_handler)
    return app

if __name__ == "__main__":
    web.run_app(create_app())
