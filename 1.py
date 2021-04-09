# 1. Реализовать класс «Дата», функция-конструктор которого должна принимать
# дату в виде строки формата «день-месяц-год». В рамках класса реализовать
# два метода. Первый, с декоратором @classmethod, должен извлекать число, месяц,
# год и преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod,
# должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
# Проверить работу полученной структуры на реальных данных.

class MyDate:
    def __init__(self, str_date):
        self.str_date = str_date

    @classmethod
    def date_number(cls, str_date):
        day = int(str_date.split('-')[0])
        month = int(str_date.split('-')[1])
        year = int(str_date.split('-')[2])
        return (day, month, year)

    @staticmethod
    def date_valid(d, m, y):
        # определение количества дней в месяце в словаре
        count_day = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}

        # определение высокосного года
        if y % 4 == 0 and y % 100 != 0 or y % 400 == 0:
            count_day.update({2: 29})
        else:
            count_day.update({2: 28})

        # определение правильности ввода даты
        if y < 0:
            print(f'Год указан неверно => {y}')
        if not 1 <= m <= 12:
            print(f'Месяц указан неверно => {m} (Допустимое значение: 1-12)')
        if not 1 <= d <= count_day.get(m):
            print(f'Число указано неверно => {d} (Допустимое значение: 1-{count_day.get(m)})', end='')
            if d == 29 and count_day.get(2) != 29:
                print(' Год не высокосный! В феврале 28 дней!')
        else:
            print(f'Дата указана корректно!!! => {d}.{m}.{y}')


my_date = input('Введите дату в формате dd-mm-yyyy: ')
date = MyDate(my_date)

date_1 = MyDate.date_number(date.str_date)
print(f'Числовой кортеж даты: {date_1}')

MyDate.date_valid(date_1[0], date_1[1], date_1[2])
