# Задача 2.
# Дано целое N > 1, первый член A и знаменатель D геометрической
# прогрессии. Сформировать и вывести N членов: A, A*D, A*D**2, ... .


n = int(input("Введите N (> 1): "))
a = float(input("Введите первый член A: "))
d = float(input("Введите знаменатель D: "))
if n <= 1:
    print("N должно быть больше 1.")
else:
    numbers = []
    current = a
    for i in range(n):
        numbers.append(current)
        current = current * d
    print("Массив:", numbers)
