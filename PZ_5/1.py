# 1. Создать программно файл в текстовом формате, записать в него построчно данные,
# вводимые пользователем. Об окончании ввода данных свидетельствует пустая строка.

f = open('text_1.txt', 'a', encoding='UTF-8')
while True:
    my_data = input(f'Введите данные для записи в файл: ')
    if my_data == '':
        f.close()
        break
    f.write(f'{my_data}\n')
