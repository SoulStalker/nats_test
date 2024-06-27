import asyncio
from asyncio import CancelledError


import nats
from nats.aio.msg import Msg


# Функция-обработчик полученных сообщений
async def message_handler(msg: Msg):
    subject = msg.subject
    data = msg.data.decode()
    print(f"Received message from {subject}: {data}")


async def main():
    # Подключаемся к NATS серверу
    nc = await nats.connect("nats://192.168.10.50:4222")

    # Сабжект для подписки
    subject = "my.first.*"

    # Подписываемся на указанный самбджект
    await nc.subscribe(subject, cb=message_handler)
    print(f"Subscribed to {subject}")

    # Создаем future для поддержания соединения открытым
    try:
        await asyncio.Future()
    except CancelledError:
        pass
    finally:
        # Закрываем соединение
        await nc.close()


asyncio.run(main())