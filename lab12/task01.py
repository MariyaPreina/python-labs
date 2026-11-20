# Задача 1. Продемонстрировать основные операции с очередью.
# FIFO: первый добавленный элемент извлекается первым.

from collections import deque


def main():
    q = deque()
    numbers = list(map(int, input("Введите числа для очереди через пробел: ").split()))
    for number in numbers:
        q.append(number)

    print("Очередь (начало слева):", list(q))
    if not q:
        print("Очередь пуста.")
        return

    # Просмотр сохраняет элемент, а popleft удаляет его из очереди.
    print("Первый элемент:", q[0])
    print("Удалили из начала:", q.popleft())
    print("Осталось в очереди:", list(q))
    print("Количество оставшихся элементов:", len(q))

    target = int(input("Какое число найти в оставшейся очереди? "))
    if target in q:
        print("Число найдено.")
    else:
        print("Число не найдено.")

    print("Перебор оставшихся элементов:", end=" ")
    for number in q:
        print(number, end=" ")
    print()

    q.clear()
    print("После очистки:", list(q))
    if not q:
        print("Очередь пуста.")


if __name__ == "__main__":
    main()
