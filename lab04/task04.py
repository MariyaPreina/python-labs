# Задача 4.
# Палиндром: написать функцию, которая рекурсивно проверяет,
# является ли заданная строка палиндромом.


def is_palindrome(text, left=0, right=None):
    if right is None:
        right = len(text) - 1
    # Границы встретились или пересеклись: все пары символов совпали.
    if left >= right:
        return True
    if text[left] != text[right]:
        return False
    # Сдвигаем границы к середине, не создавая копий строки.
    return is_palindrome(text, left + 1, right - 1)

if __name__ == "__main__":
    text = input("Введите строку: ")
    if is_palindrome(text):
        print("Строка является палиндромом.")
    else:
        print("Строка не является палиндромом.")
