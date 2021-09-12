"""
5. Пользователь вводит две буквы. Определить, на каких местах алфавита они стоят,
и сколько между ними находится букв.
"""
import string

l1 = input("Введите первую букву: ")
l2 = input("Введите вторую букву: ")

alphabet = list(string.ascii_lowercase)

p1 = alphabet.index(l1)
p2 = alphabet.index(l2)
print(f'Порядковый номер первой буквы: {p1+1} \n'
      f'Порядковый номер второй буквы: {p2+1}')

numbers_letters = abs(p1 - p2) - 1
print(f'Между буквами {l1} и {l2} находятся {numbers_letters} букв(ы)')
