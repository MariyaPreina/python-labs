// Задача 3. Номер столбца с минимальным произведением и само произведение.
function minProductColumn(matrix) {
    let minProduct = null;
    let columnNumber = 0;
    for (let j = 0; j < matrix[0].length; j++) {
        let product = 1;
        for (let i = 0; i < matrix.length; i++) product *= matrix[i][j];
        // Первый столбец задаёт минимум; при равенстве сохраняем первый найденный.
        if (minProduct === null || product < minProduct) {
            minProduct = product;
            columnNumber = j + 1;
        }
    }
    return { columnNumber, minProduct };
}
