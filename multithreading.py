import threading
import time


def calculate_sum(a, b):
    time.sleep(2)  # Імітація обчислення
    result = a + b
    print(f"Sum: {result}")


if __name__ == "__main__":
    # Створення потоку
    thread = threading.Thread(target=calculate_sum, args=(3, 4))

    # Запуск потоку
    thread.start()

    # Очікування завершення потоку
    thread.join()

    print("Main thread continues...")
