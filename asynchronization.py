import asyncio
import threading
import time
import random


async def add(a, b):
    print(f"Adding {a} + {b}")
    await asyncio.sleep(1)
    result = a + b
    print(f"Result: {result}")
    return result


async def multiply(c, d):
    print(f"Multiplying {c} * {d}")
    await asyncio.sleep(1)
    result = c * d
    print(f"Result: {result}")
    return result


async def main():
    task1 = asyncio.create_task(add(2, 3))
    task2 = asyncio.create_task(multiply(4, 5))

    result1 = await task1
    result2 = await task2

    final_result = result1 + result2
    print(f"Final Result: {final_result}")

asyncio.run(main())


# Функція 1: Симуляція обробки даних


async def process_data_async():
    print("Processing data asynchronously...")
    await asyncio.sleep(2)
    print("Data processing completed asynchronously.")

# Функція 2: Генерація структури даних


async def generate_data_structure_async():
    print("Generating data structure asynchronously...")
    data_list = [random.randint(1, 100) for _ in range(5)]
    print("Data structure generated asynchronously:", data_list)
    return data_list

# Функція 3: Інша корисна дія (асинхронна)


async def useful_action_async(data):
    print("Performing useful action asynchronously...")
    sorted_data = sorted(data)
    print("Useful action completed asynchronously. Sorted data:", sorted_data)
    return sorted_data


# Основний скрипт
async def main_async():
    start_time = time.time()

    # Виклик асинхронних функцій
    await process_data_async()
    data = await generate_data_structure_async()
    await useful_action_async(data)

    end_time = time.time()
    print(f"Async execution time: {end_time - start_time:.4f} seconds")

if __name__ == "__main__":
    import asyncio

    # Запуск асинхронної частини
    asyncio.run(main_async())
