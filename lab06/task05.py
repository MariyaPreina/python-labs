# Задача 5.
# Дана целочисленная матрица M x N. Найти номер первого столбца,
# содержащего только нечётные числа. Если такого столбца нет, вывести 0.


def main():
    m = int(input("Введите количество строк M: "))
    n = int(input("Введите количество столбцов N: "))
    if m <= 0 or n <= 0:
        print("Размеры должны быть положительными.")
        return
    matrix = []
    for i in range(m):
        row = list(map(int, input(f"Строка {i + 1} ({n} чисел через пробел): ").split()))
        if len(row) != n:
            print("Количество элементов строки должно быть равно", n)
            return
        matrix.append(row)

    column_number = 0
    for j in range(n):
        all_odd = True
        for i in range(m):
            # Одного чётного числа достаточно, чтобы отклонить весь столбец.
            if matrix[i][j] % 2 == 0:
                all_odd = False
                break
        # Если проверка пройдена, это первый подходящий столбец слева.
        if all_odd:
            column_number = j + 1
            break
    print("Номер столбца:", column_number)


if __name__ == "__main__":
    main()
