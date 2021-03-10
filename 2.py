# 2. Пользователь вводит время в секундах. Переведите время в часы,
# минуты и секунды и выведите в формате чч:мм:сс. Используйте форматирование строк.
time = int(input('Введите время в секундах: '))
hour = time // 3600
minuts = (time - hour * 3600) // 60
seconds = time - hour * 3600 - minuts * 60

if 0 <= hour < 10:
    hour_format = '0' + str(hour)
else:
    hour_format = str(hour)

if 0 <= minuts < 10:
    minuts_format = '0' + str(seconds)
else:
    minuts_format = str(minuts)

if 0 <= seconds < 10:
    seconds_format = '0' + str(seconds)
else:
    seconds_format = str(seconds)

print(f'{time} сек. = {hour_format}:{minuts_format}:{seconds_format}')
