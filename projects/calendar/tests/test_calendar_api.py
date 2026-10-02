from aiohttp.test_utils import TestServer, TestClient
import pytest
from calendar_api import create_app


@pytest.fixture
async def client():
    server = TestServer(create_app())
    client = TestClient(server)
    await client.start_server()
    yield client
    await client.close()


async def test_list_notes(client):
    resp = await client.get("/notes/2026/10")
    assert resp.status == 200


async def test_save_note(client):
    resp = await client.put("/notes/2026/10/22", json={"text": "тест"})
    assert resp.status == 200
    r = await client.get("/notes/2026/10")
    data = await r.json()
    assert data["22"] == "тест"


async def test_delete_note(client):
    resp = await client.put("/notes/2026/10/5", json={"text":"тест"})
    assert resp.status == 200
    d = await client.delete("/notes/2026/10/5")
    assert d.status == 200
    g = await client.get("/notes/2026/10")
    data = await g.json()
    assert "5" not in data























