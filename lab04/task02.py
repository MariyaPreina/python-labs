# Задача 2.
# Числа Фибоначчи: написать функцию, которая рекурсивно
# вычисляет n-е число Фибоначчи.


def fibonacci(n, memo=None):
    # Во все вложенные вызовы передаётся один и тот же словарь.
    if memo is None:
        memo = {0: 0, 1: 1}
    # Каждое число вычисляем только один раз, затем берём готовое значение.
    if n not in memo:
        memo[n] = fibonacci(n - 1, memo) + fibonacci(n - 2, memo)
    return memo[n]

if __name__ == "__main__":
    n = int(input("Введите номер n (>= 0): "))
    if n < 0:
        print("n должно быть неотрицательным.")
    else:
        print("Число Фибоначчи:", fibonacci(n))
