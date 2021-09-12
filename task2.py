"""
2. Во втором массиве сохранить индексы четных элементов первого массива. Например, если
дан массив со значениями 8, 3, 15, 6, 4, 2, то во второй массив надо заполнить значениями 1,
4, 5, 6 (или 0, 3, 4, 5 - если индексация начинается с нуля), т.к. именно в этих позициях первого
массива стоят четные числа.
"""

import random

random_numbers = [random.randrange(1, 50, 1) for i in range(6)]
even_index = []


for n in random_numbers:
    if n % 2 == 0:
        even_index.append(random_numbers.index(n))

print(even_index)

