from aiohttp import web, request



async def startup_books(app):
    app["books"] = {}
    app["next_id"] = 1


# выдает/возвращает тело заметки по id.
# читает тело, проверяет ключ text, выдает id, кладет заметку, создаем статус
async def create_book(request):
    try:
        data = await request.json()
    except Exception:
        return web.json_response({"error": "нет записей"}, status=400)
    if "title" not in data:
        return web.json_response({"error": "нет ключа title, ключ author необязателен"}, status=400)
    author = data.get("author", "неизвестен")
    book_id = request.app["next_id"]
    request.app["next_id"] += 1
    book = {"book_id": book_id, "author": author, "title": data["title"]}
    request.app["books"][book_id] = book
    return web.json_response(book, status=201)


async def books_list(request):
    books = list(request.app["books"].values())
    return web.json_response(books)


async def get_book(request):
    id = int(request.match_info["id"])
    if id not in request.app["books"]:
        return web.json_response({"error": "нет такого id"}, status=404)
    return web.json_response(request.app["books"][id])


async def update_book(request):
    id = int(request.match_info["id"])
    if id not in request.app["books"]:
        return web.json_response({"error": "нет такого id"}, status=404)
    try:
        data = await request.json()
    except Exception:
        return web.json_response({"error": "нет записей"}, status=400)
    if "title" not in data:
        return web.json_response({"error": "нет ключа title, ключ author необязателен"}, status=400)
    book = request.app["books"][id]
    book["title"] = data["title"]
    book["author"] = data.get("author", "неизвестен")
    return web.json_response(book)


async def delete_book(request):
    id = int(request.match_info["id"])
    if id not in request.app["books"]:
        return web.json_response({"error": "нет такого id"}, status=404)
    del request.app["books"][id]
    return web.json_response({"deleted":id})


def create_app():
    app = web.Application()
    app.on_startup.append(startup_books)
    app.router.add_post("/books", create_book)
    app.router.add_get("/books", books_list)
    app.router.add_get("/books/{id}", get_book)
    app.router.add_put("/books/{id}", update_book)
    app.router.add_delete("/books/{id}", delete_book)
    return app


if __name__ == "__main__":
    web.run_app(create_app())
