# Задача 2.
# Дана матрица M x N и целое K (1 <= K <= M).
# Найти сумму и произведение элементов K-й строки.


def main():
    m = int(input("Введите количество строк M: "))
    n = int(input("Введите количество столбцов N: "))
    if m <= 0 or n <= 0:
        print("Размеры должны быть положительными.")
        return
    matrix = []
    for i in range(m):
        row = list(map(float, input(f"Строка {i + 1} ({n} чисел через пробел): ").split()))
        if len(row) != n:
            print("Количество элементов строки должно быть равно", n)
            return
        matrix.append(row)

    k = int(input("Введите номер строки K: "))
    if not 1 <= k <= m:
        print("Требуется 1 <= K <= M.")
        return
    total = 0
    product = 1
    for value in matrix[k - 1]:
        total += value
        product *= value
    print("Сумма:", total)
    print("Произведение:", product)


if __name__ == "__main__":
    main()
