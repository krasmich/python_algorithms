import sys
import random
from random import randint, seed
"""
1. Подсчитать, сколько было выделено памяти под переменные в ранее разработанных
программах в рамках первых трех уроков. Проанализировать результат и определить
программы с наиболее эффективным использованием памяти.

Примечание: Для анализа возьмите любые 1-3 ваших программы или несколько вариантов кода для
одной и той же задачи. Результаты анализа вставьте в виде комментариев к коду. Также укажите в
комментариях версию Python и разрядность вашей ОС.
"""

print(f"Версия Python и разрядность ОС: {sys.version}")
# Версия Python и разрядность ОС: 3.9.6 (tags/v3.9.6:db3ff76, Jun 28 2021, 15:26:21) [MSC v.1929 64 bit (AMD64)]

# Рассмотрим 2-ое задание 3 урока:

# Во втором массиве сохранить индексы четных элементов первого массива. Например, если
# дан массив со значениями 8, 3, 15, 6, 4, 2, то во второй массив надо заполнить значениями 1,
# 4, 5, 6 (или 0, 3, 4, 5 - если индексация начинается с нуля), т.к. именно в этих позициях первого
# массива стоят четные числа.

# Мое решение
random_numbers = [random.randrange(1, 50, 1) for i in range(6)]
even_index = []


for n in random_numbers:
    if n % 2 == 0:
        even_index.append(random_numbers.index(n))

print(random_numbers, even_index)

# Решение преподавателя
seed(42)
init_list = [randint(0, 100) for _ in range(10)]
a = [i for i, item in enumerate(init_list) if item % 2 == 0]

print(init_list, a)


print(f"Сколько выделено памяти под переменные в моем решении: "
      f"{sys.getsizeof(random_numbers)} и {sys.getsizeof(even_index)}")
print(f"Сколько выделено памяти под переменные в решении преподавателя: "
      f"{sys.getsizeof(init_list)} и {sys.getsizeof(a)}")

# Сколько выделено памяти под переменные в моем решении: 120 и 88
# Сколько выделено памяти под переменные в решении преподавателя: 184 и 88

# Итог: как можно видеть мое решение несколько эффективнее с точки зрения использования памяти
