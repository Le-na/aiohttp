from aiohttp.test_utils import TestClient, TestServer
import pytest
from server.auth import create_app



@pytest.fixture
async def client():
    server = TestServer(create_app())
    client = TestClient(server)
    await client.start_server()
    yield client
    await client.close()

async def test_no_auth(client):
    resp = await client.get("/secret")
    assert resp.status == 401

async def test_with_auth(client):
    headers = {"Authorization": "token123"}
    resp = await client.get("/secret", headers=headers)
    assert resp.status == 200

