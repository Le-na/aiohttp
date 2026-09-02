from aiohttp.test_utils import TestServer, TestClient
import pytest
from server.api import create_app


@pytest.fixture
async def client():
    server = TestServer(create_app())
    client = TestClient(server)
    await client.start_server()
    yield client
    await client.close()


async def test_health(client):
    resp = await client.get("/health")
    assert resp.status == 200
    data = await resp.json()
    assert data["status"] == "ok"


async def test_echo(client):
    resp = await client.post("/echo", json = {"message":"Привет"})
    assert resp.status == 200
    data = await resp.json()
    assert data["message"] == "Привет"

async def test_not_found(client):
    resp = await client.get("/nonexistent")
    assert resp.status == 404

async def test_method_not_allowed(client):
    resp = await client.post("/health")
    assert resp.status == 405


