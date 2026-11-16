# Задача 3.
# Дана матрица M x N. Найти номер столбца с наименьшим
# произведением элементов и вывести номер и произведение.


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

    min_product = None
    column_number = 0
    for j in range(n):
        product = 1
        for i in range(m):
            product *= matrix[i][j]
        # Первый столбец задаёт исходный минимум; ноль для этого не подходит.
        if min_product is None or product < min_product:
            min_product = product
            column_number = j + 1
    print("Номер столбца:", column_number)
    print("Наименьшее произведение:", min_product)


if __name__ == "__main__":
    main()
