# 7. Создать (не программно) текстовый файл, в котором каждая строка должна содержать
# данные о фирме: название, форма собственности, выручка, издержки.
# Пример строки файла: firm_1 ООО 10000 5000.
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю
# прибыль. Если фирма получила убытки, в расчет средней прибыли ее не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями,
# а также словарь со средней прибылью. Если фирма получила убытки, также добавить ее
# в словарь (со значением убытков).

# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].

# Итоговый список сохранить в виде json-объекта в соответствующий файл.

# Пример json-объекта:
# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
# Подсказка: использовать менеджеры контекста.

import json

with open('text_7.txt') as f:
    all_firm = {}
    for firm in f.read().split('\n'):
        name_firm = firm.split()[0]
        profit_firm = int(firm.split()[2]) - int(firm.split()[3])
        all_firm.update({name_firm: profit_firm})

sum_profit = 0
count = 0
for firm in all_firm:
    if all_firm.get(firm) >= 0:
        sum_profit = sum_profit + all_firm.get(firm)
        count += 1
    else:
        all_firm.update({firm: abs(all_firm.get(firm))})

all_firm_profit = [all_firm, {'average_profit': int(sum_profit / count)}]
print(all_firm_profit)

with open('my_file.json', 'w+') as f:
    json.dump(all_firm_profit, f)

with open('my_file.json') as f:
    print(json.load(f))
