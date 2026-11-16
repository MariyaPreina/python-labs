# Задача 5.
# Дано целое число. Вывести его строку-описание вида
# «отрицательное четное число», «нулевое число»,
# «положительное нечетное число» и т. д.

number = int(input("Введите целое число: "))

if number == 0:
    description = "нулевое число"
else:
    if number > 0:
        sign = "положительное"
    else:
        sign = "отрицательное"

    if number % 2 == 0:
        parity = "четное"
    else:
        parity = "нечетное"

    description = sign + " " + parity + " число"

print(description)
