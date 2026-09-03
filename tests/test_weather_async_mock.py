from aiohttp.test_utils import TestClient, TestServer
import pytest
from unittest.mock import AsyncMock
from server.weather import create_app


@pytest.fixture
async def client():
    server = TestServer(create_app())
    client = TestClient(server)
    await client.start_server()
    yield client
    await client.close()



async def test_weather(client, monkeypatch):
    mock = AsyncMock(return_value=20)
    monkeypatch.setattr('server.weather.get_temperature', mock)
    resp = await client.get("/weather")
    assert resp.status == 200
    data = await resp.json()
    assert data["temp"] == 20
    mock.assert_called_once_with("Moscow")  # уже проверка, поэтому не нужен assert перед ним

# mock.assert_called()                  # вызвали хотя бы раз? слабая проверка. Вызвали 5 раз? Тоже пройдёт.
# mock.assert_called_once()             # вызрали ровно один раз? вызвали один раз, но не проверяет с каким аргументом
# mock.assert_called_once_with("Moscow")  # вызвали один раз И с аргументом "Moscow"? с правильным аргументом "Moscow"




