# 1. Реализовать скрипт, в котором должна быть предусмотрена функция расчета
# заработной платы сотрудника. В расчете необходимо использовать формулу:
# (выработка в часах * ставка в час) + премия. Для выполнения расчета для
# конкретных значений необходимо запускать скрипт с параметрами.

from sys import argv
script_name, time_work, work_hour, prize = argv


def my_salary(time, hour, pri):
    try:
        print(float(time) * float(hour) + float(pri))
    except ValueError:
        print('Введен неправильный формат данных')


my_salary(time_work, work_hour, prize)
