# 5. Создать (программно) текстовый файл, записать в него программно набор чисел,
# разделенных пробелами. Программа должна подсчитывать сумму чисел в файле и выводить
# ее на экран.

from random  import randint

with open('text_5.txt', 'w+') as f:
    for number in range(0, 10):
        f.write(f'{str(randint(1, 100))} ')
    f.seek(0)

    num = f.read().split()
    sum_num = sum(int(n) for n in num)

    print(num)
    print(sum_num)
