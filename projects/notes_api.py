from aiohttp import web


#создаем пустую полку со словарями
#для хранения данных
# словарь заметок {id: "заметка"}
async def startup_notes(app):
    app["notes"] = {}
    app["next_id"] = 1


# выдает/возвращает тело заметки по id.
# читает тело, проверяет ключ text, выдает id, кладет заметку, создаем статус
async def create_note(request):
    try:
        data = await request.json() #чтение тела
    except Exception:   # если ловим exception, тогда возвращаем ответ сервера - ошибку 400
        return web.json_response({"error": "нет тела"}, status=400)
    if "text" not in data:  #проверка. пока нет ключа text - не пропускать дальше -> ошибка
        return web.json_response({"error": "нет ключа text"}, status=400)
    note_id = request.app["next_id"] #взяли текущий номер id
    request.app["next_id"] += 1 #увеличили число
    note = {"note_id":note_id, "text": data["text"]}
    request.app["notes"][note_id] = note
    return web.json_response(note, status=201)





#чтение полки по id
#показать какие данные хранятся
async def list_notes(request):
    notes = list(request.app["notes"].values()) #.values() - показывает значение без ключей
    return web.json_response(notes) # формируем ответ от сервера - список list со значеними text

#возвращает 1 заметку по id
async def get_note(request):
    note_id = int(request.match_info["id"])    #получаем цифру и записываем в переменную note_id
    if note_id not in request.app["notes"]: #делаем проверку - есть ли у нас в словаре под таким id чтото
        return web.json_response({'error': 'not found'}, status=404) #если такой цифры id нет -> тогда ошибка
    note = request.app["notes"][note_id]    # если цифра id у нас есть -> обращаемся к списку по ключу note_id
    return web.json_response(note)  #возвращаем text



#удаление данных по id
async def delete_note(request):
    note_id = int(request.match_info["id"])
    if note_id not in request.app["notes"]:
        return web.json_response({"error": "not found"}, status=404)
    del request.app["notes"][note_id]
    return web.json_response({"deleted":note_id})


#изменение данных по id
async def update_note(request):
    note_id = int(request.match_info["id"])
    if note_id not in request.app['notes']:
        return web.json_response({"error": "not found"}, status=404)
    try:
        data = await request.json()
    except Exception:
        return web.json_response({"error": "нет тела"}, status=400)
    if "text" not in data:
        return web.json_response({"error": "нет ключа text"}, status=400)
    note = request.app["notes"][note_id]
    note["text"] = data["text"]
    return web.json_response(note)

async def cors(request):
    headers = {
        'Access-Control-Allow-Origin': 'http://localhost:63342',
        'Access-Control-Allow-Headers': '*',
        'Access-Control-Allow-Methods': '*',
    }
    return web.Response(headers=headers)

def create_app():
    app = web.Application()
    app.router.add_options("/notes", cors)
    app.router.add_options("/notes/{id}", cors)
    app.router.add_get("/notes", list_notes)
    app.router.add_post("/notes", create_note)
    app.router.add_get("/notes/{id}", get_note)
    app.router.add_delete("/notes/{id}", delete_note)
    app.router.add_put("/notes/{id}", update_note)
    app.on_startup.append(startup_notes)
    return app



if __name__ == "__main__":
    web.run_app(create_app())