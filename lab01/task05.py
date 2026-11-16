# Задача 5.
# Даны два ненулевых числа.
# Найти сумму, разность, произведение и частное их модулей.

a = float(input("Введите ненулевое число a: "))
b = float(input("Введите ненулевое число b: "))

a_abs = abs(a)
b_abs = abs(b)
total = a_abs + b_abs
difference = a_abs - b_abs
product = a_abs * b_abs
quotient = a_abs / b_abs

print("Сумма модулей:", total)
print("Разность модулей:", difference)
print("Произведение модулей:", product)
print("Частное модулей:", quotient)
