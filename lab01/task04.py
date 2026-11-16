# Задача 4.
# Даны два ненулевых числа.
# Найти сумму, разность, произведение и частное их квадратов.

a = float(input("Введите ненулевое число a: "))
b = float(input("Введите ненулевое число b: "))

a_squared = a ** 2
b_squared = b ** 2
total = a_squared + b_squared
difference = a_squared - b_squared
product = a_squared * b_squared
quotient = a_squared / b_squared

print("Сумма квадратов:", total)
print("Разность квадратов:", difference)
print("Произведение квадратов:", product)
print("Частное квадратов:", quotient)
