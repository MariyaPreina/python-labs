# Задача 5.
# Бинарный поиск: написать функцию, которая рекурсивно выполняет
# бинарный поиск заданного элемента в отсортированном массиве.


def binary_search(numbers, target, left, right):
    # Границы включительные. Если они пересеклись, область поиска пуста.
    if left > right:
        return -1

    middle = (left + right) // 2
    if numbers[middle] == target:
        return middle
    # Массив отсортирован: меньшее значение может быть только левее середины.
    # Середину исключаем из следующего поиска — её уже проверили.
    if target < numbers[middle]:
        return binary_search(numbers, target, left, middle - 1)
    return binary_search(numbers, target, middle + 1, right)


if __name__ == "__main__":
    numbers = list(map(int, input("Введите целые числа по возрастанию через пробел: ").split()))
    target = int(input("Введите искомое число: "))
    index = binary_search(numbers, target, 0, len(numbers) - 1)
    if index == -1:
        print("Элемент не найден.")
    else:
        print("Индекс элемента (с нуля):", index)
