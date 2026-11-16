# Задача 1.
# Дано вещественное число — цена 1 кг конфет.
# Вывести стоимость 0.1, 0.2, …, 1 кг конфет.

price = float(input("Введите цену 1 кг конфет: "))

i = 1
while i <= 10:
    weight = i / 10
    cost = price * weight
    print(f"{weight:.1f} кг: {cost:.2f} руб.")
    i = i + 1
