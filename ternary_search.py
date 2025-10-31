# Тернарный поиск по отсортированному массиву для поиска конкретного значения.
# Делим диапазон на три части с двумя разделителями m1 и m2.

from typing import List, Optional

def ternary_search(arr: List[int], target: int) -> Optional[int]:
    left, right = 0, len(arr) - 1
    while left <= right:
        third = (right - left) // 3
        m1 = left + third
        m2 = right - third

        if arr[m1] == target:
            return m1
        if arr[m2] == target:
            return m2

        if target < arr[m1]:
            right = m1 - 1       # в левой трети
        elif target > arr[m2]:
            left = m2 + 1        # в правой трети
        else:
            left = m1 + 1        # в средней трети
            right = m2 - 1
    return None

if __name__ == "__main__":
    data = [2, 4, 6, 8, 10, 12, 14]
    print("Ищем 10:", ternary_search(data, 10))  # ожидаем индекс 4
    print("Ищем 5:", ternary_search(data, 5))    # ожидаем None
