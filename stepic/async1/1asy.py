import time
import asyncio

start = time.time()


async def sleeping(n):
    print(f"Начало выполнения длительной операции № {n}: {time.time() - start:.4f}")
    await asyncio.sleep(1)  # Имитация длительной операции в 1 секунду длиной.
    print(f"Длительная операция № {n} завершена")


async def main():
    # Запуск 30 задач.
    task = [sleeping(i) for i in range(1, 31)]
    all_results = await asyncio.gather(*task)
    print(f"Выполнено {len(all_results)} операций.")
    print(f"Программа завершена за {time.time() - start:.4f}")

# Запуск главной корутины.
asyncio.run(main())