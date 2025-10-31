# Сортировка "блинами": единственная операция — переворот префикса массива.
from typing import List

def flip(a: List[int], r: int) -> None:
    """Переворачивает подмассив a[0:r+1] на месте."""
    i, j = 0, r
    while i < j:
        a[i], a[j] = a[j], a[i]
        i += 1
        j -= 1

def find_max_index(a: List[int], end: int) -> int:
    """Ищет индекс максимума в a[0:end+1]."""
    max_i = 0
    for i in range(1, end + 1):
        if a[i] > a[max_i]:
            max_i = i
    return max_i

def pancake_sort(a: List[int]) -> List[int]:
    arr = a[:]  # не портим оригинал
    n = len(arr)
    for curr in range(n - 1, 0, -1):
        max_i = find_max_index(arr, curr)
        if max_i != curr:
            # Шаг 1–2: поднимаем максимум на позицию 0
            flip(arr, max_i)
            # Шаг 3: кидаем максимум на позицию curr
            flip(arr, curr)
    return arr

if __name__ == "__main__":
    data = [3, 6, 1, 10, 2, 7]
    print("Исходный:", data)
    print("Отсортированный:", pancake_sort(data))
