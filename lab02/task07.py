# Задача 7.
# Дан номер дня — целое число от 1 до 31 и месяца — целое число
# от 1 до 12 (1 — январь, 2 — февраль и т. д.).
# Вывести дату в виде текста (например, «пятое января»).

day = int(input("Введите день (1–31): "))
month = int(input("Введите месяц (1–12): "))

if not (1 <= day <= 31 and 1 <= month <= 12):
    print("День должен быть от 1 до 31, месяц — от 1 до 12.")
else:
    if day == 1:
        day_text = "первое"
    elif day == 2:
        day_text = "второе"
    elif day == 3:
        day_text = "третье"
    elif day == 4:
        day_text = "четвертое"
    elif day == 5:
        day_text = "пятое"
    elif day == 6:
        day_text = "шестое"
    elif day == 7:
        day_text = "седьмое"
    elif day == 8:
        day_text = "восьмое"
    elif day == 9:
        day_text = "девятое"
    elif day == 10:
        day_text = "десятое"
    elif day == 11:
        day_text = "одиннадцатое"
    elif day == 12:
        day_text = "двенадцатое"
    elif day == 13:
        day_text = "тринадцатое"
    elif day == 14:
        day_text = "четырнадцатое"
    elif day == 15:
        day_text = "пятнадцатое"
    elif day == 16:
        day_text = "шестнадцатое"
    elif day == 17:
        day_text = "семнадцатое"
    elif day == 18:
        day_text = "восемнадцатое"
    elif day == 19:
        day_text = "девятнадцатое"
    elif day == 20:
        day_text = "двадцатое"
    elif day == 21:
        day_text = "двадцать первое"
    elif day == 22:
        day_text = "двадцать второе"
    elif day == 23:
        day_text = "двадцать третье"
    elif day == 24:
        day_text = "двадцать четвертое"
    elif day == 25:
        day_text = "двадцать пятое"
    elif day == 26:
        day_text = "двадцать шестое"
    elif day == 27:
        day_text = "двадцать седьмое"
    elif day == 28:
        day_text = "двадцать восьмое"
    elif day == 29:
        day_text = "двадцать девятое"
    elif day == 30:
        day_text = "тридцатое"
    elif day == 31:
        day_text = "тридцать первое"

    if month == 1:
        month_text = "января"
    elif month == 2:
        month_text = "февраля"
    elif month == 3:
        month_text = "марта"
    elif month == 4:
        month_text = "апреля"
    elif month == 5:
        month_text = "мая"
    elif month == 6:
        month_text = "июня"
    elif month == 7:
        month_text = "июля"
    elif month == 8:
        month_text = "августа"
    elif month == 9:
        month_text = "сентября"
    elif month == 10:
        month_text = "октября"
    elif month == 11:
        month_text = "ноября"
    elif month == 12:
        month_text = "декабря"

    print(day_text + " " + month_text)
