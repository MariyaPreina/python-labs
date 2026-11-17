// Задача 1. Обход квадратной матрицы нечётного порядка по спирали против часовой стрелки.
function spiral(matrix) {
    let top = 0, bottom = matrix.length - 1;
    let left = 0, right = matrix.length - 1;
    const result = [];
    while (left <= right && top <= bottom) {
        // Вниз по левому краю; затем исключаем пройденный столбец.
        for (let i = top; i <= bottom; i++) result.push(matrix[i][left]);
        left++;
        // Вправо по нижнему краю.
        for (let j = left; j <= right; j++) result.push(matrix[bottom][j]);
        bottom--;
        // Проверки границ предотвращают повторное добавление центра.
        if (left <= right) {
            for (let i = bottom; i >= top; i--) result.push(matrix[i][right]);
            right--;
        }
        if (top <= bottom) {
            for (let j = right; j >= left; j--) result.push(matrix[top][j]);
            top++;
        }
    }
    return result;
}
