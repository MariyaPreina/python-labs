// Задача 1. Реализовать бинарный поиск в заранее отсортированном массиве.
// Результат — индекс с нуля, либо -1, если элемента нет.
function binarySearch(numbers, target) {
    let left = 0;
    let right = numbers.length - 1;
    while (left <= right) {
        // Math.floor округляет вниз: аналог // 2 для этих индексов в Python.
        const middle = Math.floor((left + right) / 2);
        if (numbers[middle] === target) return middle;
        // Проверенную середину исключаем вместе с неподходящей половиной.
        if (numbers[middle] > target) {
            right = middle - 1;
        } else {
            left = middle + 1;
        }
    }
    return -1;
}
