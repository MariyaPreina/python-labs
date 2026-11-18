# Задача 1.
# Используя словесное описание, реализовать обход дерева.
# Бинарное дерево поиска, вставка, поиск и
# симметричный обход (левое поддерево, узел, правое поддерево).


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def insert(root, value):
    # Пустое место найдено: возвращаем новый узел для связи с родителем.
    if root is None:
        return Node(value)
    if value < root.value:
        # Меньшие значения идут влево; сохраняем возвращённый корень поддерева.
        root.left = insert(root.left, value)
    else:
        # Равные значения тоже сохраняем — в правом поддереве.
        root.right = insert(root.right, value)
    return root


def search(root, value):
    # None означает, что дошли до пустой ветки и значение не найдено.
    if root is None or root.value == value:
        return root
    # Благодаря порядку значений достаточно искать только в одном поддереве.
    if value < root.value:
        return search(root.left, value)
    return search(root.right, value)


def inorder_traversal(root):
    if root is None:
        return
    # Сначала меньшие значения слева, затем текущий узел, затем большие или равные.
    inorder_traversal(root.left)
    print(root.value, end=" ")
    inorder_traversal(root.right)


def show_tree(root, level=0, label="Корень"):
    # Отступ показывает глубину, подпись — связь с родителем.
    if root is None:
        return
    print("    " * level + f"{label}: {root.value}")
    show_tree(root.left, level + 1, "Слева")
    show_tree(root.right, level + 1, "Справа")


if __name__ == "__main__":
    tree = None
    values = list(map(int, input("Введите целые числа для дерева через пробел: ").split()))
    for value in values:
        # Присваивание сохраняет корень, в том числе при первой вставке.
        tree = insert(tree, value)

    print("\nДерево (отступы показывают вложенность):")
    show_tree(tree)
    if tree is None:
        print("Дерево пустое.")

    target = int(input("Введите искомое число: "))
    result = search(tree, target)
    if result is not None:
        print("Элемент найден:", result.value)
    else:
        print("Элемент не найден:", target)

    print("\nОбход: левое поддерево → узел → правое поддерево")
    print("Числа по возрастанию:", end=" ")
    inorder_traversal(tree)
    print()
