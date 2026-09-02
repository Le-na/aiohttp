from aiohttp.test_utils import TestClient, TestServer
import pytest
from server.lifecycle import create_app



@pytest.fixture
async def client():
    server = TestServer(create_app())
    client = TestClient(server)
    await client.start_server()
    yield client
    await client.close()


async def test_db_connected(client):
    resp = await client.get("/status")
    assert resp.status == 200
    data = await resp.json()
    assert data["db"]["connected"] == True