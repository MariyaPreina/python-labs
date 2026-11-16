# Задача 8.
# Дано целое число в диапазоне 10–40, определяющее количество
# учебных заданий. Вывести строку-описание, обеспечив правильное
# согласование со словами «учебное задание», например:
# 18 — «восемнадцать учебных заданий».

number = int(input("Введите количество заданий (10–40): "))

if number == 10:
    number_text = "десять"
elif number == 11:
    number_text = "одиннадцать"
elif number == 12:
    number_text = "двенадцать"
elif number == 13:
    number_text = "тринадцать"
elif number == 14:
    number_text = "четырнадцать"
elif number == 15:
    number_text = "пятнадцать"
elif number == 16:
    number_text = "шестнадцать"
elif number == 17:
    number_text = "семнадцать"
elif number == 18:
    number_text = "восемнадцать"
elif number == 19:
    number_text = "девятнадцать"
else:
    tens = number // 10
    units = number % 10
    if tens == 2:
        number_text = "двадцать"
    elif tens == 3:
        number_text = "тридцать"
    else:
        number_text = "сорок"

    if units == 1:
        unit_text = "одно"
    elif units == 2:
        unit_text = "два"
    elif units == 3:
        unit_text = "три"
    elif units == 4:
        unit_text = "четыре"
    elif units == 5:
        unit_text = "пять"
    elif units == 6:
        unit_text = "шесть"
    elif units == 7:
        unit_text = "семь"
    elif units == 8:
        unit_text = "восемь"
    elif units == 9:
        unit_text = "девять"
    if units != 0:
        number_text = number_text + " " + unit_text

# У 11–14 особое окончание, поэтому проверяем их раньше последней цифры.
if 11 <= number <= 14:
    ending = "учебных заданий"
elif number % 10 == 1:
    ending = "учебное задание"
elif 2 <= number % 10 <= 4:
    ending = "учебных задания"
else:
    ending = "учебных заданий"

print(number_text + " " + ending)
