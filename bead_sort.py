# Bead/Gravity sort — работает только для неотрицательных целых.
from typing import List

def bead_sort(a: List[int]) -> List[int]:
    if not a:
        return []
    if any(x < 0 for x in a):
        raise ValueError("Bead sort поддерживает только неотрицательные целые числа.")
    if max(a) == 0:
        return a[:]

    max_val = max(a)

    # 1) Формируем 'решётку' бусин (rows x max_val), где True = бусина
    grid = [[False] * max_val for _ in a]
    for i, val in enumerate(a):
        for j in range(val):
            grid[i][j] = True

    # 2) "Гравитация": для каждого столбца считаем, сколько бусин, и «опускаем» их вниз
    for j in range(max_val):
        count = sum(grid[i][j] for i in range(len(a)))  # сколько бусин в столбце j
        # Снизу count True, сверху False
        for i in range(len(a) - 1, -1, -1):
            grid[i][j] = count > 0
            count -= 1

    # 3) Считываем длины рядов (кол-во True подряд слева)
    res = []
    for i in range(len(a)):
        val = 0
        for j in range(max_val):
            if grid[i][j]:
                val += 1
            else:
                break
        res.append(val)

    return res

if __name__ == "__main__":
    data = [5, 3, 1, 7, 4]
    print("Исходный:", data)
    print("Отсортированный:", bead_sort(data))
