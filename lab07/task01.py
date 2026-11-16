# Задача 1.
# Используя словесное и визуальное описание, реализовать сортировку пузырьком.
# Элементы сортируются по возрастанию (равные значения допускаются).


def bubble_sort(numbers):
    # end — индекс последнего элемента ещё не отсортированной части.
    for end in range(len(numbers) - 1, 0, -1):
        swapped = False
        # Обмены соседей доводят максимум этой части до позиции end.
        for i in range(end):
            if numbers[i] > numbers[i + 1]:
                numbers[i], numbers[i + 1] = numbers[i + 1], numbers[i]
                swapped = True
        # Если за весь проход обменов не было, список уже отсортирован.
        if not swapped:
            break


if __name__ == "__main__":
    numbers = list(map(int, input("Введите целые числа через пробел: ").split()))
    bubble_sort(numbers)
    print("Отсортированный массив:", numbers)
