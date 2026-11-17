// Задача 1. Построить бинарное дерево поиска, найти число и выполнить обход.
class Node {
    constructor(value) {
        this.value = value;
        this.left = null;
        this.right = null;
    }
}

function insert(root, value) {
    // Дошли до пустого места — создаём узел для связи с родителем.
    if (root === null) return new Node(value);
    if (value < root.value) {
        root.left = insert(root.left, value);
    } else {
        // Большие и равные значения добавляем справа.
        root.right = insert(root.right, value);
    }
    return root;
}

function search(root, value) {
    // Пустая ветка означает, что число не найдено.
    if (root === null || root.value === value) return root;
    if (value < root.value) return search(root.left, value);
    return search(root.right, value);
}

function inorderTraversal(root) {
    if (root === null) return;
    // Левое поддерево, сам узел, правое поддерево — значения по возрастанию.
    inorderTraversal(root.left);
    console.log(root.value);
    inorderTraversal(root.right);
}
