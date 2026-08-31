from aiohttp import web
from aiohttp.web_app import Application



# async def stream(request):
#     resp = web.StreamResponse()
#     await resp.prepare(request)
#     for i in range(5):
#         await resp.write(f"кусок {i}\n".encode())
#     return resp

# Чтобы на странице браузера не была ошибка 404: Not Found
# и чтобы браузер не скачивал файл с "кусочками", а показывал нужно указать Content-Type
async def stream(request):
    resp = web.StreamResponse()
    resp.content_type = "text/html"    #text/plain — простой текст, с тегами и переносами.
    # text/html — HTML игнорирует теги, переносы и пишет все в одной строке страницы браузера
    await resp.prepare(request)
    for i in range(5):
        await resp.write(f"кусок {i}\n".encode())
    return resp


def create_app():
    app = web.Application()
    app.router.add_get("/stream", stream)
    return app

if __name__ == "__main__":
    app = create_app()
    web.run_app(app)


























