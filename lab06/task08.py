# Задача 8.
# Дана матрица M x N (M и N чётные). Поменять местами
# левую верхнюю и правую нижнюю четверти.


def main():
    m = int(input("Введите количество строк M: "))
    n = int(input("Введите количество столбцов N: "))
    if m <= 0 or n <= 0:
        print("Размеры должны быть положительными.")
        return
    if m % 2 != 0 or n % 2 != 0:
        print("Оба размера должны быть чётными.")
        return
    matrix = []
    for i in range(m):
        row = list(map(float, input(f"Строка {i + 1} ({n} чисел через пробел): ").split()))
        if len(row) != n:
            print("Количество элементов строки должно быть равно", n)
            return
        matrix.append(row)

    half_rows = m // 2
    half_columns = n // 2
    # Обходим только верхнюю левую четверть, чтобы не поменять пары обратно.
    for i in range(half_rows):
        for j in range(half_columns):
            other_i = i + half_rows
            other_j = j + half_columns
            matrix[i][j], matrix[other_i][other_j] = (
                matrix[other_i][other_j], matrix[i][j]
            )
    print("Результат:")
    for row in matrix:
        print(*row)


if __name__ == "__main__":
    main()
