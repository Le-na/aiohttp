from aiohttp.test_utils import TestClient, TestServer
import pytest
from counter_api import create_app


@pytest.fixture
async def client():
    server = TestServer(create_app())
    client = TestClient(server)
    await client.start_server()
    yield  client
    await client.close()


#отправляем запросы и увеличиваем счетчик
async def test_inc(client):
    resp = await client.post("/inc")
    assert resp.status == 200

#проверяем обнуляемость счетчика
async def test_reset(client):
    resp = await client.post("/reset")
    assert resp.status == 200
    assert await resp.json() == {"counter": 0}

# тест на отсутствие побочных эффектов
# читаем файл 3 раза и проверяем, что ничего не изменилось
async def test_stats_readonly(client):
    #читаем файл 3 раза
    await client.get("/stats")
    await client.get("/stats")
    await client.get("/stats")
    # проверяем не изменился ли счетчик
    resp = await client.get("/stats")
    data = await resp.json()
    assert data["counter"] == 0
