import asyncio
import time


async def notification():
    time.sleep(10)
    print("Созвон через 10 минут!")


async def main():
    task = asyncio.create_task(notification())            # запускаем корутину
    print("Едим")
    print("Разговариваем с коллегой")

asyncio.run(main())