"""
6. Пользователь вводит номер буквы в алфавите. Определить, какая это буква.
"""
import string

alphabet = list(string.ascii_lowercase)

n = int(input("Введите номер буквы в алфавите: "))

if n > 26:
    print(f'Ошибка: необходимо ввести номер, который меньше или равен 26')
elif n <= 26:
    print(f"Номеру {n} соответсвует буква {alphabet[n-1]}")
