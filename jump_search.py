# Требуется отсортированный массив. Идём скачками длиной m = floor(sqrt(n)),
# затем делаем линейный поиск внутри найденного блока.

import math
from typing import List, Optional

def jump_search(arr: List[int], target: int) -> Optional[int]:
    n = len(arr)
    if n == 0:
        return None

    m = int(math.sqrt(n))
    # Фаза прыжков
    prev, curr = 0, 0
    while curr < n and arr[curr] < target:
        prev = curr
        curr += m
    # Линейная проверка в блоке [prev..min(curr, n-1)]
    end = min(curr, n - 1)
    for i in range(prev, end + 1):
        if arr[i] == target:
            return i
    return None

if __name__ == "__main__":
    data = [1, 3, 5, 7, 9, 12, 15, 18, 21]
    print("Ищем 12:", jump_search(data, 12))  # ожидаем индекс 5
    print("Ищем 4:", jump_search(data, 4))    # ожидаем None
