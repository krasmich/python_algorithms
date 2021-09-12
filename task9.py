"""
9. Найти максимальный элемент среди минимальных элементов столбцов матрицы.
"""
import random

size = 4
matrix = [[random.randint(0, 100) for _ in range(size)] for _ in range(size)]

for row in matrix:
    print(*row, sep='\t')

max_el = matrix[0][0]

for j in range(size):
    min_el = matrix[0][j]

    for i in range(size):
        if matrix[i][j] < min_el:
            min_el = matrix[i][j]

    if min_el > max_el:
        max_el = min_el

print(f'максмиальный элемент среди минимальных: {max_el}')
