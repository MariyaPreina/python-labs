// Очередь FIFO: первый добавленный элемент извлекается первым.
// Для учебного примера используем массив; shift имеет сложность O(n).
class Queue {
    constructor() {
        this.items = [];
    }

    enqueue(value) {
        this.items.push(value); // Добавляем в конец.
    }

    dequeue() {
        return this.items.shift(); // Удаляем первый; для пустой очереди — undefined.
    }

    peek() {
        return this.items[0]; // Первый элемент без удаления.
    }

    isEmpty() {
        return this.items.length === 0;
    }

    size() {
        return this.items.length;
    }

    contains(value) {
        return this.items.includes(value);
    }

    toArray() {
        return [...this.items]; // Копия элементов в порядке очереди.
    }

    clear() {
        this.items.length = 0;
    }
}
