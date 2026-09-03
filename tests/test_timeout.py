import asyncio
from aiohttp.test_utils import TestClient, TestServer
import pytest
from server.slow_api import create_app


@pytest.fixture
async def client():
    server = TestServer(create_app())
    client = TestClient(server)
    await client.start_server()
    yield client
    await client.close()


async def test_timeout(client):
    assert asyncio.TimeoutError
