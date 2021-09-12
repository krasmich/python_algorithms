"""
5. В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и
позицию (индекс) в массиве.
"""
from random import randint

arr = [randint(-10, 10) for _ in range(10)]
print(arr)

i = 0
index = -1
while i < len(arr):
    if arr[i] < 0 and index == -1:
        index = i
    elif arr[i] < 0 and arr[i] > arr[index]:
        index = i
    i += 1

print(f'максимальный отрицательный элемент {arr[index]} находится на {index+1} позиции')
