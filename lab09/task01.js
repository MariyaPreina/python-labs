// Задача 1. Реализовать сортировку выбором по возрастанию.
function selectionSort(numbers) {
    for (let i = 0; i < numbers.length - 1; i++) {
        let minIndex = i;
        // Ищем индекс минимума в оставшейся части массива.
        for (let j = i + 1; j < numbers.length; j++) {
            if (numbers[j] < numbers[minIndex]) minIndex = j;
        }
        // Ставим найденный минимум на позицию i.
        if (minIndex !== i) {
            [numbers[i], numbers[minIndex]] = [numbers[minIndex], numbers[i]];
        }
    }
}
