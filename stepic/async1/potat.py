import asyncio

async def cook_potatoes():
    print("Почистили и отправили в кастрюлю, ждем-с")
    await asyncio.sleep(10)
    print('Картофан готов, достаем')

async def cut_bread(count: int):
    #пилим хлеб на count кусков
    for i in range(count):
        await asyncio.sleep(4)
        print(f'Отрезали кусок {i + 1}')
    
    print(f'Отрезали {count} кусков')

async def main():
    #запускаем задачи
    task1 = asyncio.create_task(cook_potatoes())
    task2 = asyncio.create_task(cut_bread(4))

    await task1
    await task2

    print('Кушать подано - садитесь жрать!')

asyncio.run(main())