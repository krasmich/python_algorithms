"""
8. Матрица 5x4 заполняется вводом с клавиатуры кроме последних элементов строк. Программа
должна вычислять сумму введенных элементов каждой строки и записывать ее в последнюю
ячейку строки. В конце следует вывести полученную матрицу
"""
m = 5
n = 4
matrix = []

for i in range(n):
    row = []
    summ = 0

    for j in range(m-1):
        number = int(input(f'строка {i}, элемент {j}: '))
        summ += number
        row.append(number)

    row.append(summ)
    matrix.append(row)

for line in matrix:
    for _ in line:
        print(f'{_:>5}', end='')
    print()
