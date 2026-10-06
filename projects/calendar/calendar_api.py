import os
import sqlite3

from aiohttp import web



async def init_db(app):
    conn = sqlite3.connect(os.path.join(os.path.dirname(__file__), "calendar.db"))
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS notes (year TEXT, month TEXT, day TEXT, text TEXT, UNIQUE(year, month, day))")
    app["db"] = conn


async def list_notes(request):
    year = request.match_info["year"]
    month = request.match_info["month"]
    conn = request.app["db"]
    cur = conn.cursor()
    cur.execute("SELECT day, text FROM notes WHERE year = ? AND month = ?", (year, month))
    notes = cur.fetchall()
    res = (dict(notes))
    return web.json_response(res)


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
    conn = request.app["db"]
    cur = conn.cursor()
    cur.execute(f"INSERT INTO notes(year, month, day, text) VALUES (?, ?, ?, ?) "
                f"ON CONFLICT(year, month, day) DO UPDATE SET text=?", (year, month, day, text, text))
    conn.commit()
    return web.json_response({"key": key, "day": day, "text": text})


async def delete_note(request):
    year = request.match_info["year"]
    month = request.match_info["month"]
    day = request.match_info["day"]
    conn = request.app["db"]
    cur = conn.cursor()
    cur.execute("DELETE FROM notes WHERE year = ? AND month = ? AND day = ?", (year, month, day))
    conn.commit()
    return web.json_response({"deleted": day})


def create_app():
    app = web.Application()
    app.router.add_get("/notes/{year}/{month}", list_notes)
    app.router.add_put("/notes/{year}/{month}/{day}", save_note)
    app.router.add_delete("/notes/{year}/{month}/{day}", delete_note)
    app.on_startup.append(init_db)
    app.router.add_static("/static", os.path.join(os.path.dirname(__file__), "static"))
    return app


if __name__ == "__main__":
    web.run_app(create_app())