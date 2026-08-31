import pytest   #Импортирование библиотеки pytest
from aiohttp.test_utils import TestServer, TestClient
#из библиотеки aiohttp функции test_utils мы импортируем инструменты TestServer и TestClient
# TestServeer - запускает сервер
# TestClient - создает клиента
from server.static import create_app    #импортируем приложение(Application) из файла static из папки server


@pytest.fixture
async def client():
    #TestServer(create_app()) соханяет настройки в переменной сервер,
    # пользуемсяя настройками из функции create_app() там лежат загрузчики пути
    # client = TestClient(server) создает клиента для параметров server из функции create_app()
    #await client.start_server() - запускает сервер
    #yield client - отдаёт клиент тесту, потом закрывается (пауза, если все отработало, тогда закррытие клиентского соединения)
    # и выход программы тестирования

    server = TestServer(create_app())
    client = TestClient(server)
    await client.start_server()
    yield client
    await client.close()



async def test_static_index(client):
    #создание ассинхронной функции для отлова ошибок
    # resp = await client.get("/static/index.html") сохраняем ответ Responce на запрос GET в переменной,
    # чтобы работать с полученными данными и не отправлять при запросы для каждой проверки
    # assert - это ПРОВЕРКА на совпадение, если не совпадает тест падает
    # assert resp.status == 200 - отлавлливание ошибки статуса, если не совпадает с 200
    # assert resp.content_type == "text/html" - (внуутри ответа находится строка content_type - это атриут ответа)
    # Content-Type действительно передаётся как header, в коде это resp.content_type — свойство объекта/атрибут ответа
    # и проверяется content_type это "text/html"
    # text = await resp.text() - тут мы сохрняем body
    # assert text == "\n<h1>Привет от Елены!</h1>" и проверяем на соответствие к тексту.
    # Я так понимаю, что можно создать главный html файл и потом сравнивнивать его с созданным файлом/проверочным файлом на соответствие?
    # но чаще всего сравнивают (статус, тип, часть текста), а не точное содержаниефайла

    resp = await client.get("/static/index.html")
    assert resp.status == 200
    assert resp.content_type == "text/html"
    text = await resp.text()
    # assert text == "\n<h1>Привет от Елены!</h1>" лучше не использовать такую конструкцию,
    # потому что она очень жестко проверяеет на совпадение символов
    assert "Привет от Елены" in text
