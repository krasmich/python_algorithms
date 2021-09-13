"""
1. Проанализировать скорость и сложность одного любого алгоритма,
разработанных в рамках домашнего задания первых трех уроков.
"""

# в качестве примера взято 4 задание из 3 урока (Определить, какое число в массиве встречается чаще всего)
# функция mostfrequent реализует алгоритм, который сделал я
# функция teacher_algorithm реализует алгоритм, который сделал преподаватель

import cProfile
import random
from random import randint
from collections import Counter


def mostfrequent(arr, n):
    arr.sort()

    max_count = 1
    res = arr[0]
    curr_count = 1

    for i in range(1, n):
        if (arr[i] == arr[i - 1]):
            curr_count += 1

        else:
            if (curr_count > max_count):
                max_count = curr_count
                res = arr[i - 1]

            curr_count = 1

    if (curr_count > max_count):
        max_count = curr_count
        res = arr[n - 1]

    return res


arr = [random.randrange(1, 100000, 1) for i in range(100000)]
n = len(arr)
print(mostfrequent(arr, n))


def teacher_algorithm(size):
    init_list = [randint(0, 100000) for _ in range(size)]
    return Counter(init_list).most_common(1)


print(teacher_algorithm(100000))

cProfile.run('mostfrequent(arr, n)')
cProfile.run('teacher_algorithm(n)')

   #       5 function calls in 0.012 seconds
   #
   # Ordered by: standard name
   #
   # ncalls  tottime  percall  cumtime  percall filename:lineno(function)
   #      1    0.000    0.000    0.012    0.012 <string>:1(<module>)
   #      1    0.011    0.011    0.012    0.012 task1.py:16(mostfrequent)
   #      1    0.000    0.000    0.012    0.012 {built-in method builtins.exec}
   #      1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
   #      1    0.001    0.001    0.001    0.001 {method 'sort' of 'list' objects}
   #
   #
   #       531168 function calls (531156 primitive calls) in 0.166 seconds
   #
   # Ordered by: standard name
   #
   # ncalls  tottime  percall  cumtime  percall filename:lineno(function)
   #      1    0.001    0.001    0.166    0.166 <string>:1(<module>)
   #      1    0.000    0.000    0.007    0.007 __init__.py:581(__init__)
   #      1    0.000    0.000    0.003    0.003 __init__.py:600(most_common)
   #      1    0.000    0.000    0.007    0.007 __init__.py:649(update)
   #      7    0.000    0.000    0.000    0.000 _collections_abc.py:409(__subclasshook__)
   #      1    0.000    0.000    0.000    0.000 abc.py:117(__instancecheck__)
   #    7/1    0.000    0.000    0.000    0.000 abc.py:121(__subclasscheck__)
   #      1    0.000    0.000    0.003    0.003 heapq.py:521(nlargest)
   # 100000    0.038    0.000    0.056    0.000 random.py:237(_randbelow_with_getrandbits)
   # 100000    0.052    0.000    0.108    0.000 random.py:290(randrange)
   # 100000    0.028    0.000    0.136    0.000 random.py:334(randint)
   #      1    0.000    0.000    0.166    0.166 task1.py:46(teacher_algorithm)
   #      1    0.021    0.021    0.156    0.156 task1.py:47(<listcomp>)
   #      1    0.000    0.000    0.000    0.000 {built-in method _abc._abc_instancecheck}
   #    7/1    0.000    0.000    0.000    0.000 {built-in method _abc._abc_subclasscheck}
   #      1    0.007    0.007    0.007    0.007 {built-in method _collections._count_elements}
   #      1    0.000    0.000    0.166    0.166 {built-in method builtins.exec}
   #      1    0.000    0.000    0.000    0.000 {built-in method builtins.isinstance}
   #      1    0.000    0.000    0.000    0.000 {built-in method builtins.iter}
   #      1    0.003    0.003    0.003    0.003 {built-in method builtins.max}
   # 100000    0.006    0.000    0.006    0.000 {method 'bit_length' of 'int' objects}
   #      1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
   # 131131    0.011    0.000    0.011    0.000 {method 'getrandbits' of '_random.Random' objects}
   #      1    0.000    0.000    0.000    0.000 {method 'items' of 'dict' objects}


# выводы:
# 1. данные алгортимы имеет линейную сложность
# 2. асимптотический анализ показывает:
# время выполнения алгоритма mostfrequent занимает на моем компьютере примерно 0.012 секунд,
# в томе время как алгоритм teacher_algorithm тратит на выполнение примерно 0.166 секунд.
# Это говорит, о том, что алгоритм mostfrequent является более эффективным
