# 3. Реализовать базовый класс Worker (работник), в котором определить атрибуты:
# name, surname, position (должность), income (доход). Последний атрибут должен
# быть защищенным и ссылаться на словарь, содержащий элементы: оклад и премия,
# например, {"wage": wage, "bonus": bonus}. Создать класс Position (должность)
# на базе класса Worker. В классе Position реализовать методы получения полного
# имени сотрудника (get_full_name) и дохода с учетом премии (get_total_income).
# Проверить работу примера на реальных данных (создать экземпляры класса Position,
# передать данные, проверить значения атрибутов, вызвать методы экземпляров).

class Worker:
    name = 'Имя'
    surname = 'Фамилия'
    position = 'должность'
    _income = {'wage': 80000, 'bonus': 20000}

class Position(Worker):
    def get_full_name(self):
        full_name = f'{self.surname} {self.name}'
        return full_name

    def get_total_income(self):
        total_income = float(self._income.get('wage')) + float(self._income.get('bonus'))
        return total_income

my_posit = Position()
my_posit.name = 'Сергей'
my_posit.surname = 'Иванов'
my_posit.position = 'Старший менеджер'
my_posit._income = {'wage': 100000, 'bonus': 30000}
#print(my_posit.name, my_posit.surname, my_posit.position, my_posit._income)
print(f'{my_posit.position} {my_posit.get_full_name()} => {my_posit.get_total_income()}')

my_posit_2 = Position()
my_posit_2.name = 'Максим'
my_posit_2.surname = 'Петров'
my_posit_2.position = 'Менеджер'
print(f'{my_posit_2.position} {my_posit_2.get_full_name()} => {my_posit_2.get_total_income()}')

my_posit_3 = Position()
my_posit_3.name = input('Введите имя сотрудника: ')
my_posit_3.surname = input('Введите фамилию сотрудника: ')
my_posit_3.position = input('Введите должность сотрудника: ')
wage = float(input(f'Введите оклад {my_posit_3.get_full_name()}: '))
bonus = float(input(f'Введите премию {my_posit_3.get_full_name()}: '))
my_posit_3._income = {'wage': wage, 'bonus': bonus}
print(f'{my_posit_3.position} {my_posit_3.get_full_name()} => {my_posit_3.get_total_income()}')
