import aiohttp
from aiohttp.test_utils import TestClient, TestServer
import pytest
from server.mock_api import create_app
from server.client_fetch import fetch_data, fetch_safe
from server.error_api import error_create_app




@pytest.fixture()
async def client():
    server = TestServer(create_app())
    client = TestClient(server)
    await client.start_server()
    yield client
    await server.close()


async def test_client_fetch(client):
    url = str(client.make_url("/weather"))
    data = await fetch_data(url)
    assert data["temp"] == 25

# @pytest.fixture и yield  - не нужна, потому что переиспользовать сервер мы не будем
# у нас тольько 1 тест
# если 3 теста с сервером ошибок, тогда с fixture
async def test_fetch_error():
    server = TestServer(error_create_app())
    client = TestClient(server)
    await client.start_server()
    url = str(client.make_url("/error"))
    with pytest.raises(aiohttp.ClientResponseError):
        await fetch_safe(url)
    await client.close()
