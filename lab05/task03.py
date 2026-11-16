# Задача 3.
# Даны целые N > 2, A и B. Сформировать целочисленный массив размера N:
# первый элемент A, второй B, каждый следующий — сумма всех предыдущих.


n = int(input("Введите N (> 2): "))
a = int(input("Введите A: "))
b = int(input("Введите B: "))
if n <= 2:
    print("N должно быть больше 2.")
else:
    numbers = [a, b]
    total = a + b
    for i in range(2, n):
        # total уже содержит сумму всех ранее добавленных элементов.
        numbers.append(total)
        total = total + numbers[-1]
    print("Массив:", numbers)
