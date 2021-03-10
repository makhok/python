# 4. Пользователь вводит целое положительное число.
# Найдите самую большую цифру в числе. Для решения
# используйте цикл while и арифметические операции.

numbers = list(input('Введите целое положительное число:'))
max_number = int(numbers[0])
count = 0

while count < len(numbers)-1:
    count += 1
    if int(numbers[count]) > max_number:
        max_number = int(numbers[count])

print(numbers)
print(f'max = {max_number}')
