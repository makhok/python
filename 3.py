# 3. Узнайте у пользователя число n. Найдите сумму чисел
# n + nn + nnn. Например, пользователь ввёл число 3.
# Считаем 3 + 33 + 333 = 369.

number_str = input('Введите число:')
number_1 = int(number_str)
number_2 = int(number_str * 2)
number_3 = int(number_str * 3)
summa = number_1 + number_2 + number_3
print(f'{number_1} + {number_2} + {number_3} = {summa}')
