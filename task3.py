"""
3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
"""
import random


def swappos(random_list, p1, p2):
    random_list[p1], random_list[p2] = random_list[p2], random_list[p1]
    return random_list


random_list = [random.randrange(1, 50, 1) for i in range(10)]
print(random_list)
print(f"макс. число - {max(random_list)}, мин. число - {min(random_list)}")

pos1, pos2 = random_list.index(max(random_list)), random_list.index(min(random_list))

print(swappos(random_list, pos1, pos2))
