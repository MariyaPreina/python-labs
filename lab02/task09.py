# Задача 9.
# Дано целое число в диапазоне 100–999. Вывести его строку-описание,
# например: 256 — «двести пятьдесят шесть»,
# 814 — «восемьсот четырнадцать».

number = int(input("Введите целое число от 100 до 999: "))

# Например, для 256 получаем сотни 2, остаток 56, десятки 5, единицы 6.
hundreds = number // 100
remainder = number % 100
tens = remainder // 10
units = remainder % 10

if hundreds == 1:
    text = "сто"
elif hundreds == 2:
    text = "двести"
elif hundreds == 3:
    text = "триста"
elif hundreds == 4:
    text = "четыреста"
elif hundreds == 5:
    text = "пятьсот"
elif hundreds == 6:
    text = "шестьсот"
elif hundreds == 7:
    text = "семьсот"
elif hundreds == 8:
    text = "восемьсот"
elif hundreds == 9:
    text = "девятьсот"

# Числа 10–19 называются целиком, без отдельных названий десятков и единиц.
if 10 <= remainder <= 19:
    if remainder == 10:
        tail = "десять"
    elif remainder == 11:
        tail = "одиннадцать"
    elif remainder == 12:
        tail = "двенадцать"
    elif remainder == 13:
        tail = "тринадцать"
    elif remainder == 14:
        tail = "четырнадцать"
    elif remainder == 15:
        tail = "пятнадцать"
    elif remainder == 16:
        tail = "шестнадцать"
    elif remainder == 17:
        tail = "семнадцать"
    elif remainder == 18:
        tail = "восемнадцать"
    elif remainder == 19:
        tail = "девятнадцать"
    text = text + " " + tail
else:
    if tens == 2:
        tens_text = "двадцать"
    elif tens == 3:
        tens_text = "тридцать"
    elif tens == 4:
        tens_text = "сорок"
    elif tens == 5:
        tens_text = "пятьдесят"
    elif tens == 6:
        tens_text = "шестьдесят"
    elif tens == 7:
        tens_text = "семьдесят"
    elif tens == 8:
        tens_text = "восемьдесят"
    elif tens == 9:
        tens_text = "девяносто"
    if tens >= 2:
        text = text + " " + tens_text

    if units == 1:
        unit_text = "один"
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
        text = text + " " + unit_text

print(text)
