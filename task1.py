"""
1. Определить количество различных подстрок с использованием хеш-функции. Задача: на вход
функции дана строка, требуется вернуть количество различных подстрок в этой строке.
"""


def count_substring(s: str):
    set_hash = set()

    for i in range(len(s) - 1):
        for j in range(i + 1, len(s) + 1):
            set_hash.add(hash(s[i:j]))

    counter = len(set_hash)
    return counter


user_str = input('Введите строку: ')
count = count_substring(user_str)
print(f'В строке "{user_str}" {count} различных подстрок')
