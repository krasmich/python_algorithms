"""
1. В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны каждому из
чисел в диапазоне от 2 до 9.
"""

number_from = 2
number_to = 99

result = [0]*8
list_numbers = list(range(number_from, number_to+1))

for number in list_numbers:
    for div in range(2, 10):
        if number % div == 0:
            result[div - 2] += 1

i = 0
while i < len(result):
    print(f'На {i + 2} делятся {result[i]} чисел/числа')
    i += 1
