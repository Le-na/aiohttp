from aiohttp.test_utils import TestClient, TestServer
import pytest
from server.weather import create_app

d

@pytest.fixture
async def client():
    server = TestServer(create_app())
    client = TestClient(server)
    await client.start_server()
    yield client
    await client.close()

async def fake_get_temperature(city):
    return 20


async def test_weather(client, monkeypatch):
    monkeypatch.setattr("server.weather.get_temperature", fake_get_temperature)
    resp = await client.get("/weather")
    assert resp.status == 200
    data = await resp.json()
    assert data["temp"] == 20
