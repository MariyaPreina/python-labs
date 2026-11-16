# Задача 9.
# Дана матрица M x N. Упорядочить строки так, чтобы их первые
# элементы образовывали возрастающую последовательность.


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

    # Перемещаются целые строки; порядок чисел внутри каждой сохраняется.
    matrix.sort(key=lambda row: row[0])
    print("Результат:")
    for row in matrix:
        print(*row)


if __name__ == "__main__":
    main()
