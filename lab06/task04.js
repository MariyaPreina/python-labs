// Задача 4. Количество элементов выше среднего в каждом столбце.
function countAboveAverage(matrix) {
    const result = [];
    for (let j = 0; j < matrix[0].length; j++) {
        let total = 0;
        for (let i = 0; i < matrix.length; i++) total += matrix[i][j];
        const average = total / matrix.length;
        let count = 0;
        // Второй проход: теперь среднее известно и можно сравнивать.
        for (let i = 0; i < matrix.length; i++) {
            if (matrix[i][j] > average) count++;
        }
        result.push(count);
    }
    return result;
}
