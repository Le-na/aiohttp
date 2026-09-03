from aiohttp import web


"""
    await ws.prepare(request) 
    await - тк prepare то ассинхронный метод
    ws это объект WebSocketResponse (ws = web.WebSocketResponse())
    prepare - метод, который подготавливает ответ. Он переключает соединение с обычного HTTP на WebSocket. 
                Это называется 'handshake' - рукопожатие. Клиент и сервер договариваются: 'дальше общаемся по WebSocket'
     
    request - входящий запрос от клиета. он передается в prepare, чтобы запомнить от кого подключение
"""



def create_app():
    app = web.Application()
    app.router.add_get("/ws", websocket_handler)
    return app

if __name__ == "__main__":
    web.run_app(create_app())