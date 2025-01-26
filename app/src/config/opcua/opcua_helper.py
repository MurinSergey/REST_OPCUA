import asyncio

from asyncua import Client, Node, ua
from asyncua.common.subscription import DataChangeNotif
from asyncua.common.node import Node

nodes = [
    "ns=3;i=1004",
    "ns=3;i=1006",
    "ns=3;i=1008"
]

class SubscriptionHandler:
    def datachange_notification(self, node: Node, val, data: DataChangeNotif):
        print('===========================================')
        print(f"Нода: {node} Значение: {val} Дата: {data.monitored_item.Value.ServerTimestamp} Состояние: {data.monitored_item.Value.StatusCode_.name}")
        print('===========================================')

async def start_subscription(url:str, nodes: list):
    async with Client(url=url) as client:
        handler = SubscriptionHandler()
        subscription = await client.create_subscription(500, handler)
        print(subscription.parameters.MaxNotificationsPerPublish)
        var = [client.get_node(node) for node in nodes]
        await subscription.subscribe_data_change(var)
        #print([i.node.nodeid.to_string() for in subscription._monitored_items.values()])
        while 1:
            await asyncio.sleep(1)
            await client.check_connection()

async def main_loop():
    while 1:
        print(">>>>>ПОДКЛЮЧЕНИЕ К OPC")
        try:
            await start_subscription("opc.tcp://ES-BPASUTP-163:53530/OPCUA/SimulationServer", nodes)
        except (ConnectionError, ua.UaError, TimeoutError):
            await asyncio.sleep(1)