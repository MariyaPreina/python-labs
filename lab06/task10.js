// Задача 10. Суммы диагоналей квадратной матрицы, параллельных главной (включая её).
function diagonalSums(matrix) {
    const m = matrix.length;
    const result = [];
    // offset = j - i: идём от нижнего левого угла к верхнему правому.
    for (let offset = -(m - 1); offset < m; offset++) {
        let total = 0;
        // Начало диагонали лежит в первом столбце или первой строке.
        let i = Math.max(0, -offset);
        let j = Math.max(0, offset);
        while (i < m && j < m) {
            total += matrix[i][j];
            i++;
            j++;
        }
        result.push({ offset, total }); // offset === 0 — главная диагональ.
    }
    return result;
}
