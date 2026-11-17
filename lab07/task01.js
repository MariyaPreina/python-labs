// Задача 1. Реализовать сортировку пузырьком по возрастанию.
function bubbleSort(numbers) {
    // После прохода максимум оказывается на позиции end.
    for (let end = numbers.length - 1; end > 0; end--) {
        let swapped = false;
        for (let i = 0; i < end; i++) {
            if (numbers[i] > numbers[i + 1]) {
                [numbers[i], numbers[i + 1]] = [numbers[i + 1], numbers[i]];
                swapped = true;
            }
        }
        // Ни одного обмена за проход — весь массив уже отсортирован.
        if (!swapped) break;
    }
}
