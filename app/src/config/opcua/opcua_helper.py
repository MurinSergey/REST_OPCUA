import asyncio

from asyncua import Client, Node, ua
from asyncua.common.subscription import DataChangeNotif
from asyncua.common.node import Node
from ...config import settings
from ...models.opcua.tables import OpcuaCurrentValue

#Хранилище считываемых узлов/тегов
monitored_items: list[OpcuaCurrentValue] = []

nodes = [
    "ns=3;i=1004",
    "ns=3;i=1006",
    "ns=3;i=1008"
]

opcua_client = Client(settings.opcua.host)

class OpcuaClient():
    _client = None

    def __init__(self, url:str) -> None:
        self._client = Client(url=url)

   
class SubscriptionHandler:
    def datachange_notification(self, node: Node, val, data: DataChangeNotif):
        # print('===========================================')
        # print(f"Нода: {node} Значение: {val} Дата: {data.monitored_item.Value.ServerTimestamp} Состояние: {data.monitored_item.Value.StatusCode_.name}")
        # print('===========================================')
        pass

async def start_subscription(nodes: list):
    async with opcua_client:
        handler = SubscriptionHandler()
        subscription = await opcua_client.create_subscription(500, handler)
        #print(subscription.parameters.MaxNotificationsPerPublish)
        var = [opcua_client.get_node(node) for node in nodes]
        await subscription.subscribe_data_change(var)
        #print([i.node.nodeid.to_string() for in subscription._monitored_items.values()])
        while 1:
            await asyncio.sleep(1)
            await opcua_client.check_connection()

async def main_loop():
    while 1:
        print(">>>>>ПОДКЛЮЧЕНИЕ К OPC")
        try:
            await start_subscription(nodes)
        except (ConnectionError, ua.UaError, TimeoutError):
            await asyncio.sleep(1)