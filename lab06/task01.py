# Задача 1.
# Дана квадратная матрица A порядка M (M нечётное). Начиная с A1,1,
# вывести элементы по спирали против часовой стрелки: первый столбец,
# последняя строка, последний столбец снизу вверх, первая строка справа
# налево и далее внутрь. Последним выводится центральный элемент.


def main():
    m = int(input("Введите количество строк M: "))
    n = m
    if m <= 0:
        print("Размеры должны быть положительными.")
        return
    if m % 2 == 0:
        print("Порядок матрицы должен быть нечётным.")
        return
    matrix = []
    for i in range(m):
        row = list(map(float, input(f"Строка {i + 1} ({n} чисел через пробел): ").split()))
        if len(row) != n:
            print("Количество элементов строки должно быть равно", n)
            return
        matrix.append(row)

    # Четыре границы отделяют ещё не пройденную часть матрицы.
    top, bottom = 0, m - 1
    left, right = 0, n - 1
    result = []
    while left <= right and top <= bottom:
        # Вниз по левому краю, затем убираем этот столбец из области.
        for i in range(top, bottom + 1):
            result.append(matrix[i][left])
        left += 1
        # Вправо по нижнему краю; левый нижний угол уже пройден.
        for j in range(left, right + 1):
            result.append(matrix[bottom][j])
        bottom -= 1
        # Проверки не дают повторно вывести центральный элемент.
        # Вверх по правому краю, если остался непройденный столбец.
        if left <= right:
            for i in range(bottom, top - 1, -1):
                result.append(matrix[i][right])
            right -= 1
        # Влево по верхнему краю, если осталась непройденная строка.
        if top <= bottom:
            for j in range(right, left - 1, -1):
                result.append(matrix[top][j])
            top += 1
    print("Спираль:", *result)


if __name__ == "__main__":
    main()
