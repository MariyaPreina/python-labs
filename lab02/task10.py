# Задача 10.
# В восточном календаре принят 60-летний цикл, состоящий из
# 12-летних подциклов цветов: зеленый, красный, желтый, белый и черный.
# В каждом подцикле годы носят названия животных: крысы, коровы, тигра,
# зайца, дракона, змеи, лошади, овцы, обезьяны, курицы, собаки и свиньи.
# По номеру года определить его название, если 1984 год — начало цикла:
# «год зеленой крысы».

year = int(input("Введите номер года: "))

# По условию: цвет меняется раз в 12 лет, полный цикл длится 60 лет.
cycle_year = (year - 1984) % 60
color_index = cycle_year // 12
animal_index = cycle_year % 12

if animal_index == 0:
    animal = "крысы"
elif animal_index == 1:
    animal = "коровы"
elif animal_index == 2:
    animal = "тигра"
elif animal_index == 3:
    animal = "зайца"
elif animal_index == 4:
    animal = "дракона"
elif animal_index == 5:
    animal = "змеи"
elif animal_index == 6:
    animal = "лошади"
elif animal_index == 7:
    animal = "овцы"
elif animal_index == 8:
    animal = "обезьяны"
elif animal_index == 9:
    animal = "курицы"
elif animal_index == 10:
    animal = "собаки"
elif animal_index == 11:
    animal = "свиньи"

# Тигр, заяц и дракон требуют формы «зеленого», остальные — «зеленой».
if animal_index == 2 or animal_index == 3 or animal_index == 4:
    if color_index == 0:
        color = "зеленого"
    elif color_index == 1:
        color = "красного"
    elif color_index == 2:
        color = "желтого"
    elif color_index == 3:
        color = "белого"
    elif color_index == 4:
        color = "черного"
else:
    if color_index == 0:
        color = "зеленой"
    elif color_index == 1:
        color = "красной"
    elif color_index == 2:
        color = "желтой"
    elif color_index == 3:
        color = "белой"
    elif color_index == 4:
        color = "черной"

print("год " + color + " " + animal)
