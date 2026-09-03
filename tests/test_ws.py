from aiohttp.test_utils import TestClient, TestServer
import pytest
from server.ws import create_app


@pytest.fixture
async def client():
    server = TestServer(create_app())
    client = TestClient(server)
    await client.start_server()
    yield client
    await client.close()


async def test_echo(client):
    ws = await client.ws_connect("/websocket_handler")   #подключилась к websocket
    await ws.send_str("Привет") #отправлляю сообщение
    msg = await ws.receive_str()    #получаю сообщение
    assert msg == "Привет" #проверяю
    await ws.close()    #закрываю


