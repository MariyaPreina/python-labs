# Задача 7.
# Дана матрица M x N. Поменять местами столбцы, содержащие
# минимальный и максимальный элементы всей матрицы.


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

    # Запоминаем столбцы крайних значений всей матрицы, а не каждой строки.
    min_value = max_value = matrix[0][0]
    min_column = max_column = 0
    for i in range(m):
        for j in range(n):
            if matrix[i][j] < min_value:
                min_value = matrix[i][j]
                min_column = j
            if matrix[i][j] > max_value:
                max_value = matrix[i][j]
                max_column = j
    # Обмен в каждой строке переставляет два столбца целиком.
    for row in matrix:
        row[min_column], row[max_column] = row[max_column], row[min_column]
    print("Результат:")
    for row in matrix:
        print(*row)


if __name__ == "__main__":
    main()
