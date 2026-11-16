# Задача 4.
# Дан массив A размера N. Вывести элементы в порядке:
# A1, AN, A2, AN-1, A3, AN-2, ... .


numbers = list(map(float, input("Введите элементы массива через пробел: ").split()))
n = len(numbers)
if n < 1:
    print("Требуется не менее 1 элементов.")
else:
    left = 0
    right = n - 1
    result = []
    while left <= right:
        result.append(numbers[left])
        # При нечётном N центральный элемент добавляется только один раз.
        if left != right:
            result.append(numbers[right])
        left = left + 1
        right = right - 1
    print("Порядок элементов:", result)
