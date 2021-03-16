# 5. Программа запрашивает у пользователя строку чисел, разделенных пробелом.
# При нажатии Enter должна выводиться сумма чисел. Пользователь может продолжить
# ввод чисел, разделенных пробелом и снова нажать Enter. Сумма вновь введенных
# чисел будет добавляться к уже подсчитанной сумме. Но если вместо числа вводится
# специальный символ, выполнение программы завершается. Если специальный символ
# введен после нескольких чисел, то вначале нужно добавить сумму этих чисел
# к полученной ранее сумме и после этого завершить программу.

def my_func():
    sum_str = 0
    while True:
        numbers_str = input('Ведите числа через пробел: ')
        try:
            for n in numbers_str.split():
                sum_str = sum_str + float(n)
            print(sum_str)
        except ValueError:
            print(sum_str)
            print('Введены не числовые данные')
            break

my_func()




