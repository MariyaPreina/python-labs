# Задача 1.
# Используя словесное описание, реализовать бинарный поиск.
# Массив заранее отсортирован по неубыванию. Вернуть индекс искомого
# элемента (с нуля), а при его отсутствии — -1.


def binary_search(numbers, target):
    left = 0
    right = len(numbers) - 1
    # Границы включены: при left == right остаётся проверить один элемент.
    while left <= right:
        middle = (left + right) // 2
        if numbers[middle] == target:
            return middle
        # Середину уже проверили. Отбрасываем её вместе с неподходящей половиной.
        if numbers[middle] > target:
            # Всё правее середины тоже больше искомого значения.
            right = middle - 1
        else:
            # Всё левее середины тоже меньше искомого значения.
            left = middle + 1
    return -1


if __name__ == "__main__":
    numbers = list(map(int, input("Введите целые числа по возрастанию через пробел: ").split()))
    target = int(input("Введите искомое число: "))
    result = binary_search(numbers, target)
    print("Индекс элемента (с нуля; -1 — не найден):", result)
