// Задача 1. Реализовать сортировку вставками по возрастанию.
function insertionSort(numbers) {
    // Слева от i элементы уже отсортированы.
    for (let i = 1; i < numbers.length; i++) {
        const current = numbers[i];
        let j = i - 1;
        // Сдвигаем большие числа вправо, сохраняя current отдельно.
        while (j >= 0 && numbers[j] > current) {
            numbers[j + 1] = numbers[j];
            j--;
        }
        // j остановился перед местом вставки; при j = -1 вставляем в начало.
        numbers[j + 1] = current;
    }
}
