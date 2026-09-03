from aiohttp.test_utils import TestClient, TestServer
import pytest
from server.error_api import create_app



@pytest.fixture
async def client():
    server = TestServer(create_app())
    client = TestClient(server)
    await client.start_server()
    yield client
    await client.close()


async def test_server_error(client):
    resp = await client.get("/error")
    assert resp.status == 500