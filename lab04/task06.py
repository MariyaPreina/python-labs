# Задача 6.
# Обратный порядок слов: написать функцию, которая рекурсивно
# меняет порядок слов в заданной строке на обратный.


def reverse_words(text):
    # Делим на первое слово и весь остаток строки, а не на все слова сразу.
    parts = text.split(maxsplit=1)
    if len(parts) == 0:
        return ""
    if len(parts) == 1:
        return parts[0]
    # Сначала разворачиваем остаток, затем приписываем первое слово в конец.
    return reverse_words(parts[1]) + " " + parts[0]


if __name__ == "__main__":
    text = input("Введите строку: ")
    print("Обратный порядок слов:", reverse_words(text.strip()))
