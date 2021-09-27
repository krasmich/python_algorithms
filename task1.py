"""
1. Отсортируйте по убыванию методом пузырька одномерный целочисленный массив, 
заданный случайными числами на промежутке [-100; 100). Выведите на экран исходный и отсортированный массивы. 
Сортировка должна быть реализована в виде функции. По возможности доработайте алгоритм (сделайте его умнее).
"""

import random

lst = [random.randrange(-100, 100) for i in range(30)]


def bubble_sort(arr, reverse=False):

	sing = int(reverse) * 2 - 1
	pos = 1

	while pos < len(arr):
		is_sorted = True 

		for i in range(len(arr) - pos):
			if arr[i] * sing < arr[i + 1] * sing:
				arr[i], arr[i+1] = arr[i+1], arr[i]
				is_sorted = False

		if is_sorted:
			break

		pos += 1


print(lst)
bubble_sort(lst, reverse=True)
print(lst)
