# Задача 1.
# Используя словесное и визуальное описание, реализовать сортировку выбором.
# Элементы сортируются по возрастанию (равные значения допускаются).


def selection_sort(numbers):
    # Слева от i уже стоят наименьшие элементы на своих местах.
    for i in range(len(numbers) - 1):
        min_index = i
        # Во время поиска запоминаем индекс минимума, не меняя сам список.
        for j in range(i + 1, len(numbers)):
            if numbers[j] < numbers[min_index]:
                min_index = j
        # Обмен выполняется только после просмотра всей оставшейся части.
        if min_index != i:
            numbers[i], numbers[min_index] = numbers[min_index], numbers[i]


if __name__ == "__main__":
    numbers = list(map(int, input("Введите целые числа через пробел: ").split()))
    selection_sort(numbers)
    print("Отсортированный массив:", numbers)
