"""
2. Написать два алгоритма нахождения i-го по счёту простого числа.
● Без использования Решета Эратосфена;
● Использовать алгоритм решето Эратосфена
"""
import cProfile

def simple_prime(n):
    """
    Функция поиска i-го простого числа,
    без использования алгоритма Решета Эратосфена
    """
    arr_s = []

    for i in range(2, n + 1):
        k = 0
        for j in range(1, i + 1):
            if i % j == 0:
                k += 1
        if k == 2:
            arr_s.append(i)

    return arr_s


def sieve(n2):
    """
    Функция поиска i-го простого числа,
    c использованием алгоритма Решета Эратосфена
    """
    arr_c = [1 for i in range(n2 + 1)]
    i = 2
    while (i * i <= n2):
        if (arr_c[i] == 1):
            for j in range(i * i, n2 + 1, i):
                arr_c[j] = 0
        i += 1

    for i in range(2, n2 + 1):
        if (arr_c[i] == 1):
            print(i, end=' ')


cProfile.run('simple_prime(10000)')
cProfile.run('sieve(10000)')

   #       1233 function calls in 1.801 seconds
   #
   # Ordered by: standard name
   #
   # ncalls  tottime  percall  cumtime  percall filename:lineno(function)
   #      1    0.000    0.000    1.801    1.801 <string>:1(<module>)
   #      1    1.801    1.801    1.801    1.801 task2.py:8(simple_prime)
   #      1    0.000    0.000    1.801    1.801 {built-in method builtins.exec}
   #   1229    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
   #      1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
   #
   #
   # 1234 function calls in 0.014 seconds
   #
   # Ordered by: standard name
   #
   # ncalls  tottime  percall  cumtime  percall filename:lineno(function)
   #      1    0.000    0.000    0.014    0.014 <string>:1(<module>)
   #      1    0.001    0.001    0.014    0.014 task2.py:29(sieve)
   #      1    0.000    0.000    0.000    0.000 task2.py:34(<listcomp>)
   #      1    0.000    0.000    0.014    0.014 {built-in method builtins.exec}
   #   1229    0.013    0.000    0.013    0.000 {built-in method builtins.print}
   #      1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


# вывод:
# алгорим решета Эратосфена гораздо эффективен



