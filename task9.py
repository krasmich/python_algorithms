"""
9. Среди натуральных чисел, которые были введены, найти наибольшее по сумме цифр.
Вывести на экран это число и сумму его цифр.
"""


def sum_numbers(n):
    summ = 0
    for f in n:
        summ += int(f)
    return summ


list_number = [i for i in input('Введите числа и нажмите Enter: ').split()]

max_n = 0
max_sum = 0
for i in list_number:
    if sum_numbers(i) > max_sum:
        max_n = i
        max_sum = sum_numbers(i)

print(f'У числа {max_n} была наибольшая сумма цифр - {max_sum}')
