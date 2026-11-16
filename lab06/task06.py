# Задача 6.
# Дана матрица M x N. В каждой строке поменять местами
# минимальный и максимальный элементы.


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

    for row in matrix:
        # Индексы ищем заново в каждой строке; перестановку делаем после поиска.
        min_index = 0
        max_index = 0
        for j in range(1, n):
            if row[j] < row[min_index]:
                min_index = j
            if row[j] > row[max_index]:
                max_index = j
        row[min_index], row[max_index] = row[max_index], row[min_index]
    print("Результат:")
    for row in matrix:
        print(*row)


if __name__ == "__main__":
    main()
