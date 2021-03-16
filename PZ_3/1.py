# 1. Реализовать функцию, принимающую два числа (позиционные аргументы)
# и выполняющую их деление. Числа запрашивать у пользователя,
# предусмотреть обработку ситуации деления на ноль.

def my_func_division(div_1, div_2):
    try:
        print(float(div_1)/float(div_2))
    except ZeroDivisionError:
        print('На ноль делить нельзя')
        return
    except ValueError:
        print('Введены не числовые данные')
        return


a = input('Введите делимое: ')
b = input('Введите делитель: ')
my_func_division(a, b)


