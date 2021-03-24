# 4. Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую
# построчно данные. При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.

with open('text_4.1.txt', 'r', encoding='UTF-8') as f:
    new_my_str = []
    while True:
        my_str = f.readline()
        if 'One' in my_str:
            new_my_str.append(my_str.replace('One', 'Один'))
        if 'Two' in my_str:
            new_my_str.append(my_str.replace('Two', 'Два'))
        if 'Three' in my_str:
            new_my_str.append(my_str.replace('Three', 'Три'))
        if 'Four' in my_str:
            new_my_str.append(my_str.replace('Four', 'Четыре'))

        if my_str == '':
            break

        new_f = open('text_4.2.txt', 'w', encoding='UTF-8')
        new_f.writelines(new_my_str)
        new_f.close()
