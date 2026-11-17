// Задача 5. Номер первого столбца только с нечётными числами, либо 0.
function firstOddColumn(matrix) {
    for (let j = 0; j < matrix[0].length; j++) {
        let allOdd = true;
        for (let i = 0; i < matrix.length; i++) {
            // Одного чётного числа достаточно, чтобы отклонить столбец.
            if (matrix[i][j] % 2 === 0) {
                allOdd = false;
                break;
            }
        }
        if (allOdd) return j + 1;
    }
    return 0;
}
