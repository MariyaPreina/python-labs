// Задача 7. Обмен столбцов с минимумом и максимумом всей матрицы. Изменяет её на месте.
function swapMinMaxColumns(matrix) {
    let minValue = matrix[0][0], maxValue = matrix[0][0];
    let minColumn = 0, maxColumn = 0;
    for (let i = 0; i < matrix.length; i++) {
        for (let j = 0; j < matrix[i].length; j++) {
            if (matrix[i][j] < minValue) {
                minValue = matrix[i][j];
                minColumn = j;
            }
            if (matrix[i][j] > maxValue) {
                maxValue = matrix[i][j];
                maxColumn = j;
            }
        }
    }
    // Перестановка двух элементов в каждой строке меняет столбцы целиком.
    for (const row of matrix) {
        [row[minColumn], row[maxColumn]] = [row[maxColumn], row[minColumn]];
    }
}
