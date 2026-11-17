// Задача 8. Обмен верхней левой и нижней правой четвертей на месте. Оба размера чётные.
function swapQuarters(matrix) {
    const halfRows = matrix.length / 2;
    const halfColumns = matrix[0].length / 2;
    // Обходим только одну четверть, иначе поменяем пары обратно.
    for (let i = 0; i < halfRows; i++) {
        for (let j = 0; j < halfColumns; j++) {
            const otherI = i + halfRows;
            const otherJ = j + halfColumns;
            [matrix[i][j], matrix[otherI][otherJ]] =
                [matrix[otherI][otherJ], matrix[i][j]];
        }
    }
}
