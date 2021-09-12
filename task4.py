"""
4. Определить, какое число в массиве встречается чаще всего.
"""
import random


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

arr = [random.randrange(1, 1000, 1) for i in range(100)]
n = len(arr)
print(mostfrequent(arr, n))
