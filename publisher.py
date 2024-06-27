import asyncio

import nats


async def main():
    # Подключаемся к NATS серверу
    nc = await nats.connect("nats://192.168.10.50:4222")

    # Сообщение для отправки
    message = "Hello from Python publisher!"

    # Сабджект, в который отправляется сообщение
    subject = "my.first.subject"

    # Публикуем сообщение в указанный топик
    await nc.publish(subject, message.encode())

    print(f"Message '{message}' published in subject '{subject}'")

    # Закрываем соединение
    await nc.close()

asyncio.run(main())
