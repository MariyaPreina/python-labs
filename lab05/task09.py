# Задача 9.
# Дан массив размера N. Найти номер последнего локального максимума:
# элемента, который больше любого из своих соседей.


numbers = list(map(float, input("Введите элементы массива через пробел: ").split()))
n = len(numbers)
if n < 2:
    print("Требуется не менее 2 элементов.")
else:
    last_maximum = 0
    # Ищем справа налево: первый найденный максимум будет последним по номеру.
    # Крайний элемент сравнивается только с одним существующим соседом.
    for i in range(n - 1, -1, -1):
        greater_left = i == 0 or numbers[i] > numbers[i - 1]
        greater_right = i == n - 1 or numbers[i] > numbers[i + 1]
        if greater_left and greater_right:
            last_maximum = i + 1
            break
    print("Номер последнего локального максимума:", last_maximum)
