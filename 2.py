# 2. Создать текстовый файл (не программно), сохранить в нем несколько строк,
# выполнить подсчет количества строк, количества слов в каждой строке.

with open('text_2.txt', 'r', encoding='UTF-8') as f:
    file_str = f.read()
    print(f'Исходный файл:\n{file_str}')
    file_list = file_str.split('\n')
    print(f'Количество строк в исходном файле: {len(file_list)}')
    for line in file_list:
        print(f'Количество слов в строке "{line}" => {len(line.split())}')
