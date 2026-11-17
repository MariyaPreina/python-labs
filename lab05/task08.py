# Задача 8.
# Дан массив A размера N. Найти минимум среди элементов
# с чётными номерами: A2, A4, A6, ... .


numbers = list(map(float, input("Введите элементы массива через пробел: ").split()))
n = len(numbers)
if n < 2:
    print("Требуется не менее 2 элементов.")
else:
    # Начинаем со второго элемента: его номер 2, индекс 1.
    minimum = numbers[1]
    # С индекса 3 до n (не включая), шаг 2: проверяем позиции 4, 6, 8…
    for i in range(3, n, 2):
        if numbers[i] < minimum:
            minimum = numbers[i]
    print("Минимум:", minimum)
