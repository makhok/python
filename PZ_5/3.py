# 3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников
# и величину их окладов. Определить, кто из сотрудников имеет оклад менее 20 тыс.,
# вывести фамилии этих сотрудников. Выполнить подсчет средней величины дохода сотрудников.

with open('text_3.txt', 'r', encoding='UTF-8') as f:
    my_list = f.read().split('\n')
    my_dict = {}

    for i in my_list:
        name = i.split()[0]
        money = float(i.split()[1])
        my_dict.update({name: money})
    print(my_dict)

    print('Оклад менее 20 тыс.:')
    for i in my_dict:
        if my_dict[i] < 20000:
            print(i, my_dict[i])

    print(f'Средний доход сотрудников: {sum(my_dict.values())/len(my_dict.values())}')
