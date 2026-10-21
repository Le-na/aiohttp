# from calendar import monthrange
# # print(calendar.month(2026, 10))
#
#
#
#
# #
# # data = monthrange(2026, 10)
# # print(type(data))
#
# first, days = monthrange(2028, 2)
# names = ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота", "Воскресенье"]
# print(f"Февраль 2028: {days} день, первое число — {names[first]} (индекс {first})")
#
#

import os

from aiohttp import web
from calendar import monthrange, monthcalendar


months_in_a_year = {
    1: "Январь",
    2: "Февраль",
    3: "Март",
    4: "Апрель",
    5: "Май",
    6: "Июнь",
    7: "Июль",
    8: "Август",
    9: "Сентябрь",
    10: "Октябрь",
    11: "Ноябрь",
    12: "Декабрь",

}

# days_in_a_week = {
#     "0": "Понедельник",
#     "1": "Вторник",
#     "2": "Среда",
#     "3": "Четверг",
#     "4": "Пятница",
#     "5": "Суббота",
#     "6": "Воскресенье"
#
# }



async def month(request):
    try:
        y = int(request.match_info["year"])
        m = int(request.match_info["month"])
    except ValueError:
        return web.json_response("Год и Месяц должны быть числами", status=400)
    if m < 1 or m > 12:
        return web.json_response("есть всего 1-12 месяцев в году", status=400)
    month_matrix = monthcalendar(y, m)
    return web.json_response({"year": y, "month": m, "month_name": months_in_a_year[m], "weeks": month_matrix})






def create_app():
    app = web.Application()
    app.router.add_get("/calendar/{year}/{month}", month)
    app.router.add_static("/static",
                          os.path.join(os.path.dirname(__file__), "calendar_static"))
    return app

if __name__ == "__main__":
    web.run_app(create_app())












