# Задача 6.
# Дан массив размера N и целые K, L (1 <= K <= L <= N).
# Найти среднее арифметическое элементов с номерами от K до L включительно.


numbers = list(map(float, input("Введите элементы массива через пробел: ").split()))
n = len(numbers)
if n < 1:
    print("Требуется не менее 1 элементов.")
else:
    k = int(input("Введите K: "))
    l = int(input("Введите L: "))
    if not 1 <= k <= l <= n:
        print("Требуется 1 <= K <= L <= N.")
    else:
        total = 0
        # range не включает правую границу: индексы идут от K-1 до L-1.
        for i in range(k - 1, l):
            total = total + numbers[i]
        print("Среднее арифметическое:", total / (l - k + 1))
