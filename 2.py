# 2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления
# на нуль. Проверьте его работу на данных, вводимых пользователем. При вводе
# пользователем нуля в качестве делителя программа должна корректно обработать
# эту ситуацию и не завершиться с ошибкой.

class My_ZeroDivisionError(ZeroDivisionError):
    def __init__(self, text):
        self.text = text


try:
    n = int(input('Введите делитель: '))
    if n == 0:
        raise My_ZeroDivisionError('На ноль делить нельзя!!!')
    print(f'100 / {n} = {100 / n}')
except ValueError:
    print('Вы ввели не число!')
except My_ZeroDivisionError as error:
    print(error)
