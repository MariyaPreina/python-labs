# Задача 4.
# Дана матрица M x N. В каждом столбце найти количество элементов,
# больших среднего арифметического всех элементов этого столбца.


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

    for j in range(n):
        total = 0
        for i in range(m):
            total += matrix[i][j]
        average = total / m
        count = 0
        # Среднее известно только после первого прохода по столбцу.
        for i in range(m):
            if matrix[i][j] > average:
                count += 1
        print("Столбец", j + 1, "— количество:", count)


if __name__ == "__main__":
    main()
