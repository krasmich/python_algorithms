"""
6. В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
Сами минимальный и максимальный элементы в сумму не включать.
"""

from random import randint


arr = [randint(-10, 10) for _ in range(10)]
print(arr)
min_number = arr.index(min(arr))
max_number = arr.index(max(arr))

if min_number < max_number:
    print(sum(arr[min_number + 1: max_number]))
else:
    print(sum(arr[max_number + 1: min_number]))
