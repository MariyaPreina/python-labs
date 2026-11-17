// Задача 6. Поменять минимум и максимум в каждой строке. Изменяет исходную матрицу.
function swapRowMinMax(matrix) {
    for (const row of matrix) {
        let minIndex = 0;
        let maxIndex = 0;
        for (let j = 1; j < row.length; j++) {
            if (row[j] < row[minIndex]) minIndex = j;
            if (row[j] > row[maxIndex]) maxIndex = j;
        }
        // Меняем после поиска; при повторениях выбраны первые минимум и максимум.
        [row[minIndex], row[maxIndex]] = [row[maxIndex], row[minIndex]];
    }
}
