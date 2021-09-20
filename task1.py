"""
1.Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4
квартала (т.е. 4 отдельных числа) для каждого предприятия.. Программа должна определить
среднюю прибыль (за год для всех предприятий) и вывести наименования предприятий, чья
прибыль выше среднего и отдельно вывести наименования предприятий, чья прибыль ниже
среднего
"""
from collections import namedtuple

enterprise = namedtuple('enterprise', ['name', 'quarters', 'profit'])
all_enterprise = set()

num = int(input("Введите количество предприятий: "))
total_profit = 0
for i in range(1, num + 1):
    profit = 0
    quarters = []
    name = input(f'Введите название предприятия {i}: ')

    for j in range(4):
        quarters.append(int(input(f'Прибыль за {j + 1}-й квартал: ')))
        profit += quarters[j]

    company = enterprise(name=name, quarters=tuple(quarters), profit=profit)

    all_enterprise.add(company)
    total_profit += profit

average = total_profit / num
print(f'Средняя прибыль: {average}')

print('Предприятия с прибылью выше среднего:')
for company in all_enterprise:
    if company.profit > average:
        print(f'Предприятие {company.name} заработало {company.profit}')

print(f'Предприятия с прибылью ниже среднего:')
for company in all_enterprise:
    if company.profit < average:
        print(f'Предприятие {company.name} заработало {company.profit}')
