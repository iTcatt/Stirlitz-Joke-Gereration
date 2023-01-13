import asyncio
import uuid
from typing import MutableMapping

from aio_pika import Message, connect
from aio_pika.abc import (
    AbstractChannel,
    AbstractConnection,
    AbstractIncomingMessage, 
    AbstractQueue,
)


class RpcClient:
    connection: AbstractConnection
    channel: AbstractChannel
    callback_queue: AbstractQueue
    loop: asyncio.AbstractEventLoop

    def __init__(self) -> None:
        self.futures: MutableMapping[str, asyncio.Future] = {}
        self.loop = asyncio.get_running_loop()

    async def connect(self) -> "RpcClient":
        self.connection = await connect(
            "amqp://guest:guest@localhost/", loop=self.loop,
        )
        self.channel = await self.connection.channel()
        self.callback_queue = await self.channel.declare_queue(exclusive=True)
        # print("I am here", self.callback_queue.name)
        await self.callback_queue.consume(self.on_response)

        return self


    def on_response(self, message: AbstractIncomingMessage) -> None:
        if message.correlation_id is None:
            print(f"Bad message {message!r}")
            return

        future: asyncio.Future = self.futures.pop(message.correlation_id)
        future.set_result(message.body)


    async def call(self, lauch: str) -> str:
        correlation_id = str(uuid.uuid4())
        future = self.loop.create_future()

        self.futures[correlation_id] = future

        await self.channel.default_exchange.publish(
            Message(
                lauch.encode(),
                content_type="text/plain",
                correlation_id=correlation_id,
                reply_to=self.callback_queue.name,
            ),
            routing_key="rpc_queue",
        )

        return await future


async def generation() -> str:
    generation_rpc = await RpcClient().connect()
    print(" [x] Requesting 'Шутка:'")
    try:
        response = await generation_rpc.call('Шутка:')
    except Exception:
        pass
    
    print(f" [.] Got {response.decode()}")
    return response.decode()

