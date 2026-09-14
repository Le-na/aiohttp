from aiohttp.test_utils import TestClient, TestServer
import pytest
from server.exam_server import create_app


@pytest.fixture
async def client():
    server = TestServer(create_app())
    client = TestClient(server)
    await client.start_server()
    yield client
    await client.close()


async def test_add(client):
    resp = await client.get("/add?a=2&b=3")
    assert resp.status == 200
    data = await resp.json()
    assert data['result'] == 5


async def test_greet_hello_name(client):
    resp = await client.get("/greet?name=Аня")
    data = await resp.json()
    assert "Аня" in data["hello"]


async def test_greet_hello_guest(client):
    resp = await client.get("/greet")
    data = await resp.json()
    assert "гость" in data["hello"]


async def test_post_without_key(client):
    resp = await client.post("/echo", json={"text":"привет"})
    assert resp.status == 401


async def test_post_with_key(client):
    resp = await client.post("echo",
                             json={"text":"привет"},
                             headers={"X-API-KEY":"secret123"})
    assert resp.status == 200

