import pytest
from aiohttp.test_utils import TestClient, TestServer
import pytest
from server.server_hello import create_app

@pytest.fixture
async def client():
    server = TestServer(create_app())
    client = TestClient(server)
    await client.start_server()
    yield client
    await client.close()

@pytest.mark.asyncio
async def test_hello(client):
    resp = await client.get("/")
    assert resp.status == 200
    text = await resp.text()
    assert text == "Привет!"

@pytest.mark.asyncio
async def test_bye(client):
    resp = await client.get("/bye")
    assert resp.status == 200
    text = await resp.text()
    assert text == "Пока!"