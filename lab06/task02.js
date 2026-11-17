// Задача 2. Сумма и произведение K-й строки; k — номер от 1 до числа строк.
function rowSumAndProduct(matrix, k) {
    let total = 0;
    let product = 1;
    // Номеру k соответствует индекс k - 1.
    for (const value of matrix[k - 1]) {
        total += value;
        product *= value;
    }
    return { total, product };
}
