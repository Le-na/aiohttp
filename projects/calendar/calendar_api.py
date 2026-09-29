import os

from aiohttp import web




async def startup_calendar(app):
    app["notes"] = {}



async def list_notes(request):
    year = request.match_info["year"]
    month = request.match_info["month"]
    key = f"{year}-{month}"
    return web.json_response(request.app["notes"].get(key, {}))


async def save_note(request):
    year = request.match_info["year"]
    month = request.match_info["month"]
    day = request.match_info["day"]
    key = f"{year}-{month}"
    try:
        data = await request.json()
    except Exception:
        return web.json_response({"error": "Invalid data"}, status=400)
    text = data.get("text")
    notes = request.app["notes"]
    notes.setdefault(key, {})[day] = text
    return web.json_response({"key": key, "day": day, "text": text})






async def delete_note(request):
    year = request.match_info["year"]
    month = request.match_info["month"]
    day = request.match_info["day"]
    key = f"{year}-{month}"

    notes = request.app["notes"]
    month_notes = notes.get(key, {})
    month_notes.pop(day, None)
    return web.json_response({"deleted": day})



def create_app():
    app = web.Application()
    app.router.add_get("/notes/{year}/{month}", list_notes)
    app.router.add_put("/notes/{year}/{month}/{day}", save_note)
    app.router.add_delete("/notes/{year}/{month}/{day}", delete_note)
    app.on_startup.append(startup_calendar)
    app.router.add_static("/static", os.path.join(os.path.dirname(__file__), "static"))
    return app


if __name__ == "__main__":
    web.run_app(create_app())