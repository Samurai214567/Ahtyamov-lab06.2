# Блочная (bucket) сортировка для вещественных чисел в диапазоне [0, 1).
from typing import List

def bucket_sort(arr: List[float]) -> List[float]:

    n = len(arr)
    if n <= 1:
        return arr[:]

    # 1) Кол-во корзин обычно берут около n
    k = n

    # 2) Создаём пустые корзины
    buckets: List[List[float]] = [[] for _ in range(k)]

    # 3) Функция распределения для диапазона [0,1)
    for x in arr:
        if x < 0 or x >= 1:
            raise ValueError("Для простоты пример ожидает числа в [0,1). Масштабируйте данные при необходимости.")
        idx = min(k - 1, int(x * k))  # индекс корзины
        buckets[idx].append(x)

    # 4) Сортируем каждую корзину (используем встроенную сортировку Python)
    for b in buckets:
        b.sort()

    # 5) Сливаем результаты
    result: List[float] = []
    for b in buckets:
        result.extend(b)
    return result


if __name__ == "__main__":
    data = [0.78, 0.17, 0.39, 0.26, 0.72, 0.94, 0.21, 0.12, 0.23, 0.68]
    print("Исходный:", data)
    print("Отсортированный:", bucket_sort(data))
