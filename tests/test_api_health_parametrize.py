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

@pytest.mark.parametrize("method, url, expected_status", [
    ("GET", "/health", 200 ),
    ("GET", "/nonexistent", 404),
    # ("POST", "/echo", 405 ),
    ("POST", "/echo", 200 ),
])
async def test_status(method, client, url, expected_status):
    if method == "GET":
        resp = await client.get(url)
        assert resp.status == expected_status
    elif method == "POST":
        resp = await client.post(url, json={"message":"привет"})
        assert resp.status == expected_status





