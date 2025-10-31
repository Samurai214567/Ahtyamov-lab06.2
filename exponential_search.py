# Сначала быстро расширяем диапазон экспоненциально (1,2,4,8,...) пока не "перешагнём" цель,
# потом двоичный поиск на найденном отрезке.

from typing import List, Optional

def binary_search_range(arr: List[int], left: int, right: int, target: int) -> Optional[int]:
    """Обычный бинарный поиск на полуинтервале [left, right]."""
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        if arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return None

def exponential_search(arr: List[int], target: int) -> Optional[int]:
    n = len(arr)
    if n == 0:
        return None
    if arr[0] == target:
        return 0

    i = 1
    # Экспоненциальное расширение
    while i < n and arr[i] < target:
        i *= 2

    left = i // 2
    right = min(i, n - 1)
    return binary_search_range(arr, left, right, target)

if __name__ == "__main__":
    data = [1, 2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
    print("Ищем 17:", exponential_search(data, 17))  # ожидаем индекс 7
    print("Ищем 4:", exponential_search(data, 4))    # ожидаем None
